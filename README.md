# harbor
These APIs provide services for manipulating Harbor project.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/angeiv/python-harbor.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/angeiv/python-harbor.git`)

Then import the package:
```python
import harbor
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import harbor
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
body = harbor.Label() # Label | The label that added to the artifact. Only the ID property is needed.
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Add label to artifact
    api_instance.add_label(body, project_name, repository_name, reference, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ArtifactApi->add_label: %s\n" % e)
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
_from = '_from_example' # str | The artifact from which the new artifact is copied from, the format should be \"project/repository:tag\" or \"project/repository@digest\".
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Copy artifact
    api_instance.copy_artifact(project_name, repository_name, _from, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ArtifactApi->copy_artifact: %s\n" % e)
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
body = harbor.Tag() # Tag | The JSON object of tag.
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Create tag
    api_instance.create_tag(body, project_name, repository_name, reference, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ArtifactApi->create_tag: %s\n" % e)
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete the specific artifact
    api_instance.delete_artifact(project_name, repository_name, reference, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ArtifactApi->delete_artifact: %s\n" % e)
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
tag_name = 'tag_name_example' # str | The name of the tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Delete tag
    api_instance.delete_tag(project_name, repository_name, reference, tag_name, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ArtifactApi->delete_tag: %s\n" % e)
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
addition = 'addition_example' # str | The type of addition.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Get the addition of the specific artifact
    api_response = api_instance.get_addition(project_name, repository_name, reference, addition, x_request_id=x_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactApi->get_addition: %s\n" % e)
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
with_tag = true # bool | Specify whether the tags are inclued inside the returning artifacts (optional) (default to true)
with_label = false # bool | Specify whether the labels are inclued inside the returning artifacts (optional) (default to false)
with_scan_overview = false # bool | Specify whether the scan overview is inclued inside the returning artifacts (optional) (default to false)
with_signature = false # bool | Specify whether the signature is inclued inside the returning artifacts (optional) (default to false)
with_immutable_status = false # bool | Specify whether the immutable status is inclued inside the tags of the returning artifacts. Only works when setting \"with_tag=true\" (optional) (default to false)

try:
    # Get the specific artifact
    api_response = api_instance.get_artifact(project_name, repository_name, reference, x_request_id=x_request_id, page=page, page_size=page_size, with_tag=with_tag, with_label=with_label, with_scan_overview=with_scan_overview, with_signature=with_signature, with_immutable_status=with_immutable_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactApi->get_artifact: %s\n" % e)
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
with_tag = true # bool | Specify whether the tags are included inside the returning artifacts (optional) (default to true)
with_label = false # bool | Specify whether the labels are included inside the returning artifacts (optional) (default to false)
with_scan_overview = false # bool | Specify whether the scan overview is included inside the returning artifacts (optional) (default to false)
with_signature = false # bool | Specify whether the signature is included inside the tags of the returning artifacts. Only works when setting \"with_tag=true\" (optional) (default to false)
with_immutable_status = false # bool | Specify whether the immutable status is included inside the tags of the returning artifacts. Only works when setting \"with_tag=true\" (optional) (default to false)

try:
    # List artifacts
    api_response = api_instance.list_artifacts(project_name, repository_name, x_request_id=x_request_id, q=q, page=page, page_size=page_size, with_tag=with_tag, with_label=with_label, with_scan_overview=with_scan_overview, with_signature=with_signature, with_immutable_status=with_immutable_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactApi->list_artifacts: %s\n" % e)
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)
q = 'q_example' # str | Query string to query resources. Supported query patterns are \"exact match(k=v)\", \"fuzzy match(k=~v)\", \"range(k=[min~max])\", \"list with union releationship(k={v1 v2 v3})\" and \"list with intersetion relationship(k=(v1 v2 v3))\". The value of range and list can be string(enclosed by \" or '), integer or time(in format \"2020-04-09 02:36:00\"). All of these query patterns should be put in the query string \"q=xxx\" and splitted by \",\". e.g. q=k1=v1,k2=~v2,k3=[min~max] (optional)
page = 1 # int | The page number (optional) (default to 1)
page_size = 10 # int | The size of per page (optional) (default to 10)
with_signature = false # bool | Specify whether the signature is included inside the returning tags (optional) (default to false)
with_immutable_status = false # bool | Specify whether the immutable status is included inside the returning tags (optional) (default to false)

try:
    # List tags
    api_response = api_instance.list_tags(project_name, repository_name, reference, x_request_id=x_request_id, q=q, page=page, page_size=page_size, with_signature=with_signature, with_immutable_status=with_immutable_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactApi->list_tags: %s\n" % e)
# Configure HTTP basic authorization: basic
configuration = harbor.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = harbor.ArtifactApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | The name of the project
repository_name = 'repository_name_example' # str | The name of the repository. If it contains slash, encode it with URL encoding. e.g. a/b -> a%252Fb
reference = 'reference_example' # str | The reference of the artifact, can be digest or tag
label_id = 789 # int | The ID of the label that removed from the artifact.
x_request_id = 'x_request_id_example' # str | An unique ID for the request (optional)

try:
    # Remove label from artifact
    api_instance.remove_label(project_name, repository_name, reference, label_id, x_request_id=x_request_id)
except ApiException as e:
    print("Exception when calling ArtifactApi->remove_label: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/v2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtifactApi* | [**add_label**](docs/ArtifactApi.md#add_label) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/labels | Add label to artifact
*ArtifactApi* | [**copy_artifact**](docs/ArtifactApi.md#copy_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts | Copy artifact
*ArtifactApi* | [**create_tag**](docs/ArtifactApi.md#create_tag) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags | Create tag
*ArtifactApi* | [**delete_artifact**](docs/ArtifactApi.md#delete_artifact) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference} | Delete the specific artifact
*ArtifactApi* | [**delete_tag**](docs/ArtifactApi.md#delete_tag) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags/{tag_name} | Delete tag
*ArtifactApi* | [**get_addition**](docs/ArtifactApi.md#get_addition) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/additions/{addition} | Get the addition of the specific artifact
*ArtifactApi* | [**get_artifact**](docs/ArtifactApi.md#get_artifact) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference} | Get the specific artifact
*ArtifactApi* | [**list_artifacts**](docs/ArtifactApi.md#list_artifacts) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts | List artifacts
*ArtifactApi* | [**list_tags**](docs/ArtifactApi.md#list_tags) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/tags | List tags
*ArtifactApi* | [**remove_label**](docs/ArtifactApi.md#remove_label) | **DELETE** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/labels/{label_id} | Remove label from artifact
*AuditlogApi* | [**list_audit_logs**](docs/AuditlogApi.md#list_audit_logs) | **GET** /audit-logs | Get recent logs of the projects which the user is a member of
*ProjectApi* | [**get_logs**](docs/ProjectApi.md#get_logs) | **GET** /projects/{project_name}/logs | Get recent logs of the projects
*RepositoryApi* | [**delete_repository**](docs/RepositoryApi.md#delete_repository) | **DELETE** /projects/{project_name}/repositories/{repository_name} | Delete repository
*RepositoryApi* | [**get_repository**](docs/RepositoryApi.md#get_repository) | **GET** /projects/{project_name}/repositories/{repository_name} | Get repository
*RepositoryApi* | [**list_repositories**](docs/RepositoryApi.md#list_repositories) | **GET** /projects/{project_name}/repositories | List repositories
*RepositoryApi* | [**update_repository**](docs/RepositoryApi.md#update_repository) | **PUT** /projects/{project_name}/repositories/{repository_name} | Update repository
*ScanApi* | [**get_report_log**](docs/ScanApi.md#get_report_log) | **GET** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan/{report_id}/log | Get the log of the scan report
*ScanApi* | [**scan_artifact**](docs/ScanApi.md#scan_artifact) | **POST** /projects/{project_name}/repositories/{repository_name}/artifacts/{reference}/scan | Scan the artifact

## Documentation For Models

 - [AdditionLink](docs/AdditionLink.md)
 - [AdditionLinks](docs/AdditionLinks.md)
 - [Annotations](docs/Annotations.md)
 - [Artifact](docs/Artifact.md)
 - [AuditLog](docs/AuditLog.md)
 - [Error](docs/Error.md)
 - [Errors](docs/Errors.md)
 - [ExtraAttrs](docs/ExtraAttrs.md)
 - [Label](docs/Label.md)
 - [NativeReportSummary](docs/NativeReportSummary.md)
 - [Platform](docs/Platform.md)
 - [Reference](docs/Reference.md)
 - [Repository](docs/Repository.md)
 - [ScanOverview](docs/ScanOverview.md)
 - [Tag](docs/Tag.md)
 - [VulnerabilitySummary](docs/VulnerabilitySummary.md)

## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author


