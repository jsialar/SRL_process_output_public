# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ICA_SDK.api_client import ApiClient
from ICA_SDK.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class WorkflowSignalsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fail_signal(self, signal_id, **kwargs):  # noqa: E501
        """Fail a workflow signal  # noqa: E501

        Responds to a pending workflow signal with a failure result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fail_signal(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signal_id: ID of the workflow signal (required)
        :param FailWorkflowSignalRequest body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WorkflowSignal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.fail_signal_with_http_info(signal_id, **kwargs)  # noqa: E501

    def fail_signal_with_http_info(self, signal_id, **kwargs):  # noqa: E501
        """Fail a workflow signal  # noqa: E501

        Responds to a pending workflow signal with a failure result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fail_signal_with_http_info(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signal_id: ID of the workflow signal (required)
        :param FailWorkflowSignalRequest body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WorkflowSignal, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'signal_id',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fail_signal" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'signal_id' is set
        if self.api_client.client_side_validation and ('signal_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['signal_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signal_id` when calling `fail_signal`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'signal_id' in local_var_params:
            path_params['signalId'] = local_var_params['signal_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/workflows/signals/{signalId}:fail', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowSignal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_signal(self, signal_id, **kwargs):  # noqa: E501
        """Get the details of a workflow signal  # noqa: E501

        Gets the details of a workflow signal with a given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_signal(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signal_id: ID of the workflow signal (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WorkflowSignal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_signal_with_http_info(signal_id, **kwargs)  # noqa: E501

    def get_signal_with_http_info(self, signal_id, **kwargs):  # noqa: E501
        """Get the details of a workflow signal  # noqa: E501

        Gets the details of a workflow signal with a given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_signal_with_http_info(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signal_id: ID of the workflow signal (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WorkflowSignal, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'signal_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_signal" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'signal_id' is set
        if self.api_client.client_side_validation and ('signal_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['signal_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signal_id` when calling `get_signal`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'signal_id' in local_var_params:
            path_params['signalId'] = local_var_params['signal_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/workflows/signals/{signalId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowSignal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_signals(self, **kwargs):  # noqa: E501
        """Get a list of workflow signals  # noqa: E501

        Gets a list of workflow signals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_signals(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenant_id: ID of the tenant
        :param list[str] include: Comma-separated list of properties to include in the response
        :param int page_size: Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified.
        :param str page_token: Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified.
        :param str sort: Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending).
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WorkflowSignalList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_signals_with_http_info(**kwargs)  # noqa: E501

    def list_signals_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of workflow signals  # noqa: E501

        Gets a list of workflow signals.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_signals_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenant_id: ID of the tenant
        :param list[str] include: Comma-separated list of properties to include in the response
        :param int page_size: Number of items to include in a page. Value must be an integer between 1 and 1000. Only one of pageSize or pageToken can be specified.
        :param str page_token: Page offset descriptor. Valid page tokens are included in the response. Only one of pageSize or pageToken can be specified.
        :param str sort: Specifies the order to include list items as \"_{fieldName}_ [asc|desc]\". The second field is optional and specifies the sort direction (\"asc\" for ascending or \"desc\" for descending).
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WorkflowSignalList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'tenant_id',
            'include',
            'page_size',
            'page_token',
            'sort'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_signals" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tenant_id' in local_var_params and local_var_params['tenant_id'] is not None:  # noqa: E501
            query_params.append(('tenantId', local_var_params['tenant_id']))  # noqa: E501
        if 'include' in local_var_params and local_var_params['include'] is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501
            collection_formats['include'] = 'csv'  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] is not None:  # noqa: E501
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501
        if 'page_token' in local_var_params and local_var_params['page_token'] is not None:  # noqa: E501
            query_params.append(('pageToken', local_var_params['page_token']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/workflows/signals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowSignalList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def succeed_signal(self, signal_id, **kwargs):  # noqa: E501
        """Succeed a workflow signal  # noqa: E501

        Responds to a pending workflow signal with a successful result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.succeed_signal(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signal_id: ID of the workflow signal (required)
        :param SucceedWorkflowSignalRequest body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: WorkflowSignal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.succeed_signal_with_http_info(signal_id, **kwargs)  # noqa: E501

    def succeed_signal_with_http_info(self, signal_id, **kwargs):  # noqa: E501
        """Succeed a workflow signal  # noqa: E501

        Responds to a pending workflow signal with a successful result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.succeed_signal_with_http_info(signal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str signal_id: ID of the workflow signal (required)
        :param SucceedWorkflowSignalRequest body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(WorkflowSignal, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'signal_id',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method succeed_signal" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'signal_id' is set
        if self.api_client.client_side_validation and ('signal_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['signal_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `signal_id` when calling `succeed_signal`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'signal_id' in local_var_params:
            path_params['signalId'] = local_var_params['signal_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/workflows/signals/{signalId}:succeed', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowSignal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
