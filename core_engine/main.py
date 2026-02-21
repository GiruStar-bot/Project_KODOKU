from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# KODOKUエンジン初期化
app = FastAPI(title="Project KODOKU Engine")

# フロントエンド(React)からの通信を許可する設定（CORS）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開発中なので全許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# UIから受け取るデータの形を定義
class PolicyRequest(BaseModel):
    policy_id: str

# 政策実行のエンドポイント（ボタンを押した時にここが叩かれる）
@app.post("/execute_policy")
async def execute_policy(request: PolicyRequest):
    print(f"指令を受信しました: {request.policy_id}")
    
    # Sprint 1用のモックデータ（「計画停電」が選ばれた場合のハードコード）
    if request.policy_id == "policy_blackout_tokyo":
        return {
            "status": "success",
            "log_message": "[2026.XX.XX] 決裁完了: 首都圏・計画停電を実行。",
            "deltas": {
                "approval_rate": -15,  # 支持率激減
                "budget_balance": +50  # 支出削減で財政は改善
            },
            "map_trigger": "tokyo_lights_off" # 地図上の東京を暗くするフラグ
        }
        
    return {"status": "error", "message": "Unknown Policy"}
