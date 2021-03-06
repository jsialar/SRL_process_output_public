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


class AnalysisVersionDefinitionCompact(object):
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
        'id': 'str',
        'urn': 'str',
        'href': 'str',
        'version': 'str',
        'description': 'str',
        'supported_instrument_platform_and_types': 'list[InstrumentPlatformAndTypesResponse]',
        'status': 'str',
        'analysis_type': 'str',
        'is_dragen': 'bool',
        'analysis_settings': 'object',
        'settings': 'AnalysisVersionDefinitionSettings',
        'skip_analysis_section': 'bool',
        'analysis_sample_settings': 'object',
        'on_render_require_run_contents': 'bool',
        'analysis_definition': 'AnalysisDefinitionCompact',
        'checksum': 'str',
        'sub_tenant_id': 'str',
        'acl': 'list[str]',
        'tenant_id': 'str',
        'tenant_name': 'str',
        'created_by_client_id': 'str',
        'created_by': 'str',
        'modified_by': 'str',
        'time_created': 'datetime',
        'time_modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'href': 'href',
        'version': 'version',
        'description': 'description',
        'supported_instrument_platform_and_types': 'supportedInstrumentPlatformAndTypes',
        'status': 'status',
        'analysis_type': 'analysisType',
        'is_dragen': 'isDragen',
        'analysis_settings': 'analysisSettings',
        'settings': 'settings',
        'skip_analysis_section': 'skipAnalysisSection',
        'analysis_sample_settings': 'analysisSampleSettings',
        'on_render_require_run_contents': 'onRenderRequireRunContents',
        'analysis_definition': 'analysisDefinition',
        'checksum': 'checksum',
        'sub_tenant_id': 'subTenantId',
        'acl': 'acl',
        'tenant_id': 'tenantId',
        'tenant_name': 'tenantName',
        'created_by_client_id': 'createdByClientId',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'time_created': 'timeCreated',
        'time_modified': 'timeModified'
    }

    def __init__(self, id=None, urn=None, href=None, version=None, description=None, supported_instrument_platform_and_types=None, status=None, analysis_type=None, is_dragen=None, analysis_settings=None, settings=None, skip_analysis_section=None, analysis_sample_settings=None, on_render_require_run_contents=None, analysis_definition=None, checksum=None, sub_tenant_id=None, acl=None, tenant_id=None, tenant_name=None, created_by_client_id=None, created_by=None, modified_by=None, time_created=None, time_modified=None, local_vars_configuration=None):  # noqa: E501
        """AnalysisVersionDefinitionCompact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._urn = None
        self._href = None
        self._version = None
        self._description = None
        self._supported_instrument_platform_and_types = None
        self._status = None
        self._analysis_type = None
        self._is_dragen = None
        self._analysis_settings = None
        self._settings = None
        self._skip_analysis_section = None
        self._analysis_sample_settings = None
        self._on_render_require_run_contents = None
        self._analysis_definition = None
        self._checksum = None
        self._sub_tenant_id = None
        self._acl = None
        self._tenant_id = None
        self._tenant_name = None
        self._created_by_client_id = None
        self._created_by = None
        self._modified_by = None
        self._time_created = None
        self._time_modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if urn is not None:
            self.urn = urn
        if href is not None:
            self.href = href
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if supported_instrument_platform_and_types is not None:
            self.supported_instrument_platform_and_types = supported_instrument_platform_and_types
        if status is not None:
            self.status = status
        if analysis_type is not None:
            self.analysis_type = analysis_type
        if is_dragen is not None:
            self.is_dragen = is_dragen
        if analysis_settings is not None:
            self.analysis_settings = analysis_settings
        if settings is not None:
            self.settings = settings
        if skip_analysis_section is not None:
            self.skip_analysis_section = skip_analysis_section
        if analysis_sample_settings is not None:
            self.analysis_sample_settings = analysis_sample_settings
        if on_render_require_run_contents is not None:
            self.on_render_require_run_contents = on_render_require_run_contents
        if analysis_definition is not None:
            self.analysis_definition = analysis_definition
        if checksum is not None:
            self.checksum = checksum
        if sub_tenant_id is not None:
            self.sub_tenant_id = sub_tenant_id
        if acl is not None:
            self.acl = acl
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if tenant_name is not None:
            self.tenant_name = tenant_name
        if created_by_client_id is not None:
            self.created_by_client_id = created_by_client_id
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified

    @property
    def id(self):
        """Gets the id of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Unique object ID  # noqa: E501

        :return: The id of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnalysisVersionDefinitionCompact.

        Unique object ID  # noqa: E501

        :param id: The id of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def urn(self):
        """Gets the urn of this AnalysisVersionDefinitionCompact.  # noqa: E501

        URN of the object  # noqa: E501

        :return: The urn of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this AnalysisVersionDefinitionCompact.

        URN of the object  # noqa: E501

        :param urn: The urn of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def href(self):
        """Gets the href of this AnalysisVersionDefinitionCompact.  # noqa: E501

        HREF to the object  # noqa: E501

        :return: The href of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AnalysisVersionDefinitionCompact.

        HREF to the object  # noqa: E501

        :param href: The href of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def version(self):
        """Gets the version of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Version of analysis definition  # noqa: E501

        :return: The version of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AnalysisVersionDefinitionCompact.

        Version of analysis definition  # noqa: E501

        :param version: The version of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def description(self):
        """Gets the description of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Description of this version of analysis definition  # noqa: E501

        :return: The description of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnalysisVersionDefinitionCompact.

        Description of this version of analysis definition  # noqa: E501

        :param description: The description of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def supported_instrument_platform_and_types(self):
        """Gets the supported_instrument_platform_and_types of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Supported Instrument Platforms and Types of the analysis  # noqa: E501

        :return: The supported_instrument_platform_and_types of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: list[InstrumentPlatformAndTypesResponse]
        """
        return self._supported_instrument_platform_and_types

    @supported_instrument_platform_and_types.setter
    def supported_instrument_platform_and_types(self, supported_instrument_platform_and_types):
        """Sets the supported_instrument_platform_and_types of this AnalysisVersionDefinitionCompact.

        Supported Instrument Platforms and Types of the analysis  # noqa: E501

        :param supported_instrument_platform_and_types: The supported_instrument_platform_and_types of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: list[InstrumentPlatformAndTypesResponse]
        """

        self._supported_instrument_platform_and_types = supported_instrument_platform_and_types

    @property
    def status(self):
        """Gets the status of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Status of this version of analysis definition  # noqa: E501

        :return: The status of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AnalysisVersionDefinitionCompact.

        Status of this version of analysis definition  # noqa: E501

        :param status: The status of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def analysis_type(self):
        """Gets the analysis_type of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Analysis type of this version of analysis definition  # noqa: E501

        :return: The analysis_type of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._analysis_type

    @analysis_type.setter
    def analysis_type(self, analysis_type):
        """Sets the analysis_type of this AnalysisVersionDefinitionCompact.

        Analysis type of this version of analysis definition  # noqa: E501

        :param analysis_type: The analysis_type of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._analysis_type = analysis_type

    @property
    def is_dragen(self):
        """Gets the is_dragen of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Indicate whether an analysis is a DRAGEN analysis or not  # noqa: E501

        :return: The is_dragen of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_dragen

    @is_dragen.setter
    def is_dragen(self, is_dragen):
        """Sets the is_dragen of this AnalysisVersionDefinitionCompact.

        Indicate whether an analysis is a DRAGEN analysis or not  # noqa: E501

        :param is_dragen: The is_dragen of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: bool
        """

        self._is_dragen = is_dragen

    @property
    def analysis_settings(self):
        """Gets the analysis_settings of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Settings for the analysis (at the global analysis level)  # noqa: E501

        :return: The analysis_settings of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: object
        """
        return self._analysis_settings

    @analysis_settings.setter
    def analysis_settings(self, analysis_settings):
        """Sets the analysis_settings of this AnalysisVersionDefinitionCompact.

        Settings for the analysis (at the global analysis level)  # noqa: E501

        :param analysis_settings: The analysis_settings of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: object
        """

        self._analysis_settings = analysis_settings

    @property
    def settings(self):
        """Gets the settings of this AnalysisVersionDefinitionCompact.  # noqa: E501


        :return: The settings of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: AnalysisVersionDefinitionSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this AnalysisVersionDefinitionCompact.


        :param settings: The settings of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: AnalysisVersionDefinitionSettings
        """

        self._settings = settings

    @property
    def skip_analysis_section(self):
        """Gets the skip_analysis_section of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Skip analysis section in generated sample sheets  # noqa: E501

        :return: The skip_analysis_section of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: bool
        """
        return self._skip_analysis_section

    @skip_analysis_section.setter
    def skip_analysis_section(self, skip_analysis_section):
        """Sets the skip_analysis_section of this AnalysisVersionDefinitionCompact.

        Skip analysis section in generated sample sheets  # noqa: E501

        :param skip_analysis_section: The skip_analysis_section of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: bool
        """

        self._skip_analysis_section = skip_analysis_section

    @property
    def analysis_sample_settings(self):
        """Gets the analysis_sample_settings of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Per-sample settings for the analysis (at the per-sample level)  # noqa: E501

        :return: The analysis_sample_settings of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: object
        """
        return self._analysis_sample_settings

    @analysis_sample_settings.setter
    def analysis_sample_settings(self, analysis_sample_settings):
        """Sets the analysis_sample_settings of this AnalysisVersionDefinitionCompact.

        Per-sample settings for the analysis (at the per-sample level)  # noqa: E501

        :param analysis_sample_settings: The analysis_sample_settings of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: object
        """

        self._analysis_sample_settings = analysis_sample_settings

    @property
    def on_render_require_run_contents(self):
        """Gets the on_render_require_run_contents of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Whether the OnRenderFunction depends on RunContents or not  # noqa: E501

        :return: The on_render_require_run_contents of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: bool
        """
        return self._on_render_require_run_contents

    @on_render_require_run_contents.setter
    def on_render_require_run_contents(self, on_render_require_run_contents):
        """Sets the on_render_require_run_contents of this AnalysisVersionDefinitionCompact.

        Whether the OnRenderFunction depends on RunContents or not  # noqa: E501

        :param on_render_require_run_contents: The on_render_require_run_contents of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: bool
        """

        self._on_render_require_run_contents = on_render_require_run_contents

    @property
    def analysis_definition(self):
        """Gets the analysis_definition of this AnalysisVersionDefinitionCompact.  # noqa: E501


        :return: The analysis_definition of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: AnalysisDefinitionCompact
        """
        return self._analysis_definition

    @analysis_definition.setter
    def analysis_definition(self, analysis_definition):
        """Sets the analysis_definition of this AnalysisVersionDefinitionCompact.


        :param analysis_definition: The analysis_definition of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: AnalysisDefinitionCompact
        """

        self._analysis_definition = analysis_definition

    @property
    def checksum(self):
        """Gets the checksum of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Stores the checksum of AnalysisVersionDefinition  # noqa: E501

        :return: The checksum of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this AnalysisVersionDefinitionCompact.

        Stores the checksum of AnalysisVersionDefinition  # noqa: E501

        :param checksum: The checksum of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def sub_tenant_id(self):
        """Gets the sub_tenant_id of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Organizational or Workgroup ID. If neither are present, User ID.  # noqa: E501

        :return: The sub_tenant_id of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._sub_tenant_id

    @sub_tenant_id.setter
    def sub_tenant_id(self, sub_tenant_id):
        """Sets the sub_tenant_id of this AnalysisVersionDefinitionCompact.

        Organizational or Workgroup ID. If neither are present, User ID.  # noqa: E501

        :param sub_tenant_id: The sub_tenant_id of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._sub_tenant_id = sub_tenant_id

    @property
    def acl(self):
        """Gets the acl of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Access control list of the object  # noqa: E501

        :return: The acl of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this AnalysisVersionDefinitionCompact.

        Access control list of the object  # noqa: E501

        :param acl: The acl of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Unique identifier for the resource tenant  # noqa: E501

        :return: The tenant_id of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AnalysisVersionDefinitionCompact.

        Unique identifier for the resource tenant  # noqa: E501

        :param tenant_id: The tenant_id of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """Gets the tenant_name of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Unique tenant name for the resource tenant  # noqa: E501

        :return: The tenant_name of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this AnalysisVersionDefinitionCompact.

        Unique tenant name for the resource tenant  # noqa: E501

        :param tenant_name: The tenant_name of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

    @property
    def created_by_client_id(self):
        """Gets the created_by_client_id of this AnalysisVersionDefinitionCompact.  # noqa: E501

        ClientId that created the resource (bssh, stratus...)  # noqa: E501

        :return: The created_by_client_id of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._created_by_client_id

    @created_by_client_id.setter
    def created_by_client_id(self, created_by_client_id):
        """Sets the created_by_client_id of this AnalysisVersionDefinitionCompact.

        ClientId that created the resource (bssh, stratus...)  # noqa: E501

        :param created_by_client_id: The created_by_client_id of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._created_by_client_id = created_by_client_id

    @property
    def created_by(self):
        """Gets the created_by of this AnalysisVersionDefinitionCompact.  # noqa: E501

        User that created the resource  # noqa: E501

        :return: The created_by of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AnalysisVersionDefinitionCompact.

        User that created the resource  # noqa: E501

        :param created_by: The created_by of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this AnalysisVersionDefinitionCompact.  # noqa: E501

        User that last modified the resource  # noqa: E501

        :return: The modified_by of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this AnalysisVersionDefinitionCompact.

        User that last modified the resource  # noqa: E501

        :param modified_by: The modified_by of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def time_created(self):
        """Gets the time_created of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Time (in UTC) the resource was created  # noqa: E501

        :return: The time_created of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this AnalysisVersionDefinitionCompact.

        Time (in UTC) the resource was created  # noqa: E501

        :param time_created: The time_created of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_modified(self):
        """Gets the time_modified of this AnalysisVersionDefinitionCompact.  # noqa: E501

        Time (in UTC) the resource was modified  # noqa: E501

        :return: The time_modified of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this AnalysisVersionDefinitionCompact.

        Time (in UTC) the resource was modified  # noqa: E501

        :param time_modified: The time_modified of this AnalysisVersionDefinitionCompact.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

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
        if not isinstance(other, AnalysisVersionDefinitionCompact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnalysisVersionDefinitionCompact):
            return True

        return self.to_dict() != other.to_dict()
