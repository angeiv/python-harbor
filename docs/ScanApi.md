# harbor.ScanApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repositories_repo_name_tags_tag_scan_get**](ScanApi.md#repositories_repo_name_tags_tag_scan_get) | **GET** /repositories/{repo_name}/tags/{tag}/scan | Get the scan report
[**repositories_repo_name_tags_tag_scan_post**](ScanApi.md#repositories_repo_name_tags_tag_scan_post) | **POST** /repositories/{repo_name}/tags/{tag}/scan | Scan the image.
[**repositories_repo_name_tags_tag_scan_uuid_log_get**](ScanApi.md#repositories_repo_name_tags_tag_scan_uuid_log_get) | **GET** /repositories/{repo_name}/tags/{tag}/scan/{uuid}/log | Get scan log
[**scans_all_metrics_get**](ScanApi.md#scans_all_metrics_get) | **GET** /scans/all/metrics | Get the metrics of the latest scan all process
[**scans_schedule_metrics_get**](ScanApi.md#scans_schedule_metrics_get) | **GET** /scans/schedule/metrics | Get the metrics of the latest scheduled scan all process

# **repositories_repo_name_tags_tag_scan_get**
> Report repositories_repo_name_tags_tag_scan_get(repo_name, tag, accept=accept)

Get the scan report

Retrieve the scan report for the artifact identified by the repo_name and tag. 

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
api_instance = harbor.ScanApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Repository name
tag = 'tag_example' # str | Tag name
accept = 'accept_example' # str | Mimetype in header. e.g: \"application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0\"  (optional)

try:
    # Get the scan report
    api_response = api_instance.repositories_repo_name_tags_tag_scan_get(repo_name, tag, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->repositories_repo_name_tags_tag_scan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **tag** | **str**| Tag name | 
 **accept** | **str**| Mimetype in header. e.g: \&quot;application/vnd.scanner.adapter.vuln.report.harbor+json; version&#x3D;1.0\&quot;  | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_scan_post**
> repositories_repo_name_tags_tag_scan_post(repo_name, tag)

Scan the image.

Trigger a scan targeting the artifact identified by the repo_name and tag. 

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
api_instance = harbor.ScanApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Repository name
tag = 'tag_example' # str | Tag name

try:
    # Scan the image.
    api_instance.repositories_repo_name_tags_tag_scan_post(repo_name, tag)
except ApiException as e:
    print("Exception when calling ScanApi->repositories_repo_name_tags_tag_scan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **tag** | **str**| Tag name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_scan_uuid_log_get**
> str repositories_repo_name_tags_tag_scan_uuid_log_get(repo_name, tag, uuid)

Get scan log

Get the log text stream for the given artifact and scan action.

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
api_instance = harbor.ScanApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Repository name
tag = 'tag_example' # str | Tag name
uuid = 'uuid_example' # str | the scan unique identifier

try:
    # Get scan log
    api_response = api_instance.repositories_repo_name_tags_tag_scan_uuid_log_get(repo_name, tag, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->repositories_repo_name_tags_tag_scan_uuid_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **tag** | **str**| Tag name | 
 **uuid** | **str**| the scan unique identifier | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_all_metrics_get**
> Stats scans_all_metrics_get()

Get the metrics of the latest scan all process

Get the metrics of the latest scan all process

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
api_instance = harbor.ScanApi(harbor.ApiClient(configuration))

try:
    # Get the metrics of the latest scan all process
    api_response = api_instance.scans_all_metrics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scans_all_metrics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Stats**](Stats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scans_schedule_metrics_get**
> Stats scans_schedule_metrics_get()

Get the metrics of the latest scheduled scan all process

Get the metrics of the latest scheduled scan all process

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
api_instance = harbor.ScanApi(harbor.ApiClient(configuration))

try:
    # Get the metrics of the latest scheduled scan all process
    api_response = api_instance.scans_schedule_metrics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->scans_schedule_metrics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Stats**](Stats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

