# Quickstart Guide: セ・リーグ順位推移グラフ

**Date**: 2026-02-10
**Feature**: 001-cl-standings-graph

## Overview

このガイドでは、セ・リーグ順位推移グラフアプリケーションの開発環境をセットアップし、ローカルで実行する手順を説明します。

## Prerequisites

### 必須ツール

- **Python**: 3.11以上
- **Node.js**: 18.x以上（フロントエンド開発用、オプション）
- **Git**: バージョン管理
- **テキストエディタ**: VS Code推奨

### 推奨ツール

- **pip**: Pythonパッケージマネージャー
- **venv**: Python仮想環境
- **Live Server**: VS Code拡張機能（フロントエンド開発用）

## Quick Start (5分で起動)

### 1. リポジトリのクローン

```bash
git clone <repository-url>
cd Cleague
git checkout 001-cl-standings-graph
```

### 2. バックエンドのセットアップ

```bash
# 仮想環境の作成
cd backend
python -m venv venv

# 仮想環境の有効化
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 依存関係のインストール
pip install -r requirements.txt
```

### 3. バックエンドの起動

```bash
# 開発サーバーの起動
python src/api.py

# 別のターミナルでヘルスチェック
curl http://localhost:5000/api/health
```

### 4. フロントエンドの起動

```bash
# 新しいターミナルを開く
cd frontend

# Live Serverで起動（VS Code拡張機能）
# または、Pythonの簡易サーバー
python -m http.server 8000

# ブラウザで開く
# http://localhost:8000
```

### 5. 動作確認

1. ブラウザで `http://localhost:8000` を開く
2. 現在シーズンの順位推移グラフが表示される
3. 凡例をクリックして球団の表示/非表示を切り替える
4. 折れ線にホバーしてツールチップを確認

## Detailed Setup

### バックエンド詳細セットアップ

#### 1. 依存関係のインストール

`backend/requirements.txt`:
```txt
Flask==3.0.0
Flask-CORS==4.0.0
beautifulsoup4==4.12.0
requests==2.31.0
pytest==7.4.0
pytest-mock==3.12.0
```

インストール:
```bash
pip install -r requirements.txt
```

#### 2. 環境変数の設定（オプション）

`.env`ファイルを作成:
```env
FLASK_ENV=development
FLASK_DEBUG=1
PORT=5000
SCRAPING_TIMEOUT=10
CACHE_ENABLED=false
```

#### 3. ディレクトリ構造の確認

```
backend/
├── src/
│   ├── api.py          # Flaskアプリケーション
│   ├── scraper.py      # Webスクレイピング
│   ├── parser.py       # データ解析
│   └── models.py       # データモデル
├── tests/
│   ├── test_scraper.py
│   └── test_parser.py
├── requirements.txt
└── README.md
```

### フロントエンド詳細セットアップ

#### 1. ディレクトリ構造の確認

```
frontend/
├── index.html          # メインHTML
├── css/
│   └── styles.css      # スタイルシート
├── js/
│   ├── main.js         # エントリーポイント
│   ├── chart.js        # グラフ描画
│   ├── api.js          # API呼び出し
│   └── utils.js        # ユーティリティ
└── assets/
    └── team-logos/     # 球団ロゴ（オプション）
```

#### 2. 外部ライブラリの読み込み

`index.html`でCDN経由でChart.jsを読み込み:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

#### 3. API接続設定

`js/api.js`でAPIエンドポイントを設定:
```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

## Development Workflow

### 1. 新機能の開発

```bash
# 新しいブランチを作成
git checkout -b feature/new-feature

# コードを編集
# ...

# テストを実行
cd backend
pytest

# コミット
git add .
git commit -m "feat: add new feature"

# プッシュ
git push origin feature/new-feature
```

### 2. テストの実行

#### バックエンドテスト

```bash
cd backend

# すべてのテストを実行
pytest

# カバレッジ付きで実行
pytest --cov=src --cov-report=html

# 特定のテストファイルのみ実行
pytest tests/test_scraper.py

# 詳細出力
pytest -v
```

#### フロントエンドテスト（将来的に追加）

```bash
cd frontend

# Jestテストの実行
npm test

# E2Eテストの実行
npx playwright test
```

### 3. デバッグ

#### バックエンドデバッグ

```bash
# Flaskデバッグモードで起動
export FLASK_DEBUG=1  # macOS/Linux
set FLASK_DEBUG=1     # Windows
python src/api.py
```

#### フロントエンドデバッグ

- ブラウザの開発者ツール（F12）を使用
- Console タブでJavaScriptエラーを確認
- Network タブでAPI呼び出しを確認

## API Usage Examples

### 1. 現在シーズンのデータ取得

```bash
curl http://localhost:5000/api/standings
```

### 2. 特定年度のデータ取得

```bash
curl "http://localhost:5000/api/standings?year=2025"
```

### 3. 期間指定でデータ取得

```bash
curl "http://localhost:5000/api/standings?year=2025&startMonth=7&endMonth=9"
```

### 4. 球団情報の取得

```bash
curl http://localhost:5000/api/teams
```

### 5. ヘルスチェック

```bash
curl http://localhost:5000/api/health
```

## Common Issues & Solutions

### Issue 1: CORS エラー

**症状**: ブラウザコンソールに「CORS policy」エラーが表示される

**解決策**:
```python
# backend/src/api.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # すべてのオリジンを許可
```

### Issue 2: スクレイピング失敗

**症状**: 「データの取得に失敗しました」エラー

**原因**:
- NPB公式サイトのHTML構造変更
- ネットワーク接続の問題
- レート制限

**解決策**:
1. NPB公式サイトのHTML構造を確認
2. `scraper.py`のセレクタを更新
3. リクエスト間隔を調整

### Issue 3: グラフが表示されない

**症状**: 空白のページが表示される

**チェックリスト**:
- [ ] Chart.jsが正しく読み込まれているか（開発者ツールで確認）
- [ ] APIからデータが返ってきているか（Networkタブで確認）
- [ ] JavaScriptエラーがないか（Consoleタブで確認）
- [ ] Canvas要素が存在するか（Elementsタブで確認）

### Issue 4: Python仮想環境が有効化されない

**Windows PowerShell**:
```powershell
# 実行ポリシーの変更が必要な場合
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 仮想環境の有効化
venv\Scripts\Activate.ps1
```

## Performance Tips

### 1. データキャッシュの有効化

```python
# backend/src/api.py
from functools import lru_cache

@lru_cache(maxsize=128)
def get_standings_cached(year, start_month, end_month):
    return get_standings(year, start_month, end_month)
```

### 2. フロントエンドの最適化

```javascript
// LocalStorageでキャッシュ
const cacheKey = `standings_${year}_${startDate}_${endDate}`;
const cached = localStorage.getItem(cacheKey);
if (cached) {
    return JSON.parse(cached);
}
```

### 3. Chart.jsのパフォーマンス設定

```javascript
const config = {
    type: 'line',
    data: chartData,
    options: {
        animation: false,  // アニメーション無効化
        parsing: false,    // データ解析スキップ
        normalized: true   // 正規化データ
    }
};
```

## Next Steps

### 開発を始める前に

1. [spec.md](./spec.md) - 機能仕様を確認
2. [plan.md](./plan.md) - 実装計画を確認
3. [data-model.md](./data-model.md) - データモデルを理解
4. [contracts/api.yaml](./contracts/api.yaml) - APIコントラクトを確認

### 実装の順序

1. **Phase 1**: バックエンドAPI実装
   - スクレイピングロジック
   - データ解析
   - APIエンドポイント

2. **Phase 2**: フロントエンド実装
   - HTML/CSS構造
   - API呼び出し
   - グラフ描画

3. **Phase 3**: テスト実装
   - ユニットテスト
   - 統合テスト
   - E2Eテスト

4. **Phase 4**: デプロイ
   - Vercel/Netlifyへのデプロイ
   - 本番環境の設定

## Resources

### ドキュメント

- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [BeautifulSoup4 Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### チュートリアル

- [Chart.js Getting Started](https://www.chartjs.org/docs/latest/getting-started/)
- [Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- [Web Scraping with Python](https://realpython.com/beautiful-soup-web-scraper-python/)

### コミュニティ

- [Chart.js GitHub](https://github.com/chartjs/Chart.js)
- [Flask GitHub](https://github.com/pallets/flask)
- [Stack Overflow](https://stackoverflow.com/)

## Support

問題が発生した場合:
1. このQuickstartガイドを再確認
2. [spec.md](./spec.md)のEdge Casesを確認
3. GitHubのIssuesで質問
4. プロジェクトメンバーに相談