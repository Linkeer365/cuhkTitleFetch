import requests
# from selenium import webdriver
# from lxml import etree
# import time
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# url='http://www.cuhk.edu.cn/lists'
# driver=webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# driver.get(url)

titles_pack=[]

final_cnt=45

for page in range(1,final_cnt+1):
    titles=[]
    designed_url='http://www.cuhk.edu.cn/zh-hans/api/lists?page={}&type=all'.format(page-1)
    headers={'Host':'www.cuhk.edu.cn','Referer':'http://www.cuhk.edu.cn/lists','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','X-Requested-With': 'XMLHttpRequest',}
    page_resp=requests.get(designed_url,headers=headers)
    page_resp.encoding='utf-8'
    # print(page_resp.json())
    for pack in page_resp.json()['data']['lists']:
        # print(pack)
        title=pack['title']
        titles.append(title)
    titles_pack.append((page,tuple(enumerate(titles))))
with open('./{}'.format('titleFetch.txt'),'w',encoding='utf-8') as f:
    f.write(str(titles_pack))
    f.write('-----------')
    for titles in titles_pack:
        f.write(str(titles))
print(len(titles_pack))



# # print(driver.page_source)

# resp_html=etree.HTML(driver.page_source)
# title_finds=resp_html.xpath('//h4[starts-with(@class,"media")]/a//text()')
# print(title_finds)


# # href: //li[contains(@class,"pager-item")]/a[contains(@title,"到")]/@href
# ac=ActionChains(driver)
# btn_elem_path='//li[contains(@class,"pager-item")]'
# btn_finds=resp_html.xpath('//li[contains(@class,"pager-item")]')
# # print(btn_finds)
# driver.find_element_by_xpath(btn_elem_path).click()
# time.sleep(2)



# resp_html=etree.HTML(driver.page_source)
# title_finds=resp_html.xpath('//h4[starts-with(@class,"media")]/a//text()')
# print(title_finds)

# for btn in btn_finds:
#     ac.click(btn)
#     ac.perform()


# titles_pack=[]
# titles_pack.append(title_finds)
# for btn in btn_finds:
#     driver.find_element(btn).click()
#     print(driver.page_source)
#     # new_titles=[]
#     time.sleep(3)
