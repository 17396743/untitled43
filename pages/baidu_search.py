from selenium.webdriver.common.by import By
from base.BasePage import BasePage

'''在这一步主要编写操作的各种动作和行为、写位置信息什么的。或者存储数值，运算什么的'''
class SearchPage(BasePage):
# ==========================================================
    # 这个必须要有（必须有！）
    def __init__(self,driver,url):
        BasePage.__init__(self,driver,url)
# ==========================================================

    # 这下面都是动作行为逻辑
    #下面的都是验证百度搜索的逻辑

    #进入百度
    def go_baidu(self):
        self.get()

    #定位搜索框，并且输入要搜索的内容
    def locate_search_inout(self,key):
        self.send_keys(By.ID,"kw",key)

    #定位到百度按钮，点击
    def click_baodu_btn(self):
        self.click(By.XPATH,'//*[@id="su"]')




