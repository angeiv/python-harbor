# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import harbor
from harbor.models.retention_policy import RetentionPolicy  # noqa: E501
from harbor.rest import ApiException


class TestRetentionPolicy(unittest.TestCase):
    """RetentionPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRetentionPolicy(self):
        """Test RetentionPolicy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = harbor.models.retention_policy.RetentionPolicy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
