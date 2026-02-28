#!/usr/bin/env python3
import json
import argparse
# パーサーの作成
parser = argparse.ArgumentParser(description="サンプルのツール")

# 引数の設定
parser.add_argument("url", help="enter URL of Modpack")           # 必須の引数
#parser.add_argument("--age", type=int, default=20, help="年齢（数値）") # オプション引数

# 解析の実行
args = parser.parse_args()
print(args.url)