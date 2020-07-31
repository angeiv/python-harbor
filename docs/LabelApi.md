# harbor.LabelApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartrepo_repo_charts_name_version_labels_get**](LabelApi.md#chartrepo_repo_charts_name_version_labels_get) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
[**chartrepo_repo_charts_name_version_labels_id_delete**](LabelApi.md#chartrepo_repo_charts_name_version_labels_id_delete) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
[**chartrepo_repo_charts_name_version_labels_post**](LabelApi.md#chartrepo_repo_charts_name_version_labels_post) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.

# **chartrepo_repo_charts_name_version_labels_get**
> chartrepo_repo_charts_name_version_labels_get(repo, name, version)

Return the attahced labels of chart.

Return the attahced labels of the specified chart version.

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
api_instance = harbor.LabelApi(harbor.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version

try:
    # Return the attahced labels of chart.
    api_instance.chartrepo_repo_charts_name_version_labels_get(repo, name, version)
except ApiException as e:
    print("Exception when calling LabelApi->chartrepo_repo_charts_name_version_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 
 **version** | **str**| The chart version | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_labels_id_delete**
> chartrepo_repo_charts_name_version_labels_id_delete(repo, name, version, id)

Remove label from chart.

Remove label from the specified chart version.

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
api_instance = harbor.LabelApi(harbor.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version
id = 56 # int | The label ID

try:
    # Remove label from chart.
    api_instance.chartrepo_repo_charts_name_version_labels_id_delete(repo, name, version, id)
except ApiException as e:
    print("Exception when calling LabelApi->chartrepo_repo_charts_name_version_labels_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 
 **version** | **str**| The chart version | 
 **id** | **int**| The label ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_labels_post**
> chartrepo_repo_charts_name_version_labels_post(body, repo, name, version)

Mark label to chart.

Mark label to the specified chart version.

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
api_instance = harbor.LabelApi(harbor.ApiClient(configuration))
body = harbor.Label() # Label | The label being marked to the chart version
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version

try:
    # Mark label to chart.
    api_instance.chartrepo_repo_charts_name_version_labels_post(body, repo, name, version)
except ApiException as e:
    print("Exception when calling LabelApi->chartrepo_repo_charts_name_version_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Label**](Label.md)| The label being marked to the chart version | 
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 
 **version** | **str**| The chart version | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

