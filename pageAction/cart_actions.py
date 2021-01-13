from pageAction.ActionsManager import ActionsManager
import time

class Cart(ActionsManager):
    # 删除购物车商品
    def delete_cart(self):
        # 保证购物车里面有商品
        self.add_cart()
        # time.sleep(3)
        # 点击首页右侧的购物车
        self.pageIndex.page_click_right_cart()
        # 点击删除按钮
        self.pageCart.page_click_delete_button()
        # 点击确定删除
        self.pageCart.page_confirm_delete()

    # 加入购物车
    def add_cart(self):
        self.pageIndex.page_input_search_info()
        self.pageIndex.page_click_search_button()
        self.pageSearch.page_first_goods()
        self.pageSearch.page_switch_window()
        self.pageGoods.page_click_color()
        time.sleep(2)
        self.pageGoods.page_click_size()
        time.sleep(2)
        self.pageGoods.page_click_add_cart()