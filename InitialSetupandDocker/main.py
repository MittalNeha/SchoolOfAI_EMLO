#!/usr/bin/env python3
"""
"""
import os
import time
import argparse
import logging
import numpy as np
import torch
import json
import urllib.request

from PIL import Image
from timm.data.transforms_factory import create_transform

from timm.models import create_model, apply_test_time_pool
from timm.data import ImageDataset, create_loader, resolve_data_config
from timm.utils import AverageMeter, setup_default_logging
from timm.data.constants import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD

torch.backends.cudnn.benchmark = True
# _logger = logging.getLogger('inference')


parser = argparse.ArgumentParser(description='PyTorch ImageNet Inference')
# parser.add_argument('data', metavar='DIR',
#                     help='path to dataset')
parser.add_argument('--output_dir', metavar='DIR', default='./',
                    help='path to output files')
parser.add_argument('--model', '-m', metavar='MODEL', default='dpn92',
                    help='model architecture (default: dpn92)')
parser.add_argument('-j', '--workers', default=2, type=int, metavar='N',
                    help='number of data loading workers (default: 2)')
parser.add_argument('-b', '--batch-size', default=256, type=int,
                    metavar='N', help='mini-batch size (default: 256)')
parser.add_argument('--img-size', default=None, type=int,
                    metavar='N', help='Input image dimension')
parser.add_argument('--input-size', default=None, nargs=3, type=int,
                    metavar='N N N', help='Input all image dimensions (d h w, e.g. --input-size 3 224 224), uses model default if empty')
parser.add_argument('--mean', type=float, nargs='+', default=None, metavar='MEAN',
                    help='Override mean pixel value of dataset')
parser.add_argument('--std', type=float, nargs='+', default=None, metavar='STD',
                    help='Override std deviation of of dataset')
parser.add_argument('--interpolation', default='', type=str, metavar='NAME',
                    help='Image resize interpolation type (overrides model)')
parser.add_argument('--num-classes', type=int, default=1000,
                    help='Number classes in dataset')
parser.add_argument('--log-freq', default=10, type=int,
                    metavar='N', help='batch logging frequency (default: 10)')
parser.add_argument('--checkpoint', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('--pretrained', dest='pretrained', action='store_true',
                    help='use pre-trained model')
parser.add_argument('--num-gpu', type=int, default=0,
                    help='Number of GPUS to use, 0 means CPU')
parser.add_argument('--no-test-pool', dest='no_test_pool', action='store_true',
                    help='disable test time pool')
parser.add_argument('--topk', default=5, type=int,
                    metavar='N', help='Top-k to output to CSV')
parser.add_argument('--device', default='cpu', type=str,
                    help='gpu or cpu')
parser.add_argument('--image', default='', type=str,
                    help='input image for inference')


def main():
    args = parser.parse_args()
    # might as well try to do something useful...
    args.pretrained = args.pretrained or not args.checkpoint

    # print(args.data)

    # create model
    model = create_model(
        args.model,
        num_classes=args.num_classes,
        in_chans=3,
        pretrained=args.pretrained,
        checkpoint_path=args.checkpoint)


    config = resolve_data_config(vars(args), model=model)
    model, test_time_pool = (model, False) if args.no_test_pool else apply_test_time_pool(model, config)

    if args.num_gpu > 1:
        model = torch.nn.DataParallel(model, device_ids=list(range(args.num_gpu))).cuda()
    else:
        model = model

    if args.image.find("http") == 0:
        urllib.request.urlretrieve( args.image,"input.png")
        img = Image.open("input.png")
    else:
        img = Image.open(args.image)

    transform = create_transform(
        config['input_size'])

    img_t = transform(img)
    input = torch.unsqueeze(img_t, 0)

    # loader = create_loader(
    #     ImageDataset(args.data),
    #     input_size=config['input_size'],
    #     batch_size=args.batch_size,
    #     use_prefetcher=False,
    #     interpolation=config['interpolation'],
    #     mean=config['mean'],
    #     std=config['std'],
    #     num_workers=args.workers,
    #     crop_pct=1.0 if test_time_pool else config['crop_pct'])

    model.eval()

    k = min(args.topk, args.num_classes)
    batch_time = AverageMeter()
    end = time.time()
    topk_ids = []
    
    cls_idx = json.load(open("imagenet_class_index.json"))
    idx2label = [cls_idx[str(k)][1] for k in range(len(cls_idx))]
    with torch.no_grad():

        out = model(input)
        
        _, index = torch.max(out, 1)
        confidence = torch.nn.functional.softmax(out, dim=1)[0]
        #{"predicted": "dog", "confidence": "0.89"}
        pred = json.dumps({"predicted" : idx2label[index[0]], "confidence": str(confidence[index[0]].item())})

        print(pred)
        json.loads(pred)


if __name__ == '__main__':
    main()
