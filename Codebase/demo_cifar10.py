import json

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
        outputs=[gr.Label(num_top_classes=10)]
    )

    demo.launch(share=True)

# @hydra.main(
#     version_base="1.2", config_path=root / "configs", config_name="demo_scripted.yaml"
# )
def main() -> None:
    print("inside main")
    demo()

if __name__ == "__main__":
    main()