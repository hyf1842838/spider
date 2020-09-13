import requests
from lxml import etree
import pandas as pd

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_trs_uv=kf0swhy0_469_dbr2; _trs_ua_s_1=kf0swhy0_469_c9kg; _Jo0OQK=1F4BC169176846042F0A862808DD4180A08F3A58E49C94C622325187D9636396260E544D2962FE5625BE069230F48C4D5A0E7946CB7AAAE5DA1E969C68D457DF40ED964119F36543C1CEDDD121CB9104642E2D9ED79447D4B64295A8FE23F417AB43C1E2D1F46E73CCCGJ1Z1Yw==',
    'Host': 'www.fmprc.gov.cn',
    'Referer': 'https://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/default.shtml',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
}
hews_headers = 'https://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025'

def get_new_url():
    data = []
    # for page in range(67):
    for page in range(1):
        if page == 0:
            url = 'https://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/default.shtml'
        else:
            url = f'https://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/default_{page}.shtml'
        response = requests.get(url, headers=headers)
        response = response.content.decode('utf-8')
        url_link = etree.HTML(response)
        url_news = url_link.xpath('//div[@class="rebox_news"]/ul//li//text()')
        url_news = url_news[::2]
        url_news_url = url_link.xpath('//div[@class="rebox_news"]/ul//li//a/@href')
        url_news_url = [hews_headers+i[1:] for i in url_news_url]
        print(url_news)
        news = list(zip(url_news, url_news_url))
        data += news
    print(data)


new_header = new_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_trs_uv=kf0wjy21_469_fwik; _Jo0OQK=72762A434A3FE3C333F965E92A90B774F24D1F1D5AD8E7C5CD4C74BFE3AA14FE4CB88E359EB56BE815EA5F3772828A68974D44B5FCD719649F17708E34866716308D964119F36543C1CC5ACB6F64840EA06E2D9ED79447D4B646C6345A69FFD2005C5A54D5432EEEA82GJ1Z1dw==',
    'Host': 'www.fmprc.gov.cn',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content.decode('utf-8')
url = 'https://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/t1809844.shtml'


while True:
    try:
        proxy_ip = get_proxy()
        print(proxy_ip)
    except:
        continue
    try:
        print(f'代理ip: {proxy_ip}')
        if isinstance(headers, dict):
            response = requests.get(url=url, headers=new_header, verify=True, proxies={"http": "http://{}".format(proxy_ip)}, timeout=3)
        elif isinstance(headers, tuple):
            response = requests.get(url=url, headers=headers[0], params=headers[1], verify=True,
                                    proxies={"http": "http://{}".format(proxy_ip)}, timeout=3)
    except:
        continue
    try:
        if response.status_code == 200:
            print(333333333)
            # html = response.content.decode('utf-8')
            response = response.content.decode('utf-8')
            print(response)
            url_link = etree.HTML(response)
            url_news = url_link.xpath('//div[@id="News_Body_Txt_A"//text()')
            print(url_news)
            break
    except Exception as e:
        print(e)
        break

