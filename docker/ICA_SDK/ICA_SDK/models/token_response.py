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


class TokenResponse(object):
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
        'access_token': 'str',
        'token_type': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'token_type': 'token_type'
    }

    def __init__(self, access_token=None, token_type=None, local_vars_configuration=None):  # noqa: E501
        """TokenResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._token_type = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if token_type is not None:
            self.token_type = token_type

    @property
    def access_token(self):
        """Gets the access_token of this TokenResponse.  # noqa: E501

        The returned token is either a psToken or a JWT token depending on the context of the call.  # noqa: E501

        :return: The access_token of this TokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this TokenResponse.

        The returned token is either a psToken or a JWT token depending on the context of the call.  # noqa: E501

        :param access_token: The access_token of this TokenResponse.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def token_type(self):
        """Gets the token_type of this TokenResponse.  # noqa: E501

        The type of token requested.  # noqa: E501

        :return: The token_type of this TokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this TokenResponse.

        The type of token requested.  # noqa: E501

        :param token_type: The token_type of this TokenResponse.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

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
        if not isinstance(other, TokenResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenResponse):
            return True

        return self.to_dict() != other.to_dict()
