#!/user/bin/env python3
# -*- coding: utf-8 -*-
import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
	def setUp(self):
		print("这个是setUp")
	def tearDown(self):
		print("这个是tearDown")
#邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
	#1,2    3,4    5,6
	@ddt.data(
		[1, 2],
		[3, 4],
		[5, 6]
	)
	@ddt.unpack
	def test_add(self, a, b):
		print(a + b)

if __name__ == '__main__':
    unittest.main()