# 百度搜索Web自动化测试项目

基于百度搜索的Web自动化测试项目，通过Selenium框架实现对百度搜索核心功能的全流程验证。

## 技术栈

- Python: 编程语言
- Selenium WebDriver: Web自动化测试框架
- Pytest: 测试框架
- Jenkins: 持续集成
- Allure: 测试报告生成
- Git: 版本控制

## 项目结构

```
baidu-search-automation/
├── tests/             # 测试用例目录
├── config/            # 配置文件目录
├── reports/           # 测试报告目录
├── scripts/           # 脚本文件目录
└── docs/              # 项目文档目录
```

## 功能特性

- 搜索流程自动化验证
- 多浏览器兼容性测试
- 测试用例管理与执行
- 动态内容与异常场景处理
- 可视化报告生成

## 环境要求

- Python >= 3.8
- Chrome/Firefox 浏览器
- ChromeDriver/GeckoDriver

## 安装

```bash
# 克隆项目
git clone https://github.com/SCUklr/baidu-search-automation.git

# 进入项目目录
cd baidu-search-automation

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 安装Allure命令行工具
# Windows
scoop install allure
# Linux
sudo apt-get install allure
# Mac
brew install allure
```

## 使用说明

```bash
# 运行所有测试
pytest

# 运行特定标记的测试
pytest -m smoke
pytest -m regression
pytest -m browser

# 生成Allure报告
allure generate reports/allure-results -o reports/allure-report --clean
allure serve reports/allure-results
```

## 测试报告

测试报告将生成在 `reports` 目录下：
- HTML报告：`reports/test-report.html`
- Allure报告：`reports/allure-report`

## 持续集成

项目已配置 Jenkins 持续集成，每次代码提交都会自动运行测试并生成报告。

## 贡献指南

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情 