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


class SequencingRunConfiguration(object):
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
        'instrument_type': 'str',
        'instrument_platform': 'str',
        'num_cycles_read1': 'int',
        'num_cycles_read2': 'int',
        'read_type': 'str',
        'num_cycles_index1': 'int',
        'num_cycles_index2': 'int',
        'use_custom_primer_for_read1': 'bool',
        'use_custom_primer_for_read2': 'bool',
        'use_custom_primer_for_index1': 'bool',
        'use_custom_primer_for_index2': 'bool'
    }

    attribute_map = {
        'instrument_type': 'instrumentType',
        'instrument_platform': 'instrumentPlatform',
        'num_cycles_read1': 'numCyclesRead1',
        'num_cycles_read2': 'numCyclesRead2',
        'read_type': 'readType',
        'num_cycles_index1': 'numCyclesIndex1',
        'num_cycles_index2': 'numCyclesIndex2',
        'use_custom_primer_for_read1': 'useCustomPrimerForRead1',
        'use_custom_primer_for_read2': 'useCustomPrimerForRead2',
        'use_custom_primer_for_index1': 'useCustomPrimerForIndex1',
        'use_custom_primer_for_index2': 'useCustomPrimerForIndex2'
    }

    def __init__(self, instrument_type=None, instrument_platform=None, num_cycles_read1=None, num_cycles_read2=None, read_type=None, num_cycles_index1=None, num_cycles_index2=None, use_custom_primer_for_read1=None, use_custom_primer_for_read2=None, use_custom_primer_for_index1=None, use_custom_primer_for_index2=None, local_vars_configuration=None):  # noqa: E501
        """SequencingRunConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_type = None
        self._instrument_platform = None
        self._num_cycles_read1 = None
        self._num_cycles_read2 = None
        self._read_type = None
        self._num_cycles_index1 = None
        self._num_cycles_index2 = None
        self._use_custom_primer_for_read1 = None
        self._use_custom_primer_for_read2 = None
        self._use_custom_primer_for_index1 = None
        self._use_custom_primer_for_index2 = None
        self.discriminator = None

        if instrument_type is not None:
            self.instrument_type = instrument_type
        if instrument_platform is not None:
            self.instrument_platform = instrument_platform
        if num_cycles_read1 is not None:
            self.num_cycles_read1 = num_cycles_read1
        if num_cycles_read2 is not None:
            self.num_cycles_read2 = num_cycles_read2
        if read_type is not None:
            self.read_type = read_type
        if num_cycles_index1 is not None:
            self.num_cycles_index1 = num_cycles_index1
        if num_cycles_index2 is not None:
            self.num_cycles_index2 = num_cycles_index2
        if use_custom_primer_for_read1 is not None:
            self.use_custom_primer_for_read1 = use_custom_primer_for_read1
        if use_custom_primer_for_read2 is not None:
            self.use_custom_primer_for_read2 = use_custom_primer_for_read2
        if use_custom_primer_for_index1 is not None:
            self.use_custom_primer_for_index1 = use_custom_primer_for_index1
        if use_custom_primer_for_index2 is not None:
            self.use_custom_primer_for_index2 = use_custom_primer_for_index2

    @property
    def instrument_type(self):
        """Gets the instrument_type of this SequencingRunConfiguration.  # noqa: E501

        Type of instrument for which the run is planned  # noqa: E501

        :return: The instrument_type of this SequencingRunConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this SequencingRunConfiguration.

        Type of instrument for which the run is planned  # noqa: E501

        :param instrument_type: The instrument_type of this SequencingRunConfiguration.  # noqa: E501
        :type: str
        """

        self._instrument_type = instrument_type

    @property
    def instrument_platform(self):
        """Gets the instrument_platform of this SequencingRunConfiguration.  # noqa: E501

        Platform of instrument for which the run is planned  # noqa: E501

        :return: The instrument_platform of this SequencingRunConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._instrument_platform

    @instrument_platform.setter
    def instrument_platform(self, instrument_platform):
        """Sets the instrument_platform of this SequencingRunConfiguration.

        Platform of instrument for which the run is planned  # noqa: E501

        :param instrument_platform: The instrument_platform of this SequencingRunConfiguration.  # noqa: E501
        :type: str
        """

        self._instrument_platform = instrument_platform

    @property
    def num_cycles_read1(self):
        """Gets the num_cycles_read1 of this SequencingRunConfiguration.  # noqa: E501

        Number of read 1 cycles  # noqa: E501

        :return: The num_cycles_read1 of this SequencingRunConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._num_cycles_read1

    @num_cycles_read1.setter
    def num_cycles_read1(self, num_cycles_read1):
        """Sets the num_cycles_read1 of this SequencingRunConfiguration.

        Number of read 1 cycles  # noqa: E501

        :param num_cycles_read1: The num_cycles_read1 of this SequencingRunConfiguration.  # noqa: E501
        :type: int
        """

        self._num_cycles_read1 = num_cycles_read1

    @property
    def num_cycles_read2(self):
        """Gets the num_cycles_read2 of this SequencingRunConfiguration.  # noqa: E501

        Number of read 2 cycles  # noqa: E501

        :return: The num_cycles_read2 of this SequencingRunConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._num_cycles_read2

    @num_cycles_read2.setter
    def num_cycles_read2(self, num_cycles_read2):
        """Sets the num_cycles_read2 of this SequencingRunConfiguration.

        Number of read 2 cycles  # noqa: E501

        :param num_cycles_read2: The num_cycles_read2 of this SequencingRunConfiguration.  # noqa: E501
        :type: int
        """

        self._num_cycles_read2 = num_cycles_read2

    @property
    def read_type(self):
        """Gets the read_type of this SequencingRunConfiguration.  # noqa: E501

        Read type  # noqa: E501

        :return: The read_type of this SequencingRunConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._read_type

    @read_type.setter
    def read_type(self, read_type):
        """Sets the read_type of this SequencingRunConfiguration.

        Read type  # noqa: E501

        :param read_type: The read_type of this SequencingRunConfiguration.  # noqa: E501
        :type: str
        """

        self._read_type = read_type

    @property
    def num_cycles_index1(self):
        """Gets the num_cycles_index1 of this SequencingRunConfiguration.  # noqa: E501

        Number of index 1 cycles  # noqa: E501

        :return: The num_cycles_index1 of this SequencingRunConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._num_cycles_index1

    @num_cycles_index1.setter
    def num_cycles_index1(self, num_cycles_index1):
        """Sets the num_cycles_index1 of this SequencingRunConfiguration.

        Number of index 1 cycles  # noqa: E501

        :param num_cycles_index1: The num_cycles_index1 of this SequencingRunConfiguration.  # noqa: E501
        :type: int
        """

        self._num_cycles_index1 = num_cycles_index1

    @property
    def num_cycles_index2(self):
        """Gets the num_cycles_index2 of this SequencingRunConfiguration.  # noqa: E501

        Number of index 2 cycles  # noqa: E501

        :return: The num_cycles_index2 of this SequencingRunConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._num_cycles_index2

    @num_cycles_index2.setter
    def num_cycles_index2(self, num_cycles_index2):
        """Sets the num_cycles_index2 of this SequencingRunConfiguration.

        Number of index 2 cycles  # noqa: E501

        :param num_cycles_index2: The num_cycles_index2 of this SequencingRunConfiguration.  # noqa: E501
        :type: int
        """

        self._num_cycles_index2 = num_cycles_index2

    @property
    def use_custom_primer_for_read1(self):
        """Gets the use_custom_primer_for_read1 of this SequencingRunConfiguration.  # noqa: E501

        Indicates whether read 1 uses custom primer  # noqa: E501

        :return: The use_custom_primer_for_read1 of this SequencingRunConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_custom_primer_for_read1

    @use_custom_primer_for_read1.setter
    def use_custom_primer_for_read1(self, use_custom_primer_for_read1):
        """Sets the use_custom_primer_for_read1 of this SequencingRunConfiguration.

        Indicates whether read 1 uses custom primer  # noqa: E501

        :param use_custom_primer_for_read1: The use_custom_primer_for_read1 of this SequencingRunConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_custom_primer_for_read1 = use_custom_primer_for_read1

    @property
    def use_custom_primer_for_read2(self):
        """Gets the use_custom_primer_for_read2 of this SequencingRunConfiguration.  # noqa: E501

        Indicates whether read 2 uses custom primer  # noqa: E501

        :return: The use_custom_primer_for_read2 of this SequencingRunConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_custom_primer_for_read2

    @use_custom_primer_for_read2.setter
    def use_custom_primer_for_read2(self, use_custom_primer_for_read2):
        """Sets the use_custom_primer_for_read2 of this SequencingRunConfiguration.

        Indicates whether read 2 uses custom primer  # noqa: E501

        :param use_custom_primer_for_read2: The use_custom_primer_for_read2 of this SequencingRunConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_custom_primer_for_read2 = use_custom_primer_for_read2

    @property
    def use_custom_primer_for_index1(self):
        """Gets the use_custom_primer_for_index1 of this SequencingRunConfiguration.  # noqa: E501

        Indicates whether index 1 uses custom primer  # noqa: E501

        :return: The use_custom_primer_for_index1 of this SequencingRunConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_custom_primer_for_index1

    @use_custom_primer_for_index1.setter
    def use_custom_primer_for_index1(self, use_custom_primer_for_index1):
        """Sets the use_custom_primer_for_index1 of this SequencingRunConfiguration.

        Indicates whether index 1 uses custom primer  # noqa: E501

        :param use_custom_primer_for_index1: The use_custom_primer_for_index1 of this SequencingRunConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_custom_primer_for_index1 = use_custom_primer_for_index1

    @property
    def use_custom_primer_for_index2(self):
        """Gets the use_custom_primer_for_index2 of this SequencingRunConfiguration.  # noqa: E501

        Indicates whether index 2 uses custom primer  # noqa: E501

        :return: The use_custom_primer_for_index2 of this SequencingRunConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._use_custom_primer_for_index2

    @use_custom_primer_for_index2.setter
    def use_custom_primer_for_index2(self, use_custom_primer_for_index2):
        """Sets the use_custom_primer_for_index2 of this SequencingRunConfiguration.

        Indicates whether index 2 uses custom primer  # noqa: E501

        :param use_custom_primer_for_index2: The use_custom_primer_for_index2 of this SequencingRunConfiguration.  # noqa: E501
        :type: bool
        """

        self._use_custom_primer_for_index2 = use_custom_primer_for_index2

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
        if not isinstance(other, SequencingRunConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SequencingRunConfiguration):
            return True

        return self.to_dict() != other.to_dict()
