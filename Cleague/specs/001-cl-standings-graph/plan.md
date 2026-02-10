# Implementation Plan: セ・リーグ順位推移グラフ

**Branch**: `001-cl-standings-graph` | **Date**: 2026-02-10 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-cl-standings-graph/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

インタラクティブなWebアプリケーションとして、日本プロ野球セ・リーグの順位推移を折れ線グラフで可視化する。ユーザーは年度と期間を指定でき、リアルタイムでデータを取得して表示する。各球団の線は球団カラーで描画され、ホバーでツールチップ表示、凡例クリックで表示/非表示の切り替えが可能。

技術アプローチ：
- フロントエンド：HTML/CSS/JavaScriptによるシングルページアプリケーション
- グラフライブラリ：Chart.jsまたはD3.jsを使用
- データ取得：Webスクレイピング（Pythonバックエンド）
- デプロイ：静的ホスティング + サーバーレス関数

## Technical Context

**Language/Version**: 
- Frontend: JavaScript (ES6+) / HTML5 / CSS3
- Backend: Python 3.11+ (データ取得用)

**Primary Dependencies**: 
- Frontend: Chart.js 4.x (グラフ描画ライブラリ)
- Backend: BeautifulSoup4 / Requests (Webスクレイピング)
- Optional: Flask/FastAPI (APIサーバー、必要に応じて)

**Storage**: 
- キャッシュ: ブラウザLocalStorage（取得済みデータの一時保存）
- 永続化: 不要（リアルタイム取得のため）

**Testing**: 
- Frontend: Jest (ユニットテスト) + Playwright (E2Eテスト)
- Backend: pytest (スクレイピングロジックのテスト)

**Target Platform**: 
- Webブラウザ（Chrome, Firefox, Safari, Edge最新版）
- レスポンシブデザイン（デスクトップ優先、モバイル対応）

**Project Type**: Web application (frontend + backend API)

**Performance Goals**: 
- 初回ロード: 5秒以内（データ取得含む）
- グラフ描画: 1秒以内
- インタラクション応答: 100ms以内

**Constraints**: 
- スクレイピング対象サイトの利用規約遵守
- 過度なリクエストを避ける（レート制限考慮）
- ブラウザ互換性（ES6+サポート必須）

**Scale/Scope**: 
- 対象データ: セ・リーグ6球団 × 約200日/シーズン × 過去5年分
- 想定ユーザー数: 小規模（個人利用〜数十人）
- データポイント: 最大約6,000ポイント/グラフ

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Simplicity Check
- [x] Feature starts with minimal implementation (YAGNI principle applied)
  - MVP: 現在シーズンのグラフ表示のみから開始
  - 過去年度、期間指定は段階的に追加
- [x] New dependencies are justified and documented
  - Chart.js: 標準的なグラフライブラリ、学習コスト低、ドキュメント充実
  - BeautifulSoup4: Pythonの標準的スクレイピングライブラリ
- [x] Code prioritizes readability over clever abstractions
  - 直接的なDOM操作、明確な関数名
  - 過度なフレームワーク使用を避ける
- [x] Configuration is minimal with sensible defaults
  - デフォルト: 現在年、シーズン開始〜現在
  - 設定ファイル不要、コード内定数で管理

### Testing Check
- [x] Test strategy is defined for new features
  - ユニットテスト: データ解析ロジック、日付計算
  - 統合テスト: スクレイピング→データ変換→グラフ描画
  - E2Eテスト: ユーザーストーリー1-3の受け入れシナリオ
- [x] Bug fixes include reproduction tests
  - エッジケースのテストケースを事前定義
- [x] Tests are automated and integrated into CI/CD
  - GitHub Actions / GitLab CI での自動テスト実行
- [x] Integration tests cover critical user flows
  - P1ユーザーストーリー（デフォルト表示）を最優先

### Maintainability Check
- [x] Code is self-documenting with clear naming
  - 関数名: `fetchStandingsData()`, `renderChart()`, `parseTeamData()`
  - 変数名: `teamColors`, `dateRange`, `standingsData`
- [x] Complex logic includes explanatory comments
  - スクレイピングロジック、日付計算にコメント追加
- [x] APIs are consistent and predictable
  - RESTful API設計（必要な場合）
  - 一貫したエラーレスポンス形式
- [x] Breaking changes have migration paths
  - 初期バージョンのため該当なし
- [x] Technical debt is documented
  - TODO: キャッシュ戦略の最適化
  - TODO: エラーハンドリングの強化

## Project Structure

### Documentation (this feature)

```text
specs/001-cl-standings-graph/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
frontend/
├── index.html           # メインHTMLファイル
├── css/
│   └── styles.css       # スタイルシート
├── js/
│   ├── main.js          # エントリーポイント
│   ├── chart.js         # グラフ描画ロジック
│   ├── api.js           # データ取得API呼び出し
│   └── utils.js         # ユーティリティ関数（日付計算等）
└── assets/
    └── team-logos/      # 球団ロゴ（オプション）

backend/
├── src/
│   ├── scraper.py       # Webスクレイピングロジック
│   ├── parser.py        # データ解析・変換
│   ├── api.py           # APIエンドポイント（Flask/FastAPI）
│   └── models.py        # データモデル定義
└── tests/
    ├── test_scraper.py  # スクレイパーのテスト
    └── test_parser.py   # パーサーのテスト

tests/
├── e2e/
│   └── standings-graph.spec.js  # E2Eテスト（Playwright）
└── integration/
    └── test_data_flow.py        # 統合テスト
```

**Structure Decision**: Web application構造を選択。フロントエンドとバックエンドを分離し、フロントエンドは静的ファイルとして配信、バックエンドはAPIサーバーまたはサーバーレス関数として実装。この構造により、フロントエンドの独立したテスト・デプロイが可能で、バックエンドのスケーリングも容易。

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

該当なし - すべてのConstitution Checkに合格