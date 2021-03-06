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
from ICA_SDK.models.update_sequencing_run_configuration_request import UpdateSequencingRunConfigurationRequest  # noqa: E501
from ICA_SDK.rest import ApiException

class TestUpdateSequencingRunConfigurationRequest(unittest.TestCase):
    """UpdateSequencingRunConfigurationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateSequencingRunConfigurationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.update_sequencing_run_configuration_request.UpdateSequencingRunConfigurationRequest()  # noqa: E501
        if include_optional :
            return UpdateSequencingRunConfigurationRequest(
                run_name = '0', 
                description = '0', 
                regulatory_mode = 'RUO', 
                instrument_type = '0', 
                instrument_platform = '0', 
                num_cycles_read1 = 0, 
                num_cycles_read2 = 0, 
                read_type = 'Single', 
                num_cycles_index1 = 0, 
                num_cycles_index2 = 0, 
                use_custom_primer_for_read1 = True, 
                use_custom_primer_for_read2 = True, 
                use_custom_primer_for_index1 = True, 
                use_custom_primer_for_index2 = True
            )
        else :
            return UpdateSequencingRunConfigurationRequest(
        )

    def testUpdateSequencingRunConfigurationRequest(self):
        """Test UpdateSequencingRunConfigurationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
