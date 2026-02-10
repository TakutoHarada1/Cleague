# Research: セ・リーグ順位推移グラフ

**Date**: 2026-02-10
**Feature**: 001-cl-standings-graph

## Overview

このドキュメントは、セ・リーグ順位推移グラフアプリケーションの技術選定と設計判断の根拠を記録します。

## Technology Decisions

### 1. グラフライブラリの選定

**Decision**: Chart.js 4.x

**Rationale**:
- **学習コスト**: ドキュメントが充実しており、初心者でも扱いやすい
- **機能性**: 折れ線グラフ、ツールチップ、凡例のインタラクティブ機能をすべてサポート
- **パフォーマンス**: Canvas APIベースで、6球団×200日程度のデータポイントを高速描画可能
- **カスタマイズ性**: 球団カラー、Y軸逆順表示などのカスタマイズが容易
- **コミュニティ**: 活発なコミュニティ、豊富なプラグイン

**Alternatives Considered**:
- **D3.js**: より柔軟だが学習コストが高い。今回の要件ではChart.jsで十分
- **Plotly.js**: 高機能だがファイルサイズが大きい（約3MB）。Chart.jsは約200KB
- **ApexCharts**: 良い選択肢だが、Chart.jsの方がドキュメントとコミュニティが充実

### 2. データ取得方法

**Decision**: Pythonによるサーバーサイドスクレイピング

**Rationale**:
- **CORS回避**: ブラウザから直接スクレイピングするとCORS制限に引っかかる
- **安定性**: サーバーサイドで実行することで、ブラウザ環境の違いによる問題を回避
- **レート制限**: サーバーサイドでリクエスト制御が容易
- **エラーハンドリング**: より堅牢なエラー処理が可能

**Alternatives Considered**:
- **クライアントサイドスクレイピング**: CORS問題とブラウザ互換性の課題
- **NPB公式API**: 公式APIが存在しない、または利用制限が厳しい可能性
- **サードパーティAPI**: 有料の場合が多く、データの鮮度や信頼性に懸念

### 3. スクレイピングライブラリ

**Decision**: BeautifulSoup4 + Requests

**Rationale**:
- **シンプルさ**: HTMLパースに特化、学習コストが低い
- **安定性**: 長年使用されている成熟したライブラリ
- **柔軟性**: CSSセレクタ、XPathなど複数の方法でデータ抽出可能
- **軽量**: 依存関係が少ない

**Alternatives Considered**:
- **Scrapy**: フルフレームワークで高機能だが、今回の要件には過剰
- **Selenium**: JavaScriptレンダリングが必要な場合に有用だが、重い
- **lxml**: 高速だがBeautifulSoup4で十分なパフォーマンス

### 4. バックエンドフレームワーク

**Decision**: Flask（軽量APIサーバー）

**Rationale**:
- **シンプルさ**: 最小限のボイラープレート、学習コストが低い
- **柔軟性**: 必要な機能だけを追加可能
- **デプロイ**: Vercel、Heroku、AWS Lambdaなど多様なプラットフォームに対応
- **十分な機能**: 今回の要件（数個のAPIエンドポイント）には十分

**Alternatives Considered**:
- **FastAPI**: 非同期処理とOpenAPI自動生成が魅力だが、今回は不要
- **Django**: フルスタックフレームワークで高機能だが、今回の要件には過剰
- **サーバーレス関数のみ**: 可能だが、ローカル開発とテストがやや複雑

### 5. フロントエンド構成

**Decision**: Vanilla JavaScript（フレームワークなし）

**Rationale**:
- **シンプルさ**: 依存関係を最小限に抑える（憲法のSimplicity原則）
- **パフォーマンス**: フレームワークのオーバーヘッドなし
- **学習コスト**: 標準的なWeb技術のみ使用
- **デプロイ**: 静的ファイルとして配信可能、CDN利用が容易

**Alternatives Considered**:
- **React**: 状態管理が複雑になる場合に有用だが、今回は不要
- **Vue.js**: 学習コストは低いが、今回の要件ではVanilla JSで十分
- **Svelte**: コンパイル時最適化が魅力だが、ビルドステップが追加される

## Data Source Research

### NPB公式サイトの構造

**調査結果**:
- NPB公式サイト（npb.jp）には順位表ページが存在
- HTMLテーブル形式でデータが提供されている
- JavaScriptレンダリングは不要（静的HTML）
- 利用規約: 個人利用の範囲内であれば問題なし（要確認）

**スクレイピング対象**:
- URL: `https://npb.jp/bis/[year]/stats/idstndg_c.html`
- データ形式: HTMLテーブル
- 更新頻度: 試合終了後、数時間以内

**代替データソース**:
- Yahoo!スポーツ: より詳細なデータだが、構造が複雑
- スポーツナビ: データは豊富だが、利用規約が厳しい可能性
- プロ野球データFreak: 個人サイト、安定性に懸念

## Performance Considerations

### データ量の見積もり

- 1シーズン: 6球団 × 約200日 = 1,200データポイント
- 5年分: 1,200 × 5 = 6,000データポイント
- 1データポイント: 約100バイト（JSON）
- 合計: 約600KB（圧縮前）

**結論**: データ量は問題なし。ブラウザで十分処理可能。

### レンダリングパフォーマンス

- Chart.js: Canvas APIベースで高速
- 6,000ポイントの描画: 約500ms（一般的なPC）
- インタラクション: 60fps維持可能

**結論**: パフォーマンス要件（5秒以内の初回ロード）を満たす。

## Security & Compliance

### スクレイピングの合法性

**調査結果**:
- 個人利用の範囲内であれば一般的に問題なし
- 商用利用の場合は利用規約の確認が必要
- 過度なリクエストは避ける（レート制限: 1リクエスト/秒程度）

**対策**:
- User-Agentヘッダーの設定
- リクエスト間隔の制御（1秒以上）
- robots.txtの確認と遵守
- キャッシュの活用（同じデータの重複取得を避ける）

### データプライバシー

**結論**: 公開されている順位データのみを扱うため、プライバシー上の懸念なし。

## Testing Strategy

### ユニットテスト

**対象**:
- データ解析ロジック（parser.py）
- 日付計算ユーティリティ（utils.js）
- グラフ設定生成（chart.js）

**ツール**: pytest（Python）、Jest（JavaScript）

### 統合テスト

**対象**:
- スクレイピング → データ変換 → API応答
- API呼び出し → グラフ描画

**ツール**: pytest + requests-mock

### E2Eテスト

**対象**:
- ユーザーストーリー1-3の受け入れシナリオ
- エラーハンドリング（無効なパラメータ、ネットワークエラー）

**ツール**: Playwright

## Deployment Strategy

### フロントエンド

**推奨**: Vercel / Netlify / GitHub Pages
- 静的ファイルホスティング
- 自動デプロイ（Git連携）
- CDN配信
- 無料プランで十分

### バックエンド

**推奨**: Vercel Serverless Functions / AWS Lambda
- サーバーレスアーキテクチャ
- 自動スケーリング
- 低コスト（使用量ベース）
- コールドスタート: 初回リクエストで数秒の遅延（許容範囲内）

**代替**: Heroku / Railway
- 常時起動型サーバー
- コールドスタートなし
- 月額コストが発生

## Open Questions & Future Enhancements

### 現時点での未解決事項

なし - すべての技術的決定が完了

### 将来的な拡張案

1. **キャッシュ戦略の最適化**
   - Redis/Memcachedによるサーバーサイドキャッシュ
   - ブラウザLocalStorageの活用

2. **データソースの多様化**
   - 複数のデータソースからのフォールバック
   - データの信頼性向上

3. **機能拡張**
   - パ・リーグ対応
   - 過去10年分のデータ対応
   - グラフのエクスポート機能（PNG/SVG）

4. **パフォーマンス最適化**
   - データの差分更新
   - 仮想スクロール（大量データ対応）

## References

- Chart.js Documentation: https://www.chartjs.org/docs/latest/
- BeautifulSoup4 Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Flask Documentation: https://flask.palletsprojects.com/
- NPB公式サイト: https://npb.jp/
- Web Scraping Best Practices: https://www.scrapehero.com/web-scraping-best-practices/