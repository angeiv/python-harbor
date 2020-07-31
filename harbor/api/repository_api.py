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


class RepositoryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_repository(self, project_name, repository_name, **kwargs):  # noqa: E501
        """Delete repository  # noqa: E501

        Delete the repository specified by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repository(project_name, repository_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: The name of the project (required)
        :param str repository_name: The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_repository_with_http_info(project_name, repository_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_repository_with_http_info(project_name, repository_name, **kwargs)  # noqa: E501
            return data

    def delete_repository_with_http_info(self, project_name, repository_name, **kwargs):  # noqa: E501
        """Delete repository  # noqa: E501

        Delete the repository specified by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repository_with_http_info(project_name, repository_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: The name of the project (required)
        :param str repository_name: The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name', 'repository_name', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name' is set
        if ('project_name' not in params or
                params['project_name'] is None):
            raise ValueError("Missing the required parameter `project_name` when calling `delete_repository`")  # noqa: E501
        # verify the required parameter 'repository_name' is set
        if ('repository_name' not in params or
                params['repository_name'] is None):
            raise ValueError("Missing the required parameter `repository_name` when calling `delete_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in params:
            path_params['project_name'] = params['project_name']  # noqa: E501
        if 'repository_name' in params:
            path_params['repository_name'] = params['repository_name']  # noqa: E501

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
            '/projects/{project_name}/repositories/{repository_name}', 'DELETE',
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

    def get_repository(self, project_name, repository_name, **kwargs):  # noqa: E501
        """Get repository  # noqa: E501

        Get the repository specified by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repository(project_name, repository_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: The name of the project (required)
        :param str repository_name: The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb (required)
        :param str x_request_id: An unique ID for the request
        :return: Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_repository_with_http_info(project_name, repository_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_repository_with_http_info(project_name, repository_name, **kwargs)  # noqa: E501
            return data

    def get_repository_with_http_info(self, project_name, repository_name, **kwargs):  # noqa: E501
        """Get repository  # noqa: E501

        Get the repository specified by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repository_with_http_info(project_name, repository_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: The name of the project (required)
        :param str repository_name: The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb (required)
        :param str x_request_id: An unique ID for the request
        :return: Repository
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name', 'repository_name', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name' is set
        if ('project_name' not in params or
                params['project_name'] is None):
            raise ValueError("Missing the required parameter `project_name` when calling `get_repository`")  # noqa: E501
        # verify the required parameter 'repository_name' is set
        if ('repository_name' not in params or
                params['repository_name'] is None):
            raise ValueError("Missing the required parameter `repository_name` when calling `get_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in params:
            path_params['project_name'] = params['project_name']  # noqa: E501
        if 'repository_name' in params:
            path_params['repository_name'] = params['repository_name']  # noqa: E501

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
            '/projects/{project_name}/repositories/{repository_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Repository',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_repositories(self, project_name, **kwargs):  # noqa: E501
        """List repositories  # noqa: E501

        List repositories of the specified project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_repositories(project_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: The name of the project (required)
        :param str x_request_id: An unique ID for the request
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param int page: The page number
        :param int page_size: The size of per page
        :return: list[Repository]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_repositories_with_http_info(project_name, **kwargs)  # noqa: E501
        else:
            (data) = self.list_repositories_with_http_info(project_name, **kwargs)  # noqa: E501
            return data

    def list_repositories_with_http_info(self, project_name, **kwargs):  # noqa: E501
        """List repositories  # noqa: E501

        List repositories of the specified project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_repositories_with_http_info(project_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_name: The name of the project (required)
        :param str x_request_id: An unique ID for the request
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param int page: The page number
        :param int page_size: The size of per page
        :return: list[Repository]
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
                    " to method list_repositories" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_name' is set
        if ('project_name' not in params or
                params['project_name'] is None):
            raise ValueError("Missing the required parameter `project_name` when calling `list_repositories`")  # noqa: E501

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
            '/projects/{project_name}/repositories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Repository]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_repository(self, body, project_name, repository_name, **kwargs):  # noqa: E501
        """Update repository  # noqa: E501

        Update the repository specified by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_repository(body, project_name, repository_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Repository body: The JSON object of repository. (required)
        :param str project_name: The name of the project (required)
        :param str repository_name: The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_repository_with_http_info(body, project_name, repository_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_repository_with_http_info(body, project_name, repository_name, **kwargs)  # noqa: E501
            return data

    def update_repository_with_http_info(self, body, project_name, repository_name, **kwargs):  # noqa: E501
        """Update repository  # noqa: E501

        Update the repository specified by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_repository_with_http_info(body, project_name, repository_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Repository body: The JSON object of repository. (required)
        :param str project_name: The name of the project (required)
        :param str repository_name: The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb (required)
        :param str x_request_id: An unique ID for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_name', 'repository_name', 'x_request_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_repository`")  # noqa: E501
        # verify the required parameter 'project_name' is set
        if ('project_name' not in params or
                params['project_name'] is None):
            raise ValueError("Missing the required parameter `project_name` when calling `update_repository`")  # noqa: E501
        # verify the required parameter 'repository_name' is set
        if ('repository_name' not in params or
                params['repository_name'] is None):
            raise ValueError("Missing the required parameter `repository_name` when calling `update_repository`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_name' in params:
            path_params['project_name'] = params['project_name']  # noqa: E501
        if 'repository_name' in params:
            path_params['repository_name'] = params['repository_name']  # noqa: E501

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
            '/projects/{project_name}/repositories/{repository_name}', 'PUT',
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
