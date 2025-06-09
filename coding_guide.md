# File structure

BrickBreaker/
├── venv/                  # 虛擬環境（不要手動動它）
├── main.py                 # 遊戲主入口
├── game/                   # 遊戲主程式碼放這
│   ├── __init__.py
│   ├── app.py              # 遊戲應用程式邏輯
│   ├── window.py           # 遊戲視窗管理
│   ├── paddle.py           # 擋板邏輯
│   ├── ball.py             # 球邏輯
│   ├── brick.py            # 磚塊邏輯
│   └── settings.py         # 全域設定（如顏色、速度）
├── assets/                 # 資源檔：圖片、音效等
│   ├── images/
│   └── sounds/
├── requirements.txt        # 運行所需套件（pygame）
├── README.md               # 專案說明
└── .gitignore              # 忽略 .venv / __pycache__ 等