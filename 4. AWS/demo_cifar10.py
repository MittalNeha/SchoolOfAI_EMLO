import json
import boto3
import urllib.request

from typing import List, Tuple

import torch
# import hydra
import gradio as gr
#from omegaconf import DictConfig

# from src import utils
import logging
from torchvision import transforms

# log = utils.get_pylogger(__name__)

def demo() -> Tuple[dict, dict]:
    """Demo function.
    Returns:
        Tuple[dict, dict]: Dict with metrics and dict with all instantiated objects.
    """

    print("inside demo")

    logging.info("Running Demo")

    logging.info(f"Instantiating scripted model model.script.pt")
    model = torch.jit.load("model.script.pt")

    # log.info(f"Loaded Model: {model}")

    with open("cifar10_classes.json") as f:
        labels = list(json.load(f).values())[0]
    

    def classify_image(image):
        if image is None:
            return None
        # print(image.)
        image = transforms.ToTensor()(image)
        image = torch.tensor(image[None, ...], dtype=torch.float32)
        preds = model.forward_jit(image)
        preds = preds.squeeze()

        logging.info(preds.topk(5))
        out = {labels[idx]: float(preds[idx]) for idx in preds.topk(10)[1]}

        return out

    im = gr.Image(shape=(32, 32),type="pil")

    demo = gr.Interface(
        fn=classify_image,
        inputs=im,
        outputs=[gr.Label(num_top_classes=5)]
    )

    demo.launch(server_name="0.0.0.0")


def main() -> None:
    print("inside main")

    print("Download the model")
    bucket_name = 'mycifar10model'
    folder_prefix = 'model.script.pt'

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    bucket.download_file("model.script.pt", "model.script.pt")

    # for s3_file in bucket.objects.filter(Prefix=folder_prefix):
    #     file_object = s3_file.key
    #     file_name = str(file_object.split('/')[-1])
    #     print('Downloading file {} ...'.format(file_object))
    #     bucket.download_file(file_object, '/tmp/{}'.format(file_name))

    # try:
    #     s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
    # except botocore.exceptions.ClientError as e:
    #     if e.response['Error']['Code'] == "404":
    #         print("The object does not exist.")
    #     else:
    #         raise

    #Download the labels
    print("Downloading the class labels")
    url, filename = (
        "https://raw.githubusercontent.com/MittalNeha/SchoolOfAI_EMLO/main/Codebase/cifar10_classes.json",
        "cifar10_classes.json",
    )
    urllib.request.urlretrieve(url, filename)
    print("Downloaded")

    demo()

if __name__ == "__main__":
    main()