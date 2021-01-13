import time
import pytest

from base.baseApi import Base
from base.driver import Driver

from pageAction.login_actions import Login
from tool.readData import ReadData
import allure
'''
登录参数化的设计
1.成功登录
2.错误登录参数化

'''
data = ReadData().get_yaml('login_data','test_login')


@allure.feature('登录功能')
class TestLogin:
    def setup_class(self):
        '''
        初始化chrome浏览器
        :return:
        '''
        # 创建谷歌浏览器
        self.driver = Driver().get_driver()
        # 创建login的页面对象
        self.login = Login(self.driver)
        self.baseApi = Base(self.driver)

    @pytest.mark.parametrize('args',data)
    @allure.story('登录业务的参数化')
    @allure.title('登录的正向用例和逆向用例')
    def test_login(self,args):
        self.login.login_business(args['accounts'],args['pwd'])
        time.sleep(2)
        assert args['assert'] in self.baseApi.base_page_source

    def teardown_class(self):
        Driver().close_driver()

