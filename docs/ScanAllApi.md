# harbor.ScanAllApi

All URIs are relative to *http://localhost/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scan_all_schedule**](ScanAllApi.md#create_scan_all_schedule) | **POST** /system/scanAll/schedule | Create a schedule or a manual trigger for the scan all job.
[**get_latest_scan_all_metrics**](ScanAllApi.md#get_latest_scan_all_metrics) | **GET** /scans/all/metrics | Get the metrics of the latest scan all process
[**get_latest_scheduled_scan_all_metrics**](ScanAllApi.md#get_latest_scheduled_scan_all_metrics) | **GET** /scans/schedule/metrics | Get the metrics of the latest scheduled scan all process
[**get_scan_all_schedule**](ScanAllApi.md#get_scan_all_schedule) | **GET** /system/scanAll/schedule | Get scan all&#x27;s schedule.
[**update_scan_all_schedule**](ScanAllApi.md#update_scan_all_schedule) | **PUT** /system/scanAll/schedule | Update scan all&#x27;s schedule.

# **create_scan_all_schedule**
> create_scan_all_schedule(body)

Create a schedule or a manual trigger for the scan all job.

This endpoint is for creating a schedule or a manual trigger for the scan all job, which scans all of images in Harbor.

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
api_instance = harbor.ScanAllApi(harbor.ApiClient(configuration))
body = harbor.Schedule() # Schedule | Create a schedule or a manual trigger for the scan all job.

try:
    # Create a schedule or a manual trigger for the scan all job.
    api_instance.create_scan_all_schedule(body)
except ApiException as e:
    print("Exception when calling ScanAllApi->create_scan_all_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Schedule**](Schedule.md)| Create a schedule or a manual trigger for the scan all job. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_scan_all_metrics**
> Stats get_latest_scan_all_metrics()

Get the metrics of the latest scan all process

Get the metrics of the latest scan all process

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
api_instance = harbor.ScanAllApi(harbor.ApiClient(configuration))

try:
    # Get the metrics of the latest scan all process
    api_response = api_instance.get_latest_scan_all_metrics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanAllApi->get_latest_scan_all_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Stats**](Stats.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_scheduled_scan_all_metrics**
> Stats get_latest_scheduled_scan_all_metrics()

Get the metrics of the latest scheduled scan all process

Get the metrics of the latest scheduled scan all process

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
api_instance = harbor.ScanAllApi(harbor.ApiClient(configuration))

try:
    # Get the metrics of the latest scheduled scan all process
    api_response = api_instance.get_latest_scheduled_scan_all_metrics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanAllApi->get_latest_scheduled_scan_all_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Stats**](Stats.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan_all_schedule**
> Schedule get_scan_all_schedule()

Get scan all's schedule.

This endpoint is for getting a schedule for the scan all job, which scans all of images in Harbor.

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
api_instance = harbor.ScanAllApi(harbor.ApiClient(configuration))

try:
    # Get scan all's schedule.
    api_response = api_instance.get_scan_all_schedule()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanAllApi->get_scan_all_schedule: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Schedule**](Schedule.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scan_all_schedule**
> update_scan_all_schedule(body)

Update scan all's schedule.

This endpoint is for updating the schedule of scan all job, which scans all of images in Harbor.

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
api_instance = harbor.ScanAllApi(harbor.ApiClient(configuration))
body = harbor.Schedule() # Schedule | Updates the schedule of scan all job, which scans all of images in Harbor.

try:
    # Update scan all's schedule.
    api_instance.update_scan_all_schedule(body)
except ApiException as e:
    print("Exception when calling ScanAllApi->update_scan_all_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Schedule**](Schedule.md)| Updates the schedule of scan all job, which scans all of images in Harbor. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

