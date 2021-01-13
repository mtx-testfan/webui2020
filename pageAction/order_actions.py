from pageAction.ActionsManager import ActionsManager
import time

class Order(ActionsManager):

    # 点击立即购买，并下订单的业务
    def order_business(self):
        self.pageIndex.page_input_search_info()
        self.pageIndex.page_click_search_button()
        self.pageSearch.page_first_goods()
        self.pageSearch.page_switch_window()
        self.pageGoods.page_click_color()
        time.sleep(2)
        self.pageGoods.page_click_size()
        time.sleep(2)
        self.pageGoods.page_click_now_buy()
        # 提交订单页面-选择第一个支付方式
        self.pageOrder.page_choose_payment()
        # 提交订单页面-点击提交订单
        self.pageOrder.page_submit_order()