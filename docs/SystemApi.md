# harbor.SystemApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_cve_whitelist_get**](SystemApi.md#system_cve_whitelist_get) | **GET** /system/CVEWhitelist | Get the system level whitelist of CVE.
[**system_cve_whitelist_put**](SystemApi.md#system_cve_whitelist_put) | **PUT** /system/CVEWhitelist | Update the system level whitelist of CVE.
[**system_oidc_ping_post**](SystemApi.md#system_oidc_ping_post) | **POST** /system/oidc/ping | Test the OIDC endpoint.

# **system_cve_whitelist_get**
> CVEWhitelist system_cve_whitelist_get()

Get the system level whitelist of CVE.

Get the system level whitelist of CVE.  This API can be called by all authenticated users.

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
api_instance = harbor.SystemApi(harbor.ApiClient(configuration))

try:
    # Get the system level whitelist of CVE.
    api_response = api_instance.system_cve_whitelist_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_cve_whitelist_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CVEWhitelist**](CVEWhitelist.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_cve_whitelist_put**
> system_cve_whitelist_put(body=body)

Update the system level whitelist of CVE.

This API overwrites the system level whitelist of CVE with the list in request body.  Only system Admin has permission to call this API.

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
api_instance = harbor.SystemApi(harbor.ApiClient(configuration))
body = harbor.CVEWhitelist() # CVEWhitelist | The whitelist with new content (optional)

try:
    # Update the system level whitelist of CVE.
    api_instance.system_cve_whitelist_put(body=body)
except ApiException as e:
    print("Exception when calling SystemApi->system_cve_whitelist_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CVEWhitelist**](CVEWhitelist.md)| The whitelist with new content | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_oidc_ping_post**
> system_oidc_ping_post(body)

Test the OIDC endpoint.

Test the OIDC endpoint, the setting of the endpoint is provided in the request.  This API can only be called by system admin.

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
api_instance = harbor.SystemApi(harbor.ApiClient(configuration))
body = harbor.Body4() # Body4 | Request body for OIDC endpoint to be tested.

try:
    # Test the OIDC endpoint.
    api_instance.system_oidc_ping_post(body)
except ApiException as e:
    print("Exception when calling SystemApi->system_oidc_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)| Request body for OIDC endpoint to be tested. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

