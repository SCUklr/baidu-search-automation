"""
百度搜索页面类，实现百度搜索相关的页面操作
"""
import allure
from selenium.webdriver.common.keys import Keys
from tests.pages.base_page import BasePage
from tests.config.config import Locators, BASE_URL

class BaiduPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL

    @allure.step("打开百度首页")
    def open(self):
        """打开百度首页"""
        self.driver.get(self.url)
        return self

    @allure.step("输入搜索关键词: {keyword}")
    def input_search_text(self, keyword):
        """输入搜索关键词"""
        self.input_text(Locators.SEARCH_INPUT, keyword)
        return self

    @allure.step("点击搜索按钮")
    def click_search(self):
        """点击搜索按钮"""
        self.click(Locators.SEARCH_BUTTON)
        return self

    @allure.step("执行搜索操作: {keyword}")
    def search(self, keyword):
        """执行搜索操作"""
        self.input_search_text(keyword)
        self.click_search()
        return self

    @allure.step("获取搜索建议")
    def get_search_suggestions(self):
        """获取搜索建议列表"""
        if self.is_element_present(Locators.SEARCH_SUGGESTIONS):
            suggestions = self.find_elements(Locators.SEARCH_SUGGESTIONS)
            return [suggestion.text for suggestion in suggestions]
        return []

    @allure.step("获取搜索结果")
    def get_search_results(self):
        """获取搜索结果列表"""
        results = self.find_elements(Locators.SEARCH_RESULTS)
        return [result.text for result in results]

    @allure.step("检查搜索结果是否包含关键词: {keyword}")
    def check_results_contain_keyword(self, keyword):
        """检查搜索结果是否包含关键词"""
        results = self.get_search_results()
        return any(keyword.lower() in result.lower() for result in results)

    @allure.step("使用回车键进行搜索")
    def search_with_enter(self, keyword):
        """使用回车键进行搜索"""
        search_input = self.find_element(Locators.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.RETURN)
        return self

    @allure.step("清空搜索框")
    def clear_search_input(self):
        """清空搜索框"""
        search_input = self.find_element(Locators.SEARCH_INPUT)
        search_input.clear()
        return self 