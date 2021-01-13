from base.baseApi import Base
import pageObject
import time
'''
购物车页面
'''
class PageCart(Base):

    # 点击删除按钮
    def page_click_delete_button(self):
        self.base_click(pageObject.cart_delete_button)

    # 点击确定删除
    def page_confirm_delete(self):
        self.base_click(pageObject.cart_confirm_delete)


if __name__ == '__main__':

    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://121.42.15.146:9090/mtx/')
    from pageObject.page_login import PageLogin

    login = PageLogin(driver)
    login.page_login_success()
    cart = PageCart(driver)
    cart.page_add_cart()
    time.sleep(2)
    assert '加入成功' in driver.page_source
