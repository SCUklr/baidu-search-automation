import os
import allure
from datetime import datetime
from tests.config.config import SCREENSHOT_DIR

def take_screenshot(driver, name=None):
    """截图并添加到 Allure 报告"""
    if name is None:
        name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # 确保截图目录存在
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    
    # 保存截图
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(screenshot_path)
    
    # 添加到 Allure 报告
    allure.attach.file(
        screenshot_path,
        name=name,
        attachment_type=allure.attachment_type.PNG
    ) 