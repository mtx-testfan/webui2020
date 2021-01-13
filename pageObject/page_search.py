from base.baseApi import Base
import pageObject
'''商品详情页'''
class PageSearch(Base):
    # 选择第一个商品
    def page_first_goods(self):
        self.base_click(pageObject.cart_into_detail)

    # 切换窗口
    def page_switch_window(self):
        self.base_switch_window(pageObject.cart_detail_window_title)