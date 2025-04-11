# 百度搜索自动化测试项目

基于Python + Selenium WebDriver的百度搜索自动化测试项目，实现对百度搜索核心功能的自动化验证。

## 项目特点

- 使用Page Object Model设计模式
- 支持多浏览器测试
- 集成Allure测试报告
- 实现失败重试机制
- 自动截图和日志记录
- 支持并行测试执行

## 环境要求

- Python 3.11+
- Chrome浏览器
- Allure命令行工具

## 安装步骤

1. 克隆项目：
```bash
git clone [项目地址]
cd baidu-search-automation
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 安装Allure（Windows）：
```bash
scoop install allure
```

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
└── README.md             # 项目说明
```

## 运行测试

1. 运行所有测试：
```bash
pytest
```

2. 运行特定测试：
```bash
pytest tests/test_cases/test_baidu_search.py
```

3. 生成Allure报告：
```bash
pytest --alluredir=./reports/allure-results
allure serve ./reports/allure-results
```

## 测试用例说明

- test_search: 测试基本搜索功能
- test_search_suggestions: 测试搜索建议功能
- test_search_with_enter: 测试回车键搜索
- test_clear_search_input: 测试清空搜索框

## 配置说明

在 `tests/config/config.py` 中可以修改以下配置：

- 浏览器类型
- 测试关键词
- 等待时间
- 截图保存路径
- 失败重试次数

## 注意事项

1. 确保Chrome浏览器已安装
2. 确保网络连接正常
3. 首次运行会自动下载ChromeDriver

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License 