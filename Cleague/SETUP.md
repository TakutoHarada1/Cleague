# セットアップ手順書

## 前提条件

このアプリケーションを実行するには、以下のソフトウェアが必要です：

### 1. Python 3.11以上のインストール

**現在、Pythonがシステムにインストールされていません。**

#### Windowsへのインストール手順

1. **Python公式サイトからダウンロード**
   - https://www.python.org/downloads/ にアクセス
   - 「Download Python 3.11.x」ボタンをクリック

2. **インストーラーを実行**
   - ダウンロードした `.exe` ファイルを実行
   - ⚠️ **重要**: 「Add Python to PATH」にチェックを入れる
   - 「Install Now」をクリック

3. **インストール確認**
   ```bash
   python --version
   ```
   または
   ```bash
   py --version
   ```

---

## アプリケーションのセットアップ

### ステップ1: 仮想環境の作成

```bash
cd backend
python -m venv venv
```

### ステップ2: 仮想環境の有効化

**Windows (コマンドプロンプト)**:
```bash
venv\Scripts\activate
```

**Windows (PowerShell)**:
```bash
venv\Scripts\Activate.ps1
```

**macOS/Linux**:
```bash
source venv/bin/activate
```

### ステップ3: 依存関係のインストール

```bash
pip install -r requirements.txt
```

---

## アプリケーションの起動

### バックエンドサーバーの起動

```bash
cd backend/src
python api.py
```

サーバーが `http://localhost:5000` で起動します。

### フロントエンドの表示

#### 方法1: 直接HTMLを開く

1. エクスプローラーで `frontend/index.html` を開く
2. ブラウザで表示される

#### 方法2: HTTPサーバーを使用（推奨）

新しいターミナルを開いて：

```bash
cd frontend
python -m http.server 8000
```

ブラウザで `http://localhost:8000` にアクセス

---

## 動作確認

### 1. バックエンドの確認

ブラウザで以下のURLにアクセス：
- http://localhost:5000/api/health
- http://localhost:5000/api/teams

正常に動作していれば、JSONデータが表示されます。

### 2. フロントエンドの確認

ブラウザで `http://localhost:8000` にアクセスすると、セ・リーグ順位推移グラフが表示されます。

---

## トラブルシューティング

### エラー: "Python was not found"

→ Pythonがインストールされていないか、PATHに追加されていません。
   上記の「Python 3.11以上のインストール」を参照してください。

### エラー: "No module named 'flask'"

→ 依存関係がインストールされていません。
   ```bash
   pip install -r backend/requirements.txt
   ```

### エラー: "Address already in use"

→ ポート5000または8000が既に使用されています。
   - 他のアプリケーションを終了するか
   - 別のポートを使用してください：
     ```bash
     python api.py --port 5001
     python -m http.server 8001
     ```

### グラフが表示されない

1. **バックエンドが起動しているか確認**
   - `http://localhost:5000/api/health` にアクセス

2. **ブラウザのコンソールを確認**
   - F12キーを押して開発者ツールを開く
   - Consoleタブでエラーメッセージを確認

3. **CORSエラーの場合**
   - フロントエンドをHTTPサーバー経由で開いてください（方法2）
   - 直接HTMLファイルを開くと、CORSエラーが発生する可能性があります

---

## 次のステップ

アプリケーションが正常に起動したら：

1. ✅ 現在シーズンのグラフが表示されることを確認
2. ✅ 凡例をクリックして球団の表示/非表示を切り替え
3. ✅ グラフにホバーしてツールチップが表示されることを確認

問題がある場合は、README.mdの「注意事項」セクションを参照してください。