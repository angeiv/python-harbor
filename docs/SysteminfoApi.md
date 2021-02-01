# harbor.SysteminfoApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systeminfo_get**](SysteminfoApi.md#systeminfo_get) | **GET** /systeminfo | Get general system info
[**systeminfo_getcert_get**](SysteminfoApi.md#systeminfo_getcert_get) | **GET** /systeminfo/getcert | Get default root certificate.
[**systeminfo_volumes_get**](SysteminfoApi.md#systeminfo_volumes_get) | **GET** /systeminfo/volumes | Get system volume info (total/free size).

# **systeminfo_get**
> GeneralInfo systeminfo_get()

Get general system info

This API is for retrieving general system info, this can be called by anonymous request.  Some attributes will be omitted in the response when this API is called by anonymous request. 

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
api_instance = harbor.SysteminfoApi(harbor.ApiClient(configuration))

try:
    # Get general system info
    api_response = api_instance.systeminfo_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SysteminfoApi->systeminfo_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralInfo**](GeneralInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_getcert_get**
> str systeminfo_getcert_get()

Get default root certificate.

This endpoint is for downloading a default root certificate. 

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
api_instance = harbor.SysteminfoApi(harbor.ApiClient(configuration))

try:
    # Get default root certificate.
    api_response = api_instance.systeminfo_getcert_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SysteminfoApi->systeminfo_getcert_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_volumes_get**
> SystemInfo systeminfo_volumes_get()

Get system volume info (total/free size).

This endpoint is for retrieving system volume info that only provides for admin user.  Note that the response only reflects the storage status of local disk. 

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
api_instance = harbor.SysteminfoApi(harbor.ApiClient(configuration))

try:
    # Get system volume info (total/free size).
    api_response = api_instance.systeminfo_volumes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SysteminfoApi->systeminfo_volumes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

