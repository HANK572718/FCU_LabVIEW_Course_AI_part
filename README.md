# LabVIEW + Python 課程｜AI 段教材

逢甲大學「LabVIEW + Python」課程中，AI 延伸段落的教材與範例程式（2024，定版）。
課程前半由另一位講師負責 LabVIEW 基礎，這個 repo 是後半的 AI 部分 ——
從 LabVIEW 呼叫 Python，一路做到把 YOLOv10 用 OpenVINO 跑起來。

原規劃 2 小時，後依課堂需求擴充為 4 小時。

## 一個刻意的設計取捨

授課老師提出一個要求：**教材必須能脫離實體設備執行。**

這個限制決定了整份教材的形態 —— 每個單元都設計成「有設備更好、沒設備也跑得完」，
機器學習的部分一律準備好 CPU 可跑的路徑，不假設教室有 GPU。
連套件安裝都提供 5 種方法，包含 `pip install --find-links wheels` 的離線安裝，
因為教室電腦不一定有網路、也不一定裝得動東西。

實體設備會缺席，網路會斷，但課還是要上完。

## 內容

| 資料夾 | 主題 | 內容 |
|---|---|---|
| `Python_Node/` | LabVIEW ↔ Python 互通 | 用 LabVIEW 的 Python Node 直接呼叫 Python 函式，含對應的 `.vi` 與 `.py` 成對範例 |
| `HTTP/` | 以 HTTP 服務串接 | Python 端起服務、LabVIEW 端發 request；含 `request_tutorial` 與水塔控制情境範例 |
| `MachineLearning/` | 推論實作 | YOLOv10 模型最佳化與 OpenVINO 推論，含 `.vi` 呼叫端 |
| `pip_install.ipynb` | 環境安裝 | 5 種安裝方法，含離線 wheels |
| `_practice_answer/` | 練習解答 | — |

兩種串接方式是刻意並列的：**Python Node 適合單機、低延遲；HTTP 適合跨機、鬆耦合。**
課堂上先做前者再做後者，學生才會知道為什麼要有第二種。

## 環境

```bash
poetry install
poetry run jupyter lab
```

`pyproject.toml` 中 CUDA 版 torch 的 wheel URL 已註解保留，
預設走 CPU 版本 —— 這是為了讓沒有獨顯的教室電腦也能安裝成功。
需要 GPU 時把對應的三行取消註解即可（注意 wheel 檔名要對應 Python 版本）。

主要套件：Poetry、OpenVINO、NNCF、PyTorch、JupyterLab、FastAPI、pyngrok。

## 授權

Apache License 2.0，見 [LICENSE](LICENSE)。
