#!/usr/bin/env python3
from importlib.resources import path
import shutil
from pathlib import Path
import pprint
import json
import argparse
import os
# パーサーの作成
parser = argparse.ArgumentParser(description="サンプルのツール")

# 引数の設定
parser.add_argument("url", help="enter URL of Modpack")           # 必須の引数
parser.add_argument("-d", type=str, default="server", help="path") # オプション引数
parser.add_argument("-c", type=bool, default=False, help="if true,install client pack. if false,install server pack")
# 解析の実行
args = parser.parse_args()
print(args.url)
targ_path = Path(args.d)
if targ_path.is_dir():
    shutil.rmtree(targ_path)
os.system(f'wget "{args.url}" -O download.zip && unzip download.zip -d {args.d}/&& rm download.zip')
with open(f"{args.d}/modrinth.index.json","r") as r:
    data = json.load(r)
pprint.pprint(data)
# move overrides
os.system(f"mv {targ_path}/overrides/* {targ_path}/")
file_index = data["files"]
for file in file_index:
    if (args.c and (file["env"]["client"] != "required")) or ((not args.c) and (file["env"]["server"] != "required")):
        continue
    os.system(f"curl --create-dirs -o {targ_path}/{file["path"]} {file["downloads"][0]}")
deps = data["dependencies"]
minecraft_ver = deps["minecraft"]
if "neoforge" in deps:
    print("installing neoforge")
    neoforge_ver = deps["neoforge"]
    url = f"https://maven.neoforged.net/releases/net/neoforged/neoforge/{neoforge_ver}/neoforge-{neoforge_ver}-installer.jar"
    os.system(f"wget -O {targ_path}/installer.jar {url}")
    os.system(f"cd {targ_path}&&java -jar installer.jar --installServer")
elif "forge" in deps:
    print("installing forge")
    forge_ver = deps["forge"]
    url = f"http://files.minecraftforge.net/maven/net/minecraftforge/forge/{minecraft_ver}-{forge_ver}/forge-{minecraft_ver}-{forge_ver}-installer.jar"
    os.system(f"wget -O {targ_path}/installer.jar {url}")
    os.system(f"cd {targ_path}&&java -jar installer.jar --installServer")
elif "fabric" in deps:
    print("installing fabric")
    fabric_ver = deps["fabric"]
    url = "https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.1.1/fabric-installer-1.1.1.jar"
    os.system(f"wget -O {targ_path}/installer.jar {url}")
    os.system(f"cd {targ_path}&& java -jar fabric-installer-1.1.1.jar -loader {fabric_ver} -mcversion {minecraft_ver} server")