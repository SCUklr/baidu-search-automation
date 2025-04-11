"""
基础页面类，包含所有页面共用的方法
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure
from pathlib import Path
from datetime import datetime
from tests.config.config import SCREENSHOTS_DIR

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """查找单个元素"""
        try:
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            self.take_screenshot(f"element_not_found_{locator[1]}")
            raise

    def find_elements(self, locator):
        """查找多个元素"""
        try:
            return self.wait.until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            self.take_screenshot(f"elements_not_found_{locator[1]}")
            return []

    def click(self, locator):
        """点击元素"""
        element = self.find_element(locator)
        self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """获取元素文本"""
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator, timeout=5):
        """判断元素是否存在"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, locator, timeout=10):
        """等待元素可见"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            self.take_screenshot(f"element_not_visible_{locator[1]}")
            return False

    @allure.step("截取屏幕截图")
    def take_screenshot(self, name):
        """截取屏幕截图"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = Path(SCREENSHOTS_DIR) / f"{name}_{timestamp}.png"
        self.driver.save_screenshot(str(screenshot_path))
        allure.attach.file(str(screenshot_path), name=name,
                         attachment_type=allure.attachment_type.PNG)

    def scroll_into_view(self, locator):
        """将元素滚动到可见区域"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_page_title(self):
        """获取页面标题"""
        return self.driver.title

    def get_page_url(self):
        """获取当前URL"""
        return self.driver.current_url 