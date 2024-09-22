def convert_header(header_dict):
    new_header_dict = {
        'title': header_dict['title'],
        'emoji': "👀",
        'type': "tech", # tech: 技術記事 / idea: アイデア
        'topics': header_dict['tags'],
        'published': 'true',
        'published_at': header_dict['date'] + " 00:00"
    }
    return new_header_dict

def convert_body(body, image_conv_dir):
    conv_dict = {

    }
    conv_dict = conv_dict | image_conv_dir
    new_body = ""
    for key, value in conv_dict.items():
        new_body = body.replace(key, value)
    return new_body

def convert_hugo_to_zenn(header_dict, body, image_conv_dir):
    # ヘッダを変換
    new_header_dict = convert_header(header_dict)

    # 本文を変換
    new_body = convert_body(body, image_conv_dir)
       
    return new_header_dict, new_body