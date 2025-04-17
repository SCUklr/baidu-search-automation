"""
百度搜索测试用例
"""
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from tests.pages.baidu_page import BaiduPage
from tests.config.config import TEST_KEYWORDS, BROWSER, HEADLESS, SEARCH_KEYWORD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    """
    初始化WebDriver
    """
    if BROWSER.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Firefox()
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
        
        # 输入测试文本并清空
        page.input_search_text("test text")
        page.clear_search_input()
        
        # 验证搜索框是否为空
        search_input = page.find_element(page.SEARCH_BOX)
        assert search_input.get_attribute("value") == "", "搜索框未清空"

    @allure.story("基本搜索功能")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_with_keyword(self, driver):
        """测试基本搜索功能"""
        baidu = BaiduPage(driver)
        baidu.open().search()
        
        # 验证搜索结果
        results = baidu.get_search_results()
        assert len(results) > 0, "搜索结果为空"
        assert any(SEARCH_KEYWORD in result for result in results), "搜索结果不包含关键词"
        
    @allure.story("搜索建议功能")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_suggestions_with_keyword(self, driver):
        """测试搜索建议功能"""
        baidu = BaiduPage(driver)
        baidu.open()
        
        # 输入关键词
        search_box = baidu.wait.until(EC.presence_of_element_located(baidu.SEARCH_BOX))
        search_box.send_keys(SEARCH_KEYWORD)
        
        # 验证搜索建议
        suggestions = baidu.get_search_suggestions()
        assert len(suggestions) > 0, "搜索建议为空"
        assert any(SEARCH_KEYWORD in suggestion for suggestion in suggestions), "搜索建议不包含关键词"
        
    @allure.story("回车键搜索")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_with_enter_with_keyword(self, driver):
        """测试回车键搜索"""
        baidu = BaiduPage(driver)
        baidu.open()
        
        # 输入关键词并按回车
        search_box = baidu.wait.until(EC.presence_of_element_located(baidu.SEARCH_BOX))
        search_box.send_keys(SEARCH_KEYWORD + Keys.RETURN)
        
        # 验证搜索结果
        results = baidu.get_search_results()
        assert len(results) > 0, "搜索结果为空"
        assert any(SEARCH_KEYWORD in result for result in results), "搜索结果不包含关键词" 