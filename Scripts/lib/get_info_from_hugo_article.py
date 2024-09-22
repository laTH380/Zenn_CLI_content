import os
import yaml

def get_info(hugo_post_bundle_path):
    md_path = hugo_post_bundle_path + '/index.md'

    # mdからヘッダー部分と本文を取得
    with open(md_path, 'r', encoding='utf-8') as file:
        content = file.read()
    ## ヘッダー部分を分割
    header, body = content.split('---', 2)[1:3]
    ## ヘッダーを辞書に変換
    header_dict = yaml.safe_load(header)
    
    # bundleに含まれる画像の名前を取得
    image_files_name = [f for f in os.listdir(hugo_post_bundle_path) if os.path.isfile(os.path.join(hugo_post_bundle_path, f)) and f != 'index.md']

    return header_dict, body, image_files_name