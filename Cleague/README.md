# セ・リーグ順位推移グラフ

日本プロ野球セ・リーグの順位推移を可視化するWebアプリケーションです。

## 機能

- **現在シーズンの順位推移表示**: パラメータなしで現在シーズンのグラフを表示
- **特定年度の表示**: 年度を指定して過去シーズンを表示（実装予定）
- **期間指定表示**: 開始月・終了月を指定して特定期間を表示（実装予定）
- **インタラクティブなグラフ**: ホバーでツールチップ表示、凡例クリックで球団の表示/非表示切り替え

## 技術スタック

### フロントエンド
- HTML5 / CSS3 / Vanilla JavaScript
- Chart.js 4.x（グラフ描画）

### バックエンド
- Python 3.11+
- Flask（APIサーバー）
- BeautifulSoup4（Webスクレイピング）
- Requests（HTTP通信）

## セットアップ

### 前提条件

- Python 3.11以上
- pip（Pythonパッケージマネージャー）

### インストール手順

1. **リポジトリのクローン**
```bash
git clone <repository-url>
cd Cleague
```

2. **Python仮想環境の作成**
```bash
cd backend
python -m venv venv
```

3. **仮想環境の有効化**

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

4. **依存関係のインストール**
```bash
pip install -r requirements.txt
```

## 実行方法

### バックエンドサーバーの起動

```bash
cd backend/src
python api.py
```

サーバーは `http://localhost:5000` で起動します。

### フロントエンドの表示

ブラウザで `frontend/index.html` を開きます。

または、簡易HTTPサーバーを使用：

```bash
cd frontend
python -m http.server 8000
```

ブラウザで `http://localhost:8000` にアクセスします。

## API エンドポイント

### GET /api/standings

順位推移データを取得します。

**クエリパラメータ:**
- `year` (optional): 年度（例: 2026）
- `startMonth` (optional): 開始月（1-12）
- `endMonth` (optional): 終了月（1-12）

**レスポンス例:**
```json
{
  "period": {
    "year": 2026,
    "startDate": "2026-03-20",
    "endDate": "2026-10-10",
    "startMonth": null,
    "endMonth": null
  },
  "data": [
    {
      "date": "2026-03-20",
      "teamId": "giants",
      "rank": 1,
      "wins": 1,
      "losses": 0,
      "draws": 0,
      "winRate": 1.0,
      "gamesBehind": 0.0
    }
  ]
}
```

### GET /api/teams

球団情報を取得します。

**レスポンス例:**
```json
[
  {
    "id": "giants",
    "name": "読売ジャイアンツ",
    "shortName": "巨人",
    "color": "#FF6600",
    "league": "central"
  }
]
```

### GET /api/health

ヘルスチェックエンドポイント。

## プロジェクト構造

```
Cleague/
├── backend/
│   ├── src/
│   │   ├── api.py          # Flask APIサーバー
│   │   ├── models.py       # データモデル
│   │   ├── scraper.py      # Webスクレイピング
│   │   └── parser.py       # HTMLパーサー
│   ├── tests/              # テスト（未実装）
│   └── requirements.txt    # Python依存関係
├── frontend/
│   ├── css/
│   │   └── styles.css      # スタイルシート
│   ├── js/
│   │   ├── main.js         # エントリーポイント
│   │   ├── api.js          # APIクライアント
│   │   ├── chart.js        # Chart.js設定
│   │   └── utils.js        # ユーティリティ関数
│   └── index.html          # メインHTML
├── specs/                  # 仕様書
└── README.md
```

## 開発状況

### 完了
- ✅ Phase 1: Setup - プロジェクト構造
- ✅ Phase 2: Foundational - 基盤構築
- ✅ Phase 3: User Story 1 - MVP（現在シーズン表示）

### 予定
- ⏳ Phase 4: User Story 2 - 年度指定機能
- ⏳ Phase 5: User Story 3 - 期間指定機能
- ⏳ Phase 6: Polish - 最終調整

## ライセンス

MIT License

## 注意事項

このアプリケーションはNPB公式サイトからデータをスクレイピングします。
過度なリクエストを避け、利用規約を遵守してください。