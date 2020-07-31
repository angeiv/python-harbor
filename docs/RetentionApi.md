# harbor.RetentionApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retentions_id_executions_eid_patch**](RetentionApi.md#retentions_id_executions_eid_patch) | **PATCH** /retentions/{id}/executions/{eid} | Stop a Retention job
[**retentions_id_executions_eid_tasks_get**](RetentionApi.md#retentions_id_executions_eid_tasks_get) | **GET** /retentions/{id}/executions/{eid}/tasks | Get Retention job tasks
[**retentions_id_executions_eid_tasks_tid_get**](RetentionApi.md#retentions_id_executions_eid_tasks_tid_get) | **GET** /retentions/{id}/executions/{eid}/tasks/{tid} | Get Retention job task log
[**retentions_id_executions_get**](RetentionApi.md#retentions_id_executions_get) | **GET** /retentions/{id}/executions | Get a Retention job
[**retentions_id_executions_post**](RetentionApi.md#retentions_id_executions_post) | **POST** /retentions/{id}/executions | Trigger a Retention job
[**retentions_id_get**](RetentionApi.md#retentions_id_get) | **GET** /retentions/{id} | Get Retention Policy
[**retentions_metadatas_get**](RetentionApi.md#retentions_metadatas_get) | **GET** /retentions/metadatas | Get Retention Metadatas
[**retentions_post**](RetentionApi.md#retentions_post) | **POST** /retentions | Create Retention Policy

# **retentions_id_executions_eid_patch**
> retentions_id_executions_eid_patch(body, id, eid)

Stop a Retention job

Stop a Retention job, only support \"stop\" action now.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
body = harbor.Body6() # Body6 | The action, only support "stop" now.
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.

try:
    # Stop a Retention job
    api_instance.retentions_id_executions_eid_patch(body, id, eid)
except ApiException as e:
    print("Exception when calling RetentionApi->retentions_id_executions_eid_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)| The action, only support &quot;stop&quot; now. | 
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_executions_eid_tasks_get**
> list[RetentionExecutionTask] retentions_id_executions_eid_tasks_get(id, eid)

Get Retention job tasks

Get Retention job tasks, each repository as a task.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.

try:
    # Get Retention job tasks
    api_response = api_instance.retentions_id_executions_eid_tasks_get(id, eid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->retentions_id_executions_eid_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 

### Return type

[**list[RetentionExecutionTask]**](RetentionExecutionTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_executions_eid_tasks_tid_get**
> str retentions_id_executions_eid_tasks_tid_get(id, eid, tid)

Get Retention job task log

Get Retention job task log, tags ratain or deletion detail will be shown in a table.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
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
    api_response = api_instance.retentions_id_executions_eid_tasks_tid_get(id, eid, tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->retentions_id_executions_eid_tasks_tid_get: %s\n" % e)
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_executions_get**
> list[RetentionExecution] retentions_id_executions_get(id)

Get a Retention job

Get a Retention job, job status may be delayed before job service schedule it up.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.

try:
    # Get a Retention job
    api_response = api_instance.retentions_id_executions_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->retentions_id_executions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 

### Return type

[**list[RetentionExecution]**](RetentionExecution.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_executions_post**
> retentions_id_executions_post(body, id)

Trigger a Retention job

Trigger a Retention job, if dry_run is True, nothing would be deleted actually.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
body = harbor.Body5() # Body5 | 
id = 789 # int | Retention ID.

try:
    # Trigger a Retention job
    api_instance.retentions_id_executions_post(body, id)
except ApiException as e:
    print("Exception when calling RetentionApi->retentions_id_executions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)|  | 
 **id** | **int**| Retention ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_get**
> RetentionPolicy retentions_id_get(id)

Get Retention Policy

Get Retention Policy.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.

try:
    # Get Retention Policy
    api_response = api_instance.retentions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->retentions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 

### Return type

[**RetentionPolicy**](RetentionPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_metadatas_get**
> RetentionMetadata retentions_metadatas_get()

Get Retention Metadatas

Get Retention Metadatas.

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))

try:
    # Get Retention Metadatas
    api_response = api_instance.retentions_metadatas_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionApi->retentions_metadatas_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RetentionMetadata**](RetentionMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_post**
> retentions_post(body)

Create Retention Policy

Create Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when no retention policy binded to project yet. 

### Example
```python
from __future__ import print_function
import time
import harbor
from harbor.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.RetentionApi(harbor.ApiClient(configuration))
body = harbor.RetentionPolicy() # RetentionPolicy | Create Retention Policy successfully.

try:
    # Create Retention Policy
    api_instance.retentions_post(body)
except ApiException as e:
    print("Exception when calling RetentionApi->retentions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetentionPolicy**](RetentionPolicy.md)| Create Retention Policy successfully. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

