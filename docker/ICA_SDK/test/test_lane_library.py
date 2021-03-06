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
from ICA_SDK.models.lane_library import LaneLibrary  # noqa: E501
from ICA_SDK.rest import ApiException

class TestLaneLibrary(unittest.TestCase):
    """LaneLibrary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LaneLibrary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.lane_library.LaneLibrary()  # noqa: E501
        if include_optional :
            return LaneLibrary(
                sample_name = '0', 
                sample_urn = '0', 
                project_name = '0', 
                library_name = '0', 
                library_urn = '0', 
                adapter_sequence_read1 = '0', 
                adapter_sequence_read2 = '0', 
                index1_sequence = '0', 
                index2_sequence = '0', 
                index_container_position = '0', 
                index1_name = '0', 
                index2_name = '0', 
                library_prep_kit_urn = '0', 
                index_adapter_kit_urn = '0'
            )
        else :
            return LaneLibrary(
        )

    def testLaneLibrary(self):
        """Test LaneLibrary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
