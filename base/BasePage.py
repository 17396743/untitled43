from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''在这一步主要编写固定的代码操作，不要带入逻辑'''

class  BasePage():
 # ==========================================================
 # __init__ 这个用于初始化，和绑定操作（必须有！）
 # ==========================================================
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
# ==========================================================
        # 访问某个网页
    def get(self):
        self.driver.get(self.url)

# ==========================================================
# 这一步的写法的，嵌套写法。
# 写好一个def方法，供第二个def方法使用。
# 如： def find_element()   和  def send_keys 里面的  self.find_element()
#
# ==========================================================
# find_element 获取单数的数据参数
#显示等待，定位元素
    #*locate：可变参数 ， By.ID，"kw"
    def find_element(self,*locate):
        return WebDriverWait(self.driver,15,0.5).until(EC.presence_of_element_located(locate))

# find_element 获取多数的数据参数
    #显示等待，定位元素
    #*locate:可变参数，By.ID "kw"
    def find_elements(self,*locate):
        return WebDriverWait(self.driver,15,0.5).until(EC.presence_of_all_elements_located(locate))

# ==========================================================

    # by:定位的方式
    # value：定位方式对应的值
    def send_keys(self, by, value, content):
        self.find_element(by, value).send_keys(content)
