from base.baseApi import Base
from pageAction.ActionsManager import ActionsManager
from pageObject.page_index import PageIndex
from pageObject.page_login import PageLogin
import time


class Login(ActionsManager):

    def login_business(self, username, password):
        # 点击登录链接
        self.pageIndex.page_click_login_link()
        # 输入用户名
        self.pageLogin.page_input_username(username)
        # 输入密码
        self.pageLogin.page_input_password(password)
        # 点击登录
        self.pageLogin.page_click_login_button()
        time.sleep(3)
    # 正确登录的业务(为了方便其他功能使用)
    def login_success(self):
        # 点击登录链接
        self.pageIndex.page_click_login_link()
        # 输入用户名
        self.pageLogin.page_input_username('yaoyao')
        # 输入密码
        self.pageLogin.page_input_password('yaoyao')
        # 点击登录
        self.pageLogin.page_click_login_button()
        time.sleep(3)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://121.42.15.146:9090/mtx/')
    login = Login(driver)
    login.login_business('yaoyao','yaoyao')
    # print(driver.current_url) #获取当前页面的url地址