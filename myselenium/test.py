import time


from myselenium.chromeDriver import chrome
from myselenium.sougou import parseContent
from urllib import parse

if __name__ == "__main__":

    query = parse.quote('2019影视分享')

    url = "https://weixin.sogou.com/weixin?type=2&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=".format(query)

    print(url)

    chr = chrome.ChromeDrive()
    chr.driver.get(url)
    time.sleep(2)

    # 首页句柄
    mainHandle = chr.driver.current_window_handle
    divs = chr.driver.find_elements_by_xpath("//div[@class=\"txt-box\"]")


    sg = parseContent.Sougou()
    for div in divs:
        # print(divs[i].get_attribute("href"))
        # print(divs[i].text)
        #
        #print(div.get_attribute('innerHTML'))
        time.sleep(3)
        #
        # print("a title")
        #
        # print(divs[i].find_element_by_tag_name("h3").text)

        link_title = div.find_element_by_tag_name("h3").text

        link = chr.driver.find_element_by_link_text(link_title)
        print("link", link, link_title)
        link.click()
        time.sleep(2)

        content = sg.GetPageContent(chr, mainHandle)

        print("content", content)

        time.sleep(5)
        chr.CloseOtherWindow(mainHandle)
        if len(content.title) > 5:
            break





        # a = divs[i].find_element_by_xpath("//a/@href")
        # print(url)
        # print(i)


    # for i in range(len(divs)):
    #     print(i)

    # chrome.driver.close()
    # #设置浏览器大小
    # #chrome.driver.set_window_size()
    #
    # # cookie
    # print(chrome.driver.get_cookies())
    #
    # #页面内容
    # page = chrome.driver.page_source
    # print(page)
    #
    # time.sleep(5)
    #
    # # 页面内跳转
    # url = "https://weixin.sogou.com/weixin?type=2&s_from=input&query=2019%E6%96%B0%E7%94%B5%E5%BD%B1&ie=utf8&_sug_=n&_sug_type_=&w=01019900&sut=9092&sst0=1572511798216&lkt=8%2C1572511791607%2C1572511798106"
    # chrome.driver.get(url)
    # time.sleep(5)
    # page = chrome.driver.page_source
    # print(page)
    #
    # #获取页面title
    # print(chrome.driver.title)
    #
    # 关闭浏览器
    chr.driver.quit()