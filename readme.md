# һ����Ŀ׼��
# 1������׼��
- python 3.6.5
- pytest 4.5.0
- allure-pytest==2.8.6

# 2����װ��������cmd ��ĿĿ¼�£�Ȼ���Ȱ�װrequirements.txt
- pip3 install -r requirements.txt
- ���� pip3 install -r requirements.txt  --index-url https://pypi.douban.com/simple
- ���� pip3 install -r requirements.txt  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

# 3��ִ����������Ŀ��Ŀ¼
- pytest

# 4��ִ�д��룬���������룬������ͨ����
"""
- pytest --pytest_report ./report/Pytest_Report.html
"""

# 5������allure����
"""
- pytest --alluredir ./report/allure
- allure serve ./report/allure -p ָ���˿ں�
"""

# 6�����û����������Զ���Ч
- pytest --cmdhost="��Ŀ����"

# ��������˵������
# 1��pip������Ŀ������,cd����Ӧ��ĿĿ¼����������
- pip freeze > requirements.txt

# 2��pi��װʧ�ܣ�ʹ�ö���Դ��װ
����Դ��
- pip install nb_log -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
- pip3 install ����==�汾�� --index-url https://pypi.douban.com/simple

# 3�������ļ�����
- pytest --html=./report/report.html --self-contained-html
- addopts =  --pytest_report ./report/Pytest_Report.html

# 4��allure�����ȼ�
- blocker�� ����ȱ�ݣ�����δʵ�֣��޷���һ����
- critical������ȱ�ݣ����ܵ�ȱʧ��
- normal����һ��ȱ�ݣ��߽��������ʽ����
- minor��   ��Ҫȱ�ݣ����������ui���󲻷���
- trivial�� ��΢ȱ�ݣ�����������ʾ��������ʾ���淶��

# 5��scope����������session�� module��class��function�� Ĭ��Ϊfunction
- session �Ự����ͨ������������conftest.py�ļ�ʹ�ã����Ժ���˵��conftest.py�ļ���ʱ����˵
- module ģ�鼶�� ģ�������е�����ִ��ǰִ��һ��module�����fixture
- class �༶�� ��ÿ����ִ��ǰ����ִ��һ��class�����fixture
- function ��ǰ��ʵ���Ѿ�˵�ˣ����Ĭ����Ĭ�ϵ�ģʽ����������ģ�ÿ����������ִ��ǰ����ִ��һ��function�����fixture

   