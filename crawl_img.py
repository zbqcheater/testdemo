#!/usr/bin/env
import requests
import json
import random
import uuid, math
import os


class CrawlImg:
    """爬取百度图片"""

    def __init__(self, keyword, quantity):
        self.keyword = keyword
        self.quantity = quantity
        print(f'你要爬取{self.quantity}张{self.keyword}图片')

    def start(self):
        user_agents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Beamrise/17.2.0.9 Chrome/17.0.939.0 Safari/535.8',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)',
            'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
            'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
            'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
            'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11']
        ua = {'User-Agent': random.choice(user_agents)}
        cpn = random.randrange(0, 100)
        url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={self.keyword}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word={self.keyword}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={cpn}&rn={self.quantity}&gsm=&1576636741009=Referrer%20Policy:%20no-referrer-when-downgrade'
        try:
            r = requests.get(url, timeout=10, headers=ua)
            print(r.url)
            r.raise_for_status()
            r.encoding = 'utf-8'
            b = json.loads(r.content)
            b = b['data']
            b.pop()
            return b
        except:
            print('url获取失败')
            return '获取失败'


def save_img(url, keyword):
    base_path = os.path.abspath(os.path.dirname(__file__))
    ext = url[url.rfind('.'):]
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Beamrise/17.2.0.9 Chrome/17.0.939.0 Safari/535.8',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)',
        'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
        'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11']
    ua = {'User-Agent': random.choice(user_agents)}
    try:
        r = requests.get(url, timeout=10, headers=ua)
        r.raise_for_status()
        b64 = r.content
        save_path = base_path + f'/static/img/{keyword}/'
        file_name = str(uuid.uuid4()) + ext
        file_path = save_path + file_name
        open(file_path, 'wb').write(b64)
        print('图片保存成功...')
        return file_name
    except:
        print('图片获取失败')
        return '获取失败'


if __name__ == '__main__':
    # a = input('关键词')
    # info = CrawlImg(a, int(input()))
    # b = info.start()
    # print(len(b))
    #
    # for i in b:
    #     this_url = i['thumbURL']
    #     print(this_url)
    #     s = save_img(this_url, a)
    pass
