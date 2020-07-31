# harbor.QuotaApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotas_id_get**](QuotaApi.md#quotas_id_get) | **GET** /quotas/{id} | Get the specified quota
[**quotas_id_put**](QuotaApi.md#quotas_id_put) | **PUT** /quotas/{id} | Update the specified quota

# **quotas_id_get**
> Quota quotas_id_get(id)

Get the specified quota

Get the specified quota

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
api_instance = harbor.QuotaApi(harbor.ApiClient(configuration))
id = 56 # int | Quota ID

try:
    # Get the specified quota
    api_response = api_instance.quotas_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->quotas_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Quota ID | 

### Return type

[**Quota**](Quota.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_id_put**
> quotas_id_put(body, id)

Update the specified quota

Update hard limits of the specified quota

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
api_instance = harbor.QuotaApi(harbor.ApiClient(configuration))
body = harbor.QuotaUpdateReq() # QuotaUpdateReq | The new hard limits for the quota
id = 56 # int | Quota ID

try:
    # Update the specified quota
    api_instance.quotas_id_put(body, id)
except ApiException as e:
    print("Exception when calling QuotaApi->quotas_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuotaUpdateReq**](QuotaUpdateReq.md)| The new hard limits for the quota | 
 **id** | **int**| Quota ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

