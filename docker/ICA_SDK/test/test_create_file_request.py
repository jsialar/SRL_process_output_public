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
from ICA_SDK.models.create_file_request import CreateFileRequest  # noqa: E501
from ICA_SDK.rest import ApiException

class TestCreateFileRequest(unittest.TestCase):
    """CreateFileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateFileRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.create_file_request.CreateFileRequest()  # noqa: E501
        if include_optional :
            return CreateFileRequest(
                name = 'a', 
                volume_id = '0', 
                folder_path = '0', 
                type = '0', 
                volume_name = '0', 
                format = '0', 
                format_edam = '0', 
                metadata = None
            )
        else :
            return CreateFileRequest(
                name = 'a',
        )

    def testCreateFileRequest(self):
        """Test CreateFileRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
