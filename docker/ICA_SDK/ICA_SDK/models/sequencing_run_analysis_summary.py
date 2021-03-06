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


class SequencingRunAnalysisSummary(object):
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
        'definition_id': 'str',
        'configuration_id': 'str',
        'name': 'str',
        'display_name': 'str',
        'version': 'str',
        'organization': 'str',
        'type': 'str'
    }

    attribute_map = {
        'definition_id': 'definitionId',
        'configuration_id': 'configurationId',
        'name': 'name',
        'display_name': 'displayName',
        'version': 'version',
        'organization': 'organization',
        'type': 'type'
    }

    def __init__(self, definition_id=None, configuration_id=None, name=None, display_name=None, version=None, organization=None, type=None, local_vars_configuration=None):  # noqa: E501
        """SequencingRunAnalysisSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._definition_id = None
        self._configuration_id = None
        self._name = None
        self._display_name = None
        self._version = None
        self._organization = None
        self._type = None
        self.discriminator = None

        if definition_id is not None:
            self.definition_id = definition_id
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if version is not None:
            self.version = version
        if organization is not None:
            self.organization = organization
        if type is not None:
            self.type = type

    @property
    def definition_id(self):
        """Gets the definition_id of this SequencingRunAnalysisSummary.  # noqa: E501

        Analysis version definition id  # noqa: E501

        :return: The definition_id of this SequencingRunAnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._definition_id

    @definition_id.setter
    def definition_id(self, definition_id):
        """Sets the definition_id of this SequencingRunAnalysisSummary.

        Analysis version definition id  # noqa: E501

        :param definition_id: The definition_id of this SequencingRunAnalysisSummary.  # noqa: E501
        :type: str
        """

        self._definition_id = definition_id

    @property
    def configuration_id(self):
        """Gets the configuration_id of this SequencingRunAnalysisSummary.  # noqa: E501

        Analysis configuration id  # noqa: E501

        :return: The configuration_id of this SequencingRunAnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this SequencingRunAnalysisSummary.

        Analysis configuration id  # noqa: E501

        :param configuration_id: The configuration_id of this SequencingRunAnalysisSummary.  # noqa: E501
        :type: str
        """

        self._configuration_id = configuration_id

    @property
    def name(self):
        """Gets the name of this SequencingRunAnalysisSummary.  # noqa: E501

        Analysis name  # noqa: E501

        :return: The name of this SequencingRunAnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SequencingRunAnalysisSummary.

        Analysis name  # noqa: E501

        :param name: The name of this SequencingRunAnalysisSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this SequencingRunAnalysisSummary.  # noqa: E501

        Analysis display name  # noqa: E501

        :return: The display_name of this SequencingRunAnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SequencingRunAnalysisSummary.

        Analysis display name  # noqa: E501

        :param display_name: The display_name of this SequencingRunAnalysisSummary.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def version(self):
        """Gets the version of this SequencingRunAnalysisSummary.  # noqa: E501

        Analysis version  # noqa: E501

        :return: The version of this SequencingRunAnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SequencingRunAnalysisSummary.

        Analysis version  # noqa: E501

        :param version: The version of this SequencingRunAnalysisSummary.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def organization(self):
        """Gets the organization of this SequencingRunAnalysisSummary.  # noqa: E501

        Analysis organization  # noqa: E501

        :return: The organization of this SequencingRunAnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this SequencingRunAnalysisSummary.

        Analysis organization  # noqa: E501

        :param organization: The organization of this SequencingRunAnalysisSummary.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def type(self):
        """Gets the type of this SequencingRunAnalysisSummary.  # noqa: E501

        Analysis type  # noqa: E501

        :return: The type of this SequencingRunAnalysisSummary.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SequencingRunAnalysisSummary.

        Analysis type  # noqa: E501

        :param type: The type of this SequencingRunAnalysisSummary.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, SequencingRunAnalysisSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SequencingRunAnalysisSummary):
            return True

        return self.to_dict() != other.to_dict()
