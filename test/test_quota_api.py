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
from api.quota_api import QuotaApi  # noqa: E501
from harbor.rest import ApiException


class TestQuotaApi(unittest.TestCase):
    """QuotaApi unit test stubs"""

    def setUp(self):
        self.api = api.quota_api.QuotaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_quotas_id_get(self):
        """Test case for quotas_id_get

        Get the specified quota  # noqa: E501
        """
        pass

    def test_quotas_id_put(self):
        """Test case for quotas_id_put

        Update the specified quota  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
