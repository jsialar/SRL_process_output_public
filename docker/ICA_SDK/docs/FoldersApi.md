# ICA_SDK.FoldersApi

All URIs are relative to *https://use1.platform.illumina.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_folder**](FoldersApi.md#archive_folder) | **POST** /v1/folders/{folderId}:archive | Archive a folder
[**complete_folder_session**](FoldersApi.md#complete_folder_session) | **POST** /v1/folders/{folderId}/sessions/{sessionId}:complete | Complete a folder upload in GDS
[**copy_folder**](FoldersApi.md#copy_folder) | **POST** /v1/folders/{folderId}:copy | Copy a folder
[**create_folder**](FoldersApi.md#create_folder) | **POST** /v1/folders | Create a folder in GDS and receive credentials for upload
[**delete_folder**](FoldersApi.md#delete_folder) | **DELETE** /v1/folders/{folderId} | Deletes a folder by id
[**get_folder**](FoldersApi.md#get_folder) | **GET** /v1/folders/{folderId} | Get information about a folder in GDS.
[**get_folder_job**](FoldersApi.md#get_folder_job) | **GET** /v1/folders/{folderId}/jobs/{jobId} | Get status of a folder job in GDS
[**get_folder_session**](FoldersApi.md#get_folder_session) | **GET** /v1/folders/{folderId}/sessions/{sessionId} | Get status of a folder upload in GDS
[**list_folders**](FoldersApi.md#list_folders) | **GET** /v1/folders | Get a list of folders
[**unarchive_folder**](FoldersApi.md#unarchive_folder) | **POST** /v1/folders/{folderId}:unarchive | Unarchive a folder
[**update_folder**](FoldersApi.md#update_folder) | **PATCH** /v1/folders/{folderId} | Update a folder content or acl


# **archive_folder**
> FolderResponse archive_folder(folder_id, body)

Archive a folder

Archives a folder to a lower storage cost tier.

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be archived.
body = ICA_SDK.FolderArchiveRequest() # FolderArchiveRequest | 

    try:
        # Archive a folder
        api_response = api_instance.archive_folder(folder_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->archive_folder: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be archived.
body = ICA_SDK.FolderArchiveRequest() # FolderArchiveRequest | 

    try:
        # Archive a folder
        api_response = api_instance.archive_folder(folder_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->archive_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Unique identifier for the folder to be archived. | 
 **body** | [**FolderArchiveRequest**](FolderArchiveRequest.md)|  | 

### Return type

[**FolderResponse**](FolderResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Folder not found. |  -  |
**409** | Conflict. |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_folder_session**
> SessionResponse complete_folder_session(folder_id, session_id, body)

Complete a folder upload in GDS

Complete a folder upload in GDS.

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder related to the upload session.
session_id = 'session_id_example' # str | The id of the upload session
body = ICA_SDK.CompleteSessionRequest() # CompleteSessionRequest | The request body

    try:
        # Complete a folder upload in GDS
        api_response = api_instance.complete_folder_session(folder_id, session_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->complete_folder_session: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder related to the upload session.
session_id = 'session_id_example' # str | The id of the upload session
body = ICA_SDK.CompleteSessionRequest() # CompleteSessionRequest | The request body

    try:
        # Complete a folder upload in GDS
        api_response = api_instance.complete_folder_session(folder_id, session_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->complete_folder_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Unique identifier for the folder related to the upload session. | 
 **session_id** | **str**| The id of the upload session | 
 **body** | [**CompleteSessionRequest**](CompleteSessionRequest.md)| The request body | 

### Return type

[**SessionResponse**](SessionResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Completed upload session. |  -  |
**202** | Upload session in progress. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**409** | Conflict |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_folder**
> JobResponse copy_folder(folder_id, body, tenant_id=tenant_id)

Copy a folder

Copy a folder into a target parent folder

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be copied.
body = ICA_SDK.FolderCopyRequest() # FolderCopyRequest | 
tenant_id = 'tenant_id_example' # str | Optional parameter to copy from a shared folder in another tenant (optional)

    try:
        # Copy a folder
        api_response = api_instance.copy_folder(folder_id, body, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->copy_folder: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be copied.
body = ICA_SDK.FolderCopyRequest() # FolderCopyRequest | 
tenant_id = 'tenant_id_example' # str | Optional parameter to copy from a shared folder in another tenant (optional)

    try:
        # Copy a folder
        api_response = api_instance.copy_folder(folder_id, body, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->copy_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Unique identifier for the folder to be copied. | 
 **body** | [**FolderCopyRequest**](FolderCopyRequest.md)|  | 
 **tenant_id** | **str**| Optional parameter to copy from a shared folder in another tenant | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Folder not found. |  -  |
**409** | Conflict. |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> FolderWriteableResponse create_folder(body, include=include)

Create a folder in GDS and receive credentials for upload

Create a folder entry in GDS. Returns temporary credentials for folder upload directly to S3 when the include=objectStoreAccess parameter is used. Volume ID or volume name is required for folder creation. If a folder path is provided and does not exist, GDS automatically creates the folder path in the appropriate account.

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    body = ICA_SDK.CreateFolderRequest() # CreateFolderRequest | 
include = 'include_example' # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)

    try:
        # Create a folder in GDS and receive credentials for upload
        api_response = api_instance.create_folder(body, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->create_folder: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    body = ICA_SDK.CreateFolderRequest() # CreateFolderRequest | 
include = 'include_example' # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)

    try:
        # Create a folder in GDS and receive credentials for upload
        api_response = api_instance.create_folder(body, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFolderRequest**](CreateFolderRequest.md)|  | 
 **include** | **str**| Optionally include additional fields in the response.              Possible values: ObjectStoreAccess | [optional] 

### Return type

[**FolderWriteableResponse**](FolderWriteableResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created new Folder. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**409** | A conflict was found. Make sure the new Folder doesn&#39;t already exist. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> FolderResponse delete_folder(folder_id)

Deletes a folder by id

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be deleted.

    try:
        # Deletes a folder by id
        api_response = api_instance.delete_folder(folder_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->delete_folder: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be deleted.

    try:
        # Deletes a folder by id
        api_response = api_instance.delete_folder(folder_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Unique identifier for the folder to be deleted. | 

### Return type

[**FolderResponse**](FolderResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Folder not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> FolderResponse get_folder(folder_id, tenant_id=tenant_id, include_volume_metadata=include_volume_metadata, metadata_include=metadata_include, metadata_exclude=metadata_exclude)

Get information about a folder in GDS.

Get information for the specified folder ID.

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to retrieve.
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)
include_volume_metadata = True # bool | Optional parameter to return volume's metadata (optional)
metadata_include = 'metadata_include_example' # str | Optional parameter to specify comma separated patterns to include metadata by their field names. (optional)
metadata_exclude = 'metadata_exclude_example' # str | Optional parameter to specify comma separated patterns to exclude metadata by their field names. (optional)

    try:
        # Get information about a folder in GDS.
        api_response = api_instance.get_folder(folder_id, tenant_id=tenant_id, include_volume_metadata=include_volume_metadata, metadata_include=metadata_include, metadata_exclude=metadata_exclude)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->get_folder: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to retrieve.
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)
include_volume_metadata = True # bool | Optional parameter to return volume's metadata (optional)
metadata_include = 'metadata_include_example' # str | Optional parameter to specify comma separated patterns to include metadata by their field names. (optional)
metadata_exclude = 'metadata_exclude_example' # str | Optional parameter to specify comma separated patterns to exclude metadata by their field names. (optional)

    try:
        # Get information about a folder in GDS.
        api_response = api_instance.get_folder(folder_id, tenant_id=tenant_id, include_volume_metadata=include_volume_metadata, metadata_include=metadata_include, metadata_exclude=metadata_exclude)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Unique identifier for the folder to retrieve. | 
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional] 
 **include_volume_metadata** | **bool**| Optional parameter to return volume&#39;s metadata | [optional] 
 **metadata_include** | **str**| Optional parameter to specify comma separated patterns to include metadata by their field names. | [optional] 
 **metadata_exclude** | **str**| Optional parameter to specify comma separated patterns to exclude metadata by their field names. | [optional] 

### Return type

[**FolderResponse**](FolderResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Folder not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_job**
> JobResponse get_folder_job(folder_id, job_id)

Get status of a folder job in GDS

Get status of a folder job in GDS.

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder related to the job.
job_id = 'job_id_example' # str | The id of the job

    try:
        # Get status of a folder job in GDS
        api_response = api_instance.get_folder_job(folder_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->get_folder_job: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder related to the job.
job_id = 'job_id_example' # str | The id of the job

    try:
        # Get status of a folder job in GDS
        api_response = api_instance.get_folder_job(folder_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->get_folder_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Unique identifier for the folder related to the job. | 
 **job_id** | **str**| The id of the job | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned job. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**409** | Conflict |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_session**
> SessionResponse get_folder_session(folder_id, session_id)

Get status of a folder upload in GDS

Get status of a folder upload in GDS.

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder related to the upload session.
session_id = 'session_id_example' # str | The id of the upload session

    try:
        # Get status of a folder upload in GDS
        api_response = api_instance.get_folder_session(folder_id, session_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->get_folder_session: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder related to the upload session.
session_id = 'session_id_example' # str | The id of the upload session

    try:
        # Get status of a folder upload in GDS
        api_response = api_instance.get_folder_session(folder_id, session_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->get_folder_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Unique identifier for the folder related to the upload session. | 
 **session_id** | **str**| The id of the upload session | 

### Return type

[**SessionResponse**](SessionResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Completed upload session. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**409** | Conflict |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_folders**
> FolderListResponse list_folders(volume_id=volume_id, volume_name=volume_name, path=path, job_statuses=job_statuses, acls=acls, recursive=recursive, page_size=page_size, page_token=page_token, include=include, tenant_id=tenant_id, metadata_include=metadata_include, metadata_exclude=metadata_exclude)

Get a list of folders

Given a volumeId or volume name, get a list of folders accessible by the JWT. The default sort returned is alphabetical, ascending. The default page size is 10 items

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    volume_id = ['volume_id_example'] # list[str] | Optional field that specifies comma-separated volume IDs to include in the list (optional)
volume_name = ['volume_name_example'] # list[str] | Optional field that specifies comma-separated volume names to include in the list (optional)
path = ['path_example'] # list[str] | Optional field that specifies comma-separated paths to include in the list. Value can use wildcards (e.g. /a/b/c/*) or exact matches (e.g. /a/b/c/d/). (optional)
job_statuses = 'job_statuses_example' # str | Optional field that specifies comma-separated JobStatuses to include in the list (optional)
acls = ['acls_example'] # list[str] | Optional field that specifies comma-separated acls to include in the list (optional)
recursive = True # bool | Optional field to specify if folders should be returned recursively in and under the specified paths, or only directly in the specified paths (optional)
page_size = 56 # int | START_DESC END_DESC (optional)
page_token = 'page_token_example' # str | START_DESC END_DESC (optional)
include = 'include_example' # str | Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, InheritedAcl (optional)
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)
metadata_include = 'metadata_include_example' # str | Optional parameter to specify comma separated patterns to include metadata by their field names. (optional)
metadata_exclude = 'metadata_exclude_example' # str | Optional parameter to specify comma separated patterns to exclude metadata by their field names. (optional)

    try:
        # Get a list of folders
        api_response = api_instance.list_folders(volume_id=volume_id, volume_name=volume_name, path=path, job_statuses=job_statuses, acls=acls, recursive=recursive, page_size=page_size, page_token=page_token, include=include, tenant_id=tenant_id, metadata_include=metadata_include, metadata_exclude=metadata_exclude)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->list_folders: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    volume_id = ['volume_id_example'] # list[str] | Optional field that specifies comma-separated volume IDs to include in the list (optional)
volume_name = ['volume_name_example'] # list[str] | Optional field that specifies comma-separated volume names to include in the list (optional)
path = ['path_example'] # list[str] | Optional field that specifies comma-separated paths to include in the list. Value can use wildcards (e.g. /a/b/c/*) or exact matches (e.g. /a/b/c/d/). (optional)
job_statuses = 'job_statuses_example' # str | Optional field that specifies comma-separated JobStatuses to include in the list (optional)
acls = ['acls_example'] # list[str] | Optional field that specifies comma-separated acls to include in the list (optional)
recursive = True # bool | Optional field to specify if folders should be returned recursively in and under the specified paths, or only directly in the specified paths (optional)
page_size = 56 # int | START_DESC END_DESC (optional)
page_token = 'page_token_example' # str | START_DESC END_DESC (optional)
include = 'include_example' # str | Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, InheritedAcl (optional)
tenant_id = 'tenant_id_example' # str | Optional parameter to see shared data in another tenant (optional)
metadata_include = 'metadata_include_example' # str | Optional parameter to specify comma separated patterns to include metadata by their field names. (optional)
metadata_exclude = 'metadata_exclude_example' # str | Optional parameter to specify comma separated patterns to exclude metadata by their field names. (optional)

    try:
        # Get a list of folders
        api_response = api_instance.list_folders(volume_id=volume_id, volume_name=volume_name, path=path, job_statuses=job_statuses, acls=acls, recursive=recursive, page_size=page_size, page_token=page_token, include=include, tenant_id=tenant_id, metadata_include=metadata_include, metadata_exclude=metadata_exclude)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->list_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | [**list[str]**](str.md)| Optional field that specifies comma-separated volume IDs to include in the list | [optional] 
 **volume_name** | [**list[str]**](str.md)| Optional field that specifies comma-separated volume names to include in the list | [optional] 
 **path** | [**list[str]**](str.md)| Optional field that specifies comma-separated paths to include in the list. Value can use wildcards (e.g. /a/b/c/*) or exact matches (e.g. /a/b/c/d/). | [optional] 
 **job_statuses** | **str**| Optional field that specifies comma-separated JobStatuses to include in the list | [optional] 
 **acls** | [**list[str]**](str.md)| Optional field that specifies comma-separated acls to include in the list | [optional] 
 **recursive** | **bool**| Optional field to specify if folders should be returned recursively in and under the specified paths, or only directly in the specified paths | [optional] 
 **page_size** | **int**| START_DESC END_DESC | [optional] 
 **page_token** | **str**| START_DESC END_DESC | [optional] 
 **include** | **str**| Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, InheritedAcl | [optional] 
 **tenant_id** | **str**| Optional parameter to see shared data in another tenant | [optional] 
 **metadata_include** | **str**| Optional parameter to specify comma separated patterns to include metadata by their field names. | [optional] 
 **metadata_exclude** | **str**| Optional parameter to specify comma separated patterns to exclude metadata by their field names. | [optional] 

### Return type

[**FolderListResponse**](FolderListResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_folder**
> FolderResponse unarchive_folder(folder_id, body)

Unarchive a folder

Unarchive a folder from a lower storage cost tier.

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be unarchived.
body = ICA_SDK.FolderUnarchiveRequest() # FolderUnarchiveRequest | 

    try:
        # Unarchive a folder
        api_response = api_instance.unarchive_folder(folder_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->unarchive_folder: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be unarchived.
body = ICA_SDK.FolderUnarchiveRequest() # FolderUnarchiveRequest | 

    try:
        # Unarchive a folder
        api_response = api_instance.unarchive_folder(folder_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->unarchive_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Unique identifier for the folder to be unarchived. | 
 **body** | [**FolderUnarchiveRequest**](FolderUnarchiveRequest.md)|  | 

### Return type

[**FolderResponse**](FolderResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Folder not found. |  -  |
**409** | Conflict. |  -  |
**500** | Server Error |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> FolderWriteableResponse update_folder(folder_id, include=include, body=body)

Update a folder content or acl

Update an existing folder in GDS and return upload credentials for that folder. Changes to the folder name and other metadata are not supported at this time.  Optionally overwrite the acl for this folder if acl is provided in the request.

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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be updated.
include = 'include_example' # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)
body = ICA_SDK.FolderUpdateRequest() # FolderUpdateRequest |  (optional)

    try:
        # Update a folder content or acl
        api_response = api_instance.update_folder(folder_id, include=include, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->update_folder: %s\n" % e)
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
    api_instance = ICA_SDK.FoldersApi(api_client)
    folder_id = 'folder_id_example' # str | Unique identifier for the folder to be updated.
include = 'include_example' # str | Optionally include additional fields in the response.              Possible values: ObjectStoreAccess (optional)
body = ICA_SDK.FolderUpdateRequest() # FolderUpdateRequest |  (optional)

    try:
        # Update a folder content or acl
        api_response = api_instance.update_folder(folder_id, include=include, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FoldersApi->update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Unique identifier for the folder to be updated. | 
 **include** | **str**| Optionally include additional fields in the response.              Possible values: ObjectStoreAccess | [optional] 
 **body** | [**FolderUpdateRequest**](FolderUpdateRequest.md)|  | [optional] 

### Return type

[**FolderWriteableResponse**](FolderWriteableResponse.md)

### Authorization

[Basic](../README.md#Basic), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Folder not found. |  -  |
**0** | Unexpected issue. Please try your request again. If problem persists, please contact the system administrator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

