# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ICA_SDK
from ICA_SDK.models.task_run_logs import TaskRunLogs  # noqa: E501
from ICA_SDK.rest import ApiException

class TestTaskRunLogs(unittest.TestCase):
    """TaskRunLogs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskRunLogs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.task_run_logs.TaskRunLogs()  # noqa: E501
        if include_optional :
            return TaskRunLogs(
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                error = '0', 
                error_details = '0', 
                stdout = '0', 
                stderr = '0'
            )
        else :
            return TaskRunLogs(
        )

    def testTaskRunLogs(self):
        """Test TaskRunLogs"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
