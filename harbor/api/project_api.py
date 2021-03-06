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


class ProjectApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_project(self, body, **kwargs):  # noqa: E501
        """Create a new project.  # noqa: E501

        This endpoint is for user to create a new project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectReq body: New created project. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new project.  # noqa: E501

        This endpoint is for user to create a new project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectReq body: New created project. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

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
            '/projects', 'POST',
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

    def delete_project(self, project_id, **kwargs):  # noqa: E501
        """Delete project by projectID  # noqa: E501

        This endpoint is aimed to delete project by project ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_project_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_project_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def delete_project_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Delete project by projectID  # noqa: E501

        This endpoint is aimed to delete project by project ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `delete_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}', 'DELETE',
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

    def get_logs(self, project_name, **kwargs):  # noqa: E501
        """Get recent logs of the projects  # noqa: E501

        Get recent logs of the projects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_logs(project_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: The name of the project (required)
        :param str x_request_id: An unique ID for the request
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param int page: The page number
        :param int page_size: The size of per page
        :return: list[AuditLog]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_logs_with_http_info(project_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_logs_with_http_info(project_name, **kwargs)  # noqa: E501
            return data

    def get_logs_with_http_info(self, project_name, **kwargs):  # noqa: E501
        """Get recent logs of the projects  # noqa: E501

        Get recent logs of the projects  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_logs_with_http_info(project_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: The name of the project (required)
        :param str x_request_id: An unique ID for the request
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param int page: The page number
        :param int page_size: The size of per page
        :return: list[AuditLog]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name', 'x_request_id', 'q', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name' is set
        if ('project_name' not in params or
                params['project_name'] is None):
            raise ValueError("Missing the required parameter `project_name` when calling `get_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in params:
            path_params['project_name'] = params['project_name']  # noqa: E501

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_name}/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AuditLog]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project(self, project_id, **kwargs):  # noqa: E501
        """Return specific project detail information  # noqa: E501

        This endpoint returns specific project information by project ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def get_project_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Return specific project detail information  # noqa: E501

        This endpoint returns specific project information by project ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Project',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_deletable(self, project_id, **kwargs):  # noqa: E501
        """Get the deletable status of the project  # noqa: E501

        Get the deletable status of the project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_deletable(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: ProjectDeletable
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_deletable_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_deletable_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def get_project_deletable_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Get the deletable status of the project  # noqa: E501

        Get the deletable status of the project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_deletable_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: ProjectDeletable
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_deletable" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_project_deletable`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/_deletable', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectDeletable',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_summary(self, project_id, **kwargs):  # noqa: E501
        """Get summary of the project.  # noqa: E501

        Get summary of the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_summary(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: ProjectSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_summary_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_summary_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def get_project_summary_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Get summary of the project.  # noqa: E501

        Get summary of the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_summary_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: ProjectSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_summary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_project_summary`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{project_id}/summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectSummary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_project(self, project_name, **kwargs):  # noqa: E501
        """Check if the project name user provided already exists.  # noqa: E501

        This endpoint is used to check if the project name provided already exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_project(project_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: Project name for checking exists. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_project_with_http_info(project_name, **kwargs)  # noqa: E501
        else:
            (data) = self.head_project_with_http_info(project_name, **kwargs)  # noqa: E501
            return data

    def head_project_with_http_info(self, project_name, **kwargs):  # noqa: E501
        """Check if the project name user provided already exists.  # noqa: E501

        This endpoint is used to check if the project name provided already exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_project_with_http_info(project_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: Project name for checking exists. (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name' is set
        if ('project_name' not in params or
                params['project_name'] is None):
            raise ValueError("Missing the required parameter `project_name` when calling `head_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_name' in params:
            query_params.append(('project_name', params['project_name']))  # noqa: E501

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects', 'HEAD',
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

    def list_projects(self, **kwargs):  # noqa: E501
        """List projects  # noqa: E501

        This endpoint returns projects created by Harbor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_projects(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param int page: The page number
        :param int page_size: The size of per page
        :param str name: The name of project.
        :param bool public: The project is public or private.
        :param str owner: The name of project owner.
        :return: list[Project]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_projects_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_projects_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_projects_with_http_info(self, **kwargs):  # noqa: E501
        """List projects  # noqa: E501

        This endpoint returns projects created by Harbor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_projects_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: An unique ID for the request
        :param int page: The page number
        :param int page_size: The size of per page
        :param str name: The name of project.
        :param bool public: The project is public or private.
        :param str owner: The name of project owner.
        :return: list[Project]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'page', 'page_size', 'name', 'public', 'owner']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_projects" % key
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
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'public' in params:
            query_params.append(('public', params['public']))  # noqa: E501
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic']  # noqa: E501

        return self.api_client.call_api(
            '/projects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Project]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_project(self, body, project_id, **kwargs):  # noqa: E501
        """Update properties for a selected project.  # noqa: E501

        This endpoint is aimed to update the properties of a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectReq body: Updates of project. (required)
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_project_with_http_info(body, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_project_with_http_info(body, project_id, **kwargs)  # noqa: E501
            return data

    def update_project_with_http_info(self, body, project_id, **kwargs):  # noqa: E501
        """Update properties for a selected project.  # noqa: E501

        This endpoint is aimed to update the properties of a project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_project_with_http_info(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectReq body: Updates of project. (required)
        :param int project_id: The ID of the project (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_project`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `update_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-Id'] = params['x_request_id']  # noqa: E501

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
            '/projects/{project_id}', 'PUT',
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
