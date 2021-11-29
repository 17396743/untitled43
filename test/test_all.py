import unittest
from case.test_baidu import TestBaidu
from .HTMLTestRunner import HTMLTestRunner

if __name__=="__main__":
# unittest.TestSuite 这个是  unittest 测试脚本的绑定操作
    suite=unittest.TestSuite()
#添加参数
#添加 test_baidu 里面的类，括号里面填def的方法名，如：test_search

    suite.addTest(TestBaidu("test_search"))

    with open("report.html","wb") as f:
        HTMLTestRunner(
            stream=f,
            verbosity=2,
            title="百度搜索",
            description="miaos"
        ).run(suite)