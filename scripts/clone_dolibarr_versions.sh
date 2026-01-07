#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/Dolibarr/dolibarr.git"
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${BASE_DIR}/dolibarr"

mkdir -p "${TARGET_DIR}"

clone_version() {
  local version="$1"
  local branch="${version}.0"
  local dest="${TARGET_DIR}/${version}"

  if [[ -d "${dest}/.git" ]]; then
    echo "Dolibarr ${version} already cloned in ${dest}."
    return
  fi

  echo "Cloning Dolibarr ${version} (${branch}) into ${dest}..."
  git clone --branch "${branch}" --depth 1 "${REPO_URL}" "${dest}"
}

for version in 16 17 18 19 20 21 22; do
  clone_version "${version}"
done

cat <<'INFO'

✅ Clones completed.
- Sources are in ./dolibarr/<version>
- Drop custom modules into ./custom-modules
- Run: docker compose up -d

INFO
