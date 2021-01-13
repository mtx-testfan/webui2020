# init这层，我希望把一些容易变化的内容在这进行管理
from selenium.webdriver.common.by import By
'''整个项目的配置项'''
# 项目的url
url = 'http://121.42.15.146:9090/mtx/'
'''以下是登录页面的配置信息'''
login_link = By.CSS_SELECTOR, '.menu-hd>a:nth-child(3)'
login_input_username = By.XPATH, '//label[text()="登录账号"]/following-sibling::input'
login_input_password = By.XPATH, '//label[text()="登录密码"]/following-sibling::input'
login_click_login_button = By.XPATH, '//button[text()="登录"]'

'''以下是删除购物车的配置信息'''
cart_click_right_cart = By.XPATH, "//*[text()='购物车']"
cart_delete_button = By.XPATH, '(//tbody/tr/td[5])[1]/a'
cart_confirm_delete = By.XPATH, "//*[text()='确定']"

'''以下是加入购物车的配置信息'''
cart_search_input = By.ID, 'search-input'
cart_search_button = By.ID, 'ai-topsearch'
cart_into_detail = By.CSS_SELECTOR, 'ul.search-list>li:nth-child(1)'
cart_pink_spec = By.CSS_SELECTOR, 'li[data-value="粉色"]'
cart_size_spec = By.CSS_SELECTOR, 'li[data-value="M"]'
cart_add_cart = By.CSS_SELECTOR, "button[title='加入购物车']"
cart_detail_window_title = 'ZK爆款连衣裙'
cart_now_buy = By.XPATH,'//*[text()="立即购买"]'

'''以下是提交订单的配置信息'''
order_receive_address = By.CSS_SELECTOR,'ul.address-list>li.address-default'
order_choose_payment = By.XPATH,'//*[text()="货到付款"]'
order_submit = By.XPATH,'//*[text()="提交订单"]'

'''添加地址页面'''
address_person_center = By.XPATH, '//*[text()="个人中心"]'
address_my_address = By.LINK_TEXT, '我的地址'
address_add_new_address=By.XPATH, '//*[text()=" 新增新地址"]'
address_add_username = By.XPATH,'//*[text()="姓名"]/following-sibling::input'
address_add_password = By.XPATH,'//*[text()="电话"]/following-sibling::input'
address_add_province = By.XPATH,'(//*[text()="省市区"]/following-sibling::select)[1]'
address_add_city = By.XPATH,'(//*[text()="省市区"]/following-sibling::select)[2]'
address_add_country = By.XPATH,'(//*[text()="省市区"]/following-sibling::select)[3]'
address_add_detail_address=By.XPATH,'//*[text()="详细地址"]/following-sibling::input'
address_add_nickname = By.XPATH,'//*[text()="别名"]/following-sibling::input'
address_save = By.XPATH,'//*[text()="保存"]'
address_frame_name = By.XPATH,'(//iframe)[3]'