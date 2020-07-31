# 一、项目准备
# 1、环境准备
- python 3.6.5
- pytest 4.5.0
- allure-pytest==2.8.6

# 2、安装依赖包，cmd 项目目录下，然后先安装requirements.txt
- pip3 install -r requirements.txt
- 或者 pip3 install -r requirements.txt  --index-url https://pypi.douban.com/simple
- 或者 pip3 install -r requirements.txt  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

# 3、执行用例，项目根目录
- pytest

# 4、执行代码，命令行输入，生成普通报告
"""
- pytest --pytest_report ./report/Pytest_Report.html
"""

# 5、生成allure报告
"""
- pytest --alluredir ./report/allure
- allure serve ./report/allure -p 指定端口号
"""

# 6、设置环境变量，自动生效
- pytest --cmdhost="项目环境"

# 二、其他说明操作
# 1、pip导出项目依赖包,cd到相应项目目录命令行输入
- pip freeze > requirements.txt

# 2、pi安装失败，使用豆瓣源安装
豆瓣源：
- pip install nb_log -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
- pip3 install 库名==版本号 --index-url https://pypi.douban.com/simple

# 3、配置文件配置
- pytest --html=./report/report.html --self-contained-html
- addopts =  --pytest_report ./report/Pytest_Report.html

# 4、allure用例等级
- blocker　 阻塞缺陷（功能未实现，无法下一步）
- critical　严重缺陷（功能点缺失）
- normal　　一般缺陷（边界情况，格式错误）
- minor　   次要缺陷（界面错误与ui需求不符）
- trivial　 轻微缺陷（必须项无提示，或者提示不规范）

# 5、scope参数可以是session， module，class，function； 默认为function
- session 会话级别（通常这个级别会结合conftest.py文件使用，所以后面说到conftest.py文件的时候再说
- module 模块级别： 模块里所有的用例执行前执行一次module级别的fixture
- class 类级别 ：每个类执行前都会执行一次class级别的fixture
- function ：前面实例已经说了，这个默认是默认的模式，函数级别的，每个测试用例执行前都会执行一次function级别的fixture

   