# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from harbor.api_client import ApiClient


class ReplicationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_replication_execution(self, id, **kwargs):  # noqa: E501
        """Get the specific replication execution  # noqa: E501

        Get the replication execution specified by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_replication_execution(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the execution. (required)
        :return: ReplicationExecution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_replication_execution_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_replication_execution_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_replication_execution_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get the specific replication execution  # noqa: E501

        Get the replication execution specified by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_replication_execution_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the execution. (required)
        :return: ReplicationExecution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_replication_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_replication_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/replication/executions/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReplicationExecution',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_replication_log(self, id, task_id, **kwargs):  # noqa: E501
        """Get the log of the specific replication task  # noqa: E501

        Get the log of the specific replication task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_replication_log(id, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the execution that the tasks belongs to. (required)
        :param int task_id: The ID of the task. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_replication_log_with_http_info(id, task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_replication_log_with_http_info(id, task_id, **kwargs)  # noqa: E501
            return data

    def get_replication_log_with_http_info(self, id, task_id, **kwargs):  # noqa: E501
        """Get the log of the specific replication task  # noqa: E501

        Get the log of the specific replication task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_replication_log_with_http_info(id, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the execution that the tasks belongs to. (required)
        :param int task_id: The ID of the task. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_replication_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_replication_log`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `get_replication_log`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'task_id' in params:
            path_params['task_id'] = params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/replication/executions/{id}/tasks/{task_id}/log', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_replication_executions(self, **kwargs):  # noqa: E501
        """List replication executions  # noqa: E501

        List replication executions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_replication_executions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number
        :param int page_size: The size of per page
        :param int policy_id: The ID of the policy that the executions belong to.
        :param str status: The execution status.
        :param str trigger: The trigger mode.
        :return: list[ReplicationExecution]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_replication_executions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_replication_executions_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_replication_executions_with_http_info(self, **kwargs):  # noqa: E501
        """List replication executions  # noqa: E501

        List replication executions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_replication_executions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The page number
        :param int page_size: The size of per page
        :param int policy_id: The ID of the policy that the executions belong to.
        :param str status: The execution status.
        :param str trigger: The trigger mode.
        :return: list[ReplicationExecution]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', 'policy_id', 'status', 'trigger']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_replication_executions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'policy_id' in params:
            query_params.append(('policy_id', params['policy_id']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'trigger' in params:
            query_params.append(('trigger', params['trigger']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/replication/executions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ReplicationExecution]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_replication_tasks(self, id, **kwargs):  # noqa: E501
        """List replication tasks for a specific execution  # noqa: E501

        List replication tasks for a specific execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_replication_tasks(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the execution that the tasks belongs to. (required)
        :param int page: The page number
        :param int page_size: The size of per page
        :param str status: The task status.
        :param str resource_type: The resource type.
        :return: list[ReplicationTask]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_replication_tasks_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_replication_tasks_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_replication_tasks_with_http_info(self, id, **kwargs):  # noqa: E501
        """List replication tasks for a specific execution  # noqa: E501

        List replication tasks for a specific execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_replication_tasks_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the execution that the tasks belongs to. (required)
        :param int page: The page number
        :param int page_size: The size of per page
        :param str status: The task status.
        :param str resource_type: The resource type.
        :return: list[ReplicationTask]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'page_size', 'status', 'resource_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_replication_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_replication_tasks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'resource_type' in params:
            query_params.append(('resource_type', params['resource_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/replication/executions/{id}/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ReplicationTask]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_replication(self, body, **kwargs):  # noqa: E501
        """Start one replication execution  # noqa: E501

        Start one replication execution according to the policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_replication(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StartReplicationExecution body: The ID of policy that the execution belongs to (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.start_replication_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.start_replication_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def start_replication_with_http_info(self, body, **kwargs):  # noqa: E501
        """Start one replication execution  # noqa: E501

        Start one replication execution according to the policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_replication_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StartReplicationExecution body: The ID of policy that the execution belongs to (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_replication" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `start_replication`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/replication/executions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stop_replication(self, id, **kwargs):  # noqa: E501
        """Stop the specific replication execution  # noqa: E501

        Stop the replication execution specified by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop_replication(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the execution. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stop_replication_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.stop_replication_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def stop_replication_with_http_info(self, id, **kwargs):  # noqa: E501
        """Stop the specific replication execution  # noqa: E501

        Stop the replication execution specified by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop_replication_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the execution. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_replication" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `stop_replication`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/replication/executions/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
