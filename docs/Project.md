# Project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID | [optional] 
**owner_id** | **int** | The owner ID of the project always means the creator of the project. | [optional] 
**name** | **str** | The name of the project. | [optional] 
**creation_time** | **str** | The creation time of the project. | [optional] 
**update_time** | **str** | The update time of the project. | [optional] 
**deleted** | **bool** | A deletion mark of the project. | [optional] 
**owner_name** | **str** | The owner name of the project. | [optional] 
**togglable** | **bool** | Correspond to the UI about whether the project&#x27;s publicity is  updatable (for UI) | [optional] 
**current_user_role_id** | **int** | The role ID with highest permission of the current user who triggered the API (for UI) | [optional] 
**current_user_role_ids** | **list[int]** | The list of role ID of the current user who triggered the API (for UI) | [optional] 
**repo_count** | **int** | The number of the repositories under this project. | [optional] 
**chart_count** | **int** | The total number of charts under this project. | [optional] 
**metadata** | [**ProjectMetadata**](ProjectMetadata.md) |  | [optional] 
**cve_whitelist** | [**CVEWhitelist**](CVEWhitelist.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

