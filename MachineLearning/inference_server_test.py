from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from ultralytics import YOLOv10
from PIL import Image
import requests
import platform
import sys
import torch
import time
from pathlib import Path
import shutil

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
        
        # Return the result image directly
        return FileResponse(result_image_path, media_type='image/png')

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 其他API函數保持不變...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8111)