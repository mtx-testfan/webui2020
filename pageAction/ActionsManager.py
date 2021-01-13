from pageObject.page_index import PageIndex
from pageObject.page_login import PageLogin
from pageObject.page_cart import PageCart
from pageObject.page_order import PageOrder
from pageObject.page_goodsdetails import PageGoods
from pageObject.page_my_address import PageMyAddress
from pageObject.page_person_center import PagePersonCenter
from pageObject.page_search import PageSearch


class ActionsManager():

    def __init__(self, driver):
        '''
        实例化所有的页面对象,无论多少页面,统一进行实例化,然后业务层继承ActionsManager
        这样业务层无论用到哪个页面，都可以直接拿实例化好的页面对象去用。
        :param driver:
        '''
        self.pageIndex = PageIndex(driver)
        self.pageLogin = PageLogin(driver)
        self.pageCart = PageCart(driver)
        self.pageOrder = PageOrder(driver)
        self.pageGoods = PageGoods(driver)
        self.pageMyAddress = PageMyAddress(driver)
        self.pagePersonCenter = PagePersonCenter(driver)
        self.pageSearch = PageSearch(driver)
