import time
from base.baseApi import Base
import pageObject
import allure


class PageLogin(Base):


    # 输入用户名
    # @allure.step('输入用户名')
    def page_input_username(self, username):
        self.base_input(pageObject.login_input_username, username)

    # 输入密码
    # @allure.step('输入密码')
    def page_input_password(self,password):
        self.base_input(pageObject.login_input_password, password)

    # 点击登录  修改超时时间和频率
    # @allure.step('点击登录按钮')
    def page_click_login_button(self):
        self.base_click(pageObject.login_click_login_button)


    # 组合业务逻辑->跟你做功能测试一样的一个组合的动作，动作顺序一样


if __name__ == '__main__':
    # from selenium import webdriver
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get('http://121.42.15.146:9090/mtx/')
    # login = PageLogin(driver)
    # login.page_login('yaoyao','yaoyao')
    pass
