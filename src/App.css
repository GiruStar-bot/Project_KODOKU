import { useState } from "react";
import { Viewer, Scene } from "resium";
import { Cartesian3 } from "cesium";
import "./App.css";

function App() {
  // --- 状態管理（State） ---
  const [approvalRate, setApprovalRate] = useState(45.0); // 支持率
  const [budget, setBudget] = useState(-1200); // 財政赤字（兆円）
  const [logs, setLogs] = useState<string[]>(["[SYSTEM] KODOKU Engine Initialized."]);

  // --- Python APIを叩く関数 ---
  const executePolicy = async (policyId: string) => {
    try {
      // ローカルで動かしているPythonサーバーへリクエスト
      const response = await fetch("http://127.0.0.1:8000/execute_policy", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ policy_id: policyId }),
      });

      const result = await response.json();

      if (result.status === "success") {
        // Pythonから返ってきた数値を反映
        setApprovalRate((prev) => prev + result.deltas.approval_rate);
        setBudget((prev) => prev + result.deltas.budget_balance);
        
        // ログを追加
        setLogs((prev) => [result.log_message, ...prev]);

        // ※ここでマップ（Cesium）のテクスチャを暗くする処理などを後々追加します
      }
    } catch (error) {
      setLogs((prev) => ["[ERROR] 脳みそ(API)との通信に失敗しました。サーバー起動してますか？", ...prev]);
    }
  };

  return (
    <div className="kodoku-layout">
      {/* ＝＝＝ 左パネル：ステータスモニター ＝＝＝ */}
      <div className="side-panel">
        <div className="panel-header">MONITOR</div>
        <div className="panel-content">
          <ul className="status-list">
            <li>
              内閣支持率
              <span className="status-value" style={{ color: approvalRate < 30 ? "red" : "#00ffcc" }}>
                {approvalRate}%
              </span>
            </li>
            <li>
              国家予算残高 (兆円)
              <span className="status-value" style={{ color: "red" }}>
                {budget}
              </span>
            </li>
          </ul>

          <div className="log-box">
            <p>-- SYSTEM LOG --</p>
            {logs.map((log, index) => (
              <div key={index} style={{ marginBottom: "5px" }}>{log}</div>
            ))}
          </div>
        </div>
      </div>

      {/* ＝＝＝ 中央：現実（Cesium 3Dマップ） ＝＝＝ */}
      <div className="center-reality">
        <Viewer
          full
          animation={false}
          timeline={false}
          homeButton={false}
          navigationHelpButton={false}
          baseLayerPicker={false}
          geocoder={false}
          infoBox={false}
          selectionIndicator={false}
        >
          <Scene
            // 日本（東京付近）を初期カメラ位置に設定
            camera={{
              position: Cartesian3.fromDegrees(139.76, 35.68, 5000000), 
            }}
          />
        </Viewer>
      </div>

      {/* ＝＝＝ 右パネル：政策実行コントローラー ＝＝＝ */}
      <div className="side-panel">
        <div className="panel-header">EXECUTE</div>
        <div className="panel-content">
          <p style={{ marginBottom: "15px", fontSize: "12px", color: "#888" }}>
            ▶ 実行可能な政策リスト
          </p>

          <button
            className="policy-btn"
            onClick={() => executePolicy("policy_blackout_tokyo")}
          >
            [+] 首都圏 計画停電の実施
          </button>
          
          <button
            className="policy-btn"
            onClick={() => executePolicy("policy_tax_hike")}
          >
            [+] 消費税率変更 (15%)
          </button>

          <button
            className="policy-btn"
            style={{ borderColor: "red", color: "red", marginTop: "30px" }}
            onClick={() => alert("この機能は上位権限が必要です。")}
          >
            [!] 戒厳令の発布
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
