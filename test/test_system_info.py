# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import harbor
from models.system_info import SystemInfo  # noqa: E501
from harbor.rest import ApiException


class TestSystemInfo(unittest.TestCase):
    """SystemInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSystemInfo(self):
        """Test SystemInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = harbor.models.system_info.SystemInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
