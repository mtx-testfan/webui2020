from pageAction.ActionsManager import ActionsManager


class Address(ActionsManager):
    # 增加新地址的业务
    def addadress_business(self):
        self.pageIndex.page_click_person_info()
        self.pagePersonCenter.page_click_my_address()
        self.pageMyAddress.page_click_create_address()
        self.pageMyAddress.page_switch_iframe()
        self.pageMyAddress.page_input_name()
        self.pageMyAddress.page_input_tel()
        self.pageMyAddress.page_select_province_city_country()
        self.pageMyAddress.page_detail_address()
        self.pageMyAddress.page_nickname()
        self.pageMyAddress.page_click_save()