import pageObject
from base.baseApi import Base
import time

class PageMyAddress(Base):
    # 点击新建地址
    def page_click_create_address(self):
        self.base_click(pageObject.address_add_new_address)
    # 切换iframe
    def page_switch_iframe(self):
        iframe_el = self.base_find_element(pageObject.address_frame_name)
        self.base_switch_iframe(iframe_el)

    # 输入用户名
    def page_input_name(self):
        self.base_input(pageObject.address_add_username, '嘿嘿')

    # 输入电话
    def page_input_tel(self):
        self.base_input(pageObject.address_add_password, '13936751740')

    # 选择省市区
    def page_select_province_city_country(self):
        # 省市区----->下拉框（隐藏的下拉框）两种解决办法第一，一步一步点击第二，js改变隐藏属性
        time.sleep(3)
        # 省
        js = 'document.querySelectorAll("select")[0].style.display="inline"'
        self.base_js(js)
        ## 报错原因是因为下拉框的内容不可见

        self.base_select_visible_text(pageObject.address_add_province, '北京市')
        time.sleep(2)

        js = 'document.querySelectorAll("select")[1].style.display="inline"'
        self.base_js(js)

        # 东城区
        self.base_select_visible_text(pageObject.address_add_city, '东城区')
        time.sleep(2)
        js = 'document.querySelectorAll("select")[2].style.display="inline"'
        self.base_js(js)
        time.sleep(2)
        # 东直门街道
        self.base_select_visible_text(pageObject.address_add_country, '东直门街道')

    # 详细地址
    def page_detail_address(self):
        self.base_input(pageObject.address_add_detail_address, '北京市')

    # 别名
    def page_nickname(self):
        self.base_input(pageObject.address_add_nickname, '花花')

    # 点击保存
    def page_click_save(self):
        # 点击保存
        self.base_click(pageObject.address_save)