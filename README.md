# Modrinth Server Pack Installer

**Modrinth Server Pack Installer** は、Modrinth 形式の ModpackのダウンロードURLを指定するだけで、自動で必要なModファイルのダウンロードと、Minecraft サーバー（Fabric / Forge / NeoForge）の構築を行うPythonスクリプトです。

## 🌟 Features

- **自動ダウンロード:** `modrinth.index.json` を解析し、必要なModファイル（`.jar`）を自動で指定ディレクトリにダウンロードします。
- **環境に応じた取捨選択:** サーバー実行に不要なクライアント専用Modをスキップし、サーバー環境に必要なものだけをインストールします（オプションでクライアント用構築にも対応）。
- **ローダーの自動インストール:** Modpackが要求する前提Mod（Fabric, Forge, NeoForge）のバージョンを自動で判別し、公式インストーラーを取得してサーバー環境を構築します。

## 🛠 Requirements

このスクリプトは内部でシステムのコマンドを呼び出しているため、**Linux, macOS, または WSL (Windows Subsystem for Linux)** 環境での実行を想定しています。

* **Python 3.x**
* **Java** (構築するMinecraftのバージョンに適合したもの)
* 以下のコマンドラインツールがインストールされていること:
  * `wget`
  * `curl`
  * `unzip`

## 🚀 Setup

リポジトリをクローンして、スクリプトがあるディレクトリに移動します。
※Pythonの標準ライブラリのみを使用しているため、`pip install` による追加パッケージの導入は不要です。

```bash
wget https://github.com/Tak0yakey/ModrinthServerPackInstaller/raw/refs/heads/main/modrinth.py
```

## 📖 Usage

基本的な使い方は、インストールしたい Modpack の直接ダウンロードリンク（URL）を引数に渡すだけです。

```bash
# 基本的な実行（デフォルトではカレントディレクトリの 'server' フォルダに構築されます）
python install.py "https://example.com/path/to/modpack.zip"
```

### オプション引数

| 引数 | 型 | デフォルト | 説明 |
| :--- | :---: | :---: | :--- |
| `url` | 必須 | なし | Modpack のダウンロード URL を指定します。 |
| `-d` | 文字列 | `server` | 構築先のディレクトリパスを指定します。 |
| `-c` | 真偽値 | `False` | `True` にするとクライアント用パックとしてModをインストールします。デフォルトは `False`（サーバー用）です。 |

### 実行例

**インストール先のディレクトリ名を変更する場合 (`-d`) :**
```bash
python modrinth.py "https://example.com/path/to/modpack.zip" -d ./my_server
```

**クライアント用のModパックを構築する場合 (`-c`) :**
```bash
python modrinth.py "https://example.com/path/to/modpack.zip" -c True
```

## ⚠️ Note

- **ディレクトリの初期化:** 指定した展開先ディレクトリ（デフォルトは `server`）が既に存在する場合、**スクリプト実行時に中身がすべて削除 (`shutil.rmtree`) されてから構築が始まります**。既存のワールドデータや設定ファイルを上書き・削除しないよう、実行パスには十分ご注意ください。
- **OSの互換性:** スクリプト内で `mv` や `rm`、`wget` などのシェルコマンドを `os.system()` 経由で使用しているため、純粋な Windows (コマンドプロンプトやPowerShell) では正常に動作しません。Windows をお使いの場合は **WSL** 上で実行してください。
