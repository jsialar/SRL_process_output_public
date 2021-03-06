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
from ICA_SDK.models.update_genome_request import UpdateGenomeRequest  # noqa: E501
from ICA_SDK.rest import ApiException

class TestUpdateGenomeRequest(unittest.TestCase):
    """UpdateGenomeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateGenomeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.update_genome_request.UpdateGenomeRequest()  # noqa: E501
        if include_optional :
            return UpdateGenomeRequest(
                name = '0', 
                display_name = '0', 
                order = -2147483648, 
                is_application_specific = True, 
                build = '0', 
                organization = '0', 
                description = '0', 
                status = 'Active', 
                species = '0', 
                source = '0', 
                dragen_version = '0', 
                data_location_urn = '0', 
                genome_format = 'Dragen', 
                settings = None, 
                source_file_metadata = None, 
                acl = [
                    '0'
                    ], 
                fasta_file_urn = '0', 
                checksum = '0'
            )
        else :
            return UpdateGenomeRequest(
        )

    def testUpdateGenomeRequest(self):
        """Test UpdateGenomeRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
