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


class AnalysisDatasetCompact(object):
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
        'name': 'str',
        'display_name': 'str',
        'analysis_run': 'SequencingAnalysisRunCompact',
        'task_run_id': 'str',
        'workflow_run_id': 'str',
        'lane_number': 'int',
        'data_folder_urn': 'str',
        'data_folder_volume_path': 'str',
        'attributes': 'object',
        'analysis_dataset_type': 'AnalysisDatasetTypeCompact',
        'type': 'str',
        'qc_status': 'str',
        'qc_status_summary': 'str',
        'file_urns': 'list[str]',
        'external_id': 'str',
        'input_samples': 'list[SampleCompact]',
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
        'name': 'name',
        'display_name': 'displayName',
        'analysis_run': 'analysisRun',
        'task_run_id': 'taskRunId',
        'workflow_run_id': 'workflowRunId',
        'lane_number': 'laneNumber',
        'data_folder_urn': 'dataFolderUrn',
        'data_folder_volume_path': 'dataFolderVolumePath',
        'attributes': 'attributes',
        'analysis_dataset_type': 'analysisDatasetType',
        'type': 'type',
        'qc_status': 'qcStatus',
        'qc_status_summary': 'qcStatusSummary',
        'file_urns': 'fileUrns',
        'external_id': 'externalId',
        'input_samples': 'inputSamples',
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

    def __init__(self, id=None, urn=None, href=None, name=None, display_name=None, analysis_run=None, task_run_id=None, workflow_run_id=None, lane_number=None, data_folder_urn=None, data_folder_volume_path=None, attributes=None, analysis_dataset_type=None, type=None, qc_status=None, qc_status_summary=None, file_urns=None, external_id=None, input_samples=None, sub_tenant_id=None, acl=None, tenant_id=None, tenant_name=None, created_by_client_id=None, created_by=None, modified_by=None, time_created=None, time_modified=None, local_vars_configuration=None):  # noqa: E501
        """AnalysisDatasetCompact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._urn = None
        self._href = None
        self._name = None
        self._display_name = None
        self._analysis_run = None
        self._task_run_id = None
        self._workflow_run_id = None
        self._lane_number = None
        self._data_folder_urn = None
        self._data_folder_volume_path = None
        self._attributes = None
        self._analysis_dataset_type = None
        self._type = None
        self._qc_status = None
        self._qc_status_summary = None
        self._file_urns = None
        self._external_id = None
        self._input_samples = None
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
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if analysis_run is not None:
            self.analysis_run = analysis_run
        if task_run_id is not None:
            self.task_run_id = task_run_id
        if workflow_run_id is not None:
            self.workflow_run_id = workflow_run_id
        if lane_number is not None:
            self.lane_number = lane_number
        if data_folder_urn is not None:
            self.data_folder_urn = data_folder_urn
        if data_folder_volume_path is not None:
            self.data_folder_volume_path = data_folder_volume_path
        if attributes is not None:
            self.attributes = attributes
        if analysis_dataset_type is not None:
            self.analysis_dataset_type = analysis_dataset_type
        if type is not None:
            self.type = type
        if qc_status is not None:
            self.qc_status = qc_status
        if qc_status_summary is not None:
            self.qc_status_summary = qc_status_summary
        if file_urns is not None:
            self.file_urns = file_urns
        if external_id is not None:
            self.external_id = external_id
        if input_samples is not None:
            self.input_samples = input_samples
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
        """Gets the id of this AnalysisDatasetCompact.  # noqa: E501

        Unique object ID  # noqa: E501

        :return: The id of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnalysisDatasetCompact.

        Unique object ID  # noqa: E501

        :param id: The id of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def urn(self):
        """Gets the urn of this AnalysisDatasetCompact.  # noqa: E501

        URN of the object  # noqa: E501

        :return: The urn of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this AnalysisDatasetCompact.

        URN of the object  # noqa: E501

        :param urn: The urn of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def href(self):
        """Gets the href of this AnalysisDatasetCompact.  # noqa: E501

        HREF to the object  # noqa: E501

        :return: The href of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AnalysisDatasetCompact.

        HREF to the object  # noqa: E501

        :param href: The href of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this AnalysisDatasetCompact.  # noqa: E501

        Name of the analysis dataset  # noqa: E501

        :return: The name of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalysisDatasetCompact.

        Name of the analysis dataset  # noqa: E501

        :param name: The name of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this AnalysisDatasetCompact.  # noqa: E501

        Display name of the analysis dataset  # noqa: E501

        :return: The display_name of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AnalysisDatasetCompact.

        Display name of the analysis dataset  # noqa: E501

        :param display_name: The display_name of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def analysis_run(self):
        """Gets the analysis_run of this AnalysisDatasetCompact.  # noqa: E501


        :return: The analysis_run of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: SequencingAnalysisRunCompact
        """
        return self._analysis_run

    @analysis_run.setter
    def analysis_run(self, analysis_run):
        """Sets the analysis_run of this AnalysisDatasetCompact.


        :param analysis_run: The analysis_run of this AnalysisDatasetCompact.  # noqa: E501
        :type: SequencingAnalysisRunCompact
        """

        self._analysis_run = analysis_run

    @property
    def task_run_id(self):
        """Gets the task_run_id of this AnalysisDatasetCompact.  # noqa: E501

        Task run id of the analysis dataset  # noqa: E501

        :return: The task_run_id of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._task_run_id

    @task_run_id.setter
    def task_run_id(self, task_run_id):
        """Sets the task_run_id of this AnalysisDatasetCompact.

        Task run id of the analysis dataset  # noqa: E501

        :param task_run_id: The task_run_id of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._task_run_id = task_run_id

    @property
    def workflow_run_id(self):
        """Gets the workflow_run_id of this AnalysisDatasetCompact.  # noqa: E501

        Workflow run id of the analysis dataset  # noqa: E501

        :return: The workflow_run_id of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._workflow_run_id

    @workflow_run_id.setter
    def workflow_run_id(self, workflow_run_id):
        """Sets the workflow_run_id of this AnalysisDatasetCompact.

        Workflow run id of the analysis dataset  # noqa: E501

        :param workflow_run_id: The workflow_run_id of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._workflow_run_id = workflow_run_id

    @property
    def lane_number(self):
        """Gets the lane_number of this AnalysisDatasetCompact.  # noqa: E501

        Lane number associated with the analysis dataset  # noqa: E501

        :return: The lane_number of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: int
        """
        return self._lane_number

    @lane_number.setter
    def lane_number(self, lane_number):
        """Sets the lane_number of this AnalysisDatasetCompact.

        Lane number associated with the analysis dataset  # noqa: E501

        :param lane_number: The lane_number of this AnalysisDatasetCompact.  # noqa: E501
        :type: int
        """

        self._lane_number = lane_number

    @property
    def data_folder_urn(self):
        """Gets the data_folder_urn of this AnalysisDatasetCompact.  # noqa: E501

        Data folder urn of the analysis dataset  # noqa: E501

        :return: The data_folder_urn of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._data_folder_urn

    @data_folder_urn.setter
    def data_folder_urn(self, data_folder_urn):
        """Sets the data_folder_urn of this AnalysisDatasetCompact.

        Data folder urn of the analysis dataset  # noqa: E501

        :param data_folder_urn: The data_folder_urn of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._data_folder_urn = data_folder_urn

    @property
    def data_folder_volume_path(self):
        """Gets the data_folder_volume_path of this AnalysisDatasetCompact.  # noqa: E501

        Data folder volume path of the analysis dataset  # noqa: E501

        :return: The data_folder_volume_path of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._data_folder_volume_path

    @data_folder_volume_path.setter
    def data_folder_volume_path(self, data_folder_volume_path):
        """Sets the data_folder_volume_path of this AnalysisDatasetCompact.

        Data folder volume path of the analysis dataset  # noqa: E501

        :param data_folder_volume_path: The data_folder_volume_path of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._data_folder_volume_path = data_folder_volume_path

    @property
    def attributes(self):
        """Gets the attributes of this AnalysisDatasetCompact.  # noqa: E501

        Attributes of the analysis dataset  # noqa: E501

        :return: The attributes of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AnalysisDatasetCompact.

        Attributes of the analysis dataset  # noqa: E501

        :param attributes: The attributes of this AnalysisDatasetCompact.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def analysis_dataset_type(self):
        """Gets the analysis_dataset_type of this AnalysisDatasetCompact.  # noqa: E501


        :return: The analysis_dataset_type of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: AnalysisDatasetTypeCompact
        """
        return self._analysis_dataset_type

    @analysis_dataset_type.setter
    def analysis_dataset_type(self, analysis_dataset_type):
        """Sets the analysis_dataset_type of this AnalysisDatasetCompact.


        :param analysis_dataset_type: The analysis_dataset_type of this AnalysisDatasetCompact.  # noqa: E501
        :type: AnalysisDatasetTypeCompact
        """

        self._analysis_dataset_type = analysis_dataset_type

    @property
    def type(self):
        """Gets the type of this AnalysisDatasetCompact.  # noqa: E501

        Type of the analysis dataset  # noqa: E501

        :return: The type of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AnalysisDatasetCompact.

        Type of the analysis dataset  # noqa: E501

        :param type: The type of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def qc_status(self):
        """Gets the qc_status of this AnalysisDatasetCompact.  # noqa: E501

        QC status of the analysis dataset  # noqa: E501

        :return: The qc_status of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._qc_status

    @qc_status.setter
    def qc_status(self, qc_status):
        """Sets the qc_status of this AnalysisDatasetCompact.

        QC status of the analysis dataset  # noqa: E501

        :param qc_status: The qc_status of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._qc_status = qc_status

    @property
    def qc_status_summary(self):
        """Gets the qc_status_summary of this AnalysisDatasetCompact.  # noqa: E501

        QC summary of the analysis dataset  # noqa: E501

        :return: The qc_status_summary of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._qc_status_summary

    @qc_status_summary.setter
    def qc_status_summary(self, qc_status_summary):
        """Sets the qc_status_summary of this AnalysisDatasetCompact.

        QC summary of the analysis dataset  # noqa: E501

        :param qc_status_summary: The qc_status_summary of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._qc_status_summary = qc_status_summary

    @property
    def file_urns(self):
        """Gets the file_urns of this AnalysisDatasetCompact.  # noqa: E501

        FileUrns of the AnalysisDataset resource  # noqa: E501

        :return: The file_urns of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_urns

    @file_urns.setter
    def file_urns(self, file_urns):
        """Sets the file_urns of this AnalysisDatasetCompact.

        FileUrns of the AnalysisDataset resource  # noqa: E501

        :param file_urns: The file_urns of this AnalysisDatasetCompact.  # noqa: E501
        :type: list[str]
        """

        self._file_urns = file_urns

    @property
    def external_id(self):
        """Gets the external_id of this AnalysisDatasetCompact.  # noqa: E501

        External ID of the dataset  # noqa: E501

        :return: The external_id of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this AnalysisDatasetCompact.

        External ID of the dataset  # noqa: E501

        :param external_id: The external_id of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def input_samples(self):
        """Gets the input_samples of this AnalysisDatasetCompact.  # noqa: E501

        Input samples of the analysis dataset  # noqa: E501

        :return: The input_samples of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: list[SampleCompact]
        """
        return self._input_samples

    @input_samples.setter
    def input_samples(self, input_samples):
        """Sets the input_samples of this AnalysisDatasetCompact.

        Input samples of the analysis dataset  # noqa: E501

        :param input_samples: The input_samples of this AnalysisDatasetCompact.  # noqa: E501
        :type: list[SampleCompact]
        """

        self._input_samples = input_samples

    @property
    def sub_tenant_id(self):
        """Gets the sub_tenant_id of this AnalysisDatasetCompact.  # noqa: E501

        Organizational or Workgroup ID. If neither are present, User ID.  # noqa: E501

        :return: The sub_tenant_id of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._sub_tenant_id

    @sub_tenant_id.setter
    def sub_tenant_id(self, sub_tenant_id):
        """Sets the sub_tenant_id of this AnalysisDatasetCompact.

        Organizational or Workgroup ID. If neither are present, User ID.  # noqa: E501

        :param sub_tenant_id: The sub_tenant_id of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._sub_tenant_id = sub_tenant_id

    @property
    def acl(self):
        """Gets the acl of this AnalysisDatasetCompact.  # noqa: E501

        Access control list of the object  # noqa: E501

        :return: The acl of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this AnalysisDatasetCompact.

        Access control list of the object  # noqa: E501

        :param acl: The acl of this AnalysisDatasetCompact.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AnalysisDatasetCompact.  # noqa: E501

        Unique identifier for the resource tenant  # noqa: E501

        :return: The tenant_id of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AnalysisDatasetCompact.

        Unique identifier for the resource tenant  # noqa: E501

        :param tenant_id: The tenant_id of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """Gets the tenant_name of this AnalysisDatasetCompact.  # noqa: E501

        Unique tenant name for the resource tenant  # noqa: E501

        :return: The tenant_name of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this AnalysisDatasetCompact.

        Unique tenant name for the resource tenant  # noqa: E501

        :param tenant_name: The tenant_name of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

    @property
    def created_by_client_id(self):
        """Gets the created_by_client_id of this AnalysisDatasetCompact.  # noqa: E501

        ClientId that created the resource (bssh, stratus...)  # noqa: E501

        :return: The created_by_client_id of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._created_by_client_id

    @created_by_client_id.setter
    def created_by_client_id(self, created_by_client_id):
        """Sets the created_by_client_id of this AnalysisDatasetCompact.

        ClientId that created the resource (bssh, stratus...)  # noqa: E501

        :param created_by_client_id: The created_by_client_id of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._created_by_client_id = created_by_client_id

    @property
    def created_by(self):
        """Gets the created_by of this AnalysisDatasetCompact.  # noqa: E501

        User that created the resource  # noqa: E501

        :return: The created_by of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AnalysisDatasetCompact.

        User that created the resource  # noqa: E501

        :param created_by: The created_by of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this AnalysisDatasetCompact.  # noqa: E501

        User that last modified the resource  # noqa: E501

        :return: The modified_by of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this AnalysisDatasetCompact.

        User that last modified the resource  # noqa: E501

        :param modified_by: The modified_by of this AnalysisDatasetCompact.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def time_created(self):
        """Gets the time_created of this AnalysisDatasetCompact.  # noqa: E501

        Time (in UTC) the resource was created  # noqa: E501

        :return: The time_created of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this AnalysisDatasetCompact.

        Time (in UTC) the resource was created  # noqa: E501

        :param time_created: The time_created of this AnalysisDatasetCompact.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_modified(self):
        """Gets the time_modified of this AnalysisDatasetCompact.  # noqa: E501

        Time (in UTC) the resource was modified  # noqa: E501

        :return: The time_modified of this AnalysisDatasetCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this AnalysisDatasetCompact.

        Time (in UTC) the resource was modified  # noqa: E501

        :param time_modified: The time_modified of this AnalysisDatasetCompact.  # noqa: E501
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
        if not isinstance(other, AnalysisDatasetCompact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnalysisDatasetCompact):
            return True

        return self.to_dict() != other.to_dict()
