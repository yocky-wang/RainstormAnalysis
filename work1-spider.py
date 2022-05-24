import requests
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if __name__ == '__main__':
    # get直接返回，不再等待界面加载完成（避免网页一直加载出现超时，后面可配合WebDriverWait等待某个元素出现使用）
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"

    # 创建chrome参数对象
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    options.add_argument('window-size=1600x900')  # 指定浏览器分辨率
    options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    # options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开启管理者模式
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # 禁止图片和css加载
    prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    browser = webdriver.Chrome(chrome_options=options)
    browser.set_page_load_timeout(3)
    browser.set_script_timeout(3)  # 这两种设置都进行才有效
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'
    }
    url = 'https://www.baidu.com/s'

    group = ['京津冀城市群城市', '粤港澳大湾区城市', '长三角城市群城市']
    city = [['北京','天津','石家庄','唐山','保定','秦皇岛','廊坊','沧州','承德','张家口'],
            ['香港','澳门','广州','深圳','珠海','佛山','中山','东莞','肇庆','江门','惠州'],
            ['无锡','常州','苏州','南通','扬州','镇江','盐城','泰州','杭州','宁波','温州','湖州','嘉兴','绍兴','金华','舟山','台州','合肥','芜湖','马鞍山','铜陵','安庆','滁州','池州','宣城']]
    word = ' 暴雨 内涝'
    list_kw = []
    # driver = webdriver.Chrome()
    # driver.set_page_load_timeout(0.5)
    for x in range(1):
        for y in range(len(city[x])):
            kw = city[x][y]+word
            list_kw.clear()
            for page in range(0, 39, 10):
                param = {
                    'wd': kw,
                    'pn': str(page),
                    'tn': 'news'
                }

                response = requests.get(url=url,params=param,headers=headers)
                page_text = response.text
                tree = etree.HTML(page_text)
                r = tree.xpath('//div[@id="content_left"]//h3/a/@href')
                list_kw.append(r)
            print(kw)
            print(list_kw[0][2])
            for i in range(len(list_kw)):
                for j in range(len(list_kw[i])):
                    print('i,j:', i, j)
                    href = list_kw[i][j]
                    fileName = group[x] + '/' + city[x][y] + '/' + str(i) + str(j) + '.html'
                    try:
                        # response = requests.get(url=href)
                        # page_text = response.text
                        browser.get(href)
                        page_text = browser.page_source
                        fileName = group[x]+'/'+city[x][y]+'/'+str(i)+str(j) + '.html'
                        with open(fileName, 'w', encoding='utf-8') as fp:
                            fp.seek(0)
                            fp.truncate()
                            fp.write(page_text)
                    except Exception as err:
                        # print(err)
                        print('timeout')
                        browser.execute_script('window.stop()')