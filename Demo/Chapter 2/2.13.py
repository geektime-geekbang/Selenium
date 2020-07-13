from selenium import webdriver
from time import sleep, strftime, localtime, time

import os
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()

        sleep(2)

        # self.driver.save_screenshot('baidu.png')
        # st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        # fime_name = st + '.png'
        # self.driver.save_screenshot(fime_name)

        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        fime_name = st + '.png'

        path = os.path.abspath('scrennshot')
        file_path = path+'/'+fime_name
        self.driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    case = TestCase()
    case.test1()