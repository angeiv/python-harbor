# harbor.RetentionApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_retention**](RetentionApi.md#create_retention) | **POST** /retentions | Create Retention Policy
[**get_rentenition_metadata**](RetentionApi.md#get_rentenition_metadata) | **GET** /retentions/metadatas | Get Retention Metadatas
[**get_retention**](RetentionApi.md#get_retention) | **GET** /retentions/{id} | Get Retention Policy
[**get_retention_task_log**](RetentionApi.md#get_retention_task_log) | **GET** /retentions/{id}/executions/{eid}/tasks/{tid} | Get Retention job task log
[**list_retention_executions**](RetentionApi.md#list_retention_executions) | **GET** /retentions/{id}/executions | Get Retention executions
[**list_retention_tasks**](RetentionApi.md#list_retention_tasks) | **GET** /retentions/{id}/executions/{eid}/tasks | Get Retention tasks
[**operate_retention_execution**](RetentionApi.md#operate_retention_execution) | **PATCH** /retentions/{id}/executions/{eid} | Stop a Retention execution
[**trigger_retention_execution**](RetentionApi.md#trigger_retention_execution) | **POST** /retentions/{id}/executions | Trigger a Retention Execution
[**update_retention**](RetentionApi.md#update_retention) | **PUT** /retentions/{id} | Update Retention Policy

# **create_retention**
> create_retention(body)

Create Retention Policy

Create Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when no retention policy binded to project yet.

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
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
body = harbor.RetentionPolicy() # RetentionPolicy | Create Retention Policy successfully.

try:
    # Create Retention Policy
    api_instance.create_retention(body)
except ApiException as e:
    print("Exception when calling RetentionApi->create_retention: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetentionPolicy**](RetentionPolicy.md)| Create Retention Policy successfully. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rentenition_metadata**
> RetentionMetadata get_rentenition_metadata()

Get Retention Metadatas

Get Retention Metadatas.

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
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))

try:
    # Get Retention Metadatas
    api_response = api_instance.get_rentenition_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->get_rentenition_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RetentionMetadata**](RetentionMetadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retention**
> RetentionPolicy get_retention(id)

Get Retention Policy

Get Retention Policy.

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
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.

try:
    # Get Retention Policy
    api_response = api_instance.get_retention(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->get_retention: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 

### Return type

[**RetentionPolicy**](RetentionPolicy.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retention_task_log**
> str get_retention_task_log(id, eid, tid)

Get Retention job task log

Get Retention job task log, tags ratain or deletion detail will be shown in a table.

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
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.
tid = 789 # int | Retention execution ID.

try:
    # Get Retention job task log
    api_response = api_instance.get_retention_task_log(id, eid, tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->get_retention_task_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 
 **tid** | **int**| Retention execution ID. | 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_retention_executions**
> list[RetentionExecution] list_retention_executions(id, page=page, page_size=page_size)

Get Retention executions

Get Retention executions, execution status may be delayed before job service schedule it up.

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
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.
page = 789 # int | The page number. (optional)
page_size = 789 # int | The size of per page. (optional)

try:
    # Get Retention executions
    api_response = api_instance.list_retention_executions(id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->list_retention_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **page** | **int**| The page number. | [optional] 
 **page_size** | **int**| The size of per page. | [optional] 

### Return type

[**list[RetentionExecution]**](RetentionExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_retention_tasks**
> list[RetentionExecutionTask] list_retention_tasks(id, eid, page=page, page_size=page_size)

Get Retention tasks

Get Retention tasks, each repository as a task.

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
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.
page = 789 # int | The page number. (optional)
page_size = 789 # int | The size of per page. (optional)

try:
    # Get Retention tasks
    api_response = api_instance.list_retention_tasks(id, eid, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->list_retention_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 
 **page** | **int**| The page number. | [optional] 
 **page_size** | **int**| The size of per page. | [optional] 

### Return type

[**list[RetentionExecutionTask]**](RetentionExecutionTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operate_retention_execution**
> operate_retention_execution(body, id, eid)

Stop a Retention execution

Stop a Retention execution, only support \"stop\" action now.

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
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
body = harbor.Body1() # Body1 | The action, only support "stop" now.
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.

try:
    # Stop a Retention execution
    api_instance.operate_retention_execution(body, id, eid)
except ApiException as e:
    print("Exception when calling RetentionApi->operate_retention_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| The action, only support &quot;stop&quot; now. | 
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_retention_execution**
> trigger_retention_execution(body, id)

Trigger a Retention Execution

Trigger a Retention Execution, if dry_run is True, nothing would be deleted actually.

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
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
body = harbor.Body() # Body | 
id = 789 # int | Retention ID.

try:
    # Trigger a Retention Execution
    api_instance.trigger_retention_execution(body, id)
except ApiException as e:
    print("Exception when calling RetentionApi->trigger_retention_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 
 **id** | **int**| Retention ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_retention**
> update_retention(body, id)

Update Retention Policy

Update Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when retention policy has already binded to project.

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
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
body = harbor.RetentionPolicy() # RetentionPolicy | 
id = 789 # int | Retention ID.

try:
    # Update Retention Policy
    api_instance.update_retention(body, id)
except ApiException as e:
    print("Exception when calling RetentionApi->update_retention: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetentionPolicy**](RetentionPolicy.md)|  | 
 **id** | **int**| Retention ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

