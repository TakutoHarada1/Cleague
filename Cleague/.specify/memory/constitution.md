<!--
Sync Impact Report
==================
Version: N/A → 1.0.0 (Initial Constitution)
Modified Principles: N/A (Initial creation)
Added Sections:
- Core Principles (3 principles: Simplicity, Testing, Maintainability)
- Development Workflow
- Quality Standards
- Governance
Removed Sections: N/A
Templates Requiring Updates:
✅ .specify/templates/plan-template.md (updated - Constitution Check section aligned with 3 principles)
✅ .specify/templates/spec-template.md (reviewed - already aligned with Testing and Maintainability principles)
✅ .specify/templates/tasks-template.md (reviewed - already aligned with Testing principle and independent story implementation)
Follow-up TODOs: None
-->

# Cleague Constitution

## Core Principles

### I. Simplicity

シンプルさを最優先とする。複雑さは必要性が明確に証明された場合のみ許容される。

**必須要件**:
- すべての機能は最小限の実装から開始すること（YAGNI原則）
- 新しい依存関係の追加は、その必要性を文書化し承認を得ること
- コードは読みやすさを優先し、過度な抽象化を避けること
- 設定ファイルは最小限に保ち、合理的なデフォルト値を提供すること

**根拠**: シンプルなシステムは理解しやすく、保守しやすく、バグが少ない。複雑さは技術的負債の主要な原因である。

### II. Testing

すべてのコードは適切にテストされなければならない。テストは品質保証の基盤である。

**必須要件**:
- 新機能には対応するテストを含めること
- バグ修正には再現テストを含めること
- テストは自動化され、CI/CDパイプラインで実行されること
- テストカバレッジは意味のある指標として使用すること（目標ではなく）
- 統合テストは重要なユーザーフローをカバーすること

**根拠**: テストは回帰を防ぎ、リファクタリングを安全にし、ドキュメントとしても機能する。

### III. Maintainability

長期的な保守性を考慮した設計と実装を行う。

**必須要件**:
- コードは自己文書化されていること（明確な命名、適切な構造）
- 複雑なロジックにはコメントで意図を説明すること
- APIは一貫性があり、予測可能であること
- 破壊的変更は慎重に検討し、移行パスを提供すること
- 技術的負債は記録し、定期的に見直すこと

**根拠**: 保守性の高いコードベースは、長期的な開発速度を維持し、新しいメンバーのオンボーディングを容易にする。

## Development Workflow

### コードレビュー
- すべての変更はプルリクエストを通じて行うこと
- 少なくとも1名のレビュー承認が必要
- レビューは建設的で、学習の機会として活用すること

### ブランチ戦略
- `main`ブランチは常にデプロイ可能な状態を維持
- 機能開発は`feature/`プレフィックスのブランチで行う
- バグ修正は`fix/`プレフィックスのブランチで行う

### コミットメッセージ
- Conventional Commits形式を使用すること
- 変更の理由と影響を明確に記述すること

## Quality Standards

### コード品質
- リンターとフォーマッターの設定に従うこと
- 警告は無視せず、適切に対処すること
- コードレビューでの指摘事項は真摯に受け止めること

### ドキュメント
- READMEは最新の状態を保つこと
- APIの変更は必ずドキュメントを更新すること
- 複雑な機能には使用例を含めること

### パフォーマンス
- パフォーマンスの問題は測定してから最適化すること
- 早すぎる最適化は避けること
- ボトルネックが特定された場合は優先的に対処すること

## Governance

### 憲法の優先順位
この憲法はすべての開発プラクティスに優先する。憲法との矛盾が生じた場合は、憲法に従うこと。

### 修正手順
憲法の修正には以下が必要:
1. 修正提案の文書化（理由、影響範囲、移行計画）
2. チームメンバーの承認
3. バージョン番号の適切な更新
4. 関連ドキュメントの同期

### バージョニング
- MAJOR: 後方互換性のない原則の削除・再定義
- MINOR: 新原則の追加、既存原則の大幅な拡張
- PATCH: 文言の明確化、タイポ修正

### コンプライアンス
- すべてのプルリクエストは憲法への準拠を確認すること
- 憲法違反は正当な理由がない限り却下すること
- 定期的に憲法の有効性を見直すこと

**Version**: 1.0.0 | **Ratified**: 2026-02-10 | **Last Amended**: 2026-02-10