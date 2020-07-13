from selenium import webdriver
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/framesTest.htm')
    def test1(self):

        top = self.driver.find_element_by_name('top')
        self.driver.switch_to.frame(top)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]').click()

        self.driver.switch_to.default_content()

        sleep(3)

        second = self.driver.find_element_by_xpath('/html/frameset/frame[2]')

        self.driver.switch_to.frame(second)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[2]').click()

        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test1()