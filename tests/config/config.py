"""
测试配置文件
"""
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from pathlib import Path

# 加载环境变量
load_dotenv()

# 浏览器配置
BROWSER = os.getenv('BROWSER', 'chrome')  # 默认使用 Chrome
HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'  # 是否使用无头模式

# 测试配置
BASE_URL = "https://www.baidu.com"
SEARCH_KEYWORD = "自动化测试"
WAIT_TIMEOUT = 10  # 等待超时时间（秒）

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

# 报告配置
REPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'reports')
SCREENSHOT_DIR = os.path.join(REPORT_DIR, 'screenshots')

# 确保目录存在
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True) 