import pageObject
from base.baseApi import Base


class PagePersonCenter(Base):
    # 点击我的地址
    def page_click_my_address(self):
        self.base_click(pageObject.address_my_address)



