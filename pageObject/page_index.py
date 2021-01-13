from base.baseApi import Base
import pageObject


class PageIndex(Base):
    # 点击个人中心
    def page_click_person_info(self):
        self.base_click(pageObject.address_person_center)

    # 点击首页登录链接
    def page_click_login_link(self):
        self.base_click(pageObject.login_link)

    # 点击首页右上角的购物图标
    def page_click_right_cart(self):
        self.base_click(pageObject.cart_click_right_cart)

    # 确定输入框，输入连衣裙
    def page_input_search_info(self):
        self.base_input(pageObject.cart_search_input, '连衣裙')

    # 点击搜索按钮
    def page_click_search_button(self):
        self.base_click(pageObject.cart_search_button)

