# harbor.ScannersApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_scanner_candidates_get**](ScannersApi.md#projects_project_id_scanner_candidates_get) | **GET** /projects/{project_id}/scanner/candidates | Get scanner registration candidates for configurating project level scanner
[**projects_project_id_scanner_get**](ScannersApi.md#projects_project_id_scanner_get) | **GET** /projects/{project_id}/scanner | Get project level scanner
[**projects_project_id_scanner_put**](ScannersApi.md#projects_project_id_scanner_put) | **PUT** /projects/{project_id}/scanner | Configure scanner for the specified project
[**scanners_get**](ScannersApi.md#scanners_get) | **GET** /scanners | List scanner registrations
[**scanners_ping_post**](ScannersApi.md#scanners_ping_post) | **POST** /scanners/ping | Tests scanner registration settings
[**scanners_post**](ScannersApi.md#scanners_post) | **POST** /scanners | Create a scanner registration
[**scanners_registration_id_delete**](ScannersApi.md#scanners_registration_id_delete) | **DELETE** /scanners/{registration_id} | Delete a scanner registration
[**scanners_registration_id_get**](ScannersApi.md#scanners_registration_id_get) | **GET** /scanners/{registration_id} | Get a scanner registration details
[**scanners_registration_id_metadata_get**](ScannersApi.md#scanners_registration_id_metadata_get) | **GET** /scanners/{registration_id}/metadata | Get the metadata of the specified scanner registration
[**scanners_registration_id_patch**](ScannersApi.md#scanners_registration_id_patch) | **PATCH** /scanners/{registration_id} | Set system default scanner registration
[**scanners_registration_id_put**](ScannersApi.md#scanners_registration_id_put) | **PUT** /scanners/{registration_id} | Update a scanner registration

# **projects_project_id_scanner_candidates_get**
> list[ScannerRegistration] projects_project_id_scanner_candidates_get(project_id)

Get scanner registration candidates for configurating project level scanner

Retrieve the system configured scanner registrations as candidates of setting project level scanner. 

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
project_id = 789 # int | The project identifier.

try:
    # Get scanner registration candidates for configurating project level scanner
    api_response = api_instance.projects_project_id_scanner_candidates_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannersApi->projects_project_id_scanner_candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project identifier. | 

### Return type

[**list[ScannerRegistration]**](ScannerRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_scanner_get**
> ScannerRegistration projects_project_id_scanner_get(project_id)

Get project level scanner

Get the scanner registration of the specified project. If no scanner registration is configured for the specified project, the system default scanner registration will be returned.

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
project_id = 789 # int | The project identifier.

try:
    # Get project level scanner
    api_response = api_instance.projects_project_id_scanner_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannersApi->projects_project_id_scanner_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project identifier. | 

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_scanner_put**
> projects_project_id_scanner_put(body, project_id)

Configure scanner for the specified project

Set one of the system configured scanner registration as the indepndent scanner of the specified project.

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
body = harbor.ProjectScanner() # ProjectScanner | 
project_id = 789 # int | The project identifier.

try:
    # Configure scanner for the specified project
    api_instance.projects_project_id_scanner_put(body, project_id)
except ApiException as e:
    print("Exception when calling ScannersApi->projects_project_id_scanner_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectScanner**](ProjectScanner.md)|  | 
 **project_id** | **int**| The project identifier. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_get**
> list[ScannerRegistration] scanners_get()

List scanner registrations

Returns a list of currently configured scanner registrations. 

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))

try:
    # List scanner registrations
    api_response = api_instance.scanners_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannersApi->scanners_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ScannerRegistration]**](ScannerRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_ping_post**
> scanners_ping_post(body)

Tests scanner registration settings

Pings scanner adapter to test endpoint URL and authorization settings. 

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
body = harbor.ScannerRegistrationSettings() # ScannerRegistrationSettings | A scanner registration settings to be tested.

try:
    # Tests scanner registration settings
    api_instance.scanners_ping_post(body)
except ApiException as e:
    print("Exception when calling ScannersApi->scanners_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScannerRegistrationSettings**](ScannerRegistrationSettings.md)| A scanner registration settings to be tested. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_post**
> scanners_post(body)

Create a scanner registration

Creats a new scanner registration with the given data. 

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
body = harbor.ScannerRegistrationReq() # ScannerRegistrationReq | A scanner registration to be created.

try:
    # Create a scanner registration
    api_instance.scanners_post(body)
except ApiException as e:
    print("Exception when calling ScannersApi->scanners_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScannerRegistrationReq**](ScannerRegistrationReq.md)| A scanner registration to be created. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_registration_id_delete**
> ScannerRegistration scanners_registration_id_delete(registration_id)

Delete a scanner registration

Deletes the specified scanner registration. 

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifier.

try:
    # Delete a scanner registration
    api_response = api_instance.scanners_registration_id_delete(registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannersApi->scanners_registration_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. | 

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_registration_id_get**
> ScannerRegistration scanners_registration_id_get(registration_id)

Get a scanner registration details

Retruns the details of the specified scanner registration. 

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifer.

try:
    # Get a scanner registration details
    api_response = api_instance.scanners_registration_id_get(registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannersApi->scanners_registration_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifer. | 

### Return type

[**ScannerRegistration**](ScannerRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_registration_id_metadata_get**
> ScannerAdapterMetadata scanners_registration_id_metadata_get(registration_id)

Get the metadata of the specified scanner registration

Get the metadata of the specified scanner registration, including the capabilities and customzied properties. 

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifier.

try:
    # Get the metadata of the specified scanner registration
    api_response = api_instance.scanners_registration_id_metadata_get(registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScannersApi->scanners_registration_id_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| The scanner registration identifier. | 

### Return type

[**ScannerAdapterMetadata**](ScannerAdapterMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_registration_id_patch**
> scanners_registration_id_patch(body, registration_id)

Set system default scanner registration

Set the specified scanner registration as the system default one. 

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
body = harbor.IsDefault() # IsDefault | 
registration_id = 'registration_id_example' # str | The scanner registration identifier.

try:
    # Set system default scanner registration
    api_instance.scanners_registration_id_patch(body, registration_id)
except ApiException as e:
    print("Exception when calling ScannersApi->scanners_registration_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IsDefault**](IsDefault.md)|  | 
 **registration_id** | **str**| The scanner registration identifier. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scanners_registration_id_put**
> scanners_registration_id_put(body, registration_id)

Update a scanner registration

Updates the specified scanner registration. 

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
api_instance = harbor.ScannersApi(harbor.ApiClient(configuration))
body = harbor.ScannerRegistrationReq() # ScannerRegistrationReq | A scanner registraiton to be updated.
registration_id = 'registration_id_example' # str | The scanner registration identifier.

try:
    # Update a scanner registration
    api_instance.scanners_registration_id_put(body, registration_id)
except ApiException as e:
    print("Exception when calling ScannersApi->scanners_registration_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScannerRegistrationReq**](ScannerRegistrationReq.md)| A scanner registraiton to be updated. | 
 **registration_id** | **str**| The scanner registration identifier. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

