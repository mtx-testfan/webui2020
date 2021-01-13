from base.baseApi import Base
from base.driver import Driver
from pageAction.login_actions import Login
from pageAction.order_actions import Order
from pageObject.page_login import PageLogin
import time
import allure


@allure.feature('下订单功能')
class TestOrder:
    def setup_class(self):
        # 创建谷歌浏览器
        self.driver = Driver().get_driver()
        # 调用成功的登录方法
        Login(self.driver).login_success()
        # 创建购物车的对象
        # self.cart = Cart(self.driver)
        # 创建订单的对象
        self.order = Order(self.driver)
        self.baseApi = Base(self.driver)

    def teardown_class(self):
        Driver().close_driver()

    # 测试用例:提交订单
    @allure.story('提交订单功能的测试')
    def test_order(self):
        self.order.order_business()
        time.sleep(1)
        assert '提交成功' in self.baseApi.base_page_source

