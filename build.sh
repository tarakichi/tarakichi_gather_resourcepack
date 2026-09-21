#!/usr/bin/env bash
# リソースパック（pack.zip）を作って、SHA1 を表示する。作業ツリーの内容から作る（コミット前でも使える）
set -euo pipefail
cd "$(dirname "$0")"
rm -f pack.zip
zip -r -X pack.zip pack.mcmeta pack.png assets > /dev/null
echo "pack.zip を作りました"
sha1sum pack.zip
