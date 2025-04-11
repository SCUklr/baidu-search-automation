"""
测试配置文件
"""
from selenium.webdriver.common.by import By
from pathlib import Path

# 基础URL
BASE_URL = "https://www.baidu.com"

# 浏览器配置
BROWSER_TYPE = "chrome"  # 可选: chrome, firefox
HEADLESS = False  # 是否使用无头模式
IMPLICIT_WAIT = 10  # 隐式等待时间（秒）

# 测试数据
TEST_KEYWORDS = [
    "Python",
    "Selenium",
    "自动化测试",
    "软件测试"
]

# 页面元素定位器
class Locators:
    # 搜索框
    SEARCH_INPUT = (By.ID, "kw")
    # 搜索按钮
    SEARCH_BUTTON = (By.ID, "su")
    # 搜索结果
    SEARCH_RESULTS = (By.XPATH, "//div[contains(@class, 'result')]")
    # 搜索建议
    SEARCH_SUGGESTIONS = (By.CLASS_NAME, "bdsug-overflow")

# 项目路径
PROJECT_ROOT = Path(__file__).parent.parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"

# 确保必要的目录存在
REPORTS_DIR.mkdir(exist_ok=True)
SCREENSHOTS_DIR.mkdir(exist_ok=True)

# Allure报告配置
ALLURE_RESULTS_DIR = REPORTS_DIR / "allure-results"
ALLURE_REPORT_DIR = REPORTS_DIR / "allure-report"

# 重试配置
MAX_RETRY = 2  # 失败用例最大重试次数 