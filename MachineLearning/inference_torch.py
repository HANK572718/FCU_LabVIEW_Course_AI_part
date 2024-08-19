import matplotlib.pyplot as plt
from PIL import Image
import torch
from ultralytics import YOLOv10
from ultralytics.utils import ops, yaml_load, yaml_save
import types
from notebook_utils import download_file
from pathlib import Path


def inference():
    # 設定設備
    torch.cuda.set_device(0)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # 創建模型目錄
    models_dir = Path("./models")
    models_dir.mkdir(exist_ok=True)

    # 設定圖片路徑
    IMAGE_PATH = Path("MachineLearning/data/grape.jpg")
    TORCH_MODEL = Path("MachineLearning/models/yolov10n.pt")  # 使用下載後的模型路徑

    # 載入 YOLOv10 模型，並移動模型到指定設備
    torch_yolo_model = YOLOv10(TORCH_MODEL, task="detect")
    torch_yolo_model.to(device=device)

    # 進行物體檢測
    res_torch = torch_yolo_model(IMAGE_PATH, iou=0.45, conf=0.2)

    # 將檢測結果轉換為圖片並顯示
    image = Image.fromarray(res_torch[0].plot()[:, :, ::-1])
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    return "finish"


if __name__ == "__main__":
    inference()
