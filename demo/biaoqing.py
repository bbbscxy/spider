import requests
import parsel

# 爬虫表情包：https://www.fabiaoqing.com/biaoqing/lists/page/1.html

response = requests.get("https://www.fabiaoqing.com/biaoqing/lists/page/1.html")
selector = parsel.Selector(response.text)
imgs = selector.css('img.ui.image.lazy')
for img in imgs:
    # print(img.get())
    url = img.css('img::attr(data-original)').get()
    title = img.css('img::attr(title)').get()
    # print(title, url)
    img_response = requests.get(url)
    suffix = url.split('.')[-1]
    file_name = title + '.' + suffix
    try:
        with open('images/' + file_name, mode='wb') as f:
            f.write(img_response.content)
    except:
        print('保存错误', file_name)