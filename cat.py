import os
import requests
from bs4 import BeautifulSoup

search_query = 'cat'  # 搜索查询词
num_pages = 10  # 需要爬取的页数
folder_name = 'cat_images'  # 图片保存的文件夹名称

# 创建保存图片的文件夹
os.makedirs(folder_name, exist_ok=True)

# 循环爬取每一页的图片
for page in range(num_pages):
    start = page * 10  # 每页的起始索引
    url = f"https://www.google.com/search?q={search_query}&tbm=isch&start={start}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    
    # 下载每张图片并保存到文件夹
    for i, img in enumerate(image_tags):
        img_url = img['src']
        if img_url.startswith('http') or img_url.startswith('https'):
            response = requests.get(img_url)
            file_name = f"image_{page}_{i}.jpg"
            file_path = os.path.join(folder_name, file_name)
            with open(file_path, 'wb') as f:
                f.write(response.content)
                print(f"Downloaded {file_name}")

print("Image scraping completed.")
