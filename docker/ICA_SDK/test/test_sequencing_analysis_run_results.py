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
from ICA_SDK.models.sequencing_analysis_run_results import SequencingAnalysisRunResults  # noqa: E501
from ICA_SDK.rest import ApiException

class TestSequencingAnalysisRunResults(unittest.TestCase):
    """SequencingAnalysisRunResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SequencingAnalysisRunResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.sequencing_analysis_run_results.SequencingAnalysisRunResults()  # noqa: E501
        if include_optional :
            return SequencingAnalysisRunResults(
                demuxing_results = ICA_SDK.models.demuxing_results.demuxingResults(), 
                analysis_results = ICA_SDK.models.analysis_results.analysisResults(), 
                launch_parameters_snapshot = ICA_SDK.models.launch_parameters_snapshot.launchParametersSnapshot(), 
                sample_mapping = ICA_SDK.models.sample_mapping.sampleMapping(), 
                sample_sheet_snapshot = '0', 
                created_by = '0', 
                modified_by = '0', 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return SequencingAnalysisRunResults(
        )

    def testSequencingAnalysisRunResults(self):
        """Test SequencingAnalysisRunResults"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
