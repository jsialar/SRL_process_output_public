# ICA_SDK.UsagesApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage**](UsagesApi.md#get_usage) | **GET** /v1/usages | Get current tenant&#39;s usage detail by period.  Default returns current period usage data. 
[**get_usage_details**](UsagesApi.md#get_usage_details) | **GET** /v1/usages/details | Get current tenant&#39;s usage detail by period.  Default returns current period usage data. 
[**get_usage_periods**](UsagesApi.md#get_usage_periods) | **GET** /v1/usages/periods | Get periods detail info 


# **get_usage**
> UsageResponse get_usage(periods=periods)

Get current tenant's usage detail by period.  Default returns current period usage data. 

This endpoint provides the ability for the user to get the aggregated usage data

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.UsagesApi(api_client)
    periods = 56 # int |  (optional)

    try:
        # Get current tenant's usage detail by period.  Default returns current period usage data. 
        api_response = api_instance.get_usage(periods=periods)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsagesApi->get_usage: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.UsagesApi(api_client)
    periods = 56 # int |  (optional)

    try:
        # Get current tenant's usage detail by period.  Default returns current period usage data. 
        api_response = api_instance.get_usage(periods=periods)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsagesApi->get_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **periods** | **int**|  | [optional] 

### Return type

[**UsageResponse**](UsageResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The usages are returned successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to subscribe to the given event type or deliver to the given delivery target. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_details**
> UsageResponse get_usage_details(period_id=period_id)

Get current tenant's usage detail by period.  Default returns current period usage data. 

This endpoint provides the billing details for specified period id. Summarize each compute usage and daily gds usage

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.UsagesApi(api_client)
    period_id = 56 # int |  (optional)

    try:
        # Get current tenant's usage detail by period.  Default returns current period usage data. 
        api_response = api_instance.get_usage_details(period_id=period_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsagesApi->get_usage_details: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.UsagesApi(api_client)
    period_id = 56 # int |  (optional)

    try:
        # Get current tenant's usage detail by period.  Default returns current period usage data. 
        api_response = api_instance.get_usage_details(period_id=period_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsagesApi->get_usage_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_id** | **int**|  | [optional] 

### Return type

[**UsageResponse**](UsageResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The usages are returned successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to subscribe to the given event type or deliver to the given delivery target. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_periods**
> UsageResponse get_usage_periods(limit=limit)

Get periods detail info 

This endpoint provides the periods details

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.UsagesApi(api_client)
    limit = 26 # int |  (optional) (default to 26)

    try:
        # Get periods detail info 
        api_response = api_instance.get_usage_periods(limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsagesApi->get_usage_periods: %s\n" % e)
```

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import ICA_SDK
from ICA_SDK.rest import ApiException
from pprint import pprint
configuration = ICA_SDK.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = ICA_SDK.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://use1.platform.illumina.com
configuration.host = "https://use1.platform.illumina.com"

# Enter a context with an instance of the API client
with ICA_SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ICA_SDK.UsagesApi(api_client)
    limit = 26 # int |  (optional) (default to 26)

    try:
        # Get periods detail info 
        api_response = api_instance.get_usage_periods(limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsagesApi->get_usage_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 26]

### Return type

[**UsageResponse**](UsageResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The periods are returned successfully. |  -  |
**400** | An invalid or missing input parameter will result in a bad request. |  -  |
**401** | The acting identity cannot be authenticated and authorized. |  -  |
**403** | The acting identity is not authorized to subscribe to the given event type or deliver to the given delivery target. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

