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
git clone https://github.com/Tak0yakey/ModrinthServerPackInstaller.git
cd ModrinthServerPackInstaller
```
