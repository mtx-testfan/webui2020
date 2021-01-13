from base.baseApi import Base
from base.driver import Driver
from pageAction.cart_actions import Cart
from pageAction.login_actions import Login
import time
import allure

@allure.feature('购物车功能')
class TestCart:
    def setup_class(self):
        # 创建谷歌浏览器
        self.driver = Driver().get_driver()
        # 调用成功的登录方法
        Login(self.driver).login_success()
        self.baseApi = Base(self.driver)
        # 创建购物车的对象
        self.cart = Cart(self.driver)

    def teardown_class(self):
        Driver().close_driver()

    # 用例1：加入购物车
    @allure.story('加入购物车的功能测试')
    def test_add_cart(self):
        self.cart.add_cart()
        time.sleep(3)
        assert '加入成功' in self.baseApi.base_page_source

    # 用例2：删除购物车商品
    @allure.story('删除购物车功能的测试')
    def test_delete_cart(self):
        self.cart.delete_cart()
        time.sleep(3)
        assert '删除成功' in self.baseApi.base_page_source
