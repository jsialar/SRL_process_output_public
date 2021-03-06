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


class User(object):
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
        'full_name': 'str',
        'user_name': 'str',
        'domain': 'Domain',
        'type': 'str'
    }

    attribute_map = {
        'full_name': 'fullName',
        'user_name': 'userName',
        'domain': 'domain',
        'type': 'type'
    }

    def __init__(self, full_name=None, user_name=None, domain=None, type=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._full_name = None
        self._user_name = None
        self._domain = None
        self._type = None
        self.discriminator = None

        if full_name is not None:
            self.full_name = full_name
        if user_name is not None:
            self.user_name = user_name
        if domain is not None:
            self.domain = domain
        if type is not None:
            self.type = type

    @property
    def full_name(self):
        """Gets the full_name of this User.  # noqa: E501


        :return: The full_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this User.


        :param full_name: The full_name of this User.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def user_name(self):
        """Gets the user_name of this User.  # noqa: E501


        :return: The user_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this User.


        :param user_name: The user_name of this User.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def domain(self):
        """Gets the domain of this User.  # noqa: E501


        :return: The domain of this User.  # noqa: E501
        :rtype: Domain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this User.


        :param domain: The domain of this User.  # noqa: E501
        :type: Domain
        """

        self._domain = domain

    @property
    def type(self):
        """Gets the type of this User.  # noqa: E501


        :return: The type of this User.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this User.


        :param type: The type of this User.  # noqa: E501
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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
