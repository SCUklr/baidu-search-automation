"""
测试工具类，包含通用的测试辅助函数
"""
import time
import random
from functools import wraps
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def retry_on_failure(max_attempts=3, delay=1):
    """
    失败重试装饰器
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def wait_for_page_load(driver, timeout=10):
    """
    等待页面加载完成
    """
    try:
        old_page = driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(driver, timeout).until(
            EC.staleness_of(old_page)
        )
    except TimeoutException:
        pass

def generate_random_string(length=8):
    """
    生成随机字符串
    """
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(chars) for _ in range(length))

@allure.step("等待元素可见: {locator}")
def wait_for_element(driver, locator, timeout=10):
    """
    等待元素可见
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element
    except TimeoutException:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="element_not_visible",
            attachment_type=allure.attachment_type.PNG
        )
        raise

def is_element_visible(driver, locator, timeout=5):
    """
    检查元素是否可见
    """
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return True
    except TimeoutException:
        return False

def scroll_to_element(driver, element):
    """
    滚动到元素位置
    """
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)  # 等待滚动完成

def get_element_attributes(element):
    """
    获取元素的所有属性
    """
    return element.get_property('attributes') 