from base.baseApi import Base
from base.driver import Driver
from pageAction.Address_action import Address
from pageAction.login_actions import Login


import time
import allure
@allure.feature('增加地址功能测试')
class TestAddAddress:
    def setup_class(self):
        # 创建谷歌浏览器
        self.driver = Driver().get_driver()
        # 创建login的页面对象
        # 调用成功的登录方法
        Login(self.driver).login_success()
        self.baseApi = Base(self.driver)
        # 创建新地址的对象
        self.address = Address(self.driver)

    def teardown_class(self):
        Driver().close_driver()

    # 用例1：新增地址
    @allure.story('新增地址功能的正向用例')
    def test_add_address(self):
        self.address.addadress_business()
        time.sleep(1)
        assert '新增成功' in self.baseApi.base_page_source


