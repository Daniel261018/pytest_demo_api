# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-07-26 14:19

import pytest
from common.connect_mysql import execute_sql

@pytest.fixture()
def delete_user():
    delete_sql = 'delete from auth_user where username = "test1992"'
    execute_sql(delete_sql)
    yield