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
from api.auditlog_api import AuditlogApi  # noqa: E501
from harbor.rest import ApiException


class TestAuditlogApi(unittest.TestCase):
    """AuditlogApi unit test stubs"""

    def setUp(self):
        self.api = api.auditlog_api.AuditlogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_audit_logs(self):
        """Test case for list_audit_logs

        Get recent logs of the projects which the user is a member of  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
