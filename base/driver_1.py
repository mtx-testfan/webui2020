import time

from selenium import webdriver
import threading
class Driver(object):
    driver = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
        return cls.driver


if __name__ == '__main__':
    def task():
        obj = Driver.get_driver()
        print(obj)
    obj1 = task()
    print(id(obj1))
    obj2 = task()
    print(id(obj2))
    # for i in range(10):
    #     t = threading.Thread(target=task)
    #     t.start()
    # time.sleep(20)
    # obj = Driver.get_driver()
    # print(obj)


