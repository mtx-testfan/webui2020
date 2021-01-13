import time

from selenium import webdriver
import threading
import pageObject

class Driver(object):
    # 创建线程锁，保证线程安全
    _instance_lock = threading.Lock()
    driver = None

    # 获取driver对象
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 创建线程锁(上锁-释放锁)
            with Driver._instance_lock:
                if cls.driver is None:
                    cls.driver = webdriver.Chrome()
                    cls.driver.maximize_window()
                    cls.driver.get(pageObject.url)
        return cls.driver

    # 关闭driver
    @classmethod
    def close_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


if __name__ == '__main__':
    def task():
        obj = Driver.get_driver()
        print(obj)

    for i in range(10):
        t = threading.Thread(target=task)
        t.start()

    time.sleep(20)
    obj = Driver.get_driver('http://121.42.15.146:9090/mtx/')
    print(obj)


