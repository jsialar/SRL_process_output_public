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


class IndexAdapterKitSettings(object):
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
        'default_index_strategy': 'str',
        'override_cycles': 'str',
        'fixed_layout': 'bool',
        'multiplate': 'bool',
        'multiple_indexes_per_well': 'bool',
        'fixed_index_positions': 'list[str]',
        'enable_custom_index_cycles': 'bool',
        'num_cycles_index1_override': 'int',
        'num_cycles_index2_override': 'int',
        'fixed_layout_position_key_by_index_id': 'bool',
        'custom_bcl_convert_settings': 'dict(str, str)'
    }

    attribute_map = {
        'default_index_strategy': 'defaultIndexStrategy',
        'override_cycles': 'overrideCycles',
        'fixed_layout': 'fixedLayout',
        'multiplate': 'multiplate',
        'multiple_indexes_per_well': 'multipleIndexesPerWell',
        'fixed_index_positions': 'fixedIndexPositions',
        'enable_custom_index_cycles': 'enableCustomIndexCycles',
        'num_cycles_index1_override': 'numCyclesIndex1Override',
        'num_cycles_index2_override': 'numCyclesIndex2Override',
        'fixed_layout_position_key_by_index_id': 'fixedLayoutPositionKeyByIndexId',
        'custom_bcl_convert_settings': 'customBclConvertSettings'
    }

    def __init__(self, default_index_strategy=None, override_cycles=None, fixed_layout=None, multiplate=None, multiple_indexes_per_well=None, fixed_index_positions=None, enable_custom_index_cycles=None, num_cycles_index1_override=None, num_cycles_index2_override=None, fixed_layout_position_key_by_index_id=None, custom_bcl_convert_settings=None, local_vars_configuration=None):  # noqa: E501
        """IndexAdapterKitSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_index_strategy = None
        self._override_cycles = None
        self._fixed_layout = None
        self._multiplate = None
        self._multiple_indexes_per_well = None
        self._fixed_index_positions = None
        self._enable_custom_index_cycles = None
        self._num_cycles_index1_override = None
        self._num_cycles_index2_override = None
        self._fixed_layout_position_key_by_index_id = None
        self._custom_bcl_convert_settings = None
        self.discriminator = None

        if default_index_strategy is not None:
            self.default_index_strategy = default_index_strategy
        if override_cycles is not None:
            self.override_cycles = override_cycles
        if fixed_layout is not None:
            self.fixed_layout = fixed_layout
        if multiplate is not None:
            self.multiplate = multiplate
        if multiple_indexes_per_well is not None:
            self.multiple_indexes_per_well = multiple_indexes_per_well
        if fixed_index_positions is not None:
            self.fixed_index_positions = fixed_index_positions
        if enable_custom_index_cycles is not None:
            self.enable_custom_index_cycles = enable_custom_index_cycles
        if num_cycles_index1_override is not None:
            self.num_cycles_index1_override = num_cycles_index1_override
        if num_cycles_index2_override is not None:
            self.num_cycles_index2_override = num_cycles_index2_override
        if fixed_layout_position_key_by_index_id is not None:
            self.fixed_layout_position_key_by_index_id = fixed_layout_position_key_by_index_id
        if custom_bcl_convert_settings is not None:
            self.custom_bcl_convert_settings = custom_bcl_convert_settings

    @property
    def default_index_strategy(self):
        """Gets the default_index_strategy of this IndexAdapterKitSettings.  # noqa: E501

        Default index strategy for index adapter kit  # noqa: E501

        :return: The default_index_strategy of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_index_strategy

    @default_index_strategy.setter
    def default_index_strategy(self, default_index_strategy):
        """Sets the default_index_strategy of this IndexAdapterKitSettings.

        Default index strategy for index adapter kit  # noqa: E501

        :param default_index_strategy: The default_index_strategy of this IndexAdapterKitSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoIndex", "Single", "Dual"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and default_index_strategy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `default_index_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(default_index_strategy, allowed_values)
            )

        self._default_index_strategy = default_index_strategy

    @property
    def override_cycles(self):
        """Gets the override_cycles of this IndexAdapterKitSettings.  # noqa: E501

        Override cycles settings for index adapter kit  # noqa: E501

        :return: The override_cycles of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: str
        """
        return self._override_cycles

    @override_cycles.setter
    def override_cycles(self, override_cycles):
        """Sets the override_cycles of this IndexAdapterKitSettings.

        Override cycles settings for index adapter kit  # noqa: E501

        :param override_cycles: The override_cycles of this IndexAdapterKitSettings.  # noqa: E501
        :type: str
        """

        self._override_cycles = override_cycles

    @property
    def fixed_layout(self):
        """Gets the fixed_layout of this IndexAdapterKitSettings.  # noqa: E501

        Indicates if the index adapter kit is a fixed layout kit  # noqa: E501

        :return: The fixed_layout of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_layout

    @fixed_layout.setter
    def fixed_layout(self, fixed_layout):
        """Sets the fixed_layout of this IndexAdapterKitSettings.

        Indicates if the index adapter kit is a fixed layout kit  # noqa: E501

        :param fixed_layout: The fixed_layout of this IndexAdapterKitSettings.  # noqa: E501
        :type: bool
        """

        self._fixed_layout = fixed_layout

    @property
    def multiplate(self):
        """Gets the multiplate of this IndexAdapterKitSettings.  # noqa: E501

        Indicates if the index adapter kit is a multi-plate fixed layout kit  # noqa: E501

        :return: The multiplate of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: bool
        """
        return self._multiplate

    @multiplate.setter
    def multiplate(self, multiplate):
        """Sets the multiplate of this IndexAdapterKitSettings.

        Indicates if the index adapter kit is a multi-plate fixed layout kit  # noqa: E501

        :param multiplate: The multiplate of this IndexAdapterKitSettings.  # noqa: E501
        :type: bool
        """

        self._multiplate = multiplate

    @property
    def multiple_indexes_per_well(self):
        """Gets the multiple_indexes_per_well of this IndexAdapterKitSettings.  # noqa: E501

        Indicates if the index adapter kit supports multiple indices in one well  # noqa: E501

        :return: The multiple_indexes_per_well of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: bool
        """
        return self._multiple_indexes_per_well

    @multiple_indexes_per_well.setter
    def multiple_indexes_per_well(self, multiple_indexes_per_well):
        """Sets the multiple_indexes_per_well of this IndexAdapterKitSettings.

        Indicates if the index adapter kit supports multiple indices in one well  # noqa: E501

        :param multiple_indexes_per_well: The multiple_indexes_per_well of this IndexAdapterKitSettings.  # noqa: E501
        :type: bool
        """

        self._multiple_indexes_per_well = multiple_indexes_per_well

    @property
    def fixed_index_positions(self):
        """Gets the fixed_index_positions of this IndexAdapterKitSettings.  # noqa: E501

        Fixed layout index positions for this index adapter kit  Format: \"{[Plate-]Well[-IndexesCount]}/{Index1Name}[-{Index2Name}]\"  # noqa: E501

        :return: The fixed_index_positions of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._fixed_index_positions

    @fixed_index_positions.setter
    def fixed_index_positions(self, fixed_index_positions):
        """Sets the fixed_index_positions of this IndexAdapterKitSettings.

        Fixed layout index positions for this index adapter kit  Format: \"{[Plate-]Well[-IndexesCount]}/{Index1Name}[-{Index2Name}]\"  # noqa: E501

        :param fixed_index_positions: The fixed_index_positions of this IndexAdapterKitSettings.  # noqa: E501
        :type: list[str]
        """

        self._fixed_index_positions = fixed_index_positions

    @property
    def enable_custom_index_cycles(self):
        """Gets the enable_custom_index_cycles of this IndexAdapterKitSettings.  # noqa: E501

        Indicates if the UI will display a checkbox to enable users to enter custom index cycles for the kit  # noqa: E501

        :return: The enable_custom_index_cycles of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_custom_index_cycles

    @enable_custom_index_cycles.setter
    def enable_custom_index_cycles(self, enable_custom_index_cycles):
        """Sets the enable_custom_index_cycles of this IndexAdapterKitSettings.

        Indicates if the UI will display a checkbox to enable users to enter custom index cycles for the kit  # noqa: E501

        :param enable_custom_index_cycles: The enable_custom_index_cycles of this IndexAdapterKitSettings.  # noqa: E501
        :type: bool
        """

        self._enable_custom_index_cycles = enable_custom_index_cycles

    @property
    def num_cycles_index1_override(self):
        """Gets the num_cycles_index1_override of this IndexAdapterKitSettings.  # noqa: E501

        Indicates if the UI should use this value as the default Index1Cycles entry  # noqa: E501

        :return: The num_cycles_index1_override of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: int
        """
        return self._num_cycles_index1_override

    @num_cycles_index1_override.setter
    def num_cycles_index1_override(self, num_cycles_index1_override):
        """Sets the num_cycles_index1_override of this IndexAdapterKitSettings.

        Indicates if the UI should use this value as the default Index1Cycles entry  # noqa: E501

        :param num_cycles_index1_override: The num_cycles_index1_override of this IndexAdapterKitSettings.  # noqa: E501
        :type: int
        """

        self._num_cycles_index1_override = num_cycles_index1_override

    @property
    def num_cycles_index2_override(self):
        """Gets the num_cycles_index2_override of this IndexAdapterKitSettings.  # noqa: E501

        Indicates if the UI should use this value as the default Index2Cycles entry  # noqa: E501

        :return: The num_cycles_index2_override of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: int
        """
        return self._num_cycles_index2_override

    @num_cycles_index2_override.setter
    def num_cycles_index2_override(self, num_cycles_index2_override):
        """Sets the num_cycles_index2_override of this IndexAdapterKitSettings.

        Indicates if the UI should use this value as the default Index2Cycles entry  # noqa: E501

        :param num_cycles_index2_override: The num_cycles_index2_override of this IndexAdapterKitSettings.  # noqa: E501
        :type: int
        """

        self._num_cycles_index2_override = num_cycles_index2_override

    @property
    def fixed_layout_position_key_by_index_id(self):
        """Gets the fixed_layout_position_key_by_index_id of this IndexAdapterKitSettings.  # noqa: E501

        Indicates the container position for FixedLayout is based on IndexId  # noqa: E501

        :return: The fixed_layout_position_key_by_index_id of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_layout_position_key_by_index_id

    @fixed_layout_position_key_by_index_id.setter
    def fixed_layout_position_key_by_index_id(self, fixed_layout_position_key_by_index_id):
        """Sets the fixed_layout_position_key_by_index_id of this IndexAdapterKitSettings.

        Indicates the container position for FixedLayout is based on IndexId  # noqa: E501

        :param fixed_layout_position_key_by_index_id: The fixed_layout_position_key_by_index_id of this IndexAdapterKitSettings.  # noqa: E501
        :type: bool
        """

        self._fixed_layout_position_key_by_index_id = fixed_layout_position_key_by_index_id

    @property
    def custom_bcl_convert_settings(self):
        """Gets the custom_bcl_convert_settings of this IndexAdapterKitSettings.  # noqa: E501

        Key-value pairs of Custom BCL Convert settings for the IndexAdapterKit  # noqa: E501

        :return: The custom_bcl_convert_settings of this IndexAdapterKitSettings.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_bcl_convert_settings

    @custom_bcl_convert_settings.setter
    def custom_bcl_convert_settings(self, custom_bcl_convert_settings):
        """Sets the custom_bcl_convert_settings of this IndexAdapterKitSettings.

        Key-value pairs of Custom BCL Convert settings for the IndexAdapterKit  # noqa: E501

        :param custom_bcl_convert_settings: The custom_bcl_convert_settings of this IndexAdapterKitSettings.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_bcl_convert_settings = custom_bcl_convert_settings

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
        if not isinstance(other, IndexAdapterKitSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IndexAdapterKitSettings):
            return True

        return self.to_dict() != other.to_dict()
