"""
Pytest配置文件
"""
import pytest
import allure
from datetime import datetime
from tests.config.config import ALLURE_RESULTS_DIR

def pytest_configure(config):
    """
    Pytest配置
    """
    # 确保allure结果目录存在
    ALLURE_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    测试报告钩子
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        # 添加测试开始时间
        setattr(item, "start_time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        # 添加测试持续时间
        if hasattr(report, "duration"):
            duration = report.duration
            allure.dynamic.description(f"测试持续时间: {duration:.2f} 秒")
        
        # 测试失败时添加截图
        if report.failed:
            if hasattr(item, "funcargs") and "driver" in item.funcargs:
                driver = item.funcargs["driver"]
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

@pytest.fixture(scope="session", autouse=True)
def configure_html_report_env(request):
    """
    配置HTML报告环境信息
    """
    request.config._metadata = {
        "项目名称": "百度搜索自动化测试",
        "测试环境": "测试环境",
        "Python版本": pytest.__version__,
        "操作系统": request.config.invocation_params.args[0] if request.config.invocation_params.args else "Unknown"
    } 