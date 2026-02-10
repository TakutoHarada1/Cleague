# Data Model: セ・リーグ順位推移グラフ

**Date**: 2026-02-10
**Feature**: 001-cl-standings-graph

## Overview

このドキュメントは、セ・リーグ順位推移グラフアプリケーションで使用するデータモデルを定義します。

## Core Entities

### 1. Team（球団）

セ・リーグに所属する6球団の情報を表現します。

**Attributes**:
- `id`: string - 球団の一意識別子（例: "giants", "tigers"）
- `name`: string - 球団の正式名称（例: "読売ジャイアンツ"）
- `shortName`: string - 球団の略称（例: "巨人"）
- `color`: string - 球団カラー（HEX形式、例: "#FF6600"）
- `league`: string - 所属リーグ（固定値: "central"）

**Validation Rules**:
- `id`: 必須、英数字のみ、小文字
- `name`: 必須、1-50文字
- `shortName`: 必須、1-10文字
- `color`: 必須、HEX形式（#RRGGBB）
- `league`: 必須、"central"固定

**Example**:
```json
{
  "id": "giants",
  "name": "読売ジャイアンツ",
  "shortName": "巨人",
  "color": "#FF6600",
  "league": "central"
}
```

**Predefined Teams**:
```json
[
  {
    "id": "giants",
    "name": "読売ジャイアンツ",
    "shortName": "巨人",
    "color": "#FF6600",
    "league": "central"
  },
  {
    "id": "tigers",
    "name": "阪神タイガース",
    "shortName": "阪神",
    "color": "#FFE600",
    "league": "central"
  },
  {
    "id": "dragons",
    "name": "中日ドラゴンズ",
    "shortName": "中日",
    "color": "#0057B8",
    "league": "central"
  },
  {
    "id": "carp",
    "name": "広島東洋カープ",
    "shortName": "広島",
    "color": "#FF0000",
    "league": "central"
  },
  {
    "id": "baystars",
    "name": "横浜DeNAベイスターズ",
    "shortName": "DeNA",
    "color": "#6A4C9C",
    "league": "central"
  },
  {
    "id": "swallows",
    "name": "東京ヤクルトスワローズ",
    "shortName": "ヤクルト",
    "color": "#00A650",
    "league": "central"
  }
]
```

### 2. StandingsData（順位データ）

特定日時における球団の順位情報を表現します。

**Attributes**:
- `date`: string - 日付（ISO 8601形式、例: "2026-05-15"）
- `teamId`: string - 球団ID（Teamエンティティへの参照）
- `rank`: integer - 順位（1-6）
- `wins`: integer - 勝数
- `losses`: integer - 敗数
- `draws`: integer - 引分数
- `winRate`: number - 勝率（0.000-1.000）
- `gamesBehind`: number - ゲーム差（首位からの差、0.0-）

**Validation Rules**:
- `date`: 必須、ISO 8601形式（YYYY-MM-DD）
- `teamId`: 必須、有効な球団ID
- `rank`: 必須、1-6の整数
- `wins`: 必須、0以上の整数
- `losses`: 必須、0以上の整数
- `draws`: 必須、0以上の整数
- `winRate`: 必須、0.000-1.000の範囲
- `gamesBehind`: 必須、0.0以上の数値

**Calculated Fields**:
- `winRate = wins / (wins + losses)` （引分は除外）
- `gamesBehind`: 首位チームとの勝敗差を2で割った値

**Example**:
```json
{
  "date": "2026-05-15",
  "teamId": "giants",
  "rank": 1,
  "wins": 35,
  "losses": 20,
  "draws": 2,
  "winRate": 0.636,
  "gamesBehind": 0.0
}
```

**Relationships**:
- 1つのStandingsDataは1つのTeamに属する（多対一）
- 1つの日付には6つのStandingsData（各球団1つずつ）が存在する

### 3. PeriodSettings（期間設定）

グラフ表示の対象期間を表現します。

**Attributes**:
- `year`: integer - 年度（例: 2026）
- `startDate`: string - 開始日（ISO 8601形式）
- `endDate`: string - 終了日（ISO 8601形式）
- `startMonth`: integer | null - 開始月（1-12、オプション）
- `endMonth`: integer | null - 終了月（1-12、オプション）

**Validation Rules**:
- `year`: 必須、1950-現在年の範囲
- `startDate`: 必須、ISO 8601形式、シーズン期間内（3月-10月）
- `endDate`: 必須、ISO 8601形式、startDate以降
- `startMonth`: オプション、1-12の整数
- `endMonth`: オプション、1-12の整数、startMonth以降

**Business Rules**:
- シーズン期間: 3月20日頃〜10月10日頃
- startDateはendDateより前でなければならない
- startMonthが指定された場合、その月の1日が開始日
- endMonthが指定された場合、その月の末日が終了日

**Example**:
```json
{
  "year": 2026,
  "startDate": "2026-03-20",
  "endDate": "2026-10-10",
  "startMonth": null,
  "endMonth": null
}
```

**Default Values**:
- パラメータなし: 現在年、シーズン開始〜現在日
- 年度のみ: 指定年、シーズン開始〜終了
- 年度+開始月: 指定年、開始月1日〜シーズン終了
- 年度+開始月+終了月: 指定年、開始月1日〜終了月末日

### 4. ChartData（グラフデータ）

Chart.jsに渡すグラフ描画用のデータ構造です。

**Attributes**:
- `labels`: string[] - X軸ラベル（日付の配列）
- `datasets`: Dataset[] - データセット配列（各球団の折れ線）

**Dataset Structure**:
- `label`: string - データセット名（球団名）
- `data`: number[] - Y軸データ（順位の配列）
- `borderColor`: string - 線の色（球団カラー）
- `backgroundColor`: string - 背景色（透明または薄い球団カラー）
- `tension`: number - 線の曲線度（0.0-1.0、推奨: 0.1）
- `pointRadius`: number - ポイントの半径（推奨: 3）
- `pointHoverRadius`: number - ホバー時のポイント半径（推奨: 5）

**Example**:
```json
{
  "labels": ["2026-03-20", "2026-03-21", "2026-03-22"],
  "datasets": [
    {
      "label": "巨人",
      "data": [1, 1, 2],
      "borderColor": "#FF6600",
      "backgroundColor": "rgba(255, 102, 0, 0.1)",
      "tension": 0.1,
      "pointRadius": 3,
      "pointHoverRadius": 5
    },
    {
      "label": "阪神",
      "data": [2, 3, 1],
      "borderColor": "#FFE600",
      "backgroundColor": "rgba(255, 230, 0, 0.1)",
      "tension": 0.1,
      "pointRadius": 3,
      "pointHoverRadius": 5
    }
  ]
}
```

## Data Flow

### 1. データ取得フロー

```
User Request
    ↓
Frontend (index.html)
    ↓
API Request (api.js)
    ↓
Backend API (api.py)
    ↓
Scraper (scraper.py)
    ↓
NPB Website
    ↓
HTML Response
    ↓
Parser (parser.py)
    ↓
StandingsData[]
    ↓
API Response (JSON)
    ↓
Frontend (chart.js)
    ↓
ChartData
    ↓
Chart.js
    ↓
Canvas Rendering
```

### 2. データ変換フロー

```
HTML Table
    ↓ (scraper.py)
Raw Data (dict)
    ↓ (parser.py)
StandingsData[]
    ↓ (api.py)
JSON Response
    ↓ (api.js)
JavaScript Object
    ↓ (chart.js)
ChartData
    ↓ (Chart.js)
Visual Graph
```

## State Management

### Frontend State

**Application State**:
- `currentPeriod`: PeriodSettings - 現在表示中の期間
- `standingsData`: StandingsData[] - 取得済みの順位データ
- `visibleTeams`: Set<string> - 表示中の球団ID（凡例クリックで制御）
- `isLoading`: boolean - データ取得中フラグ
- `error`: string | null - エラーメッセージ

**State Transitions**:
1. 初期状態: `isLoading=false, standingsData=[], error=null`
2. データ取得開始: `isLoading=true, error=null`
3. データ取得成功: `isLoading=false, standingsData=[...]`
4. データ取得失敗: `isLoading=false, error="エラーメッセージ"`
5. 凡例クリック: `visibleTeams`を更新、グラフ再描画

### Backend State

**Stateless Design**: バックエンドは状態を保持しない
- 各リクエストは独立して処理
- キャッシュはオプション（将来的な拡張）

## Data Validation

### Input Validation

**URL Parameters**:
- `year`: 整数、1950-現在年
- `startMonth`: 整数、1-12
- `endMonth`: 整数、1-12、startMonth以降

**Validation Errors**:
- 400 Bad Request: 無効なパラメータ
- 404 Not Found: データが存在しない年度
- 500 Internal Server Error: スクレイピング失敗

### Output Validation

**API Response**:
- 必須フィールドの存在確認
- データ型の検証
- 値の範囲チェック

## Performance Considerations

### Data Size

- 1日分のデータ: 6球団 × 約100バイト = 600バイト
- 1シーズン: 200日 × 600バイト = 120KB
- 5年分: 120KB × 5 = 600KB

**結論**: データサイズは小さく、パフォーマンス上の問題なし

### Caching Strategy

**Browser Cache**:
- LocalStorageに取得済みデータを保存
- キャッシュキー: `standings_${year}_${startDate}_${endDate}`
- 有効期限: 1日（試合結果は日次更新）

**Server Cache** (将来的な拡張):
- Redis/Memcachedでスクレイピング結果をキャッシュ
- 有効期限: 1時間

## Error Handling

### Error Types

1. **Network Error**: スクレイピング対象サイトへの接続失敗
2. **Parse Error**: HTMLパースエラー、予期しない構造
3. **Validation Error**: 無効なパラメータ
4. **Not Found Error**: データが存在しない

### Error Response Format

```json
{
  "error": {
    "code": "SCRAPING_FAILED",
    "message": "データの取得に失敗しました",
    "details": "Connection timeout"
  }
}
```

## Future Enhancements

### Planned Extensions

1. **Historical Data Storage**
   - データベースに過去データを保存
   - スクレイピング頻度を削減

2. **Real-time Updates**
   - WebSocketによるリアルタイム更新
   - 試合中の順位変動を即座に反映

3. **Advanced Analytics**
   - 勝率推移グラフ
   - ゲーム差推移グラフ
   - 球団間の直接対決成績

4. **Data Export**
   - CSV/JSONエクスポート
   - グラフ画像エクスポート（PNG/SVG）