import requests
import parsel

# 爬虫表情包：https://www.fabiaoqing.com/biaoqing/lists/page/1.html

base_url = "https://www.fabiaoqing.com/biaoqing/lists/page/{}.html"
dir_name = "images/"

'''
下载图片
'''
def download_img(title, url):
    img_response = requests.get(url)
    suffix = url.split('.')[-1]
    file_name = title + '.' + suffix
    try:
        with open(dir_name + file_name, mode='wb') as f:
            f.write(img_response.content)
    except:
        print('保存错误', file_name)

'''
下载一页
'''
def download_page(page_url):
    data_list = []
    response = requests.get(page_url)
    selector = parsel.Selector(response.text)
    imgs = selector.css('img.ui.image.lazy')
    for img in imgs:
        url = img.css('img::attr(data-original)').get()
        title = img.css('img::attr(title)').get()
        data_list.append([title, url])
    return data_list

'''
下载多页
'''
for page in range(1, 10):
    page_url = base_url.format(page)
    data_list = download_page(page_url)
    for title, url in data_list:
        download_img(title, url)
