import pytest
import platform
import sys

def pytest_configure(config):
    config._metadata = {
        'Python版本': sys.version.split()[0],
        '操作系统': platform.platform(),
        '项目名称': '百度搜索自动化测试',
        '测试环境': '测试环境'
    } 