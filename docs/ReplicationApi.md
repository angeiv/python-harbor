# harbor.ReplicationApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_replication_execution**](ReplicationApi.md#get_replication_execution) | **GET** /replication/executions/{id} | Get the specific replication execution
[**get_replication_log**](ReplicationApi.md#get_replication_log) | **GET** /replication/executions/{id}/tasks/{task_id}/log | Get the log of the specific replication task
[**list_replication_executions**](ReplicationApi.md#list_replication_executions) | **GET** /replication/executions | List replication executions
[**list_replication_tasks**](ReplicationApi.md#list_replication_tasks) | **GET** /replication/executions/{id}/tasks | List replication tasks for a specific execution
[**start_replication**](ReplicationApi.md#start_replication) | **POST** /replication/executions | Start one replication execution
[**stop_replication**](ReplicationApi.md#stop_replication) | **PUT** /replication/executions/{id} | Stop the specific replication execution

# **get_replication_execution**
> ReplicationExecution get_replication_execution(id)

Get the specific replication execution

Get the replication execution specified by ID

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
api_instance = harbor.ReplicationApi(harbor.ApiClient(configuration))
id = 789 # int | The ID of the execution.

try:
    # Get the specific replication execution
    api_response = api_instance.get_replication_execution(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->get_replication_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution. | 

### Return type

[**ReplicationExecution**](ReplicationExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_replication_log**
> str get_replication_log(id, task_id)

Get the log of the specific replication task

Get the log of the specific replication task

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
api_instance = harbor.ReplicationApi(harbor.ApiClient(configuration))
id = 789 # int | The ID of the execution that the tasks belongs to.
task_id = 789 # int | The ID of the task.

try:
    # Get the log of the specific replication task
    api_response = api_instance.get_replication_log(id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->get_replication_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution that the tasks belongs to. | 
 **task_id** | **int**| The ID of the task. | 

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replication_executions**
> list[ReplicationExecution] list_replication_executions(page=page, page_size=page_size, policy_id=policy_id, status=status, trigger=trigger)

List replication executions

List replication executions

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
api_instance = harbor.ReplicationApi(harbor.ApiClient(configuration))
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
policy_id = 56 # int | The ID of the policy that the executions belong to. (optional)
status = 'status_example' # str | The execution status. (optional)
trigger = 'trigger_example' # str | The trigger mode. (optional)

try:
    # List replication executions
    api_response = api_instance.list_replication_executions(page=page, page_size=page_size, policy_id=policy_id, status=status, trigger=trigger)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->list_replication_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **policy_id** | **int**| The ID of the policy that the executions belong to. | [optional] 
 **status** | **str**| The execution status. | [optional] 
 **trigger** | **str**| The trigger mode. | [optional] 

### Return type

[**list[ReplicationExecution]**](ReplicationExecution.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replication_tasks**
> list[ReplicationTask] list_replication_tasks(id, page=page, page_size=page_size, status=status, resource_type=resource_type)

List replication tasks for a specific execution

List replication tasks for a specific execution

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
api_instance = harbor.ReplicationApi(harbor.ApiClient(configuration))
id = 789 # int | The ID of the execution that the tasks belongs to.
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
status = 'status_example' # str | The task status. (optional)
resource_type = 'resource_type_example' # str | The resource type. (optional)

try:
    # List replication tasks for a specific execution
    api_response = api_instance.list_replication_tasks(id, page=page, page_size=page_size, status=status, resource_type=resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationApi->list_replication_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution that the tasks belongs to. | 
 **page** | **int**| The page number | [optional] [default to 1]
 **page_size** | **int**| The size of per page | [optional] [default to 10]
 **status** | **str**| The task status. | [optional] 
 **resource_type** | **str**| The resource type. | [optional] 

### Return type

[**list[ReplicationTask]**](ReplicationTask.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_replication**
> start_replication(body)

Start one replication execution

Start one replication execution according to the policy

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
api_instance = harbor.ReplicationApi(harbor.ApiClient(configuration))
body = harbor.StartReplicationExecution() # StartReplicationExecution | The ID of policy that the execution belongs to

try:
    # Start one replication execution
    api_instance.start_replication(body)
except ApiException as e:
    print("Exception when calling ReplicationApi->start_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StartReplicationExecution**](StartReplicationExecution.md)| The ID of policy that the execution belongs to | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_replication**
> stop_replication(id)

Stop the specific replication execution

Stop the replication execution specified by ID

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
api_instance = harbor.ReplicationApi(harbor.ApiClient(configuration))
id = 789 # int | The ID of the execution.

try:
    # Stop the specific replication execution
    api_instance.stop_replication(id)
except ApiException as e:
    print("Exception when calling ReplicationApi->stop_replication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the execution. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

