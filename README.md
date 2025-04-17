# 百度搜索自动化测试项目

## 项目简介
本项目是一个基于 Python + Selenium WebDriver 的百度搜索自动化测试项目，用于验证百度搜索功能的正确性和稳定性。

## 技术栈
- Python 3.8+
- Selenium WebDriver
- Pytest
- Jenkins
- Allure
- Git

## 功能特点
1. 搜索流程自动化验证
2. 多浏览器兼容性测试
3. 动态内容处理
4. 异常场景处理
5. 自动化测试报告生成

## 项目结构
```
baidu-search-automation/
├── tests/
│   ├── config/             # 配置文件
│   ├── pages/             # 页面对象
│   ├── test_cases/        # 测试用例
│   └── utils/             # 工具类
├── reports/               # 测试报告
├── requirements.txt       # 项目依赖
├── pytest.ini            # pytest配置
├── Jenkinsfile           # Jenkins配置
└── README.md             # 项目说明
```

## 环境要求
- Python 3.8+
- Chrome/Firefox 浏览器
- Jenkins
- Allure

## 安装步骤
1. 克隆项目
```bash
git clone https://github.com/SCUklr/baidu-search-automation.git
cd baidu-search-automation
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 安装 Allure（Windows）
```bash
scoop install allure
```

## 运行测试
1. 运行所有测试
```bash
pytest
```

2. 运行特定测试
```bash
pytest tests/test_cases/test_baidu_search.py
```

3. 生成 Allure 报告
```bash
pytest --alluredir=./reports/allure-results
allure serve ./reports/allure-results
```

## Jenkins 配置
1. 安装 Jenkins
2. 安装必要的插件：
   - Git
   - Allure
   - Pipeline
3. 创建新的 Pipeline 项目
4. 配置 Jenkinsfile

## 测试报告
测试报告将生成在 `reports` 目录下：
- HTML 报告：`reports/test-report.html`
- Allure 报告：`reports/allure-report`

## 注意事项
1. 确保已安装 Chrome 或 Firefox 浏览器
2. 确保网络连接正常
3. 首次运行会自动下载浏览器驱动 