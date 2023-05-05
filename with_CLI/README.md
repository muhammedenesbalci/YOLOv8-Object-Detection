## YOLOV8 with CLI(Command Line Interface)

  

**Usage**

Pip install the ultralytics package including all requirements.  
  

    pip install ultralytics  

  
  
Run this comman in CLI.  
  

    yolo predict model=yolov8n.pt source='img.jpg' show=True save_txt=True  

**Models**

| Model | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |  
| ------------------------------------------------------------------------------------ | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |  
| [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt) | 640 | 37.3 | 80.4 | 0.99 | 3.2 | 8.7 |  
| [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt) | 640 | 44.9 | 128.4 | 1.20 | 11.2 | 28.6 |  
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt) | 640 | 50.2 | 234.7 | 1.83 | 25.9 | 78.9 |  
| [YOLOv8l](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l.pt) | 640 | 52.9 | 375.2 | 2.39 | 43.7 | 165.2 |  
| [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt) | 640 | 53.9 | 479.1 | 3.53 | 68.2 | 257.8 |  
  

**Parameters**

 source: # source directory for images or videos  
- show: False # show results if possible  
- save_txt: False # save results as .txt file  
- save_conf: False # save results with confidence scores  
- save_crop: False # save cropped images with results  
- show_labels: True # show object labels in plots  
- show_conf: True # show object confidence scores in plots  
- vid_stride: 1 # video frame-rate stride  
- line_thickness: 3 # bounding box thickness (pixels)  
- visualize: False # visualize model features  
- augment: False # apply image augmentation to prediction sources  
- agnostic_nms: False # class-agnostic NMS  
- classes: # filter results by class, i.e. class=0, or class=[0,2,3]  
- retina_masks: False # use high-resolution segmentation masks  
- boxes: True # Show boxes in segmentation predictions