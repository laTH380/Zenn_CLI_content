def convert_header(header_dict):
    new_header_dict = {
        'title': header_dict['title'],
        'emoji': '👀',
        'type': 'tech', # tech: 技術記事 / idea: アイデア
        'topics': header_dict['tags'],
        'published': 'true',
        'published_at': header_dict['date']
    }
    samune = header_dict['featureImage']
    return new_header_dict, samune

def arrange_body(body, samune):
    new_body = f'![thumbnail]({samune}){body}'
    return new_body


def convert_body(body, image_conv_dir):
    conv_dict = {
        '{{< highlight html >}}' : '```html',
        '{{< highlight css >}}' : '```css',
        '{{< highlight js >}}' : '```js',
        '{{< highlight bash >}}' : '```bash',
        '{{< highlight python >}}' : '```python',
        '{{< /highlight >}}' : '```',
    }
    conv_dict = conv_dict | image_conv_dir
    for key, value in conv_dict.items():
        body = body.replace(key, value)
    return body



def convert_hugo_to_zenn(header_dict, body, image_conv_dir):
    # ヘッダを変換
    new_header_dict, samune = convert_header(header_dict)

    # 本文をに追加情報を追加
    new_body = arrange_body(body, samune)

    # 本文を変換
    new_body = convert_body(new_body, image_conv_dir)

    return new_header_dict, new_body