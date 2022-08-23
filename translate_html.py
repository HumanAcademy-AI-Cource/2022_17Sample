#!/usr/bin/env python3

# ライブラリのインポート
import boto3


# 読み込むファイル名
in_filename = "README.html"
out_filename = "README_EN.html"

# AWSを使った翻訳の準備
translate = boto3.client(service_name="translate")

# HTMLファイルを読み込む
with open(in_filename, "r") as f:
    read_data = f.read()

# HTMLファイルの中身を翻訳
translated_text = translate.translate_text(
    Text=read_data,
    SourceLanguageCode="ja",
    TargetLanguageCode="en"
)["TranslatedText"]
print("○  翻訳前: \n{}".format(read_data))
print("○  翻訳後: \n{}".format(translated_text))
print("=================================================")

with open(out_filename, "w") as f:
    f.write(translated_text)
