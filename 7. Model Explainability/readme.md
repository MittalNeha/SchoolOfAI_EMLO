## Using the pretrained  model ResNet18 demonstrating Model Explanation with

- IG
- IG w/ Noise Tunnel
- Saliency
- Occlusion
- SHAP
- GradCAM
- GradCAM++

Code : ![Colab Notebook](./Session7_Explainability.ipynb)


| Original Image | IG | IG w/ Noise Tunnel | Saliency | Occlusion | SHAP | GradCAM | GradCAM++ |
:----------------------------:|:--------------------------------:|:--------------------------------:|:--------------------------------:|:--------------------------------:|:--------------------------------:|:--------------------------------:|:--------------------------------:|
![](test_images/elephant.JPG)| ![](test_images/elephant_IG.png) | ![](test_images/elephant_NT.png) | ![](test_images/elephant_saliency.jpg) | ![](test_images/elephant_occ.jpg) | ![](test_images/elephant_shap.png) | ![](test_images/elephant_gc.png) | ![](test_images/elephant_gcp.png)
![](test_images/hare.jpg) | ![](test_images/hare_IG.png) | ![](test_images/hare_noisetunnel.png) | ![](test_images/hare_saliency.jpg) | ![](test_images/hare_occ.jpg) | ![](test_images/hare_shap.png) | ![](test_images/hare_gradcam.png) | ![](test_images/hare_gradcamplus.png)
![](test_images/monitor.jpg) | ![](./test_images/monitor_ig.png) | ![](./test_images/monitor_nt.png) | ![](./test_images/monitor_saliency.jpg) | ![](./test_images/monitor_occ.jpg) | ![](./test_images/monitor_shap.png) | ![](./test_images/monitor_gc.png) | ![](./test_images/monitor_gcp.png)
![](./test_images/ostrich.JPG) | ![](./test_images/ostrich_ig.png) | ![](./test_images/ostrich_nt.png) | ![](./test_images/ostrich_saliency.jpg) | ![](./test_images/ostrich_occ.jpg) | ![](./test_images/ostrich_shap.png) | ![](./test_images/ostrich_gc.png) | ![](./test_images/ostrich_gcp.png)
![](./test_images/palace.jpg) | ![](./test_images/palace_ig.jpg) | ![](./test_images/palace_nt.jpg) | ![](./test_images/palace_saliency.jpg) | ![](./test_images/palace_occ.jpg) | ![](./test_images/palace_grad_shap.jpg) | ![](./test_images/palace_gradcam.png) | ![](./test_images/palace_gradcamplus.png)
![](./test_images/plate.jpg) | ![](./test_images/plate_ig.png) | ![](./test_images/plate_nt.png) |![](./test_images/plate_saliency.jpg) |![](./test_images/plate_occ.jpg) |![](./test_images/plate_shap.png) |![](./test_images/plate_gc.png) |![](./test_images/plate_gcp.png)
![](./test_images/tricycle.jpg) | ![](./test_images/tricycle_ig.png) | ![](./test_images/tricycle_nt.png) | ![](./test_images/tricycle_saliency.jpg) | ![](./test_images/tricycle_occ.jpg) | ![](./test_images/tricycle_shap.png) | ![](./test_images/tricycle_gc.png) | ![](./test_images/tricycle_gcp.png)
![](./test_images/zebra.JPG) | ![](./test_images/zebra_ig.png) | ![](./test_images/zebra_nt.png) | ![](./test_images/zebra_saliency.jpg) | ![](./test_images/zebra_occ.jpg) | ![](./test_images/zebra_shap.png) | ![](./test_images/zebra_gc.png) | ![](./test_images/zebra_gcp.png)
![](./test_images/van.jpg) | ![](./test_images/van_ig.png) | ![](./test_images/van_nt.png) | ![](./test_images/van_saliency.jpg) | ![](./test_images/van_occ.jpg) | ![](./test_images/van_shap.png) | ![](./test_images/van_gc.png) | ![](./test_images/van_gcp.png)
![](./test_images/car.jpg) | ![](./test_images/car_ig.jpg) | ![](./test_images/car_nt.jpg) | ![](./test_images/car_saliency.jpg) | ![](./test_images/car_occ.jpg) | ![](./test_images/car_grad_shap.jpg) | ![](./test_images/car_gc.png) | ![](./test_images/car_gcp.png)|