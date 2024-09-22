import sys
import os
import shutil
import subprocess

from lib import get_info_from_hugo_article, convert_hugo_zenn


sorce_post_bundle_dir_path = sys.argv[1] #Hugoの記事のpost_bundleのディレクトリパス
zenn_dir_path="C:/Users/thiro/Documents/CreationProgram/my_homepage/Zenn_CLI_content" #ZennCLIのディレクトリパス


# Hugoの記事から必要な情報を取得
header_dict, body, image_files_name = get_info_from_hugo_article.get_info(sorce_post_bundle_dir_path)

# ZennCLIのディレクトリにデフォルト記事作成
os.chdir(f'{zenn_dir_path}')
command = [os.path.join("C:/Program Files/nodejs/npx.cmd"), "zenn", "new:article"]
result = subprocess.run(command, check=True, text=True, capture_output=True)
created_article_path = result.stdout.split(' ')[1]
created_article_name = os.path.splitext(os.path.basename(created_article_path))[0]

#画像ディレクトリを作成し、画像をコピー
image_dir_path = f'./images/articles/{created_article_name}'
os.mkdir(image_dir_path)
image_conv_dir = {}
for image_file_name in image_files_name:
    source_image_path = os.path.join(sorce_post_bundle_dir_path, image_file_name)
    dest_image_path = os.path.join(image_dir_path, image_file_name)
    shutil.copy(source_image_path, dest_image_path)
    image_conv_dir[f'({image_file_name})'] = f'(/images/articles/{created_article_name}/{image_file_name})'

# Zenn用の記事に変換
new_header_dict, new_body = convert_hugo_zenn.convert_hugo_to_zenn(header_dict, body, image_conv_dir)

# 記事を書き込む
with open(f'./articles/{created_article_name}.md', 'w', encoding='utf-8') as file:
    file.write('---\n')
    for key, value in new_header_dict.items():
        file.write(f'{key}: {value}\n')
    file.write('---\n')
    file.write(new_body)

# 記事を投稿
subprocess.run(["git", "add", "."], check=True, text=True, capture_output=True)
subprocess.run(["git", "commit", "-m", "記事投稿"], check=True, text=True, capture_output=True)
subprocess.run(["git", "push"], check=True, text=True, capture_output=True)