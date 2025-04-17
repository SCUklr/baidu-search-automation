"""
百度搜索页面类，实现百度搜索相关的页面操作
"""
import allure
from selenium.webdriver.common.keys import Keys
from tests.pages.base_page import BasePage
from tests.config.config import BASE_URL, WAIT_TIMEOUT, SEARCH_KEYWORD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaiduPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)
        
    # 页面元素定位
    SEARCH_BOX = (By.ID, "kw")
    SEARCH_BUTTON = (By.ID, "su")
    SEARCH_SUGGESTIONS = (By.CSS_SELECTOR, ".bdsug ul li")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".result.c-container")

    @allure.step("打开百度首页")
    def open(self):
        """打开百度首页"""
        self.driver.get(self.url)
        return self

    @allure.step("输入搜索关键词: {keyword}")
    def input_search_text(self, keyword):
        """输入搜索关键词"""
        self.input_text(self.SEARCH_BOX, keyword)
        return self

    @allure.step("点击搜索按钮")
    def click_search(self):
        """点击搜索按钮"""
        self.click(self.SEARCH_BUTTON)
        return self

    @allure.step("执行搜索操作: {keyword}")
    def search(self, keyword=SEARCH_KEYWORD):
        """执行搜索操作"""
        # 输入搜索关键词
        search_box = self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_box.clear()
        search_box.send_keys(keyword)
        
        # 点击搜索按钮
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()
        
        # 等待搜索结果加载
        self.wait.until(EC.presence_of_all_elements_located(self.SEARCH_RESULTS))
        return self

    @allure.step("获取搜索建议")
    def get_search_suggestions(self):
        """获取搜索建议列表"""
        try:
            # 等待搜索建议出现
            self.wait.until(EC.presence_of_element_located(self.SEARCH_SUGGESTIONS))
            suggestions = self.driver.find_elements(*self.SEARCH_SUGGESTIONS)
            return [suggestion.text for suggestion in suggestions]
        except:
            return []

    @allure.step("获取搜索结果")
    def get_search_results(self):
        """获取搜索结果列表"""
        results = self.driver.find_elements(*self.SEARCH_RESULTS)
        return [result.text for result in results]

    @allure.step("检查搜索结果是否包含关键词: {keyword}")
    def check_results_contain_keyword(self, keyword):
        """检查搜索结果是否包含关键词"""
        results = self.get_search_results()
        return any(keyword.lower() in result.lower() for result in results)

    @allure.step("使用回车键进行搜索")
    def search_with_enter(self, keyword):
        """使用回车键进行搜索"""
        search_input = self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_input.clear()
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.RETURN)
        
        # 等待搜索结果加载
        self.wait.until(EC.presence_of_all_elements_located(self.SEARCH_RESULTS))
        return self

    @allure.step("清空搜索框")
    def clear_search_input(self):
        """清空搜索框"""
        search_input = self.find_element(self.SEARCH_BOX)
        search_input.clear()
        return self 