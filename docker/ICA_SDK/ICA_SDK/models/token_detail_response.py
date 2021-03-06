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


class TokenDetailResponse(object):
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
        'uid': 'str',
        'name': 'str',
        'username': 'str',
        'current_workgroup': 'Workgroup',
        'tid': 'str',
        'acls': 'list[str]',
        'domain': 'Domain'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'username': 'username',
        'current_workgroup': 'currentWorkgroup',
        'tid': 'tid',
        'acls': 'acls',
        'domain': 'domain'
    }

    def __init__(self, uid=None, name=None, username=None, current_workgroup=None, tid=None, acls=None, domain=None, local_vars_configuration=None):  # noqa: E501
        """TokenDetailResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._name = None
        self._username = None
        self._current_workgroup = None
        self._tid = None
        self._acls = None
        self._domain = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if current_workgroup is not None:
            self.current_workgroup = current_workgroup
        if tid is not None:
            self.tid = tid
        if acls is not None:
            self.acls = acls
        if domain is not None:
            self.domain = domain

    @property
    def uid(self):
        """Gets the uid of this TokenDetailResponse.  # noqa: E501


        :return: The uid of this TokenDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this TokenDetailResponse.


        :param uid: The uid of this TokenDetailResponse.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this TokenDetailResponse.  # noqa: E501


        :return: The name of this TokenDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TokenDetailResponse.


        :param name: The name of this TokenDetailResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def username(self):
        """Gets the username of this TokenDetailResponse.  # noqa: E501


        :return: The username of this TokenDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TokenDetailResponse.


        :param username: The username of this TokenDetailResponse.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def current_workgroup(self):
        """Gets the current_workgroup of this TokenDetailResponse.  # noqa: E501


        :return: The current_workgroup of this TokenDetailResponse.  # noqa: E501
        :rtype: Workgroup
        """
        return self._current_workgroup

    @current_workgroup.setter
    def current_workgroup(self, current_workgroup):
        """Sets the current_workgroup of this TokenDetailResponse.


        :param current_workgroup: The current_workgroup of this TokenDetailResponse.  # noqa: E501
        :type: Workgroup
        """

        self._current_workgroup = current_workgroup

    @property
    def tid(self):
        """Gets the tid of this TokenDetailResponse.  # noqa: E501


        :return: The tid of this TokenDetailResponse.  # noqa: E501
        :rtype: str
        """
        return self._tid

    @tid.setter
    def tid(self, tid):
        """Sets the tid of this TokenDetailResponse.


        :param tid: The tid of this TokenDetailResponse.  # noqa: E501
        :type: str
        """

        self._tid = tid

    @property
    def acls(self):
        """Gets the acls of this TokenDetailResponse.  # noqa: E501


        :return: The acls of this TokenDetailResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._acls

    @acls.setter
    def acls(self, acls):
        """Sets the acls of this TokenDetailResponse.


        :param acls: The acls of this TokenDetailResponse.  # noqa: E501
        :type: list[str]
        """

        self._acls = acls

    @property
    def domain(self):
        """Gets the domain of this TokenDetailResponse.  # noqa: E501


        :return: The domain of this TokenDetailResponse.  # noqa: E501
        :rtype: Domain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this TokenDetailResponse.


        :param domain: The domain of this TokenDetailResponse.  # noqa: E501
        :type: Domain
        """

        self._domain = domain

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
        if not isinstance(other, TokenDetailResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenDetailResponse):
            return True

        return self.to_dict() != other.to_dict()
