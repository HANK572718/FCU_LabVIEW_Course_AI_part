from pathlib import Path
import requests
import types
from ultralytics.utils import ops, yaml_load, yaml_save
from ultralytics import YOLOv10
import torch
from PIL import Image
import matplotlib.pyplot as plt


def main_inference(models_dir: str, image_path: str):
    # models_dir = Path("MachineLearning/models")
    models_dir = Path(models_dir)
    image_path = Path(image_path)
    models_dir.mkdir(exist_ok=True)

    model_weights_url = "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt"
    file_name = model_weights_url.split("/")[-1]
    model_name = file_name.replace(".pt", "")

    ov_model_path = models_dir / \
        f"{model_name}_openvino_model/{model_name}.xml"
    ov_yolo_model = YOLOv10(ov_model_path.parent, task="detect")

    # 模型推理
    res = ov_yolo_model(image_path, iou=0.45, conf=0.2)

    # 生成圖像
    result_image = Image.fromarray(res[0].plot()[:, :, ::-1])

    # 顯示圖像
    plt.imshow(result_image)
    plt.axis('off')  # 不顯示坐標軸
    plt.show()

    return "Finish"
    # return result_image  # 返回結果圖像


if __name__ == "__main__":
    MODELS_DIR = "MachineLearning/models"
    IMAGE_PATH = "MachineLearning/data/grape.jpg"
    
    # MODELS_DIR = Path("MachineLearning/models")
    # IMAGE_PATH = Path("MachineLearning/data/grape.jpg")
    main_inference(MODELS_DIR, IMAGE_PATH)
    # result = {}  # 創建一個字典來存儲結果
    # result["test1"] = main_inference(IMAGE_PATH)  # 將推理結果存入字典中
