from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from ultralytics import YOLOv10
from PIL import Image
import requests
import platform
import sys
import torch
import time

app = FastAPI()

class ImagePath(BaseModel):
    path: str

def download_model_if_needed(models_dir: Path, model_weights_url: str) -> Path:
    models_dir.mkdir(exist_ok=True)
    file_name = model_weights_url.split("/")[-1]
    model_path = models_dir / file_name

    if not model_path.exists():
        print(f"Downloading model weights from {model_weights_url}...")
        response = requests.get(model_weights_url)
        with open(model_path, "wb") as f:
            f.write(response.content)
        print("Download completed.")
    else:
        print("Model weights already exist.")

    return model_path

def load_model(model_path: Path) -> YOLOv10:
    model_name = model_path.stem  # Get the model name without extension
    ov_model_path = model_path.parent / f"{model_name}_openvino_model/{model_name}.xml"
    return YOLOv10(ov_model_path.parent, task="detect")

def infer_and_save_image(model: YOLOv10, image_path: Path, save_dir: Path) -> Path:
    res = model(image_path, iou=0.45, conf=0.2)
    
    # Create a result image from the result
    result_image = Image.fromarray(res[0].plot()[:, :, ::-1])
    
    # Save the result image
    save_dir.mkdir(parents=True, exist_ok=True)
    result_image_path = save_dir / f"result_{image_path.name}"
    result_image.save(result_image_path)
    
    return result_image_path

@app.post("/infer/", response_class=JSONResponse)
async def infer_yolov10(image_path: ImagePath):
    try:
        MODELS_DIR = Path("MachineLearning/models")
        image_path = Path(image_path.path)
        
        model_weights_url = "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt"
        
        # Download model if not exists
        model_path = download_model_if_needed(MODELS_DIR, model_weights_url)
        
        # Load the YOLOv10 model
        model = load_model(model_path)
        
        # Define a directory to save results
        results_dir = Path("MachineLearning/results")
        
        # Infer and save image
        result_image_path = infer_and_save_image(model, image_path, results_dir)
        
        return {"result_image_path": str(result_image_path)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/model_name/", response_class=JSONResponse)
async def get_model_name():
    model_weights_url = "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt"
    model_name = model_weights_url.split("/")[-1].replace(".pt", "")
    return {"model_name": model_name}

@app.get("/environment_info/", response_class=JSONResponse)
async def get_environment_info():
    results = []

    # 1. 顯示 Python 版本資訊、位元數、位置
    python_version = platform.python_version()
    python_bits = platform.architecture()[0]
    python_executable = sys.executable  # 取得 Python 執行檔位置

    results.append("=== Python Information ===")
    results.append(f"Version: {python_version}")
    results.append(f"Bits: {python_bits}")
    results.append(f"Executable Location: {python_executable}\n")

    # 2. 顯示可用的 Torch devices
    devices = [torch.device('cpu')] + [torch.device(f'cuda:{i}') for i in range(torch.cuda.device_count())]
    
    results.append("=== Torch Devices ===")
    torch_vision = torch.__version__
    results.append(f"Torch Version: {torch_vision}")
    for device in devices:
        results.append(str(device))

    # 3. 測試每個設備的運行時間
    tensor_size = (1000, 1000)  # 調整 tensor 矩陣的大小
    repetitions = 1
    results.append("\n=== Tensor Computation Time ===")
    for device in devices:
        start_time = time.time()
        tensor_a = torch.randn(tensor_size, device=device)
        tensor_b = torch.randn(tensor_size, device=device)
        for _ in range(repetitions):
            tensor_sum = tensor_a + tensor_b  # Tensor 加法
            tensor_product = tensor_a @ tensor_b  # 矩陣乘法
            tensor_mean = tensor_sum.mean()  # 計算平均值
        elapsed_time = time.time() - start_time
        results.append(
            f"Time taken for tensor operations on {device}: {elapsed_time:.4f} seconds")

    # 4. 驗證 OpenVINO 安裝以及可用設備
    try:
        from openvino.runtime import Core  # 更新引用來匹配 openvino 的最近版本
        ie = Core()
        available_devices = ie.available_devices
        results.append("\n=== OpenVINO Information ===")
        results.append("OpenVINO is installed.")
        results.append("Available devices: " + str(available_devices))
    except ImportError:
        results.append("\n=== OpenVINO Information ===")
        results.append("OpenVINO is NOT installed.")

    return {"environment_info": "\n".join(results)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8111)