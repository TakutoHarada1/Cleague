# VSCodeでWSL(Ubuntu)のホームディレクトリを開く方法

## 前提条件

### 1. WSL拡張機能の確認とインストール

VSCodeに「WSL」拡張機能がインストールされているか確認します:

1. VSCodeの左サイドバーで拡張機能アイコン(四角が4つ並んだアイコン)をクリック
2. 検索ボックスに「WSL」と入力
3. 「WSL」(Microsoft製)が表示されたら:
   - インストール済みの場合: 「インストール済み」と表示されます
   - 未インストールの場合: 「インストール」ボタンをクリックしてインストール

## 方法1: コマンドパレットから開く(推奨)

最も簡単で確実な方法です:

1. VSCodeで `Ctrl+Shift+P` を押してコマンドパレットを開く
2. 「WSL: Open Folder in WSL」と入力して選択
3. WSLディストリビューション一覧から「Ubuntu」を選択
4. ファイルブラウザが開くので、ホームディレクトリ(`/home/ユーザー名`)を選択
5. 「OK」をクリック

VSCodeが再起動し、WSL環境でフォルダが開きます。

## 方法2: WSLターミナルから開く

コマンドラインに慣れている場合に便利です:

1. Windowsのスタートメニューから「Ubuntu」を起動
2. ホームディレクトリにいることを確認(デフォルトでホームディレクトリにいます)
   ```bash
   pwd  # 現在のディレクトリを確認
   ```
3. VSCodeを起動:
   ```bash
   code .
   ```

初回実行時は、VSCode Serverのインストールが自動的に行われます。

## 方法3: リモートエクスプローラーから開く

視覚的に操作したい場合に便利です:

1. VSCodeの左サイドバーで「リモートエクスプローラー」アイコンをクリック
   - アイコンが見つからない場合は、`Ctrl+Shift+P` → 「Remote-Explorer: Focus on Remote View」
2. 「WSL Targets」セクションを展開
3. 「Ubuntu」を見つけて、右側のフォルダアイコンをクリック
4. ホームディレクトリ(`/home/ユーザー名`)を選択

## 方法4: 直接パスを指定して開く

特定のパスがわかっている場合:

1. VSCodeで `Ctrl+K` → `Ctrl+O` (フォルダを開く)
2. アドレスバーに以下のように入力:
   ```
   \\wsl$\Ubuntu\home\ユーザー名
   ```
3. Enterキーを押す

## 確認方法

WSL環境で正しく開けているか確認:

1. VSCodeの左下隅を確認
   - 「WSL: Ubuntu」と表示されていればOK
2. ターミナルを開く(`Ctrl+``)
   - Bashプロンプトが表示されればOK
   - `uname -a` を実行してLinuxと表示されればOK

## トラブルシューティング

### WSL拡張機能が見つからない

- VSCodeを最新版に更新してください
- 拡張機能マーケットプレイスで「ms-vscode-remote.remote-wsl」を検索

### `code` コマンドが見つからない

WSLターミナルで以下を実行:
```bash
# PATHを確認
echo $PATH

# VSCode Serverを手動でインストール
code --install-extension ms-vscode-remote.remote-wsl
```

### 接続が遅い、または失敗する

1. WSLを再起動:
   ```bash
   wsl --shutdown
   ```
2. Windowsを再起動
3. ファイアウォール設定を確認

### ファイルのパーミッションエラー

WSL内で適切な権限を設定:
```bash
chmod 755 /home/ユーザー名
```

## 便利なTips

### デフォルトでWSLで開く設定

VSCodeの設定(`Ctrl+,`)で以下を追加:
```json
{
  "remote.WSL.useShellEnvironment": true,
  "terminal.integrated.defaultProfile.windows": "Ubuntu (WSL)"
}
```

### WSLのホームディレクトリをWindowsから参照

Windowsエクスプローラーのアドレスバーに:
```
\\wsl$\Ubuntu\home\ユーザー名
```

### よく使うフォルダをワークスペースに保存

1. WSLフォルダを開いた状態で
2. `ファイル` → `ワークスペースに名前を付けて保存`
3. 次回から簡単に開けます

## 参考リンク

- [VSCode WSL拡張機能ドキュメント](https://code.visualstudio.com/docs/remote/wsl)
- [WSL公式ドキュメント](https://docs.microsoft.com/ja-jp/windows/wsl/)