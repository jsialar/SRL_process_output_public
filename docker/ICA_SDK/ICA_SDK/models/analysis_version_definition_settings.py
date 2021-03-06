# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ICA_SDK.configuration import Configuration


class AnalysisVersionDefinitionSettings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'sample_sheet': 'AnalysisVersionDefinitionSettingsSampleSheetConfiguration',
        'run_analysis_settings': 'object',
        'run_setup_validation': 'RunSetupValidation',
        'workflow_metadata': 'WorkflowMetadataDto'
    }

    attribute_map = {
        'sample_sheet': 'sampleSheet',
        'run_analysis_settings': 'runAnalysisSettings',
        'run_setup_validation': 'runSetupValidation',
        'workflow_metadata': 'workflowMetadata'
    }

    def __init__(self, sample_sheet=None, run_analysis_settings=None, run_setup_validation=None, workflow_metadata=None, local_vars_configuration=None):  # noqa: E501
        """AnalysisVersionDefinitionSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sample_sheet = None
        self._run_analysis_settings = None
        self._run_setup_validation = None
        self._workflow_metadata = None
        self.discriminator = None

        if sample_sheet is not None:
            self.sample_sheet = sample_sheet
        if run_analysis_settings is not None:
            self.run_analysis_settings = run_analysis_settings
        if run_setup_validation is not None:
            self.run_setup_validation = run_setup_validation
        if workflow_metadata is not None:
            self.workflow_metadata = workflow_metadata

    @property
    def sample_sheet(self):
        """Gets the sample_sheet of this AnalysisVersionDefinitionSettings.  # noqa: E501


        :return: The sample_sheet of this AnalysisVersionDefinitionSettings.  # noqa: E501
        :rtype: AnalysisVersionDefinitionSettingsSampleSheetConfiguration
        """
        return self._sample_sheet

    @sample_sheet.setter
    def sample_sheet(self, sample_sheet):
        """Sets the sample_sheet of this AnalysisVersionDefinitionSettings.


        :param sample_sheet: The sample_sheet of this AnalysisVersionDefinitionSettings.  # noqa: E501
        :type: AnalysisVersionDefinitionSettingsSampleSheetConfiguration
        """

        self._sample_sheet = sample_sheet

    @property
    def run_analysis_settings(self):
        """Gets the run_analysis_settings of this AnalysisVersionDefinitionSettings.  # noqa: E501

        Run analysis settings for a sequencing run  # noqa: E501

        :return: The run_analysis_settings of this AnalysisVersionDefinitionSettings.  # noqa: E501
        :rtype: object
        """
        return self._run_analysis_settings

    @run_analysis_settings.setter
    def run_analysis_settings(self, run_analysis_settings):
        """Sets the run_analysis_settings of this AnalysisVersionDefinitionSettings.

        Run analysis settings for a sequencing run  # noqa: E501

        :param run_analysis_settings: The run_analysis_settings of this AnalysisVersionDefinitionSettings.  # noqa: E501
        :type: object
        """

        self._run_analysis_settings = run_analysis_settings

    @property
    def run_setup_validation(self):
        """Gets the run_setup_validation of this AnalysisVersionDefinitionSettings.  # noqa: E501


        :return: The run_setup_validation of this AnalysisVersionDefinitionSettings.  # noqa: E501
        :rtype: RunSetupValidation
        """
        return self._run_setup_validation

    @run_setup_validation.setter
    def run_setup_validation(self, run_setup_validation):
        """Sets the run_setup_validation of this AnalysisVersionDefinitionSettings.


        :param run_setup_validation: The run_setup_validation of this AnalysisVersionDefinitionSettings.  # noqa: E501
        :type: RunSetupValidation
        """

        self._run_setup_validation = run_setup_validation

    @property
    def workflow_metadata(self):
        """Gets the workflow_metadata of this AnalysisVersionDefinitionSettings.  # noqa: E501


        :return: The workflow_metadata of this AnalysisVersionDefinitionSettings.  # noqa: E501
        :rtype: WorkflowMetadataDto
        """
        return self._workflow_metadata

    @workflow_metadata.setter
    def workflow_metadata(self, workflow_metadata):
        """Sets the workflow_metadata of this AnalysisVersionDefinitionSettings.


        :param workflow_metadata: The workflow_metadata of this AnalysisVersionDefinitionSettings.  # noqa: E501
        :type: WorkflowMetadataDto
        """

        self._workflow_metadata = workflow_metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalysisVersionDefinitionSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnalysisVersionDefinitionSettings):
            return True

        return self.to_dict() != other.to_dict()
