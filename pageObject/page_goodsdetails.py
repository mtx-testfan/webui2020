from base.baseApi import Base
import pageObject
'''商品详情页'''
class PageGoods(Base):
    # 点击登录链接前缀page 页面层 见名知意  loc元素定位的东西
    # 点击颜色
    def page_click_color(self):
        self.base_click(pageObject.cart_pink_spec)

    # 点击尺寸
    def page_click_size(self):
        self.base_click(pageObject.cart_size_spec)

    # 点击加入购物车
    def page_click_add_cart(self):
        self.base_click(pageObject.cart_add_cart)

    # 点击立即购买
    def page_click_now_buy(self):
        self.base_click(pageObject.cart_now_buy)