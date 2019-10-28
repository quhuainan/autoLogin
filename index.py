import time

import selenium
from selenium import webdriver
import lxml.html
import urllib3

if __name__ == '__main__':
    print("python")

    sel = selenium.webdriver.Chrome()
    mainUrl = "https://yijian.yy.com"
    etree = lxml.html.etree
    sel.get(mainUrl)
    time.sleep(1)
    try:
        sel.find_element_by_xpath('//*[@id="app"]/header/div/div[6]/a').click()
        print("点击登录按钮")
    except:
        print("11")
    time.sleep(1)
    try:
        sel.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/p').click()
        print("点击登录YY按钮")
    except:
        print("111")
    time.sleep(1)
    sel.switch_to.frame('udbsdk_frm_normal')

    try:
        sel.find_element_by_xpath('//*[@id="m_commonLogin"]/div[1]/span/input').send_keys("15510974083")
        print("输入账号")
    except:
        print("输入账号出错")
    time.sleep(1)
    try:
        sel.find_element_by_xpath('//*[@id="m_commonLogin"]/div[2]/span/input').send_keys("quhuai112")
        print("输入密码")
    except:
        print("输入密码出错")
    time.sleep(1)

    try:
        sel.find_element_by_xpath('//*[@id="m_commonLogin"]/div[4]/a[1]').click()
        print("登录成功")
    except:
        print("登录失败")
    time.sleep(3)
    print('cookies', sel.get_cookies())
    cookie = [item["name"] + "=" + item["value"] for item in sel.get_cookies()]
    cookiestr = ';'.join(item for item in cookie)
    print('cookies', cookiestr)

    homeurl = sel.current_url
    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': cookiestr,
        'Referer': mainUrl,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = urllib3.PoolManager().request('POST', mainUrl, headers=headers)
    print(response.status, response.data.decode('utf-8'))

    #
    # //*[@id="m_commonLogin"]/div[2]/span/input
