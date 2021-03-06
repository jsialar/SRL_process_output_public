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


class WorkflowRun(object):
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
        'time_started': 'datetime',
        'time_stopped': 'datetime',
        'status': 'str',
        'idempotency_key': 'str',
        'status_summary': 'str',
        'error': 'str',
        'error_cause': 'str',
        'workflow_version': 'WorkflowVersionCompact',
        'created_by_client_id': 'str',
        'input': 'object',
        'output': 'object',
        'definition': 'str',
        'engine_parameters': 'str',
        'time_created': 'datetime',
        'time_modified': 'datetime',
        'created_by': 'str',
        'modified_by': 'str',
        'tenant_id': 'str',
        'acl': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'href': 'href',
        'name': 'name',
        'time_started': 'timeStarted',
        'time_stopped': 'timeStopped',
        'status': 'status',
        'idempotency_key': 'idempotencyKey',
        'status_summary': 'statusSummary',
        'error': 'error',
        'error_cause': 'errorCause',
        'workflow_version': 'workflowVersion',
        'created_by_client_id': 'createdByClientId',
        'input': 'input',
        'output': 'output',
        'definition': 'definition',
        'engine_parameters': 'engineParameters',
        'time_created': 'timeCreated',
        'time_modified': 'timeModified',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'tenant_id': 'tenantId',
        'acl': 'acl'
    }

    def __init__(self, id=None, urn=None, href=None, name=None, time_started=None, time_stopped=None, status=None, idempotency_key=None, status_summary=None, error=None, error_cause=None, workflow_version=None, created_by_client_id=None, input=None, output=None, definition=None, engine_parameters=None, time_created=None, time_modified=None, created_by=None, modified_by=None, tenant_id=None, acl=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowRun - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._urn = None
        self._href = None
        self._name = None
        self._time_started = None
        self._time_stopped = None
        self._status = None
        self._idempotency_key = None
        self._status_summary = None
        self._error = None
        self._error_cause = None
        self._workflow_version = None
        self._created_by_client_id = None
        self._input = None
        self._output = None
        self._definition = None
        self._engine_parameters = None
        self._time_created = None
        self._time_modified = None
        self._created_by = None
        self._modified_by = None
        self._tenant_id = None
        self._acl = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if urn is not None:
            self.urn = urn
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        if time_started is not None:
            self.time_started = time_started
        if time_stopped is not None:
            self.time_stopped = time_stopped
        if status is not None:
            self.status = status
        if idempotency_key is not None:
            self.idempotency_key = idempotency_key
        if status_summary is not None:
            self.status_summary = status_summary
        if error is not None:
            self.error = error
        if error_cause is not None:
            self.error_cause = error_cause
        if workflow_version is not None:
            self.workflow_version = workflow_version
        if created_by_client_id is not None:
            self.created_by_client_id = created_by_client_id
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if definition is not None:
            self.definition = definition
        if engine_parameters is not None:
            self.engine_parameters = engine_parameters
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if acl is not None:
            self.acl = acl

    @property
    def id(self):
        """Gets the id of this WorkflowRun.  # noqa: E501

        Unique resource ID  # noqa: E501

        :return: The id of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkflowRun.

        Unique resource ID  # noqa: E501

        :param id: The id of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def urn(self):
        """Gets the urn of this WorkflowRun.  # noqa: E501

        URN of the resource  # noqa: E501

        :return: The urn of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this WorkflowRun.

        URN of the resource  # noqa: E501

        :param urn: The urn of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def href(self):
        """Gets the href of this WorkflowRun.  # noqa: E501

        HREF to the resource  # noqa: E501

        :return: The href of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this WorkflowRun.

        HREF to the resource  # noqa: E501

        :param href: The href of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this WorkflowRun.  # noqa: E501

        Name of the workflow run  # noqa: E501

        :return: The name of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowRun.

        Name of the workflow run  # noqa: E501

        :param name: The name of this WorkflowRun.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def time_started(self):
        """Gets the time_started of this WorkflowRun.  # noqa: E501

        The time (in UTC) the workflow run started  # noqa: E501

        :return: The time_started of this WorkflowRun.  # noqa: E501
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """Sets the time_started of this WorkflowRun.

        The time (in UTC) the workflow run started  # noqa: E501

        :param time_started: The time_started of this WorkflowRun.  # noqa: E501
        :type: datetime
        """

        self._time_started = time_started

    @property
    def time_stopped(self):
        """Gets the time_stopped of this WorkflowRun.  # noqa: E501

        The time (in UTC) the Workflow Run stopped  # noqa: E501

        :return: The time_stopped of this WorkflowRun.  # noqa: E501
        :rtype: datetime
        """
        return self._time_stopped

    @time_stopped.setter
    def time_stopped(self, time_stopped):
        """Sets the time_stopped of this WorkflowRun.

        The time (in UTC) the Workflow Run stopped  # noqa: E501

        :param time_stopped: The time_stopped of this WorkflowRun.  # noqa: E501
        :type: datetime
        """

        self._time_stopped = time_stopped

    @property
    def status(self):
        """Gets the status of this WorkflowRun.  # noqa: E501

        Workflow run status  # noqa: E501

        :return: The status of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkflowRun.

        Workflow run status  # noqa: E501

        :param status: The status of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def idempotency_key(self):
        """Gets the idempotency_key of this WorkflowRun.  # noqa: E501


        :return: The idempotency_key of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._idempotency_key

    @idempotency_key.setter
    def idempotency_key(self, idempotency_key):
        """Sets the idempotency_key of this WorkflowRun.


        :param idempotency_key: The idempotency_key of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._idempotency_key = idempotency_key

    @property
    def status_summary(self):
        """Gets the status_summary of this WorkflowRun.  # noqa: E501

        Workflow run status summary  # noqa: E501

        :return: The status_summary of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._status_summary

    @status_summary.setter
    def status_summary(self, status_summary):
        """Sets the status_summary of this WorkflowRun.

        Workflow run status summary  # noqa: E501

        :param status_summary: The status_summary of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._status_summary = status_summary

    @property
    def error(self):
        """Gets the error of this WorkflowRun.  # noqa: E501

        Error for a failed workflow run  # noqa: E501

        :return: The error of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this WorkflowRun.

        Error for a failed workflow run  # noqa: E501

        :param error: The error of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_cause(self):
        """Gets the error_cause of this WorkflowRun.  # noqa: E501

        Error cause for a failed workflow run  # noqa: E501

        :return: The error_cause of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._error_cause

    @error_cause.setter
    def error_cause(self, error_cause):
        """Sets the error_cause of this WorkflowRun.

        Error cause for a failed workflow run  # noqa: E501

        :param error_cause: The error_cause of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._error_cause = error_cause

    @property
    def workflow_version(self):
        """Gets the workflow_version of this WorkflowRun.  # noqa: E501


        :return: The workflow_version of this WorkflowRun.  # noqa: E501
        :rtype: WorkflowVersionCompact
        """
        return self._workflow_version

    @workflow_version.setter
    def workflow_version(self, workflow_version):
        """Sets the workflow_version of this WorkflowRun.


        :param workflow_version: The workflow_version of this WorkflowRun.  # noqa: E501
        :type: WorkflowVersionCompact
        """

        self._workflow_version = workflow_version

    @property
    def created_by_client_id(self):
        """Gets the created_by_client_id of this WorkflowRun.  # noqa: E501

        Client ID of the Origin Request  # noqa: E501

        :return: The created_by_client_id of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._created_by_client_id

    @created_by_client_id.setter
    def created_by_client_id(self, created_by_client_id):
        """Sets the created_by_client_id of this WorkflowRun.

        Client ID of the Origin Request  # noqa: E501

        :param created_by_client_id: The created_by_client_id of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._created_by_client_id = created_by_client_id

    @property
    def input(self):
        """Gets the input of this WorkflowRun.  # noqa: E501

        Input to workflow run, as JSON  # noqa: E501

        :return: The input of this WorkflowRun.  # noqa: E501
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this WorkflowRun.

        Input to workflow run, as JSON  # noqa: E501

        :param input: The input of this WorkflowRun.  # noqa: E501
        :type: object
        """

        self._input = input

    @property
    def output(self):
        """Gets the output of this WorkflowRun.  # noqa: E501

        Output from workflow run, as JSON  # noqa: E501

        :return: The output of this WorkflowRun.  # noqa: E501
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this WorkflowRun.

        Output from workflow run, as JSON  # noqa: E501

        :param output: The output of this WorkflowRun.  # noqa: E501
        :type: object
        """

        self._output = output

    @property
    def definition(self):
        """Gets the definition of this WorkflowRun.  # noqa: E501

        Definition of the workflow version  # noqa: E501

        :return: The definition of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this WorkflowRun.

        Definition of the workflow version  # noqa: E501

        :param definition: The definition of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._definition = definition

    @property
    def engine_parameters(self):
        """Gets the engine_parameters of this WorkflowRun.  # noqa: E501

        Workflow Engine Parameters  # noqa: E501

        :return: The engine_parameters of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._engine_parameters

    @engine_parameters.setter
    def engine_parameters(self, engine_parameters):
        """Sets the engine_parameters of this WorkflowRun.

        Workflow Engine Parameters  # noqa: E501

        :param engine_parameters: The engine_parameters of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._engine_parameters = engine_parameters

    @property
    def time_created(self):
        """Gets the time_created of this WorkflowRun.  # noqa: E501

        Time (in UTC) the resource was created  # noqa: E501

        :return: The time_created of this WorkflowRun.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this WorkflowRun.

        Time (in UTC) the resource was created  # noqa: E501

        :param time_created: The time_created of this WorkflowRun.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_modified(self):
        """Gets the time_modified of this WorkflowRun.  # noqa: E501

        Time (in UTC) the resource was modified  # noqa: E501

        :return: The time_modified of this WorkflowRun.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this WorkflowRun.

        Time (in UTC) the resource was modified  # noqa: E501

        :param time_modified: The time_modified of this WorkflowRun.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

    @property
    def created_by(self):
        """Gets the created_by of this WorkflowRun.  # noqa: E501

        User that created the resource  # noqa: E501

        :return: The created_by of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WorkflowRun.

        User that created the resource  # noqa: E501

        :param created_by: The created_by of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this WorkflowRun.  # noqa: E501

        User that modified the resource  # noqa: E501

        :return: The modified_by of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this WorkflowRun.

        User that modified the resource  # noqa: E501

        :param modified_by: The modified_by of this WorkflowRun.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def tenant_id(self):
        """Gets the tenant_id of this WorkflowRun.  # noqa: E501

        Tenant ID the resource belongs to  # noqa: E501

        :return: The tenant_id of this WorkflowRun.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this WorkflowRun.

        Tenant ID the resource belongs to  # noqa: E501

        :param tenant_id: The tenant_id of this WorkflowRun.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) > 255):
            raise ValueError("Invalid value for `tenant_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) < 0):
            raise ValueError("Invalid value for `tenant_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def acl(self):
        """Gets the acl of this WorkflowRun.  # noqa: E501

        Access control list of the resource  # noqa: E501

        :return: The acl of this WorkflowRun.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this WorkflowRun.

        Access control list of the resource  # noqa: E501

        :param acl: The acl of this WorkflowRun.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

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
        if not isinstance(other, WorkflowRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowRun):
            return True

        return self.to_dict() != other.to_dict()
