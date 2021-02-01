# GeneralInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**with_notary** | **bool** | If the Harbor instance is deployed with nested notary. | [optional] 
**with_chartmuseum** | **bool** | If the Harbor instance is deployed with nested chartmuseum. | [optional] 
**registry_url** | **str** | The url of registry against which the docker command should be issued. | [optional] 
**external_url** | **str** | The external URL of Harbor, with protocol. | [optional] 
**auth_mode** | **str** | The auth mode of current Harbor instance. | [optional] 
**project_creation_restriction** | **str** | Indicate who can create projects, it could be &#x27;adminonly&#x27; or &#x27;everyone&#x27;. | [optional] 
**self_registration** | **bool** | Indicate whether the Harbor instance enable user to register himself. | [optional] 
**has_ca_root** | **bool** | Indicate whether there is a ca root cert file ready for download in the file system. | [optional] 
**harbor_version** | **str** | The build version of Harbor. | [optional] 
**registry_storage_provider_name** | **str** | The storage provider&#x27;s name of Harbor registry | [optional] 
**read_only** | **bool** | The flag to indicate whether Harbor is in readonly mode. | [optional] 
**notification_enable** | **bool** | The flag to indicate whether notification mechanism is enabled on Harbor instance. | [optional] 
**authproxy_settings** | [**AuthproxySetting**](AuthproxySetting.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

