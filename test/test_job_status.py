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
from models.job_status import JobStatus  # noqa: E501
from harbor.rest import ApiException


class TestJobStatus(unittest.TestCase):
    """JobStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobStatus(self):
        """Test JobStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = harbor.models.job_status.JobStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
