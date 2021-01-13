import time

from base.baseApi import Base
import pageObject



class PageOrder(Base):

    # 选择第一个付款方式
    def page_choose_payment(self):
        self.base_click(pageObject.order_choose_payment)

    # 点击提交订单按钮
    def page_submit_order(self):
        self.base_click(pageObject.order_submit)





if __name__ == '__main__':
    pass
    # from selenium import webdriver
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get('http://121.42.15.146:9090/mtx/')
    # from pageObject.page_login import PageLogin
    #
    # login = PageLogin(driver)
    # login.page_login_success()
    # # 调用购物车的立即支付
    # cart = PageCart(driver)
    # cart.page_now_buy()
    # order = PageOrder(driver)
    # order.page_order_business()
    # time.sleep(1)
    # assert '提交成功' in driver.page_source