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


class LaneLibraryResponse(object):
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
        'sample_name': 'str',
        'sample_urn': 'str',
        'data_aggregation_group': 'str',
        'project_name': 'str',
        'library_name': 'str',
        'library_urn': 'str',
        'adapter_sequence_read1': 'str',
        'adapter_sequence_read2': 'str',
        'index_container_position': 'str',
        'index1_sequence': 'str',
        'index2_sequence': 'str',
        'index1_name': 'str',
        'index2_name': 'str',
        'library_prep_kit_name': 'str',
        'library_prep_kit_urn': 'str',
        'index_adapter_kit_name': 'str',
        'index_adapter_kit_urn': 'str',
        'adapter_behavior': 'str',
        'override_cycles': 'str',
        'library': 'LibraryCompact'
    }

    attribute_map = {
        'sample_name': 'sampleName',
        'sample_urn': 'sampleUrn',
        'data_aggregation_group': 'dataAggregationGroup',
        'project_name': 'projectName',
        'library_name': 'libraryName',
        'library_urn': 'libraryUrn',
        'adapter_sequence_read1': 'adapterSequenceRead1',
        'adapter_sequence_read2': 'adapterSequenceRead2',
        'index_container_position': 'indexContainerPosition',
        'index1_sequence': 'index1Sequence',
        'index2_sequence': 'index2Sequence',
        'index1_name': 'index1Name',
        'index2_name': 'index2Name',
        'library_prep_kit_name': 'libraryPrepKitName',
        'library_prep_kit_urn': 'libraryPrepKitUrn',
        'index_adapter_kit_name': 'indexAdapterKitName',
        'index_adapter_kit_urn': 'indexAdapterKitUrn',
        'adapter_behavior': 'adapterBehavior',
        'override_cycles': 'overrideCycles',
        'library': 'library'
    }

    def __init__(self, sample_name=None, sample_urn=None, data_aggregation_group=None, project_name=None, library_name=None, library_urn=None, adapter_sequence_read1=None, adapter_sequence_read2=None, index_container_position=None, index1_sequence=None, index2_sequence=None, index1_name=None, index2_name=None, library_prep_kit_name=None, library_prep_kit_urn=None, index_adapter_kit_name=None, index_adapter_kit_urn=None, adapter_behavior=None, override_cycles=None, library=None, local_vars_configuration=None):  # noqa: E501
        """LaneLibraryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sample_name = None
        self._sample_urn = None
        self._data_aggregation_group = None
        self._project_name = None
        self._library_name = None
        self._library_urn = None
        self._adapter_sequence_read1 = None
        self._adapter_sequence_read2 = None
        self._index_container_position = None
        self._index1_sequence = None
        self._index2_sequence = None
        self._index1_name = None
        self._index2_name = None
        self._library_prep_kit_name = None
        self._library_prep_kit_urn = None
        self._index_adapter_kit_name = None
        self._index_adapter_kit_urn = None
        self._adapter_behavior = None
        self._override_cycles = None
        self._library = None
        self.discriminator = None

        if sample_name is not None:
            self.sample_name = sample_name
        if sample_urn is not None:
            self.sample_urn = sample_urn
        if data_aggregation_group is not None:
            self.data_aggregation_group = data_aggregation_group
        if project_name is not None:
            self.project_name = project_name
        if library_name is not None:
            self.library_name = library_name
        if library_urn is not None:
            self.library_urn = library_urn
        if adapter_sequence_read1 is not None:
            self.adapter_sequence_read1 = adapter_sequence_read1
        if adapter_sequence_read2 is not None:
            self.adapter_sequence_read2 = adapter_sequence_read2
        if index_container_position is not None:
            self.index_container_position = index_container_position
        if index1_sequence is not None:
            self.index1_sequence = index1_sequence
        if index2_sequence is not None:
            self.index2_sequence = index2_sequence
        if index1_name is not None:
            self.index1_name = index1_name
        if index2_name is not None:
            self.index2_name = index2_name
        if library_prep_kit_name is not None:
            self.library_prep_kit_name = library_prep_kit_name
        if library_prep_kit_urn is not None:
            self.library_prep_kit_urn = library_prep_kit_urn
        if index_adapter_kit_name is not None:
            self.index_adapter_kit_name = index_adapter_kit_name
        if index_adapter_kit_urn is not None:
            self.index_adapter_kit_urn = index_adapter_kit_urn
        if adapter_behavior is not None:
            self.adapter_behavior = adapter_behavior
        if override_cycles is not None:
            self.override_cycles = override_cycles
        if library is not None:
            self.library = library

    @property
    def sample_name(self):
        """Gets the sample_name of this LaneLibraryResponse.  # noqa: E501

        Sample name  # noqa: E501

        :return: The sample_name of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._sample_name

    @sample_name.setter
    def sample_name(self, sample_name):
        """Sets the sample_name of this LaneLibraryResponse.

        Sample name  # noqa: E501

        :param sample_name: The sample_name of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._sample_name = sample_name

    @property
    def sample_urn(self):
        """Gets the sample_urn of this LaneLibraryResponse.  # noqa: E501

        Sample URN  # noqa: E501

        :return: The sample_urn of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._sample_urn

    @sample_urn.setter
    def sample_urn(self, sample_urn):
        """Sets the sample_urn of this LaneLibraryResponse.

        Sample URN  # noqa: E501

        :param sample_urn: The sample_urn of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._sample_urn = sample_urn

    @property
    def data_aggregation_group(self):
        """Gets the data_aggregation_group of this LaneLibraryResponse.  # noqa: E501

        Data aggregation group of the sample  # noqa: E501

        :return: The data_aggregation_group of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._data_aggregation_group

    @data_aggregation_group.setter
    def data_aggregation_group(self, data_aggregation_group):
        """Sets the data_aggregation_group of this LaneLibraryResponse.

        Data aggregation group of the sample  # noqa: E501

        :param data_aggregation_group: The data_aggregation_group of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._data_aggregation_group = data_aggregation_group

    @property
    def project_name(self):
        """Gets the project_name of this LaneLibraryResponse.  # noqa: E501

        Project Name of the sample  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated.  # noqa: E501

        :return: The project_name of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this LaneLibraryResponse.

        Project Name of the sample  Note: This field is an alias of DataAggregationGroup field until DataAggregationGroups is deprecated.  # noqa: E501

        :param project_name: The project_name of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def library_name(self):
        """Gets the library_name of this LaneLibraryResponse.  # noqa: E501

        Library name  # noqa: E501

        :return: The library_name of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._library_name

    @library_name.setter
    def library_name(self, library_name):
        """Sets the library_name of this LaneLibraryResponse.

        Library name  # noqa: E501

        :param library_name: The library_name of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._library_name = library_name

    @property
    def library_urn(self):
        """Gets the library_urn of this LaneLibraryResponse.  # noqa: E501

        Library URN  # noqa: E501

        :return: The library_urn of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._library_urn

    @library_urn.setter
    def library_urn(self, library_urn):
        """Sets the library_urn of this LaneLibraryResponse.

        Library URN  # noqa: E501

        :param library_urn: The library_urn of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._library_urn = library_urn

    @property
    def adapter_sequence_read1(self):
        """Gets the adapter_sequence_read1 of this LaneLibraryResponse.  # noqa: E501

        Read 1 adapter sequence  # noqa: E501

        :return: The adapter_sequence_read1 of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._adapter_sequence_read1

    @adapter_sequence_read1.setter
    def adapter_sequence_read1(self, adapter_sequence_read1):
        """Sets the adapter_sequence_read1 of this LaneLibraryResponse.

        Read 1 adapter sequence  # noqa: E501

        :param adapter_sequence_read1: The adapter_sequence_read1 of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._adapter_sequence_read1 = adapter_sequence_read1

    @property
    def adapter_sequence_read2(self):
        """Gets the adapter_sequence_read2 of this LaneLibraryResponse.  # noqa: E501

        Read 2 adapter sequence  # noqa: E501

        :return: The adapter_sequence_read2 of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._adapter_sequence_read2

    @adapter_sequence_read2.setter
    def adapter_sequence_read2(self, adapter_sequence_read2):
        """Sets the adapter_sequence_read2 of this LaneLibraryResponse.

        Read 2 adapter sequence  # noqa: E501

        :param adapter_sequence_read2: The adapter_sequence_read2 of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._adapter_sequence_read2 = adapter_sequence_read2

    @property
    def index_container_position(self):
        """Gets the index_container_position of this LaneLibraryResponse.  # noqa: E501

        The container position (well or plate+well position) for the library that is using index adapter kit with fixed index position  # noqa: E501

        :return: The index_container_position of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._index_container_position

    @index_container_position.setter
    def index_container_position(self, index_container_position):
        """Sets the index_container_position of this LaneLibraryResponse.

        The container position (well or plate+well position) for the library that is using index adapter kit with fixed index position  # noqa: E501

        :param index_container_position: The index_container_position of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._index_container_position = index_container_position

    @property
    def index1_sequence(self):
        """Gets the index1_sequence of this LaneLibraryResponse.  # noqa: E501

        Index 1 sequence  of the library  # noqa: E501

        :return: The index1_sequence of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._index1_sequence

    @index1_sequence.setter
    def index1_sequence(self, index1_sequence):
        """Sets the index1_sequence of this LaneLibraryResponse.

        Index 1 sequence  of the library  # noqa: E501

        :param index1_sequence: The index1_sequence of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._index1_sequence = index1_sequence

    @property
    def index2_sequence(self):
        """Gets the index2_sequence of this LaneLibraryResponse.  # noqa: E501

        Index 2 sequence of the library  # noqa: E501

        :return: The index2_sequence of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._index2_sequence

    @index2_sequence.setter
    def index2_sequence(self, index2_sequence):
        """Sets the index2_sequence of this LaneLibraryResponse.

        Index 2 sequence of the library  # noqa: E501

        :param index2_sequence: The index2_sequence of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._index2_sequence = index2_sequence

    @property
    def index1_name(self):
        """Gets the index1_name of this LaneLibraryResponse.  # noqa: E501

        Name of index 1 sequence  # noqa: E501

        :return: The index1_name of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._index1_name

    @index1_name.setter
    def index1_name(self, index1_name):
        """Sets the index1_name of this LaneLibraryResponse.

        Name of index 1 sequence  # noqa: E501

        :param index1_name: The index1_name of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._index1_name = index1_name

    @property
    def index2_name(self):
        """Gets the index2_name of this LaneLibraryResponse.  # noqa: E501

        Name of index 2 sequence  # noqa: E501

        :return: The index2_name of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._index2_name

    @index2_name.setter
    def index2_name(self, index2_name):
        """Sets the index2_name of this LaneLibraryResponse.

        Name of index 2 sequence  # noqa: E501

        :param index2_name: The index2_name of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._index2_name = index2_name

    @property
    def library_prep_kit_name(self):
        """Gets the library_prep_kit_name of this LaneLibraryResponse.  # noqa: E501

        Name of library prep kit  # noqa: E501

        :return: The library_prep_kit_name of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._library_prep_kit_name

    @library_prep_kit_name.setter
    def library_prep_kit_name(self, library_prep_kit_name):
        """Sets the library_prep_kit_name of this LaneLibraryResponse.

        Name of library prep kit  # noqa: E501

        :param library_prep_kit_name: The library_prep_kit_name of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._library_prep_kit_name = library_prep_kit_name

    @property
    def library_prep_kit_urn(self):
        """Gets the library_prep_kit_urn of this LaneLibraryResponse.  # noqa: E501

        URN of library prep kit  # noqa: E501

        :return: The library_prep_kit_urn of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._library_prep_kit_urn

    @library_prep_kit_urn.setter
    def library_prep_kit_urn(self, library_prep_kit_urn):
        """Sets the library_prep_kit_urn of this LaneLibraryResponse.

        URN of library prep kit  # noqa: E501

        :param library_prep_kit_urn: The library_prep_kit_urn of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._library_prep_kit_urn = library_prep_kit_urn

    @property
    def index_adapter_kit_name(self):
        """Gets the index_adapter_kit_name of this LaneLibraryResponse.  # noqa: E501

        Name of index adapter kit  # noqa: E501

        :return: The index_adapter_kit_name of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._index_adapter_kit_name

    @index_adapter_kit_name.setter
    def index_adapter_kit_name(self, index_adapter_kit_name):
        """Sets the index_adapter_kit_name of this LaneLibraryResponse.

        Name of index adapter kit  # noqa: E501

        :param index_adapter_kit_name: The index_adapter_kit_name of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._index_adapter_kit_name = index_adapter_kit_name

    @property
    def index_adapter_kit_urn(self):
        """Gets the index_adapter_kit_urn of this LaneLibraryResponse.  # noqa: E501

        URN of index adapter kit  # noqa: E501

        :return: The index_adapter_kit_urn of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._index_adapter_kit_urn

    @index_adapter_kit_urn.setter
    def index_adapter_kit_urn(self, index_adapter_kit_urn):
        """Sets the index_adapter_kit_urn of this LaneLibraryResponse.

        URN of index adapter kit  # noqa: E501

        :param index_adapter_kit_urn: The index_adapter_kit_urn of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._index_adapter_kit_urn = index_adapter_kit_urn

    @property
    def adapter_behavior(self):
        """Gets the adapter_behavior of this LaneLibraryResponse.  # noqa: E501

        Adapter behavior for this entry  # noqa: E501

        :return: The adapter_behavior of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._adapter_behavior

    @adapter_behavior.setter
    def adapter_behavior(self, adapter_behavior):
        """Sets the adapter_behavior of this LaneLibraryResponse.

        Adapter behavior for this entry  # noqa: E501

        :param adapter_behavior: The adapter_behavior of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._adapter_behavior = adapter_behavior

    @property
    def override_cycles(self):
        """Gets the override_cycles of this LaneLibraryResponse.  # noqa: E501

        Override cycles for this entry  # noqa: E501

        :return: The override_cycles of this LaneLibraryResponse.  # noqa: E501
        :rtype: str
        """
        return self._override_cycles

    @override_cycles.setter
    def override_cycles(self, override_cycles):
        """Sets the override_cycles of this LaneLibraryResponse.

        Override cycles for this entry  # noqa: E501

        :param override_cycles: The override_cycles of this LaneLibraryResponse.  # noqa: E501
        :type: str
        """

        self._override_cycles = override_cycles

    @property
    def library(self):
        """Gets the library of this LaneLibraryResponse.  # noqa: E501


        :return: The library of this LaneLibraryResponse.  # noqa: E501
        :rtype: LibraryCompact
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this LaneLibraryResponse.


        :param library: The library of this LaneLibraryResponse.  # noqa: E501
        :type: LibraryCompact
        """

        self._library = library

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
        if not isinstance(other, LaneLibraryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LaneLibraryResponse):
            return True

        return self.to_dict() != other.to_dict()
