import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import os


def get_pdf_arxiv(web_site,path):
    rep = urllib.request.urlopen(urllib.request.Request(web_site))
    page = rep.read().decode('utf-8')
    pdf_download = re.findall('<meta name="citation_pdf_url" content="(.*?)"/>',page,re.S)#查询到网页中对应的pdf下载链接
    print(pdf_download[0])
    if (len(pdf_download) != 0):
        try:
            u = urllib.request.urlopen(pdf_download[0])
        except urllib.error.HTTPError:
            print(pdf_download[0], "url file not found")
            return
        block_sz = 8192
        with open(path, 'wb') as f:
            while True:
                buffer = u.read(block_sz)
                if buffer:
                    f.write(buffer)
                else:
                    break
        print("Sucessful to download " + path)

def ans(name):
    name1 = name.replace(' ','%20')
    url = 'https://dblp.org/search?q='+name1
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a',itemprop="url")
    for tag in tags: 
      url1 = tag.get('href', None)
      break

    req = urllib.request.Request(url1+'.html')
    response = urllib.request.urlopen(req)
    the_page = response.read().decode('utf-8')
    s=''
    paper_title = re.findall('<span class="title" itemprop="name">(.*?)</span>',the_page,re.S)#检索页面中给的论文名字
    print(paper_title[0])
    paper_web = re.findall('view</b></p><ul><li class="ee"><a href="(.*?)" itemprop="url">',the_page,re.S)#存储对应网址
    print(paper_web[0]) 
    for i in range(len(paper_web)):
            s = s + paper_title[i] + '\n'
            #以下代码去除了原有网页论文名字中无法保存为window文件名的符号，采用下划线_代替
            paper_title[i] = paper_title[i].replace('"', '')
            list = paper_title[i].split(" ")
            paper_title[i] = "_".join(list)
            list = paper_title[i].split(":")
            paper_title[i] = "_".join(list)
            list = paper_title[i].split("?")
            paper_title[i] = "_".join(list)
            list = paper_title[i].split("<sub>")
            paper_title[i] = "_".join(list)
            list = paper_title[i].split("</sub>")
            paper_title[i] = "_".join(list)
            list = paper_title[i].split("<sup>")
            paper_title[i] = "_".join(list)
            list = paper_title[i].split("</sup>")
            paper_title[i] = "_".join(list)
            
            
            if (paper_web[i].find("arxiv") != -1): #查看网址中是否包含arxiv词汇
                print(paper_title[i])
                path_dir = "C:\\Users\\pyl\\Desktop\\"
                dir_list=os.listdir(path_dir)
                path = paper_title[i] + "pdf"
                if path not in dir_list:
                    get_pdf_arxiv(paper_web[i], path_dir + path)
    print(s)
    return s
