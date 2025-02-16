#!/bin/zsh

# GitHubリポジトリのURL（自分のGitHubアカウントのURLに変更する）
REPO_URL="git@github.com:your-username/your-repository.git"

# 必要なツールのチェック
if ! command -v git &> /dev/null; then
    echo "❌ Gitがインストールされていません。インストールしてください。"
    exit 1
fi

# Gitリポジトリの初期化（必要なら）
if [ ! -d ".git" ]; then
    echo "🚀 Gitリポジトリを初期化中..."
    git init
    git remote add origin "$REPO_URL"
fi

# ファイルを追加
echo "📂 変更を追加..."
git add .

# コミットメッセージ（ユーザーに入力させる or 自動で日時を入れる）
echo "📝 コミットメッセージを入力（空なら自動設定）:"
read COMMIT_MSG
if [[ -z "$COMMIT_MSG" ]]; then
    COMMIT_MSG="Auto commit - $(date)"
fi

git commit -m "$COMMIT_MSG"

# ブランチの確認と設定
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

if [[ "$CURRENT_BRANCH" != "main" && "$CURRENT_BRANCH" != "master" ]]; then
    echo "🔀 ブランチを main に設定..."
    git branch -M main
fi

# GitHubへプッシュ
echo "🚀 GitHubへアップロード中..."
git push -u origin main

echo "✅ 完了！GitHubへアップロードされました。"
