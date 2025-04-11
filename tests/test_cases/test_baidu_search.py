"""
百度搜索测试用例
"""
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.pages.baidu_page import BaiduPage
from tests.config.config import TEST_KEYWORDS, BROWSER_TYPE, HEADLESS

@pytest.fixture(scope="function")
def driver():
    """
    设置浏览器驱动
    """
    if BROWSER_TYPE.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if HEADLESS:
            options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    else:
        raise ValueError(f"Unsupported browser type: {BROWSER_TYPE}")
    
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("百度搜索")
class TestBaiduSearch:
    
    @allure.story("基本搜索功能")
    @allure.title("测试搜索功能 - {keyword}")
    @pytest.mark.parametrize("keyword", TEST_KEYWORDS)
    def test_search(self, driver, keyword):
        """
        测试基本搜索功能
        """
        page = BaiduPage(driver)
        page.open()
        
        # 执行搜索
        page.search(keyword)
        
        # 验证搜索结果
        assert page.check_results_contain_keyword(keyword), f"搜索结果中未找到关键词: {keyword}"
    
    @allure.story("搜索建议功能")
    @allure.title("测试搜索建议功能")
    def test_search_suggestions(self, driver):
        """
        测试搜索建议功能
        """
        page = BaiduPage(driver)
        page.open()
        
        # 输入部分关键词
        page.input_search_text("pyth")
        
        # 获取并验证搜索建议
        suggestions = page.get_search_suggestions()
        assert len(suggestions) > 0, "未显示搜索建议"
        assert any("python" in suggestion.lower() for suggestion in suggestions), "搜索建议中未包含相关关键词"
    
    @allure.story("回车搜索功能")
    @allure.title("测试回车键搜索功能")
    def test_search_with_enter(self, driver):
        """
        测试使用回车键进行搜索
        """
        page = BaiduPage(driver)
        page.open()
        
        # 使用回车键搜索
        keyword = "selenium python"
        page.search_with_enter(keyword)
        
        # 验证搜索结果
        assert page.check_results_contain_keyword(keyword), f"使用回车键搜索未找到关键词: {keyword}"
    
    @allure.story("清空搜索框功能")
    @allure.title("测试清空搜索框功能")
    def test_clear_search_input(self, driver):
        """
        测试清空搜索框功能
        """
        page = BaiduPage(driver)
        page.open()
        
        # 输入文本并清空
        page.input_search_text("test text")
        page.clear_search_input()
        
        # 验证搜索框是否为空
        search_input = page.find_element(page.locators.SEARCH_INPUT)
        assert search_input.get_attribute("value") == "", "搜索框未被清空" 