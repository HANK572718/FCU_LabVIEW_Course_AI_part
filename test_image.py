from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

# 設定上傳文件的存儲路徑
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "info": file_location}

@app.get("/images/{filename}")
async def get_image(filename: str):
    file_path = f"{UPLOAD_DIR}/{filename}"
    return FileResponse(file_path)

# 運行應用時： uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8013)

