# FCU LabVIEW × Python 課程｜AI Part

逢甲大學 2024 暑期「LabVIEW 基礎培訓與學術應用線上研習營」的 AI 段教材，
由諾亞思科技協辦。本 repo 收錄 AI Part 的範例程式與練習題，
涵蓋 LabVIEW 與 Python 的串接方式，以及 YOLOv10 + OpenVINO 的推論實作。

## 教學資源

| 資源 | 連結 |
|---|---|
| 教材主頁：環境建置教學、課程簡報 | https://hank.craft.me/r5ImVc5OFYpBgo |
| 0923 課堂定版：同上，附 `LabVIEW_AI_20240923_fix.pdf` | https://hank.craft.me/IT7tFJ7qtJ7GJf |

環境建置的完整步驟與截圖請以教材主頁為準，本 README 只列重點。

## 課程內容

| 目錄 | 主題 | 說明 |
|---|---|---|
| `Python_Node/` | Python Node 直呼 | LabVIEW 2019+ 的 Python Node 呼叫 Python 函式，`.vi` 與 `.py` 成對範例 |
| `HTTP/` | HTTP / REST 串接 | Python 端以 FastAPI 建立 server，LabVIEW 端以 HTTP Client VI 呼叫；含 request 教學與水塔控制範例 |
| `MachineLearning/` | 推論實作 | YOLOv10 模型最佳化與 OpenVINO 推論，含裝置列舉、CPU / GPU 計算時間比較，以及 LabVIEW 呼叫端 |
| `_practice_answer/` | 練習題解答 | practice1（HTTP）、practice2（推論） |
| `pip_install.ipynb` | 套件安裝 | 一鍵安裝 notebook，為課程主推的安裝方式 |

課程亦示範以 pyngrok 將本地 FastAPI server 轉發至公網，供教室環境無法直接連線時使用。

## 環境需求

- Windows
- Python **3.9 64-bit**（YOLOv10 的硬性需求）
- Git
- 虛擬環境擇一：Anaconda（課程示範）、venv、Poetry

## 安裝

```bash
git clone https://github.com/HANK572718/FCU_LabVIEW_Course_AI_part.git
cd FCU_LabVIEW_Course_AI_part
```

建立 Python 3.9 虛擬環境後，以下列任一方式安裝套件：

- **方法一（主推）**：在 VS Code 開啟 `pip_install.ipynb`，選擇該虛擬環境為 kernel 後逐格執行
- **方法二**：`poetry install`（`pyproject.toml` 限 Python ≥ 3.9、Windows）

`pyproject.toml` 中 CUDA 版 torch 的 wheel 已註解保留，預設安裝 CPU 版本。
需要 GPU 時取消對應三行的註解，並確認 wheel 檔名與 Python 版本相符。

## 注意事項

1. 範例程式已放在各目錄中，練習題解答另置於 `_practice_answer/`。
   **使用練習題程式時請複製到對應目錄**：
   - practice1 的 `calculator.py` → `HTTP/`
   - practice2 的兩支 inference 程式 → `MachineLearning/`
2. **執行本專案的 LabVIEW 程式前，請先關閉其他 LabVIEW 專案**，
   否則 Application Directory 會讀到其他專案的路徑而非 VI 本身的路徑。
3. Python Node 需指定 `python.exe` 的絕對路徑。
4. 本 repo 自 2024-09-23 定版後未再更新。

## 授權

Apache License 2.0，見 [LICENSE](LICENSE)。
