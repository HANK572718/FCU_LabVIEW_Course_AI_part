

# from pathlib import Path
# from ultralytics import YOLOv10
# from PIL import Image
# import matplotlib.pyplot as plt
# import requests


# def download_model_if_needed(models_dir: Path, model_weights_url: str) -> Path:
#     """
#     Check if the model weights exist; if not, download them.
#     """
#     models_dir.mkdir(exist_ok=True)
#     file_name = model_weights_url.split("/")[-1]
#     model_path = models_dir / file_name

#     if not model_path.exists():
#         print(f"Downloading model weights from {model_weights_url}...")
#         response = requests.get(model_weights_url)
#         with open(model_path, "wb") as f:
#             f.write(response.content)
#         print("Download completed.")
#     else:
#         print("Model weights already exist.")

#     return model_path


# def load_model(model_path: Path) -> YOLOv10:
#     """
#     Load the YOLOv10 model.
#     """
#     model_name = model_path.stem  # Get the model name without extension
#     ov_model_path = model_path.parent / \
#         f"{model_name}_openvino_model/{model_name}.xml"
#     return YOLOv10(ov_model_path.parent, task="detect")


# def infer_and_display(model: YOLOv10, image_path: Path) -> None:
#     """
#     Perform inference on the given image and display the results.
#     """
#     res = model(image_path, iou=0.45, conf=0.2)
#     result_image = Image.fromarray(res[0].plot()[:, :, ::-1])
#     result_image.save("test1.png")

#     plt.imshow(result_image)
#     plt.axis('off')
#     plt.show()


# def main_inference(models_dir: str, image_path: str):
#     """
#     Main function to perform YOLOv10 inference.
#     """
#     models_dir = Path(models_dir)
#     image_path = Path(image_path)

#     model_weights_url = "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt"

#     # Download model if not exists
#     model_path = download_model_if_needed(models_dir, model_weights_url)

#     # Load the YOLOv10 model
#     model = load_model(model_path)

#     # Perform inference and display results
#     infer_and_display(model, image_path)

#     return "Finish"


# if __name__ == "__main__":
#     MODELS_DIR = "MachineLearning/models"
#     IMAGE_PATH = "MachineLearning/data/grape.jpg"
#     result = main_inference(MODELS_DIR, IMAGE_PATH)
#     print(result)  # Outputs the completion status


from pathlib import Path
from ultralytics import YOLOv10
from PIL import Image
import matplotlib.pyplot as plt
import requests


def download_model_if_needed(models_dir: Path, model_weights_url: str) -> Path:
    """
    Check if the model weights exist; if not, download them.
    """
    models_dir.mkdir(exist_ok=True, parents=True)  # Ensure all parent directories are created
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
    """
    Load the YOLOv10 model.
    """
    model_name = model_path.stem  # Get the model name without extension
    ov_model_path = model_path.parent / f"{model_name}_openvino_model/{model_name}.xml"
    return YOLOv10(ov_model_path.parent, task="detect")


def infer_and_display(model: YOLOv10, image_path: Path) -> None:
    """
    Perform inference on the given image and display the results.
    """
    res = model(image_path, iou=0.45, conf=0.2)
    result_image = Image.fromarray(res[0].plot()[:, :, ::-1])
    
    # Set the output_path relative to image_path
    output_path = image_path.parent.parent / "results"  # Create 'results' folder in the same directory as the image
    output_path.mkdir(exist_ok=True)  # Ensure the output directory exists

    result_image.save(output_path / "test1.png")  # Save the result image

    plt.imshow(result_image)
    plt.axis('off')
    plt.show()


def main_inference(models_dir: str, image_path: str):
    """
    Main function to perform YOLOv10 inference.
    """
    models_dir = Path(models_dir)
    image_path = Path(image_path)

    model_weights_url = "https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt"

    # Download model if not exists
    model_path = download_model_if_needed(models_dir, model_weights_url)

    # Load the YOLOv10 model
    model = load_model(model_path)

    # Perform inference and display results
    infer_and_display(model, image_path)

    return "Finish"


if __name__ == "__main__":
    MODELS_DIR = "MachineLearning/models"
    IMAGE_PATH = "MachineLearning/data/grape.jpg"
    result = main_inference(MODELS_DIR, IMAGE_PATH)
    print(result)  # Outputs the completion status
    