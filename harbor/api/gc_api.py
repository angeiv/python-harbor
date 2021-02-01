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


class GcApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_gc_schedule(self, body, **kwargs):  # noqa: E501
        """Create a gc schedule.  # noqa: E501

        This endpoint is for update gc schedule.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_gc_schedule(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: Updates of gc's schedule. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_gc_schedule_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_gc_schedule_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_gc_schedule_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a gc schedule.  # noqa: E501

        This endpoint is for update gc schedule.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_gc_schedule_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: Updates of gc's schedule. (required)
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
                    " to method create_gc_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_gc_schedule`")  # noqa: E501

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
            '/system/gc/schedule', 'POST',
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

    def get_gc(self, gc_id, **kwargs):  # noqa: E501
        """Get gc status.  # noqa: E501

        This endpoint let user get gc status filtered by specific ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gc(gc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gc_id: The ID of the gc log (required)
        :return: GCHistory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gc_with_http_info(gc_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gc_with_http_info(gc_id, **kwargs)  # noqa: E501
            return data

    def get_gc_with_http_info(self, gc_id, **kwargs):  # noqa: E501
        """Get gc status.  # noqa: E501

        This endpoint let user get gc status filtered by specific ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gc_with_http_info(gc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gc_id: The ID of the gc log (required)
        :return: GCHistory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gc_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gc" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gc_id' is set
        if ('gc_id' not in params or
                params['gc_id'] is None):
            raise ValueError("Missing the required parameter `gc_id` when calling `get_gc`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gc_id' in params:
            path_params['gc_id'] = params['gc_id']  # noqa: E501

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
            '/system/gc/{gc_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GCHistory',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gc_history(self, **kwargs):  # noqa: E501
        """Get gc results.  # noqa: E501

        This endpoint let user get gc execution history.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gc_history(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param int page: The page number
        :param int page_size: The size of per page
        :return: list[GCHistory]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gc_history_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_gc_history_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_gc_history_with_http_info(self, **kwargs):  # noqa: E501
        """Get gc results.  # noqa: E501

        This endpoint let user get gc execution history.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gc_history_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max]
        :param int page: The page number
        :param int page_size: The size of per page
        :return: list[GCHistory]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gc_history" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

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
            '/system/gc', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GCHistory]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_gc_log(self, gc_id, **kwargs):  # noqa: E501
        """Get gc job log.  # noqa: E501

        This endpoint let user get gc job logs filtered by specific ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gc_log(gc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gc_id: The ID of the gc log (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gc_log_with_http_info(gc_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_gc_log_with_http_info(gc_id, **kwargs)  # noqa: E501
            return data

    def get_gc_log_with_http_info(self, gc_id, **kwargs):  # noqa: E501
        """Get gc job log.  # noqa: E501

        This endpoint let user get gc job logs filtered by specific ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gc_log_with_http_info(gc_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gc_id: The ID of the gc log (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gc_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gc_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gc_id' is set
        if ('gc_id' not in params or
                params['gc_id'] is None):
            raise ValueError("Missing the required parameter `gc_id` when calling `get_gc_log`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gc_id' in params:
            path_params['gc_id'] = params['gc_id']  # noqa: E501

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
            '/system/gc/{gc_id}/log', 'GET',
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

    def get_gc_schedule(self, **kwargs):  # noqa: E501
        """Get gc's schedule.  # noqa: E501

        This endpoint is for get schedule of gc job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gc_schedule(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GCHistory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_gc_schedule_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_gc_schedule_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_gc_schedule_with_http_info(self, **kwargs):  # noqa: E501
        """Get gc's schedule.  # noqa: E501

        This endpoint is for get schedule of gc job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_gc_schedule_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GCHistory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gc_schedule" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/system/gc/schedule', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GCHistory',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_gc_schedule(self, body, **kwargs):  # noqa: E501
        """Update gc's schedule.  # noqa: E501

        This endpoint is for update gc schedule.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_gc_schedule(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: Updates of gc's schedule. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_gc_schedule_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_gc_schedule_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_gc_schedule_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update gc's schedule.  # noqa: E501

        This endpoint is for update gc schedule.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_gc_schedule_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: Updates of gc's schedule. (required)
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
                    " to method update_gc_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_gc_schedule`")  # noqa: E501

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
            '/system/gc/schedule', 'PUT',
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
