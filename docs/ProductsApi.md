# harbor.ProductsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartrepo_charts_post**](ProductsApi.md#chartrepo_charts_post) | **POST** /chartrepo/charts | Upload a chart file to the defult &#x27;library&#x27; project.
[**chartrepo_health_get**](ProductsApi.md#chartrepo_health_get) | **GET** /chartrepo/health | Check the health of chart repository service.
[**chartrepo_repo_charts_get**](ProductsApi.md#chartrepo_repo_charts_get) | **GET** /chartrepo/{repo}/charts | Get all the charts under the specified project
[**chartrepo_repo_charts_name_delete**](ProductsApi.md#chartrepo_repo_charts_name_delete) | **DELETE** /chartrepo/{repo}/charts/{name} | Delete all the versions of the specified chart
[**chartrepo_repo_charts_name_get**](ProductsApi.md#chartrepo_repo_charts_name_get) | **GET** /chartrepo/{repo}/charts/{name} | Get all the versions of the specified chart
[**chartrepo_repo_charts_name_version_delete**](ProductsApi.md#chartrepo_repo_charts_name_version_delete) | **DELETE** /chartrepo/{repo}/charts/{name}/{version} | Delete the specified chart version
[**chartrepo_repo_charts_name_version_get**](ProductsApi.md#chartrepo_repo_charts_name_version_get) | **GET** /chartrepo/{repo}/charts/{name}/{version} | Get the specified chart version
[**chartrepo_repo_charts_name_version_labels_get**](ProductsApi.md#chartrepo_repo_charts_name_version_labels_get) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
[**chartrepo_repo_charts_name_version_labels_id_delete**](ProductsApi.md#chartrepo_repo_charts_name_version_labels_id_delete) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
[**chartrepo_repo_charts_name_version_labels_post**](ProductsApi.md#chartrepo_repo_charts_name_version_labels_post) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
[**chartrepo_repo_charts_post**](ProductsApi.md#chartrepo_repo_charts_post) | **POST** /chartrepo/{repo}/charts | Upload a chart file to the specified project.
[**chartrepo_repo_prov_post**](ProductsApi.md#chartrepo_repo_prov_post) | **POST** /chartrepo/{repo}/prov | Upload a provance file to the specified project.
[**configurations_get**](ProductsApi.md#configurations_get) | **GET** /configurations | Get system configurations.
[**configurations_put**](ProductsApi.md#configurations_put) | **PUT** /configurations | Modify system configurations.
[**email_ping_post**](ProductsApi.md#email_ping_post) | **POST** /email/ping | Test connection and authentication with email server.
[**health_get**](ProductsApi.md#health_get) | **GET** /health | Health check API
[**internal_switchquota_put**](ProductsApi.md#internal_switchquota_put) | **PUT** /internal/switchquota | Enable or disable quota.
[**internal_syncquota_post**](ProductsApi.md#internal_syncquota_post) | **POST** /internal/syncquota | Sync quota from registry/chart to DB.
[**internal_syncregistry_post**](ProductsApi.md#internal_syncregistry_post) | **POST** /internal/syncregistry | Sync repositories from registry to DB.
[**labels_get**](ProductsApi.md#labels_get) | **GET** /labels | List labels according to the query strings.
[**labels_id_delete**](ProductsApi.md#labels_id_delete) | **DELETE** /labels/{id} | Delete the label specified by ID.
[**labels_id_get**](ProductsApi.md#labels_id_get) | **GET** /labels/{id} | Get the label specified by ID.
[**labels_id_put**](ProductsApi.md#labels_id_put) | **PUT** /labels/{id} | Update the label properties.
[**labels_id_resources_get**](ProductsApi.md#labels_id_resources_get) | **GET** /labels/{id}/resources | Get the resources that the label is referenced by.
[**labels_post**](ProductsApi.md#labels_post) | **POST** /labels | Post creates a label
[**ldap_groups_search_get**](ProductsApi.md#ldap_groups_search_get) | **GET** /ldap/groups/search | Search available ldap groups.
[**ldap_ping_post**](ProductsApi.md#ldap_ping_post) | **POST** /ldap/ping | Ping available ldap service.
[**ldap_users_import_post**](ProductsApi.md#ldap_users_import_post) | **POST** /ldap/users/import | Import selected available ldap users.
[**ldap_users_search_get**](ProductsApi.md#ldap_users_search_get) | **GET** /ldap/users/search | Search available ldap users.
[**logs_get**](ProductsApi.md#logs_get) | **GET** /logs | Get recent logs of the projects which the user is a member of
[**projects_get**](ProductsApi.md#projects_get) | **GET** /projects | List projects
[**projects_head**](ProductsApi.md#projects_head) | **HEAD** /projects | Check if the project name user provided already exists.
[**projects_post**](ProductsApi.md#projects_post) | **POST** /projects | Create a new project.
[**projects_project_id_delete**](ProductsApi.md#projects_project_id_delete) | **DELETE** /projects/{project_id} | Delete project by projectID
[**projects_project_id_get**](ProductsApi.md#projects_project_id_get) | **GET** /projects/{project_id} | Return specific project detail information
[**projects_project_id_immutabletagrules_get**](ProductsApi.md#projects_project_id_immutabletagrules_get) | **GET** /projects/{project_id}/immutabletagrules | List all immutable tag rules of current project
[**projects_project_id_immutabletagrules_id_delete**](ProductsApi.md#projects_project_id_immutabletagrules_id_delete) | **DELETE** /projects/{project_id}/immutabletagrules/{id} | Delete the immutable tag rule.
[**projects_project_id_immutabletagrules_id_put**](ProductsApi.md#projects_project_id_immutabletagrules_id_put) | **PUT** /projects/{project_id}/immutabletagrules/{id} | Update the immutable tag rule or enable or disable the rule
[**projects_project_id_immutabletagrules_post**](ProductsApi.md#projects_project_id_immutabletagrules_post) | **POST** /projects/{project_id}/immutabletagrules | Add an immutable tag rule to current project
[**projects_project_id_logs_get**](ProductsApi.md#projects_project_id_logs_get) | **GET** /projects/{project_id}/logs | Get access logs accompany with a relevant project.
[**projects_project_id_members_get**](ProductsApi.md#projects_project_id_members_get) | **GET** /projects/{project_id}/members | Get all project member information
[**projects_project_id_members_mid_delete**](ProductsApi.md#projects_project_id_members_mid_delete) | **DELETE** /projects/{project_id}/members/{mid} | Delete project member
[**projects_project_id_members_mid_get**](ProductsApi.md#projects_project_id_members_mid_get) | **GET** /projects/{project_id}/members/{mid} | Get the project member information
[**projects_project_id_members_mid_put**](ProductsApi.md#projects_project_id_members_mid_put) | **PUT** /projects/{project_id}/members/{mid} | Update project member
[**projects_project_id_members_post**](ProductsApi.md#projects_project_id_members_post) | **POST** /projects/{project_id}/members | Create project member
[**projects_project_id_metadatas_get**](ProductsApi.md#projects_project_id_metadatas_get) | **GET** /projects/{project_id}/metadatas | Get project metadata.
[**projects_project_id_metadatas_meta_name_delete**](ProductsApi.md#projects_project_id_metadatas_meta_name_delete) | **DELETE** /projects/{project_id}/metadatas/{meta_name} | Delete metadata of a project
[**projects_project_id_metadatas_meta_name_get**](ProductsApi.md#projects_project_id_metadatas_meta_name_get) | **GET** /projects/{project_id}/metadatas/{meta_name} | Get project metadata
[**projects_project_id_metadatas_meta_name_put**](ProductsApi.md#projects_project_id_metadatas_meta_name_put) | **PUT** /projects/{project_id}/metadatas/{meta_name} | Update metadata of a project.
[**projects_project_id_metadatas_post**](ProductsApi.md#projects_project_id_metadatas_post) | **POST** /projects/{project_id}/metadatas | Add metadata for the project.
[**projects_project_id_put**](ProductsApi.md#projects_project_id_put) | **PUT** /projects/{project_id} | Update properties for a selected project.
[**projects_project_id_robots_get**](ProductsApi.md#projects_project_id_robots_get) | **GET** /projects/{project_id}/robots | Get all robot accounts of specified project
[**projects_project_id_robots_post**](ProductsApi.md#projects_project_id_robots_post) | **POST** /projects/{project_id}/robots | Create a robot account for project
[**projects_project_id_robots_robot_id_delete**](ProductsApi.md#projects_project_id_robots_robot_id_delete) | **DELETE** /projects/{project_id}/robots/{robot_id} | Delete the specified robot account
[**projects_project_id_robots_robot_id_get**](ProductsApi.md#projects_project_id_robots_robot_id_get) | **GET** /projects/{project_id}/robots/{robot_id} | Return the infor of the specified robot account.
[**projects_project_id_robots_robot_id_put**](ProductsApi.md#projects_project_id_robots_robot_id_put) | **PUT** /projects/{project_id}/robots/{robot_id} | Update status of robot account.
[**projects_project_id_scanner_candidates_get**](ProductsApi.md#projects_project_id_scanner_candidates_get) | **GET** /projects/{project_id}/scanner/candidates | Get scanner registration candidates for configurating project level scanner
[**projects_project_id_scanner_get**](ProductsApi.md#projects_project_id_scanner_get) | **GET** /projects/{project_id}/scanner | Get project level scanner
[**projects_project_id_summary_get**](ProductsApi.md#projects_project_id_summary_get) | **GET** /projects/{project_id}/summary | Get summary of the project.
[**projects_project_id_webhook_jobs_get**](ProductsApi.md#projects_project_id_webhook_jobs_get) | **GET** /projects/{project_id}/webhook/jobs | List project webhook jobs
[**projects_project_id_webhook_lasttrigger_get**](ProductsApi.md#projects_project_id_webhook_lasttrigger_get) | **GET** /projects/{project_id}/webhook/lasttrigger | Get project webhook policy last trigger info
[**projects_project_id_webhook_policies_get**](ProductsApi.md#projects_project_id_webhook_policies_get) | **GET** /projects/{project_id}/webhook/policies | List project webhook policies.
[**projects_project_id_webhook_policies_policy_id_delete**](ProductsApi.md#projects_project_id_webhook_policies_policy_id_delete) | **DELETE** /projects/{project_id}/webhook/policies/{policy_id} | Delete webhook policy of a project
[**projects_project_id_webhook_policies_policy_id_get**](ProductsApi.md#projects_project_id_webhook_policies_policy_id_get) | **GET** /projects/{project_id}/webhook/policies/{policy_id} | Get project webhook policy
[**projects_project_id_webhook_policies_policy_id_put**](ProductsApi.md#projects_project_id_webhook_policies_policy_id_put) | **PUT** /projects/{project_id}/webhook/policies/{policy_id} | Update webhook policy of a project.
[**projects_project_id_webhook_policies_post**](ProductsApi.md#projects_project_id_webhook_policies_post) | **POST** /projects/{project_id}/webhook/policies | Create project webhook policy.
[**projects_project_id_webhook_policies_test_post**](ProductsApi.md#projects_project_id_webhook_policies_test_post) | **POST** /projects/{project_id}/webhook/policies/test | Test project webhook connection
[**quotas_get**](ProductsApi.md#quotas_get) | **GET** /quotas | List quotas
[**quotas_id_get**](ProductsApi.md#quotas_id_get) | **GET** /quotas/{id} | Get the specified quota
[**quotas_id_put**](ProductsApi.md#quotas_id_put) | **PUT** /quotas/{id} | Update the specified quota
[**registries_get**](ProductsApi.md#registries_get) | **GET** /registries | List registries.
[**registries_id_delete**](ProductsApi.md#registries_id_delete) | **DELETE** /registries/{id} | Delete specific registry.
[**registries_id_get**](ProductsApi.md#registries_id_get) | **GET** /registries/{id} | Get registry.
[**registries_id_info_get**](ProductsApi.md#registries_id_info_get) | **GET** /registries/{id}/info | Get registry info.
[**registries_id_namespace_get**](ProductsApi.md#registries_id_namespace_get) | **GET** /registries/{id}/namespace | List namespaces of registry
[**registries_id_put**](ProductsApi.md#registries_id_put) | **PUT** /registries/{id} | Update a given registry.
[**registries_ping_post**](ProductsApi.md#registries_ping_post) | **POST** /registries/ping | Ping status of a registry.
[**registries_post**](ProductsApi.md#registries_post) | **POST** /registries | Create a new registry.
[**replication_adapters_get**](ProductsApi.md#replication_adapters_get) | **GET** /replication/adapters | List supported adapters.
[**replication_executions_get**](ProductsApi.md#replication_executions_get) | **GET** /replication/executions | List replication executions.
[**replication_executions_id_get**](ProductsApi.md#replication_executions_id_get) | **GET** /replication/executions/{id} | Get the execution of the replication.
[**replication_executions_id_put**](ProductsApi.md#replication_executions_id_put) | **PUT** /replication/executions/{id} | Stop the execution of the replication.
[**replication_executions_id_tasks_get**](ProductsApi.md#replication_executions_id_tasks_get) | **GET** /replication/executions/{id}/tasks | Get the task list of one execution.
[**replication_executions_id_tasks_task_id_log_get**](ProductsApi.md#replication_executions_id_tasks_task_id_log_get) | **GET** /replication/executions/{id}/tasks/{task_id}/log | Get the log of one task.
[**replication_executions_post**](ProductsApi.md#replication_executions_post) | **POST** /replication/executions | Start one execution of the replication.
[**replication_policies_get**](ProductsApi.md#replication_policies_get) | **GET** /replication/policies | List replication policies
[**replication_policies_id_delete**](ProductsApi.md#replication_policies_id_delete) | **DELETE** /replication/policies/{id} | Delete the replication policy specified by ID.
[**replication_policies_id_get**](ProductsApi.md#replication_policies_id_get) | **GET** /replication/policies/{id} | Get replication policy.
[**replication_policies_id_put**](ProductsApi.md#replication_policies_id_put) | **PUT** /replication/policies/{id} | Update the replication policy
[**replication_policies_post**](ProductsApi.md#replication_policies_post) | **POST** /replication/policies | Create a replication policy
[**repositories_get**](ProductsApi.md#repositories_get) | **GET** /repositories | Get repositories accompany with relevant project and repo name.
[**repositories_repo_name_delete**](ProductsApi.md#repositories_repo_name_delete) | **DELETE** /repositories/{repo_name} | Delete a repository.
[**repositories_repo_name_labels_get**](ProductsApi.md#repositories_repo_name_labels_get) | **GET** /repositories/{repo_name}/labels | Get labels of a repository.
[**repositories_repo_name_labels_label_id_delete**](ProductsApi.md#repositories_repo_name_labels_label_id_delete) | **DELETE** /repositories/{repo_name}/labels/{label_id} | Delete label from the repository.
[**repositories_repo_name_labels_post**](ProductsApi.md#repositories_repo_name_labels_post) | **POST** /repositories/{repo_name}/labels | Add a label to the repository.
[**repositories_repo_name_put**](ProductsApi.md#repositories_repo_name_put) | **PUT** /repositories/{repo_name} | Update description of the repository.
[**repositories_repo_name_signatures_get**](ProductsApi.md#repositories_repo_name_signatures_get) | **GET** /repositories/{repo_name}/signatures | Get signature information of a repository
[**repositories_repo_name_tags_get**](ProductsApi.md#repositories_repo_name_tags_get) | **GET** /repositories/{repo_name}/tags | Get tags of a relevant repository.
[**repositories_repo_name_tags_post**](ProductsApi.md#repositories_repo_name_tags_post) | **POST** /repositories/{repo_name}/tags | Retag an image
[**repositories_repo_name_tags_tag_delete**](ProductsApi.md#repositories_repo_name_tags_tag_delete) | **DELETE** /repositories/{repo_name}/tags/{tag} | Delete a tag in a repository.
[**repositories_repo_name_tags_tag_get**](ProductsApi.md#repositories_repo_name_tags_tag_get) | **GET** /repositories/{repo_name}/tags/{tag} | Get the tag of the repository.
[**repositories_repo_name_tags_tag_labels_get**](ProductsApi.md#repositories_repo_name_tags_tag_labels_get) | **GET** /repositories/{repo_name}/tags/{tag}/labels | Get labels of an image.
[**repositories_repo_name_tags_tag_labels_label_id_delete**](ProductsApi.md#repositories_repo_name_tags_tag_labels_label_id_delete) | **DELETE** /repositories/{repo_name}/tags/{tag}/labels/{label_id} | Delete label from the image.
[**repositories_repo_name_tags_tag_labels_post**](ProductsApi.md#repositories_repo_name_tags_tag_labels_post) | **POST** /repositories/{repo_name}/tags/{tag}/labels | Add a label to image.
[**repositories_repo_name_tags_tag_manifest_get**](ProductsApi.md#repositories_repo_name_tags_tag_manifest_get) | **GET** /repositories/{repo_name}/tags/{tag}/manifest | Get manifests of a relevant repository.
[**repositories_repo_name_tags_tag_scan_post**](ProductsApi.md#repositories_repo_name_tags_tag_scan_post) | **POST** /repositories/{repo_name}/tags/{tag}/scan | Scan the image.
[**repositories_repo_name_tags_tag_scan_uuid_log_get**](ProductsApi.md#repositories_repo_name_tags_tag_scan_uuid_log_get) | **GET** /repositories/{repo_name}/tags/{tag}/scan/{uuid}/log | Get scan log
[**repositories_top_get**](ProductsApi.md#repositories_top_get) | **GET** /repositories/top | Get public repositories which are accessed most.
[**retentions_id_executions_eid_patch**](ProductsApi.md#retentions_id_executions_eid_patch) | **PATCH** /retentions/{id}/executions/{eid} | Stop a Retention job
[**retentions_id_executions_eid_tasks_get**](ProductsApi.md#retentions_id_executions_eid_tasks_get) | **GET** /retentions/{id}/executions/{eid}/tasks | Get Retention job tasks
[**retentions_id_executions_eid_tasks_tid_get**](ProductsApi.md#retentions_id_executions_eid_tasks_tid_get) | **GET** /retentions/{id}/executions/{eid}/tasks/{tid} | Get Retention job task log
[**retentions_id_executions_get**](ProductsApi.md#retentions_id_executions_get) | **GET** /retentions/{id}/executions | Get a Retention job
[**retentions_id_executions_post**](ProductsApi.md#retentions_id_executions_post) | **POST** /retentions/{id}/executions | Trigger a Retention job
[**retentions_id_get**](ProductsApi.md#retentions_id_get) | **GET** /retentions/{id} | Get Retention Policy
[**retentions_id_put**](ProductsApi.md#retentions_id_put) | **PUT** /retentions/{id} | Update Retention Policy
[**retentions_metadatas_get**](ProductsApi.md#retentions_metadatas_get) | **GET** /retentions/metadatas | Get Retention Metadatas
[**retentions_post**](ProductsApi.md#retentions_post) | **POST** /retentions | Create Retention Policy
[**scanners_get**](ProductsApi.md#scanners_get) | **GET** /scanners | List scanner registrations
[**scanners_ping_post**](ProductsApi.md#scanners_ping_post) | **POST** /scanners/ping | Tests scanner registration settings
[**scanners_registration_id_get**](ProductsApi.md#scanners_registration_id_get) | **GET** /scanners/{registration_id} | Get a scanner registration details
[**scanners_registration_id_metadata_get**](ProductsApi.md#scanners_registration_id_metadata_get) | **GET** /scanners/{registration_id}/metadata | Get the metadata of the specified scanner registration
[**scans_all_metrics_get**](ProductsApi.md#scans_all_metrics_get) | **GET** /scans/all/metrics | Get the metrics of the latest scan all process
[**scans_schedule_metrics_get**](ProductsApi.md#scans_schedule_metrics_get) | **GET** /scans/schedule/metrics | Get the metrics of the latest scheduled scan all process
[**search_get**](ProductsApi.md#search_get) | **GET** /search | Search for projects, repositories and helm charts
[**statistics_get**](ProductsApi.md#statistics_get) | **GET** /statistics | Get projects number and repositories number relevant to the user
[**system_cve_whitelist_get**](ProductsApi.md#system_cve_whitelist_get) | **GET** /system/CVEWhitelist | Get the system level whitelist of CVE.
[**system_cve_whitelist_put**](ProductsApi.md#system_cve_whitelist_put) | **PUT** /system/CVEWhitelist | Update the system level whitelist of CVE.
[**system_gc_get**](ProductsApi.md#system_gc_get) | **GET** /system/gc | Get gc results.
[**system_gc_id_get**](ProductsApi.md#system_gc_id_get) | **GET** /system/gc/{id} | Get gc status.
[**system_gc_id_log_get**](ProductsApi.md#system_gc_id_log_get) | **GET** /system/gc/{id}/log | Get gc job log.
[**system_gc_schedule_get**](ProductsApi.md#system_gc_schedule_get) | **GET** /system/gc/schedule | Get gc&#x27;s schedule.
[**system_gc_schedule_post**](ProductsApi.md#system_gc_schedule_post) | **POST** /system/gc/schedule | Create a gc schedule.
[**system_gc_schedule_put**](ProductsApi.md#system_gc_schedule_put) | **PUT** /system/gc/schedule | Update gc&#x27;s schedule.
[**system_oidc_ping_post**](ProductsApi.md#system_oidc_ping_post) | **POST** /system/oidc/ping | Test the OIDC endpoint.
[**system_scan_all_schedule_get**](ProductsApi.md#system_scan_all_schedule_get) | **GET** /system/scanAll/schedule | Get scan_all&#x27;s schedule.
[**system_scan_all_schedule_post**](ProductsApi.md#system_scan_all_schedule_post) | **POST** /system/scanAll/schedule | Create a schedule or a manual trigger for the scan all job.
[**system_scan_all_schedule_put**](ProductsApi.md#system_scan_all_schedule_put) | **PUT** /system/scanAll/schedule | Update scan all&#x27;s schedule.
[**systeminfo_get**](ProductsApi.md#systeminfo_get) | **GET** /systeminfo | Get general system info
[**systeminfo_getcert_get**](ProductsApi.md#systeminfo_getcert_get) | **GET** /systeminfo/getcert | Get default root certificate.
[**systeminfo_volumes_get**](ProductsApi.md#systeminfo_volumes_get) | **GET** /systeminfo/volumes | Get system volume info (total/free size).
[**usergroups_get**](ProductsApi.md#usergroups_get) | **GET** /usergroups | Get all user groups information
[**usergroups_group_id_delete**](ProductsApi.md#usergroups_group_id_delete) | **DELETE** /usergroups/{group_id} | Delete user group
[**usergroups_group_id_get**](ProductsApi.md#usergroups_group_id_get) | **GET** /usergroups/{group_id} | Get user group information
[**usergroups_group_id_put**](ProductsApi.md#usergroups_group_id_put) | **PUT** /usergroups/{group_id} | Update group information
[**usergroups_post**](ProductsApi.md#usergroups_post) | **POST** /usergroups | Create user group
[**users_current_get**](ProductsApi.md#users_current_get) | **GET** /users/current | Get current user info.
[**users_current_permissions_get**](ProductsApi.md#users_current_permissions_get) | **GET** /users/current/permissions | Get current user permissions.
[**users_get**](ProductsApi.md#users_get) | **GET** /users | Get registered users of Harbor.
[**users_post**](ProductsApi.md#users_post) | **POST** /users | Creates a new user account.
[**users_search_get**](ProductsApi.md#users_search_get) | **GET** /users/search | Search users by username
[**users_user_id_cli_secret_put**](ProductsApi.md#users_user_id_cli_secret_put) | **PUT** /users/{user_id}/cli_secret | Set CLI secret for a user.
[**users_user_id_delete**](ProductsApi.md#users_user_id_delete) | **DELETE** /users/{user_id} | Mark a registered user as be removed.
[**users_user_id_get**](ProductsApi.md#users_user_id_get) | **GET** /users/{user_id} | Get a user&#x27;s profile.
[**users_user_id_password_put**](ProductsApi.md#users_user_id_password_put) | **PUT** /users/{user_id}/password | Change the password on a user that already exists.
[**users_user_id_put**](ProductsApi.md#users_user_id_put) | **PUT** /users/{user_id} | Update a registered user to change his profile.
[**users_user_id_sysadmin_put**](ProductsApi.md#users_user_id_sysadmin_put) | **PUT** /users/{user_id}/sysadmin | Update a registered user to change to be an administrator of Harbor.

# **chartrepo_charts_post**
> chartrepo_charts_post(chart, prov)

Upload a chart file to the defult 'library' project.

Upload a chart file to the default 'library' project. Uploading together with the prov file at the same time is also supported.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
chart = 'chart_example' # str | 
prov = 'prov_example' # str | 

try:
    # Upload a chart file to the defult 'library' project.
    api_instance.chartrepo_charts_post(chart, prov)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_charts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart** | **str**|  | 
 **prov** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_health_get**
> InlineResponse200 chartrepo_health_get()

Check the health of chart repository service.

Check the health of chart repository service.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Check the health of chart repository service.
    api_response = api_instance.chartrepo_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_get**
> list[ChartInfoEntry] chartrepo_repo_charts_get(repo)

Get all the charts under the specified project

Get all the charts under the specified project

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo = 'repo_example' # str | The project name

try:
    # Get all the charts under the specified project
    api_response = api_instance.chartrepo_repo_charts_get(repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_charts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 

### Return type

[**list[ChartInfoEntry]**](ChartInfoEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_delete**
> chartrepo_repo_charts_name_delete(repo, name)

Delete all the versions of the specified chart

Delete all the versions of the specified chart

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name

try:
    # Delete all the versions of the specified chart
    api_instance.chartrepo_repo_charts_name_delete(repo, name)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_charts_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_get**
> ChartVersions chartrepo_repo_charts_name_get(repo, name)

Get all the versions of the specified chart

Get all the versions of the specified chart

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name

try:
    # Get all the versions of the specified chart
    api_response = api_instance.chartrepo_repo_charts_name_get(repo, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_charts_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 

### Return type

[**ChartVersions**](ChartVersions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_delete**
> chartrepo_repo_charts_name_version_delete(repo, name, version)

Delete the specified chart version

Delete the specified chart version

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version

try:
    # Delete the specified chart version
    api_instance.chartrepo_repo_charts_name_version_delete(repo, name, version)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_charts_name_version_delete: %s\n" % e)
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

# **chartrepo_repo_charts_name_version_get**
> ChartVersionDetails chartrepo_repo_charts_name_version_get(repo, name, version)

Get the specified chart version

Get the specified chart version

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version

try:
    # Get the specified chart version
    api_response = api_instance.chartrepo_repo_charts_name_version_get(repo, name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_charts_name_version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 
 **version** | **str**| The chart version | 

### Return type

[**ChartVersionDetails**](ChartVersionDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version

try:
    # Return the attahced labels of chart.
    api_instance.chartrepo_repo_charts_name_version_labels_get(repo, name, version)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_charts_name_version_labels_get: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version
id = 56 # int | The label ID

try:
    # Remove label from chart.
    api_instance.chartrepo_repo_charts_name_version_labels_id_delete(repo, name, version, id)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_charts_name_version_labels_id_delete: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Label() # Label | The label being marked to the chart version
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version

try:
    # Mark label to chart.
    api_instance.chartrepo_repo_charts_name_version_labels_post(body, repo, name, version)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_charts_name_version_labels_post: %s\n" % e)
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

# **chartrepo_repo_charts_post**
> chartrepo_repo_charts_post(chart, prov, repo)

Upload a chart file to the specified project.

Upload a chart file to the specified project. With this API, the corresponding provance file can be uploaded together with chart file at once.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
chart = 'chart_example' # str | 
prov = 'prov_example' # str | 
repo = 'repo_example' # str | The project name

try:
    # Upload a chart file to the specified project.
    api_instance.chartrepo_repo_charts_post(chart, prov, repo)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_charts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart** | **str**|  | 
 **prov** | **str**|  | 
 **repo** | **str**| The project name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_prov_post**
> chartrepo_repo_prov_post(prov, repo)

Upload a provance file to the specified project.

Upload a provance file to the specified project. The provance file should be targeted for an existing chart file.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
prov = 'prov_example' # str | 
repo = 'repo_example' # str | The project name

try:
    # Upload a provance file to the specified project.
    api_instance.chartrepo_repo_prov_post(prov, repo)
except ApiException as e:
    print("Exception when calling ProductsApi->chartrepo_repo_prov_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prov** | **str**|  | 
 **repo** | **str**| The project name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurations_get**
> ConfigurationsResponse configurations_get()

Get system configurations.

This endpoint is for retrieving system configurations that only provides for admin user. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get system configurations.
    api_response = api_instance.configurations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->configurations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationsResponse**](ConfigurationsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurations_put**
> configurations_put(body)

Modify system configurations.

This endpoint is for modifying system configurations that only provides for admin user. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Configurations() # Configurations | The configuration map can contain a subset of the attributes of the schema, which are to be updated.

try:
    # Modify system configurations.
    api_instance.configurations_put(body)
except ApiException as e:
    print("Exception when calling ProductsApi->configurations_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Configurations**](Configurations.md)| The configuration map can contain a subset of the attributes of the schema, which are to be updated. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_ping_post**
> email_ping_post(body=body)

Test connection and authentication with email server.

Test connection and authentication with email server. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.EmailServerSetting() # EmailServerSetting | Email server settings, if some of the settings are not assigned, they will be read from system configuration. (optional)

try:
    # Test connection and authentication with email server.
    api_instance.email_ping_post(body=body)
except ApiException as e:
    print("Exception when calling ProductsApi->email_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailServerSetting**](EmailServerSetting.md)| Email server settings, if some of the settings are not assigned, they will be read from system configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_get**
> OverallHealthStatus health_get()

Health check API

The endpoint returns the health stauts of the system. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Health check API
    api_response = api_instance.health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OverallHealthStatus**](OverallHealthStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_switchquota_put**
> internal_switchquota_put(body)

Enable or disable quota.

This endpoint is for enable/disable quota. When quota is disabled, no resource require/release in image/chart push and delete. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.QuotaSwitcher() # QuotaSwitcher | 

try:
    # Enable or disable quota.
    api_instance.internal_switchquota_put(body)
except ApiException as e:
    print("Exception when calling ProductsApi->internal_switchquota_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuotaSwitcher**](QuotaSwitcher.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_syncquota_post**
> internal_syncquota_post()

Sync quota from registry/chart to DB.

This endpoint is for syncing quota usage of registry/chart with database. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Sync quota from registry/chart to DB.
    api_instance.internal_syncquota_post()
except ApiException as e:
    print("Exception when calling ProductsApi->internal_syncquota_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_syncregistry_post**
> internal_syncregistry_post()

Sync repositories from registry to DB.

This endpoint is for syncing all repositories of registry with database. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Sync repositories from registry to DB.
    api_instance.internal_syncregistry_post()
except ApiException as e:
    print("Exception when calling ProductsApi->internal_syncregistry_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_get**
> list[Label] labels_get(scope, name=name, project_id=project_id, page=page, page_size=page_size)

List labels according to the query strings.

This endpoint let user list labels by name, scope and project_id 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
scope = 'scope_example' # str | The label scope. Valid values are g and p. g for global labels and p for project labels.
name = 'name_example' # str | The label name. (optional)
project_id = 789 # int | Relevant project ID, required when scope is p. (optional)
page = 56 # int | The page nubmer. (optional)
page_size = 56 # int | The size of per page. (optional)

try:
    # List labels according to the query strings.
    api_response = api_instance.labels_get(scope, name=name, project_id=project_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The label scope. Valid values are g and p. g for global labels and p for project labels. | 
 **name** | **str**| The label name. | [optional] 
 **project_id** | **int**| Relevant project ID, required when scope is p. | [optional] 
 **page** | **int**| The page nubmer. | [optional] 
 **page_size** | **int**| The size of per page. | [optional] 

### Return type

[**list[Label]**](Label.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_delete**
> labels_id_delete(id)

Delete the label specified by ID.

Delete the label specified by ID. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Label ID

try:
    # Delete the label specified by ID.
    api_instance.labels_id_delete(id)
except ApiException as e:
    print("Exception when calling ProductsApi->labels_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Label ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_get**
> Label labels_id_get(id)

Get the label specified by ID.

This endpoint let user get the label by specific ID. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Label ID

try:
    # Get the label specified by ID.
    api_response = api_instance.labels_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->labels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Label ID | 

### Return type

[**Label**](Label.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_put**
> labels_id_put(body, id)

Update the label properties.

This endpoint let user update label properties. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Label() # Label | The updated label json object.
id = 789 # int | Label ID

try:
    # Update the label properties.
    api_instance.labels_id_put(body, id)
except ApiException as e:
    print("Exception when calling ProductsApi->labels_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Label**](Label.md)| The updated label json object. | 
 **id** | **int**| Label ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_resources_get**
> Resource labels_id_resources_get(id)

Get the resources that the label is referenced by.

This endpoint let user get the resources that the label is referenced by. Only the replication policies are returned for now. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Label ID

try:
    # Get the resources that the label is referenced by.
    api_response = api_instance.labels_id_resources_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->labels_id_resources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Label ID | 

### Return type

[**Resource**](Resource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_post**
> labels_post(body)

Post creates a label

This endpoint let user creates a label. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Label() # Label | The json object of label.

try:
    # Post creates a label
    api_instance.labels_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Label**](Label.md)| The json object of label. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_groups_search_get**
> list[UserGroup] ldap_groups_search_get(groupname=groupname, groupdn=groupdn)

Search available ldap groups.

This endpoint searches the available ldap groups based on related configuration parameters. support to search by groupname or groupdn. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
groupname = 'groupname_example' # str | Ldap group name (optional)
groupdn = 'groupdn_example' # str | The LDAP group DN (optional)

try:
    # Search available ldap groups.
    api_response = api_instance.ldap_groups_search_get(groupname=groupname, groupdn=groupdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->ldap_groups_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **str**| Ldap group name | [optional] 
 **groupdn** | **str**| The LDAP group DN | [optional] 

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_ping_post**
> ldap_ping_post(body=body)

Ping available ldap service.

This endpoint ping the available ldap service for test related configuration parameters. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.LdapConf() # LdapConf | ldap configuration. support input ldap service configuration. If it's a empty request, will load current configuration from the system. (optional)

try:
    # Ping available ldap service.
    api_instance.ldap_ping_post(body=body)
except ApiException as e:
    print("Exception when calling ProductsApi->ldap_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapConf**](LdapConf.md)| ldap configuration. support input ldap service configuration. If it&#x27;s a empty request, will load current configuration from the system. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_users_import_post**
> ldap_users_import_post(body)

Import selected available ldap users.

This endpoint adds the selected available ldap users to harbor based on related configuration parameters from the system. System will try to guess the user email address and realname, add to harbor user information. If have errors when import user, will return the list of importing failed uid and the failed reason. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.LdapImportUsers() # LdapImportUsers | The uid listed for importing. This list will check users validity of ldap service based on configuration from the system.

try:
    # Import selected available ldap users.
    api_instance.ldap_users_import_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->ldap_users_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapImportUsers**](LdapImportUsers.md)| The uid listed for importing. This list will check users validity of ldap service based on configuration from the system. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_users_search_get**
> list[LdapUsers] ldap_users_search_get(username=username)

Search available ldap users.

This endpoint searches the available ldap users based on related configuration parameters. Support searched by input ladp configuration, load configuration from the system and specific filter. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
username = 'username_example' # str | Registered user ID (optional)

try:
    # Search available ldap users.
    api_response = api_instance.ldap_users_search_get(username=username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->ldap_users_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Registered user ID | [optional] 

### Return type

[**list[LdapUsers]**](LdapUsers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logs_get**
> list[AccessLog] logs_get(username=username, repository=repository, tag=tag, operation=operation, begin_timestamp=begin_timestamp, end_timestamp=end_timestamp, page=page, page_size=page_size)

Get recent logs of the projects which the user is a member of

This endpoint let user see the recent operation logs of the projects which he is member of 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
username = 'username_example' # str | Username of the operator. (optional)
repository = 'repository_example' # str | The name of repository (optional)
tag = 'tag_example' # str | The name of tag (optional)
operation = 'operation_example' # str | The operation (optional)
begin_timestamp = 'begin_timestamp_example' # str | The begin timestamp (optional)
end_timestamp = 'end_timestamp_example' # str | The end timestamp (optional)
page = 56 # int | The page number, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try:
    # Get recent logs of the projects which the user is a member of
    api_response = api_instance.logs_get(username=username, repository=repository, tag=tag, operation=operation, begin_timestamp=begin_timestamp, end_timestamp=end_timestamp, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the operator. | [optional] 
 **repository** | **str**| The name of repository | [optional] 
 **tag** | **str**| The name of tag | [optional] 
 **operation** | **str**| The operation | [optional] 
 **begin_timestamp** | **str**| The begin timestamp | [optional] 
 **end_timestamp** | **str**| The end timestamp | [optional] 
 **page** | **int**| The page number, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[AccessLog]**](AccessLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> list[Project] projects_get(name=name, public=public, owner=owner, page=page, page_size=page_size)

List projects

This endpoint returns all projects created by Harbor, and can be filtered by project name. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
name = 'name_example' # str | The name of project. (optional)
public = true # bool | The project is public or private. (optional)
owner = 'owner_example' # str | The name of project owner. (optional)
page = 56 # int | The page number, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try:
    # List projects
    api_response = api_instance.projects_get(name=name, public=public, owner=owner, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of project. | [optional] 
 **public** | **bool**| The project is public or private. | [optional] 
 **owner** | **str**| The name of project owner. | [optional] 
 **page** | **int**| The page number, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[Project]**](Project.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_head**
> projects_head(project_name)

Check if the project name user provided already exists.

This endpoint is used to check if the project name user provided already exist. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_name = 'project_name_example' # str | Project name for checking exists.

try:
    # Check if the project name user provided already exists.
    api_instance.projects_head(project_name)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| Project name for checking exists. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_post**
> projects_post(body)

Create a new project.

This endpoint is for user to create a new project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.ProjectReq() # ProjectReq | New created project.

try:
    # Create a new project.
    api_instance.projects_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectReq**](ProjectReq.md)| New created project. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_delete**
> projects_project_id_delete(project_id)

Delete project by projectID

This endpoint is aimed to delete project by project ID. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Project ID of project which will be deleted.

try:
    # Delete project by projectID
    api_instance.projects_project_id_delete(project_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID of project which will be deleted. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_get**
> Project projects_project_id_get(project_id)

Return specific project detail information

This endpoint returns specific project information by project ID. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Project ID for filtering results.

try:
    # Return specific project detail information
    api_response = api_instance.projects_project_id_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID for filtering results. | 

### Return type

[**Project**](Project.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_immutabletagrules_get**
> list[ImmutableTagRule] projects_project_id_immutabletagrules_get(project_id)

List all immutable tag rules of current project

This endpoint returns the immutable tag rules of a project 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.

try:
    # List all immutable tag rules of current project
    api_response = api_instance.projects_project_id_immutabletagrules_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_immutabletagrules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 

### Return type

[**list[ImmutableTagRule]**](ImmutableTagRule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_immutabletagrules_id_delete**
> projects_project_id_immutabletagrules_id_delete(project_id, id)

Delete the immutable tag rule.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
id = 789 # int | Immutable tag rule ID.

try:
    # Delete the immutable tag rule.
    api_instance.projects_project_id_immutabletagrules_id_delete(project_id, id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_immutabletagrules_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **id** | **int**| Immutable tag rule ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_immutabletagrules_id_put**
> projects_project_id_immutabletagrules_id_put(project_id, id, body=body)

Update the immutable tag rule or enable or disable the rule

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
id = 789 # int | Immutable tag rule ID.
body = harbor.ImmutableTagRule() # ImmutableTagRule |  (optional)

try:
    # Update the immutable tag rule or enable or disable the rule
    api_instance.projects_project_id_immutabletagrules_id_put(project_id, id, body=body)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_immutabletagrules_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **id** | **int**| Immutable tag rule ID. | 
 **body** | [**ImmutableTagRule**](ImmutableTagRule.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_immutabletagrules_post**
> projects_project_id_immutabletagrules_post(project_id, body=body)

Add an immutable tag rule to current project

This endpoint add an immutable tag rule to the project 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
body = harbor.ImmutableTagRule() # ImmutableTagRule |  (optional)

try:
    # Add an immutable tag rule to current project
    api_instance.projects_project_id_immutabletagrules_post(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_immutabletagrules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **body** | [**ImmutableTagRule**](ImmutableTagRule.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_logs_get**
> list[AccessLog] projects_project_id_logs_get(project_id, username=username, repository=repository, tag=tag, operation=operation, begin_timestamp=begin_timestamp, end_timestamp=end_timestamp, page=page, page_size=page_size)

Get access logs accompany with a relevant project.

This endpoint let user search access logs filtered by operations and date time ranges. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID
username = 'username_example' # str | Username of the operator. (optional)
repository = 'repository_example' # str | The name of repository (optional)
tag = 'tag_example' # str | The name of tag (optional)
operation = 'operation_example' # str | The operation (optional)
begin_timestamp = 'begin_timestamp_example' # str | The begin timestamp (optional)
end_timestamp = 'end_timestamp_example' # str | The end timestamp (optional)
page = 56 # int | The page number, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try:
    # Get access logs accompany with a relevant project.
    api_response = api_instance.projects_project_id_logs_get(project_id, username=username, repository=repository, tag=tag, operation=operation, begin_timestamp=begin_timestamp, end_timestamp=end_timestamp, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID | 
 **username** | **str**| Username of the operator. | [optional] 
 **repository** | **str**| The name of repository | [optional] 
 **tag** | **str**| The name of tag | [optional] 
 **operation** | **str**| The operation | [optional] 
 **begin_timestamp** | **str**| The begin timestamp | [optional] 
 **end_timestamp** | **str**| The end timestamp | [optional] 
 **page** | **int**| The page number, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[AccessLog]**](AccessLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_get**
> list[ProjectMemberEntity] projects_project_id_members_get(project_id, entityname=entityname)

Get all project member information

Get all project member information

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
entityname = 'entityname_example' # str | The entity name to search. (optional)

try:
    # Get all project member information
    api_response = api_instance.projects_project_id_members_get(project_id, entityname=entityname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **entityname** | **str**| The entity name to search. | [optional] 

### Return type

[**list[ProjectMemberEntity]**](ProjectMemberEntity.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_mid_delete**
> projects_project_id_members_mid_delete(project_id, mid)

Delete project member

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
mid = 789 # int | Member ID.

try:
    # Delete project member
    api_instance.projects_project_id_members_mid_delete(project_id, mid)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_mid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **mid** | **int**| Member ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_mid_get**
> ProjectMemberEntity projects_project_id_members_mid_get(project_id, mid)

Get the project member information

Get the project member information

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
mid = 789 # int | The member ID

try:
    # Get the project member information
    api_response = api_instance.projects_project_id_members_mid_get(project_id, mid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_mid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **mid** | **int**| The member ID | 

### Return type

[**ProjectMemberEntity**](ProjectMemberEntity.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_mid_put**
> projects_project_id_members_mid_put(project_id, mid, body=body)

Update project member

Update project member relationship

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
mid = 789 # int | Member ID.
body = harbor.RoleRequest() # RoleRequest |  (optional)

try:
    # Update project member
    api_instance.projects_project_id_members_mid_put(project_id, mid, body=body)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_mid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **mid** | **int**| Member ID. | 
 **body** | [**RoleRequest**](RoleRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_post**
> projects_project_id_members_post(project_id, body=body)

Create project member

Create project member relationship, the member can be one of the user_member and group_member,  The user_member need to specify user_id or username. If the user already exist in harbor DB, specify the user_id,  If does not exist in harbor DB, it will SearchAndOnBoard the user. The group_member need to specify id or ldap_group_dn. If the group already exist in harbor DB. specify the user group's id,  If does not exist, it will SearchAndOnBoard the group. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
body = harbor.ProjectMember() # ProjectMember |  (optional)

try:
    # Create project member
    api_instance.projects_project_id_members_post(project_id, body=body)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **body** | [**ProjectMember**](ProjectMember.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_get**
> ProjectMetadata projects_project_id_metadatas_get(project_id)

Get project metadata.

This endpoint returns metadata of the project specified by project ID. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | The ID of project.

try:
    # Get project metadata.
    api_response = api_instance.projects_project_id_metadatas_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_metadatas_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of project. | 

### Return type

[**ProjectMetadata**](ProjectMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_meta_name_delete**
> projects_project_id_metadatas_meta_name_delete(project_id, meta_name)

Delete metadata of a project

This endpoint is aimed to delete metadata of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | The ID of project.
meta_name = 'meta_name_example' # str | The name of metadat.

try:
    # Delete metadata of a project
    api_instance.projects_project_id_metadatas_meta_name_delete(project_id, meta_name)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_metadatas_meta_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of project. | 
 **meta_name** | **str**| The name of metadat. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_meta_name_get**
> ProjectMetadata projects_project_id_metadatas_meta_name_get(project_id, meta_name)

Get project metadata

This endpoint returns specified metadata of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Project ID for filtering results.
meta_name = 'meta_name_example' # str | The name of metadat.

try:
    # Get project metadata
    api_response = api_instance.projects_project_id_metadatas_meta_name_get(project_id, meta_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_metadatas_meta_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID for filtering results. | 
 **meta_name** | **str**| The name of metadat. | 

### Return type

[**ProjectMetadata**](ProjectMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_meta_name_put**
> projects_project_id_metadatas_meta_name_put(project_id, meta_name)

Update metadata of a project.

This endpoint is aimed to update the metadata of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | The ID of project.
meta_name = 'meta_name_example' # str | The name of metadat.

try:
    # Update metadata of a project.
    api_instance.projects_project_id_metadatas_meta_name_put(project_id, meta_name)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_metadatas_meta_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of project. | 
 **meta_name** | **str**| The name of metadat. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_metadatas_post**
> projects_project_id_metadatas_post(body, project_id)

Add metadata for the project.

This endpoint is aimed to add metadata of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.ProjectMetadata() # ProjectMetadata | The metadata of project.
project_id = 789 # int | Selected project ID.

try:
    # Add metadata for the project.
    api_instance.projects_project_id_metadatas_post(body, project_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_metadatas_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectMetadata**](ProjectMetadata.md)| The metadata of project. | 
 **project_id** | **int**| Selected project ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_put**
> projects_project_id_put(body, project_id)

Update properties for a selected project.

This endpoint is aimed to update the properties of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.ProjectReq() # ProjectReq | Updates of project.
project_id = 789 # int | Selected project ID.

try:
    # Update properties for a selected project.
    api_instance.projects_project_id_put(body, project_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectReq**](ProjectReq.md)| Updates of project. | 
 **project_id** | **int**| Selected project ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_robots_get**
> list[RobotAccount] projects_project_id_robots_get(project_id)

Get all robot accounts of specified project

Get all robot accounts of specified project

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.

try:
    # Get all robot accounts of specified project
    api_response = api_instance.projects_project_id_robots_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_robots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 

### Return type

[**list[RobotAccount]**](RobotAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_robots_post**
> RobotAccountPostRep projects_project_id_robots_post(body, project_id)

Create a robot account for project

Create a robot account for project

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.RobotAccountCreate() # RobotAccountCreate | Request body of creating a robot account.
project_id = 789 # int | Relevant project ID.

try:
    # Create a robot account for project
    api_response = api_instance.projects_project_id_robots_post(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_robots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RobotAccountCreate**](RobotAccountCreate.md)| Request body of creating a robot account. | 
 **project_id** | **int**| Relevant project ID. | 

### Return type

[**RobotAccountPostRep**](RobotAccountPostRep.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_robots_robot_id_delete**
> projects_project_id_robots_robot_id_delete(project_id, robot_id)

Delete the specified robot account

Delete the specified robot account

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
robot_id = 789 # int | The ID of robot account.

try:
    # Delete the specified robot account
    api_instance.projects_project_id_robots_robot_id_delete(project_id, robot_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_robots_robot_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **robot_id** | **int**| The ID of robot account. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_robots_robot_id_get**
> RobotAccount projects_project_id_robots_robot_id_get(project_id, robot_id)

Return the infor of the specified robot account.

Return the infor of the specified robot account.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
robot_id = 789 # int | The ID of robot account.

try:
    # Return the infor of the specified robot account.
    api_response = api_instance.projects_project_id_robots_robot_id_get(project_id, robot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_robots_robot_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **robot_id** | **int**| The ID of robot account. | 

### Return type

[**RobotAccount**](RobotAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_robots_robot_id_put**
> projects_project_id_robots_robot_id_put(body, project_id, robot_id)

Update status of robot account.

Used to disable/enable a specified robot account.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.RobotAccountUpdate() # RobotAccountUpdate | Request body of enable/disable a robot account.
project_id = 789 # int | Relevant project ID.
robot_id = 789 # int | The ID of robot account.

try:
    # Update status of robot account.
    api_instance.projects_project_id_robots_robot_id_put(body, project_id, robot_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_robots_robot_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RobotAccountUpdate**](RobotAccountUpdate.md)| Request body of enable/disable a robot account. | 
 **project_id** | **int**| Relevant project ID. | 
 **robot_id** | **int**| The ID of robot account. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | The project identifier.

try:
    # Get scanner registration candidates for configurating project level scanner
    api_response = api_instance.projects_project_id_scanner_candidates_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_scanner_candidates_get: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | The project identifier.

try:
    # Get project level scanner
    api_response = api_instance.projects_project_id_scanner_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_scanner_get: %s\n" % e)
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

# **projects_project_id_summary_get**
> ProjectSummary projects_project_id_summary_get(project_id)

Get summary of the project.

Get summary of the project.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID

try:
    # Get summary of the project.
    api_response = api_instance.projects_project_id_summary_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID | 

### Return type

[**ProjectSummary**](ProjectSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_jobs_get**
> list[WebhookJob] projects_project_id_webhook_jobs_get(project_id, policy_id)

List project webhook jobs

This endpoint returns webhook jobs of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
policy_id = 789 # int | The policy ID.

try:
    # List project webhook jobs
    api_response = api_instance.projects_project_id_webhook_jobs_get(project_id, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_webhook_jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **policy_id** | **int**| The policy ID. | 

### Return type

[**list[WebhookJob]**](WebhookJob.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_lasttrigger_get**
> list[WebhookLastTrigger] projects_project_id_webhook_lasttrigger_get(project_id)

Get project webhook policy last trigger info

This endpoint returns last trigger information of project webhook policy. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.

try:
    # Get project webhook policy last trigger info
    api_response = api_instance.projects_project_id_webhook_lasttrigger_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_webhook_lasttrigger_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 

### Return type

[**list[WebhookLastTrigger]**](WebhookLastTrigger.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_get**
> list[WebhookPolicy] projects_project_id_webhook_policies_get(project_id)

List project webhook policies.

This endpoint returns webhook policies of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.

try:
    # List project webhook policies.
    api_response = api_instance.projects_project_id_webhook_policies_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_webhook_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 

### Return type

[**list[WebhookPolicy]**](WebhookPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_policy_id_delete**
> projects_project_id_webhook_policies_policy_id_delete(project_id, policy_id)

Delete webhook policy of a project

This endpoint is aimed to delete webhookpolicy of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
policy_id = 789 # int | The id of webhook policy.

try:
    # Delete webhook policy of a project
    api_instance.projects_project_id_webhook_policies_policy_id_delete(project_id, policy_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_webhook_policies_policy_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **policy_id** | **int**| The id of webhook policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_policy_id_get**
> WebhookPolicy projects_project_id_webhook_policies_policy_id_get(project_id, policy_id)

Get project webhook policy

This endpoint returns specified webhook policy of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
policy_id = 789 # int | The id of webhook policy.

try:
    # Get project webhook policy
    api_response = api_instance.projects_project_id_webhook_policies_policy_id_get(project_id, policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_webhook_policies_policy_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **policy_id** | **int**| The id of webhook policy. | 

### Return type

[**WebhookPolicy**](WebhookPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_policy_id_put**
> projects_project_id_webhook_policies_policy_id_put(body, project_id, policy_id)

Update webhook policy of a project.

This endpoint is aimed to update the webhook policy of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.WebhookPolicy() # WebhookPolicy | All properties needed except "id", "project_id", "creation_time", "update_time".
project_id = 789 # int | Relevant project ID.
policy_id = 789 # int | The id of webhook policy.

try:
    # Update webhook policy of a project.
    api_instance.projects_project_id_webhook_policies_policy_id_put(body, project_id, policy_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_webhook_policies_policy_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookPolicy**](WebhookPolicy.md)| All properties needed except &quot;id&quot;, &quot;project_id&quot;, &quot;creation_time&quot;, &quot;update_time&quot;. | 
 **project_id** | **int**| Relevant project ID. | 
 **policy_id** | **int**| The id of webhook policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_post**
> projects_project_id_webhook_policies_post(body, project_id)

Create project webhook policy.

This endpoint create a webhook policy if the project does not have one. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.WebhookPolicy() # WebhookPolicy | Properties "targets" and "event_types" needed.
project_id = 789 # int | Relevant project ID

try:
    # Create project webhook policy.
    api_instance.projects_project_id_webhook_policies_post(body, project_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_webhook_policies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookPolicy**](WebhookPolicy.md)| Properties &quot;targets&quot; and &quot;event_types&quot; needed. | 
 **project_id** | **int**| Relevant project ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_webhook_policies_test_post**
> projects_project_id_webhook_policies_test_post(body, project_id)

Test project webhook connection

This endpoint tests webhook connection of a project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.WebhookPolicy() # WebhookPolicy | Only property "targets" needed.
project_id = 789 # int | Relevant project ID.

try:
    # Test project webhook connection
    api_instance.projects_project_id_webhook_policies_test_post(body, project_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_webhook_policies_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookPolicy**](WebhookPolicy.md)| Only property &quot;targets&quot; needed. | 
 **project_id** | **int**| Relevant project ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_get**
> list[Quota] quotas_get(reference=reference, reference_id=reference_id, sort=sort, page=page, page_size=page_size)

List quotas

List quotas

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
reference = 'reference_example' # str | The reference type of quota. (optional)
reference_id = 'reference_id_example' # str | The reference id of quota. (optional)
sort = 'sort_example' # str | Sort method, valid values include: 'hard.resource_name', '-hard.resource_name', 'used.resource_name', '-used.resource_name'. Here '-' stands for descending order, resource_name should be the real resource name of the quota.  (optional)
page = 56 # int | The page number, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try:
    # List quotas
    api_response = api_instance.quotas_get(reference=reference, reference_id=reference_id, sort=sort, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->quotas_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **str**| The reference type of quota. | [optional] 
 **reference_id** | **str**| The reference id of quota. | [optional] 
 **sort** | **str**| Sort method, valid values include: &#x27;hard.resource_name&#x27;, &#x27;-hard.resource_name&#x27;, &#x27;used.resource_name&#x27;, &#x27;-used.resource_name&#x27;. Here &#x27;-&#x27; stands for descending order, resource_name should be the real resource name of the quota.  | [optional] 
 **page** | **int**| The page number, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[Quota]**](Quota.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 56 # int | Quota ID

try:
    # Get the specified quota
    api_response = api_instance.quotas_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->quotas_id_get: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.QuotaUpdateReq() # QuotaUpdateReq | The new hard limits for the quota
id = 56 # int | Quota ID

try:
    # Update the specified quota
    api_instance.quotas_id_put(body, id)
except ApiException as e:
    print("Exception when calling ProductsApi->quotas_id_put: %s\n" % e)
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

# **registries_get**
> list[Registry] registries_get(name=name)

List registries.

This endpoint let user list filtered registries by name, if name is nil, list returns all registries. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
name = 'name_example' # str | Registry's name. (optional)

try:
    # List registries.
    api_response = api_instance.registries_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->registries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Registry&#x27;s name. | [optional] 

### Return type

[**list[Registry]**](Registry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_delete**
> registries_id_delete(id)

Delete specific registry.

This endpoint is for to delete specific registry. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | The registry's ID.

try:
    # Delete specific registry.
    api_instance.registries_id_delete(id)
except ApiException as e:
    print("Exception when calling ProductsApi->registries_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry&#x27;s ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_get**
> Registry registries_id_get(id)

Get registry.

This endpoint is for get specific registry.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | The registry ID.

try:
    # Get registry.
    api_response = api_instance.registries_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->registries_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry ID. | 

### Return type

[**Registry**](Registry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_info_get**
> RegistryInfo registries_id_info_get(id)

Get registry info.

Get the info of one specific registry.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | The registry ID.

try:
    # Get registry info.
    api_response = api_instance.registries_id_info_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->registries_id_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry ID. | 

### Return type

[**RegistryInfo**](RegistryInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_namespace_get**
> list[Namespace] registries_id_namespace_get(id, name=name)

List namespaces of registry

This endpoint let user list namespaces of registry according to query. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 56 # int | The registry ID.
name = 'name_example' # str | The name of namespace. (optional)

try:
    # List namespaces of registry
    api_response = api_instance.registries_id_namespace_get(id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->registries_id_namespace_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The registry ID. | 
 **name** | **str**| The name of namespace. | [optional] 

### Return type

[**list[Namespace]**](Namespace.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_id_put**
> registries_id_put(body, id)

Update a given registry.

This endpoint is for update a given registry. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.PutRegistry() # PutRegistry | Updates registry.
id = 789 # int | The registry's ID.

try:
    # Update a given registry.
    api_instance.registries_id_put(body, id)
except ApiException as e:
    print("Exception when calling ProductsApi->registries_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutRegistry**](PutRegistry.md)| Updates registry. | 
 **id** | **int**| The registry&#x27;s ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_ping_post**
> registries_ping_post(body)

Ping status of a registry.

This endpoint checks status of a registry, the registry can be given by ID or URL (together with credential) 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Registry() # Registry | Registry to ping.

try:
    # Ping status of a registry.
    api_instance.registries_ping_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->registries_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Registry**](Registry.md)| Registry to ping. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_post**
> registries_post(body)

Create a new registry.

This endpoint is for user to create a new registry. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Registry() # Registry | New created registry.

try:
    # Create a new registry.
    api_instance.registries_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->registries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Registry**](Registry.md)| New created registry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_adapters_get**
> list[str] replication_adapters_get()

List supported adapters.

This endpoint let user list supported adapters. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # List supported adapters.
    api_response = api_instance.replication_adapters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_adapters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_executions_get**
> list[ReplicationExecution] replication_executions_get(policy_id=policy_id, status=status, trigger=trigger, page=page, page_size=page_size)

List replication executions.

This endpoint let user list replication executions. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
policy_id = 56 # int | The policy ID. (optional)
status = 'status_example' # str | The execution status. (optional)
trigger = 'trigger_example' # str | The trigger mode. (optional)
page = 56 # int | The page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # List replication executions.
    api_response = api_instance.replication_executions_get(policy_id=policy_id, status=status, trigger=trigger, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_executions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The policy ID. | [optional] 
 **status** | **str**| The execution status. | [optional] 
 **trigger** | **str**| The trigger mode. | [optional] 
 **page** | **int**| The page. | [optional] 
 **page_size** | **int**| The page size. | [optional] 

### Return type

[**list[ReplicationExecution]**](ReplicationExecution.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_executions_id_get**
> ReplicationExecution replication_executions_id_get(id)

Get the execution of the replication.

This endpoint is for user to get one execution of the replication. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | The execution ID.

try:
    # Get the execution of the replication.
    api_response = api_instance.replication_executions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_executions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The execution ID. | 

### Return type

[**ReplicationExecution**](ReplicationExecution.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_executions_id_put**
> replication_executions_id_put(id)

Stop the execution of the replication.

This endpoint is for user to stop one execution of the replication. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | The execution ID.

try:
    # Stop the execution of the replication.
    api_instance.replication_executions_id_put(id)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_executions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The execution ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_executions_id_tasks_get**
> list[ReplicationTask] replication_executions_id_tasks_get(id)

Get the task list of one execution.

This endpoint is for user to get the task list of one execution. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | The execution ID.

try:
    # Get the task list of one execution.
    api_response = api_instance.replication_executions_id_tasks_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_executions_id_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The execution ID. | 

### Return type

[**list[ReplicationTask]**](ReplicationTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_executions_id_tasks_task_id_log_get**
> replication_executions_id_tasks_task_id_log_get(id, task_id)

Get the log of one task.

This endpoint is for user to get the log of one task. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | The execution ID.
task_id = 789 # int | The task ID.

try:
    # Get the log of one task.
    api_instance.replication_executions_id_tasks_task_id_log_get(id, task_id)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_executions_id_tasks_task_id_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The execution ID. | 
 **task_id** | **int**| The task ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_executions_post**
> replication_executions_post(body)

Start one execution of the replication.

This endpoint is for user to start one execution of the replication. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.ReplicationExecution() # ReplicationExecution | The execution that needs to be started, only the property "policy_id" is needed.

try:
    # Start one execution of the replication.
    api_instance.replication_executions_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_executions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplicationExecution**](ReplicationExecution.md)| The execution that needs to be started, only the property &quot;policy_id&quot; is needed. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_get**
> list[ReplicationPolicy] replication_policies_get(name=name, page=page, page_size=page_size)

List replication policies

This endpoint let user list replication policies 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
name = 'name_example' # str | The replication policy name. (optional)
page = 56 # int | The page nubmer. (optional)
page_size = 56 # int | The size of per page. (optional)

try:
    # List replication policies
    api_response = api_instance.replication_policies_get(name=name, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The replication policy name. | [optional] 
 **page** | **int**| The page nubmer. | [optional] 
 **page_size** | **int**| The size of per page. | [optional] 

### Return type

[**list[ReplicationPolicy]**](ReplicationPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_id_delete**
> replication_policies_id_delete(id)

Delete the replication policy specified by ID.

Delete the replication policy specified by ID. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Replication policy ID

try:
    # Delete the replication policy specified by ID.
    api_instance.replication_policies_id_delete(id)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_policies_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Replication policy ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_id_get**
> ReplicationPolicy replication_policies_id_get(id)

Get replication policy.

This endpoint let user get replication policy by specific ID. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | policy ID

try:
    # Get replication policy.
    api_response = api_instance.replication_policies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_policies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| policy ID | 

### Return type

[**ReplicationPolicy**](ReplicationPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_id_put**
> replication_policies_id_put(body, id)

Update the replication policy

This endpoint let user update policy. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.ReplicationPolicy() # ReplicationPolicy | The replication policy model.
id = 789 # int | policy ID

try:
    # Update the replication policy
    api_instance.replication_policies_id_put(body, id)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_policies_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplicationPolicy**](ReplicationPolicy.md)| The replication policy model. | 
 **id** | **int**| policy ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_policies_post**
> replication_policies_post(body)

Create a replication policy

This endpoint let user create a replication policy 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.ReplicationPolicy() # ReplicationPolicy | The policy model.

try:
    # Create a replication policy
    api_instance.replication_policies_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->replication_policies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReplicationPolicy**](ReplicationPolicy.md)| The policy model. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_get**
> list[Repository] repositories_get(project_id, q=q, sort=sort, label_id=label_id, page=page, page_size=page_size)

Get repositories accompany with relevant project and repo name.

This endpoint lets user search repositories accompanying with relevant project ID and repo name. Repositories can be sorted by repo name, creation_time, update_time in either ascending or descending order. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
project_id = 56 # int | Relevant project ID.
q = 'q_example' # str | Repo name for filtering results. (optional)
sort = 'sort_example' # str | Sort method, valid values include: 'name', '-name', 'creation_time', '-creation_time', 'update_time', '-update_time'. Here '-' stands for descending order.  (optional)
label_id = 56 # int | The ID of label used to filter the result. (optional)
page = 56 # int | The page number, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try:
    # Get repositories accompany with relevant project and repo name.
    api_response = api_instance.repositories_get(project_id, q=q, sort=sort, label_id=label_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **q** | **str**| Repo name for filtering results. | [optional] 
 **sort** | **str**| Sort method, valid values include: &#x27;name&#x27;, &#x27;-name&#x27;, &#x27;creation_time&#x27;, &#x27;-creation_time&#x27;, &#x27;update_time&#x27;, &#x27;-update_time&#x27;. Here &#x27;-&#x27; stands for descending order.  | [optional] 
 **label_id** | **int**| The ID of label used to filter the result. | [optional] 
 **page** | **int**| The page number, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_delete**
> repositories_repo_name_delete(repo_name)

Delete a repository.

This endpoint let user delete a repository with name. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | The name of repository which will be deleted.

try:
    # Delete a repository.
    api_instance.repositories_repo_name_delete(repo_name)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| The name of repository which will be deleted. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_labels_get**
> list[Label] repositories_repo_name_labels_get(repo_name)

Get labels of a repository.

Get labels of a repository specified by the repo_name. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | The name of repository.

try:
    # Get labels of a repository.
    api_response = api_instance.repositories_repo_name_labels_get(repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| The name of repository. | 

### Return type

[**list[Label]**](Label.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_labels_label_id_delete**
> repositories_repo_name_labels_label_id_delete(repo_name, label_id)

Delete label from the repository.

Delete the label from the repository specified by the repo_name. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | The name of repository.
label_id = 56 # int | The ID of label.

try:
    # Delete label from the repository.
    api_instance.repositories_repo_name_labels_label_id_delete(repo_name, label_id)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_labels_label_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| The name of repository. | 
 **label_id** | **int**| The ID of label. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_labels_post**
> repositories_repo_name_labels_post(body, repo_name)

Add a label to the repository.

Add a label to the repository. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Label() # Label | Only the ID property is required.
repo_name = 'repo_name_example' # str | The name of repository.

try:
    # Add a label to the repository.
    api_instance.repositories_repo_name_labels_post(body, repo_name)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Label**](Label.md)| Only the ID property is required. | 
 **repo_name** | **str**| The name of repository. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_put**
> repositories_repo_name_put(body, repo_name)

Update description of the repository.

This endpoint is used to update description of the repository. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.RepositoryDescription() # RepositoryDescription | The description of the repository.
repo_name = 'repo_name_example' # str | The name of repository which will be deleted.

try:
    # Update description of the repository.
    api_instance.repositories_repo_name_put(body, repo_name)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepositoryDescription**](RepositoryDescription.md)| The description of the repository. | 
 **repo_name** | **str**| The name of repository which will be deleted. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_signatures_get**
> list[RepoSignature] repositories_repo_name_signatures_get(repo_name)

Get signature information of a repository

This endpoint aims to retrieve signature information of a repository, the data is from the nested notary instance of Harbor. If the repository does not have any signature information in notary, this API will return an empty list with response code 200, instead of 404 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | repository name.

try:
    # Get signature information of a repository
    api_response = api_instance.repositories_repo_name_signatures_get(repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_signatures_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| repository name. | 

### Return type

[**list[RepoSignature]**](RepoSignature.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_get**
> list[DetailedTag] repositories_repo_name_tags_get(repo_name, label_id=label_id, detail=detail)

Get tags of a relevant repository.

This endpoint aims to retrieve tags from a relevant repository. If deployed with Notary, the signature property of response represents whether the image is singed or not. If the property is null, the image is unsigned. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Relevant repository name.
label_id = 'label_id_example' # str | A label ID. (optional)
detail = true # bool | Bool value indicating whether return detailed information of the tag, such as vulnerability scan info, if set to false, only tag name is returned. (optional)

try:
    # Get tags of a relevant repository.
    api_response = api_instance.repositories_repo_name_tags_get(repo_name, label_id=label_id, detail=detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Relevant repository name. | 
 **label_id** | **str**| A label ID. | [optional] 
 **detail** | **bool**| Bool value indicating whether return detailed information of the tag, such as vulnerability scan info, if set to false, only tag name is returned. | [optional] 

### Return type

[**list[DetailedTag]**](DetailedTag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_post**
> repositories_repo_name_tags_post(body, repo_name)

Retag an image

This endpoint tags an existing image with another tag in this repo, source images can be in different repos or projects. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.RetagReq() # RetagReq | Request to give source image and target tag.
repo_name = 'repo_name_example' # str | Relevant repository name.

try:
    # Retag an image
    api_instance.repositories_repo_name_tags_post(body, repo_name)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetagReq**](RetagReq.md)| Request to give source image and target tag. | 
 **repo_name** | **str**| Relevant repository name. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_delete**
> repositories_repo_name_tags_tag_delete(repo_name, tag)

Delete a tag in a repository.

This endpoint let user delete tags with repo name and tag. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | The name of repository which will be deleted.
tag = 'tag_example' # str | Tag of a repository.

try:
    # Delete a tag in a repository.
    api_instance.repositories_repo_name_tags_tag_delete(repo_name, tag)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| The name of repository which will be deleted. | 
 **tag** | **str**| Tag of a repository. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_get**
> DetailedTag repositories_repo_name_tags_tag_get(repo_name, tag)

Get the tag of the repository.

This endpoint aims to retrieve the tag of the repository. If deployed with Notary, the signature property of response represents whether the image is singed or not. If the property is null, the image is unsigned. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Relevant repository name.
tag = 'tag_example' # str | Tag of the repository.

try:
    # Get the tag of the repository.
    api_response = api_instance.repositories_repo_name_tags_tag_get(repo_name, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Relevant repository name. | 
 **tag** | **str**| Tag of the repository. | 

### Return type

[**DetailedTag**](DetailedTag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_labels_get**
> list[Label] repositories_repo_name_tags_tag_labels_get(repo_name, tag)

Get labels of an image.

Get labels of an image specified by the repo_name and tag. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | The name of repository.
tag = 'tag_example' # str | The tag of the image.

try:
    # Get labels of an image.
    api_response = api_instance.repositories_repo_name_tags_tag_labels_get(repo_name, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| The name of repository. | 
 **tag** | **str**| The tag of the image. | 

### Return type

[**list[Label]**](Label.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_labels_label_id_delete**
> repositories_repo_name_tags_tag_labels_label_id_delete(repo_name, tag, label_id)

Delete label from the image.

Delete the label from the image specified by the repo_name and tag. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | The name of repository.
tag = 'tag_example' # str | The tag of the image.
label_id = 56 # int | The ID of label.

try:
    # Delete label from the image.
    api_instance.repositories_repo_name_tags_tag_labels_label_id_delete(repo_name, tag, label_id)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_labels_label_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| The name of repository. | 
 **tag** | **str**| The tag of the image. | 
 **label_id** | **int**| The ID of label. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_labels_post**
> repositories_repo_name_tags_tag_labels_post(body, repo_name, tag)

Add a label to image.

Add a label to the image. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Label() # Label | Only the ID property is required.
repo_name = 'repo_name_example' # str | The name of repository.
tag = 'tag_example' # str | The tag of the image.

try:
    # Add a label to image.
    api_instance.repositories_repo_name_tags_tag_labels_post(body, repo_name, tag)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Label**](Label.md)| Only the ID property is required. | 
 **repo_name** | **str**| The name of repository. | 
 **tag** | **str**| The tag of the image. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_manifest_get**
> Manifest repositories_repo_name_tags_tag_manifest_get(repo_name, tag, version=version)

Get manifests of a relevant repository.

This endpoint aims to retreive manifests from a relevant repository. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Repository name
tag = 'tag_example' # str | Tag name
version = 'version_example' # str | The version of manifest, valid value are \"v1\" and \"v2\", default is \"v2\" (optional)

try:
    # Get manifests of a relevant repository.
    api_response = api_instance.repositories_repo_name_tags_tag_manifest_get(repo_name, tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_manifest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **tag** | **str**| Tag name | 
 **version** | **str**| The version of manifest, valid value are \&quot;v1\&quot; and \&quot;v2\&quot;, default is \&quot;v2\&quot; | [optional] 

### Return type

[**Manifest**](Manifest.md)

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Repository name
tag = 'tag_example' # str | Tag name

try:
    # Scan the image.
    api_instance.repositories_repo_name_tags_tag_scan_post(repo_name, tag)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_scan_post: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Repository name
tag = 'tag_example' # str | Tag name
uuid = 'uuid_example' # str | the scan unique identifier

try:
    # Get scan log
    api_response = api_instance.repositories_repo_name_tags_tag_scan_uuid_log_get(repo_name, tag, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_scan_uuid_log_get: %s\n" % e)
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

# **repositories_top_get**
> list[Repository] repositories_top_get(count=count)

Get public repositories which are accessed most.

This endpoint aims to let users see the most popular public repositories 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
count = 56 # int | The number of the requested public repositories, default is 10 if not provided. (optional)

try:
    # Get public repositories which are accessed most.
    api_response = api_instance.repositories_top_get(count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_top_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| The number of the requested public repositories, default is 10 if not provided. | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_executions_eid_patch**
> retentions_id_executions_eid_patch(body, id, eid)

Stop a Retention job

Stop a Retention job, only support \"stop\" action now.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Body6() # Body6 | The action, only support "stop" now.
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.

try:
    # Stop a Retention job
    api_instance.retentions_id_executions_eid_patch(body, id, eid)
except ApiException as e:
    print("Exception when calling ProductsApi->retentions_id_executions_eid_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)| The action, only support &quot;stop&quot; now. | 
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_executions_eid_tasks_get**
> list[RetentionExecutionTask] retentions_id_executions_eid_tasks_get(id, eid)

Get Retention job tasks

Get Retention job tasks, each repository as a task.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.

try:
    # Get Retention job tasks
    api_response = api_instance.retentions_id_executions_eid_tasks_get(id, eid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->retentions_id_executions_eid_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 

### Return type

[**list[RetentionExecutionTask]**](RetentionExecutionTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_executions_eid_tasks_tid_get**
> str retentions_id_executions_eid_tasks_tid_get(id, eid, tid)

Get Retention job task log

Get Retention job task log, tags ratain or deletion detail will be shown in a table.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.
eid = 789 # int | Retention execution ID.
tid = 789 # int | Retention execution ID.

try:
    # Get Retention job task log
    api_response = api_instance.retentions_id_executions_eid_tasks_tid_get(id, eid, tid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->retentions_id_executions_eid_tasks_tid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 
 **eid** | **int**| Retention execution ID. | 
 **tid** | **int**| Retention execution ID. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_executions_get**
> list[RetentionExecution] retentions_id_executions_get(id)

Get a Retention job

Get a Retention job, job status may be delayed before job service schedule it up.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.

try:
    # Get a Retention job
    api_response = api_instance.retentions_id_executions_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->retentions_id_executions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 

### Return type

[**list[RetentionExecution]**](RetentionExecution.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_executions_post**
> retentions_id_executions_post(body, id)

Trigger a Retention job

Trigger a Retention job, if dry_run is True, nothing would be deleted actually.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Body5() # Body5 | 
id = 789 # int | Retention ID.

try:
    # Trigger a Retention job
    api_instance.retentions_id_executions_post(body, id)
except ApiException as e:
    print("Exception when calling ProductsApi->retentions_id_executions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)|  | 
 **id** | **int**| Retention ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_get**
> RetentionPolicy retentions_id_get(id)

Get Retention Policy

Get Retention Policy.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Retention ID.

try:
    # Get Retention Policy
    api_response = api_instance.retentions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->retentions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Retention ID. | 

### Return type

[**RetentionPolicy**](RetentionPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_id_put**
> retentions_id_put(body, id)

Update Retention Policy

Update Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when retention policy has already binded to project. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.RetentionPolicy() # RetentionPolicy | 
id = 789 # int | Retention ID.

try:
    # Update Retention Policy
    api_instance.retentions_id_put(body, id)
except ApiException as e:
    print("Exception when calling ProductsApi->retentions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetentionPolicy**](RetentionPolicy.md)|  | 
 **id** | **int**| Retention ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_metadatas_get**
> RetentionMetadata retentions_metadatas_get()

Get Retention Metadatas

Get Retention Metadatas.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get Retention Metadatas
    api_response = api_instance.retentions_metadatas_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->retentions_metadatas_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RetentionMetadata**](RetentionMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retentions_post**
> retentions_post(body)

Create Retention Policy

Create Retention Policy, you can reference metadatas API for the policy model. You can check project metadatas to find whether a retention policy is already binded. This method should only be called when no retention policy binded to project yet. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.RetentionPolicy() # RetentionPolicy | Create Retention Policy successfully.

try:
    # Create Retention Policy
    api_instance.retentions_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->retentions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetentionPolicy**](RetentionPolicy.md)| Create Retention Policy successfully. | 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # List scanner registrations
    api_response = api_instance.scanners_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->scanners_get: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.ScannerRegistrationSettings() # ScannerRegistrationSettings | A scanner registration settings to be tested.

try:
    # Tests scanner registration settings
    api_instance.scanners_ping_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->scanners_ping_post: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifer.

try:
    # Get a scanner registration details
    api_response = api_instance.scanners_registration_id_get(registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->scanners_registration_id_get: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
registration_id = 'registration_id_example' # str | The scanner registration identifier.

try:
    # Get the metadata of the specified scanner registration
    api_response = api_instance.scanners_registration_id_metadata_get(registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->scanners_registration_id_metadata_get: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get the metrics of the latest scan all process
    api_response = api_instance.scans_all_metrics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->scans_all_metrics_get: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get the metrics of the latest scheduled scan all process
    api_response = api_instance.scans_schedule_metrics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->scans_schedule_metrics_get: %s\n" % e)
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

# **search_get**
> list[Search] search_get(q)

Search for projects, repositories and helm charts

The Search endpoint returns information about the projects ,repositories  and helm charts offered at public status or related to the current logged in user. The response includes the project, repository list and charts in a proper display order. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
q = 'q_example' # str | Search parameter for project and repository name.

try:
    # Search for projects, repositories and helm charts
    api_response = api_instance.search_get(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search parameter for project and repository name. | 

### Return type

[**list[Search]**](Search.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get**
> StatisticMap statistics_get()

Get projects number and repositories number relevant to the user

This endpoint is aimed to statistic all of the projects number and repositories number relevant to the logined user, also the public projects number and repositories number. If the user is admin, he can also get total projects number and total repositories number. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get projects number and repositories number relevant to the user
    api_response = api_instance.statistics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->statistics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatisticMap**](StatisticMap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get the system level whitelist of CVE.
    api_response = api_instance.system_cve_whitelist_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->system_cve_whitelist_get: %s\n" % e)
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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.CVEWhitelist() # CVEWhitelist | The whitelist with new content (optional)

try:
    # Update the system level whitelist of CVE.
    api_instance.system_cve_whitelist_put(body=body)
except ApiException as e:
    print("Exception when calling ProductsApi->system_cve_whitelist_put: %s\n" % e)
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

# **system_gc_get**
> list[GCResult] system_gc_get()

Get gc results.

This endpoint let user get latest ten gc results.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get gc results.
    api_response = api_instance.system_gc_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->system_gc_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GCResult]**](GCResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_gc_id_get**
> GCResult system_gc_id_get(id)

Get gc status.

This endpoint let user get gc status filtered by specific ID.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Relevant job ID

try:
    # Get gc status.
    api_response = api_instance.system_gc_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->system_gc_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Relevant job ID | 

### Return type

[**GCResult**](GCResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_gc_id_log_get**
> str system_gc_id_log_get(id)

Get gc job log.

This endpoint let user get gc job logs filtered by specific ID.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
id = 789 # int | Relevant job ID

try:
    # Get gc job log.
    api_response = api_instance.system_gc_id_log_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->system_gc_id_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Relevant job ID | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_gc_schedule_get**
> AdminJobSchedule system_gc_schedule_get()

Get gc's schedule.

This endpoint is for get schedule of gc job.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get gc's schedule.
    api_response = api_instance.system_gc_schedule_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->system_gc_schedule_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminJobSchedule**](AdminJobSchedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_gc_schedule_post**
> system_gc_schedule_post(body)

Create a gc schedule.

This endpoint is for update gc schedule. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.AdminJobSchedule() # AdminJobSchedule | Updates of gc's schedule.

try:
    # Create a gc schedule.
    api_instance.system_gc_schedule_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->system_gc_schedule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminJobSchedule**](AdminJobSchedule.md)| Updates of gc&#x27;s schedule. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_gc_schedule_put**
> system_gc_schedule_put(body)

Update gc's schedule.

This endpoint is for update gc schedule. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.AdminJobSchedule() # AdminJobSchedule | Updates of gc's schedule.

try:
    # Update gc's schedule.
    api_instance.system_gc_schedule_put(body)
except ApiException as e:
    print("Exception when calling ProductsApi->system_gc_schedule_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminJobSchedule**](AdminJobSchedule.md)| Updates of gc&#x27;s schedule. | 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Body4() # Body4 | Request body for OIDC endpoint to be tested.

try:
    # Test the OIDC endpoint.
    api_instance.system_oidc_ping_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->system_oidc_ping_post: %s\n" % e)
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

# **system_scan_all_schedule_get**
> AdminJobSchedule system_scan_all_schedule_get()

Get scan_all's schedule.

This endpoint is for getting a schedule for the scan all job, which scans all of images in Harbor.

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get scan_all's schedule.
    api_response = api_instance.system_scan_all_schedule_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->system_scan_all_schedule_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminJobSchedule**](AdminJobSchedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_scan_all_schedule_post**
> system_scan_all_schedule_post(body)

Create a schedule or a manual trigger for the scan all job.

This endpoint is for creating a schedule or a manual trigger for the scan all job, which scans all of images in Harbor. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.AdminJobSchedule() # AdminJobSchedule | Create a schedule or a manual trigger for the scan all job.

try:
    # Create a schedule or a manual trigger for the scan all job.
    api_instance.system_scan_all_schedule_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->system_scan_all_schedule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminJobSchedule**](AdminJobSchedule.md)| Create a schedule or a manual trigger for the scan all job. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_scan_all_schedule_put**
> system_scan_all_schedule_put(body)

Update scan all's schedule.

This endpoint is for updating the schedule of scan all job, which scans all of images in Harbor. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.AdminJobSchedule() # AdminJobSchedule | Updates the schedule of scan all job, which scans all of images in Harbor.

try:
    # Update scan all's schedule.
    api_instance.system_scan_all_schedule_put(body)
except ApiException as e:
    print("Exception when calling ProductsApi->system_scan_all_schedule_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminJobSchedule**](AdminJobSchedule.md)| Updates the schedule of scan all job, which scans all of images in Harbor. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_get**
> GeneralInfo systeminfo_get()

Get general system info

This API is for retrieving general system info, this can be called by anonymous request. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get general system info
    api_response = api_instance.systeminfo_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->systeminfo_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeneralInfo**](GeneralInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_getcert_get**
> systeminfo_getcert_get()

Get default root certificate.

This endpoint is for downloading a default root certificate. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get default root certificate.
    api_instance.systeminfo_getcert_get()
except ApiException as e:
    print("Exception when calling ProductsApi->systeminfo_getcert_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_volumes_get**
> SystemInfo systeminfo_volumes_get()

Get system volume info (total/free size).

This endpoint is for retrieving system volume info that only provides for admin user. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get system volume info (total/free size).
    api_response = api_instance.systeminfo_volumes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->systeminfo_volumes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_get**
> list[UserGroup] usergroups_get()

Get all user groups information

Get all user groups information

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get all user groups information
    api_response = api_instance.usergroups_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->usergroups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_group_id_delete**
> usergroups_group_id_delete(group_id)

Delete user group

Delete user group

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
group_id = 56 # int | 

try:
    # Delete user group
    api_instance.usergroups_group_id_delete(group_id)
except ApiException as e:
    print("Exception when calling ProductsApi->usergroups_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_group_id_get**
> UserGroup usergroups_group_id_get(group_id)

Get user group information

Get user group information

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
group_id = 789 # int | Group ID

try:
    # Get user group information
    api_response = api_instance.usergroups_group_id_get(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->usergroups_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_group_id_put**
> usergroups_group_id_put(group_id, body=body)

Update group information

Update user group information

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
group_id = 789 # int | Group ID
body = harbor.UserGroup() # UserGroup |  (optional)

try:
    # Update group information
    api_instance.usergroups_group_id_put(group_id, body=body)
except ApiException as e:
    print("Exception when calling ProductsApi->usergroups_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group ID | 
 **body** | [**UserGroup**](UserGroup.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usergroups_post**
> usergroups_post(body=body)

Create user group

Create user group information

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.UserGroup() # UserGroup |  (optional)

try:
    # Create user group
    api_instance.usergroups_post(body=body)
except ApiException as e:
    print("Exception when calling ProductsApi->usergroups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroup**](UserGroup.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_current_get**
> User users_current_get()

Get current user info.

This endpoint is to get the current user information. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))

try:
    # Get current user info.
    api_response = api_instance.users_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->users_current_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_current_permissions_get**
> list[Permission] users_current_permissions_get(scope=scope, relative=relative)

Get current user permissions.

This endpoint is to get the current user permissions. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
scope = 'scope_example' # str | Get permissions of the scope (optional)
relative = true # bool | If true, the resources in the response are relative to the scope, eg for resource '/project/1/repository' if relative is 'true' then the resource in response will be 'repository'.  (optional)

try:
    # Get current user permissions.
    api_response = api_instance.users_current_permissions_get(scope=scope, relative=relative)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->users_current_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Get permissions of the scope | [optional] 
 **relative** | **bool**| If true, the resources in the response are relative to the scope, eg for resource &#x27;/project/1/repository&#x27; if relative is &#x27;true&#x27; then the resource in response will be &#x27;repository&#x27;.  | [optional] 

### Return type

[**list[Permission]**](Permission.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> list[User] users_get(username=username, email=email, page=page, page_size=page_size)

Get registered users of Harbor.

This endpoint is for user to search registered users, support for filtering results with username.Notice, by now this operation is only for administrator. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
username = 'username_example' # str | Username for filtering results. (optional)
email = 'email_example' # str | Email for filtering results. (optional)
page = 56 # int | The page number, default is 1. (optional)
page_size = 56 # int | The size of per page. (optional)

try:
    # Get registered users of Harbor.
    api_response = api_instance.users_get(username=username, email=email, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for filtering results. | [optional] 
 **email** | **str**| Email for filtering results. | [optional] 
 **page** | **int**| The page number, default is 1. | [optional] 
 **page_size** | **int**| The size of per page. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> users_post(body)

Creates a new user account.

This endpoint is to create a user if the user does not already exist. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.User() # User | New created user.

try:
    # Creates a new user account.
    api_instance.users_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| New created user. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_search_get**
> list[UserSearch] users_search_get(username, page=page, page_size=page_size)

Search users by username

This endpoint is to search the users by username. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
username = 'username_example' # str | Username for filtering results.
page = 56 # int | The page number, default is 1. (optional)
page_size = 56 # int | The size of per page. (optional)

try:
    # Search users by username
    api_response = api_instance.users_search_get(username, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->users_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for filtering results. | 
 **page** | **int**| The page number, default is 1. | [optional] 
 **page_size** | **int**| The size of per page. | [optional] 

### Return type

[**list[UserSearch]**](UserSearch.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_cli_secret_put**
> users_user_id_cli_secret_put(body, user_id)

Set CLI secret for a user.

This endpoint let user generate a new CLI secret for himself.  This API only works when auth mode is set to 'OIDC'. Once this API returns with successful status, the old secret will be invalid, as there will be only one CLI secret for a user. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Body() # Body | JSON object that includes the new secret
user_id = 56 # int | User ID

try:
    # Set CLI secret for a user.
    api_instance.users_user_id_cli_secret_put(body, user_id)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_cli_secret_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| JSON object that includes the new secret | 
 **user_id** | **int**| User ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_delete**
> users_user_id_delete(user_id)

Mark a registered user as be removed.

This endpoint let administrator of Harbor mark a registered user as be removed.It actually won't be deleted from DB. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
user_id = 56 # int | User ID for marking as to be removed.

try:
    # Mark a registered user as be removed.
    api_instance.users_user_id_delete(user_id)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID for marking as to be removed. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_get**
> User users_user_id_get(user_id)

Get a user's profile.

Get user's profile with user id. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
user_id = 56 # int | Registered user ID

try:
    # Get a user's profile.
    api_response = api_instance.users_user_id_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID | 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_password_put**
> users_user_id_password_put(body, user_id)

Change the password on a user that already exists.

This endpoint is for user to update password. Users with the admin role can change any user's password. Guest users can change only their own password. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.Password() # Password | Password to be updated, the attribute 'old_password' is optional when the API is called by the system administrator.
user_id = 56 # int | Registered user ID.

try:
    # Change the password on a user that already exists.
    api_instance.users_user_id_password_put(body, user_id)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Password**](Password.md)| Password to be updated, the attribute &#x27;old_password&#x27; is optional when the API is called by the system administrator. | 
 **user_id** | **int**| Registered user ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_put**
> users_user_id_put(body, user_id)

Update a registered user to change his profile.

This endpoint let a registered user change his profile. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.UserProfile() # UserProfile | Only email, realname and comment can be modified.
user_id = 56 # int | Registered user ID

try:
    # Update a registered user to change his profile.
    api_instance.users_user_id_put(body, user_id)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserProfile**](UserProfile.md)| Only email, realname and comment can be modified. | 
 **user_id** | **int**| Registered user ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_sysadmin_put**
> users_user_id_sysadmin_put(body, user_id)

Update a registered user to change to be an administrator of Harbor.

This endpoint let a registered user change to be an administrator of Harbor. 

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
api_instance = harbor.ProductsApi(harbor.ApiClient(configuration))
body = harbor.HasAdminRole() # HasAdminRole | Toggle a user to admin or not.
user_id = 56 # int | Registered user ID

try:
    # Update a registered user to change to be an administrator of Harbor.
    api_instance.users_user_id_sysadmin_put(body, user_id)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_sysadmin_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HasAdminRole**](HasAdminRole.md)| Toggle a user to admin or not. | 
 **user_id** | **int**| Registered user ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

