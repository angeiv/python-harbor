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
from harbor.api.gc_api import GcApi  # noqa: E501
from harbor.rest import ApiException


class TestGcApi(unittest.TestCase):
    """GcApi unit test stubs"""

    def setUp(self):
        self.api = GcApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_gc_schedule(self):
        """Test case for create_gc_schedule

        Create a gc schedule.  # noqa: E501
        """
        pass

    def test_get_gc(self):
        """Test case for get_gc

        Get gc status.  # noqa: E501
        """
        pass

    def test_get_gc_history(self):
        """Test case for get_gc_history

        Get gc results.  # noqa: E501
        """
        pass

    def test_get_gc_log(self):
        """Test case for get_gc_log

        Get gc job log.  # noqa: E501
        """
        pass

    def test_get_gc_schedule(self):
        """Test case for get_gc_schedule

        Get gc's schedule.  # noqa: E501
        """
        pass

    def test_update_gc_schedule(self):
        """Test case for update_gc_schedule

        Update gc's schedule.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
