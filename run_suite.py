#导包
import unittest
from scripts.test01_login import TestLogin
import time
from tools.HTMLTestRunner import HTMLTestRunner
#组装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
#指定测试报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
#打开文件流
with open(report, "wb") as f:
    #创建HTMLTestRunner运行期
    runner=HTMLTestRunner(f, title="API Report")
    #运行测试套件
    runner.run(suite)
