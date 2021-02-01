# harbor.ProjectApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /projects | Create a new project.
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /projects/{project_id} | Delete project by projectID
[**get_logs**](ProjectApi.md#get_logs) | **GET** /projects/{project_name}/logs | Get recent logs of the projects
[**get_project**](ProjectApi.md#get_project) | **GET** /projects/{project_id} | Return specific project detail information
[**get_project_deletable**](ProjectApi.md#get_project_deletable) | **GET** /projects/{project_id}/_deletable | Get the deletable status of the project
[**get_project_summary**](ProjectApi.md#get_project_summary) | **GET** /projects/{project_id}/summary | Get summary of the project.
[**head_project**](ProjectApi.md#head_project) | **HEAD** /projects | Check if the project name user provided already exists.
[**list_projects**](ProjectApi.md#list_projects) | **GET** /projects | List projects
[**update_project**](ProjectApi.md#update_project) | **PUT** /projects/{project_id} | Update properties for a selected project.

# **create_project**
> create_project(body, x_request_id=x_request_id)

Create a new project.

This endpoint is for user to create a new project.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ProjectApi(harbor.ApiClient(configuration))
body = harbor.ProjectReq() # ProjectReq | New created project.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create a new project.
    api_instance.create_project(body, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectReq**](ProjectReq.md)| New created project. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id, x_request_id=x_request_id)

Delete project by projectID

This endpoint is aimed to delete project by project ID.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ProjectApi(harbor.ApiClient(configuration))
project_id = 789 # int | The ID of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete project by projectID
    api_instance.delete_project(project_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> list[AuditLog] get_logs(project_name, x_request_id=x_request_id, q=q, page=page, page_size=page_size)

Get recent logs of the projects

Get recent logs of the projects

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ProjectApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)

try:
    # Get recent logs of the projects
    api_response = api_instance.get_logs(project_name, x_request_id=x_request_id, q=q, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| The name of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **q** | **str**| Query string to query resources. Supported query patterns are \&quot;exact match(k&#x3D;v)\&quot;, \&quot;fuzzy match(k&#x3D;~v)\&quot;, \&quot;range(k&#x3D;[min~max])\&quot;, \&quot;list with union releationship(k&#x3D;{v1 v2 v3})\&quot; and \&quot;list with intersetion relationship(k&#x3D;(v1 v2 v3))\&quot;. The value of range and list can be string(enclosed by \&quot; or &#x27;), integer or time(in format \&quot;2020-04-09 02:36:00\&quot;). All of these query patterns should be put in the query string \&quot;q&#x3D;xxx\&quot; and splitted by \&quot;,\&quot;. e.g. q&#x3D;k1&#x3D;v1,k2&#x3D;~v2,k3&#x3D;[min~max] | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]

### Return type

[**list[AuditLog]**](AuditLog.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_id, x_request_id=x_request_id)

Return specific project detail information

This endpoint returns specific project information by project ID.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ProjectApi(harbor.ApiClient(configuration))
project_id = 789 # int | The ID of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Return specific project detail information
    api_response = api_instance.get_project(project_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_deletable**
> ProjectDeletable get_project_deletable(project_id, x_request_id=x_request_id)

Get the deletable status of the project

Get the deletable status of the project

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ProjectApi(harbor.ApiClient(configuration))
project_id = 789 # int | The ID of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the deletable status of the project
    api_response = api_instance.get_project_deletable(project_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_deletable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ProjectDeletable**](ProjectDeletable.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_summary**
> ProjectSummary get_project_summary(project_id, x_request_id=x_request_id)

Get summary of the project.

Get summary of the project.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ProjectApi(harbor.ApiClient(configuration))
project_id = 789 # int | The ID of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get summary of the project.
    api_response = api_instance.get_project_summary(project_id, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

[**ProjectSummary**](ProjectSummary.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_project**
> head_project(project_name, x_request_id=x_request_id)

Check if the project name user provided already exists.

This endpoint is used to check if the project name provided already exist.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ProjectApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | Project name for checking exists.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Check if the project name user provided already exists.
    api_instance.head_project(project_name, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ProjectApi->head_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| Project name for checking exists. | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> list[Project] list_projects(x_request_id=x_request_id, page=page, page_size=page_size, name=name, public=public, owner=owner)

List projects

This endpoint returns projects created by Harbor.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ProjectApi(harbor.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
name = 'name_example' # str | The name of project. (optional)
public = true # bool | The project is public or private. (optional)
owner = 'owner_example' # str | The name of project owner. (optional)

try:
    # List projects
    api_response = api_instance.list_projects(x_request_id=x_request_id, page=page, page_size=page_size, name=name, public=public, owner=owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| An unique ID for the request | [optional] 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **name** | **str**| The name of project. | [optional] 
 **public** | **bool**| The project is public or private. | [optional] 
 **owner** | **str**| The name of project owner. | [optional] 

### Return type

[**list[Project]**](Project.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> update_project(body, project_id, x_request_id=x_request_id)

Update properties for a selected project.

This endpoint is aimed to update the properties of a project.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ProjectApi(harbor.ApiClient(configuration))
body = harbor.ProjectReq() # ProjectReq | Updates of project.
project_id = 789 # int | The ID of the project
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Update properties for a selected project.
    api_instance.update_project(body, project_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectReq**](ProjectReq.md)| Updates of project. | 
 **project_id** | **int**| The ID of the project | 
 **x_request_id** | **str**| An unique ID for the request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

