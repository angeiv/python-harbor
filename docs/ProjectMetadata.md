# ProjectMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public** | **str** | The public status of the project. The valid values are \&quot;true\&quot;, \&quot;false\&quot;. | [optional] 
**enable_content_trust** | **str** | Whether content trust is enabled or not. If it is enabled, user can&#x27;t pull unsigned images from this project. The valid values are \&quot;true\&quot;, \&quot;false\&quot;. | [optional] 
**prevent_vul** | **str** | Whether prevent the vulnerable images from running. The valid values are \&quot;true\&quot;, \&quot;false\&quot;. | [optional] 
**severity** | **str** | If the vulnerability is high than severity defined here, the images can&#x27;t be pulled. The valid values are \&quot;none\&quot;, \&quot;low\&quot;, \&quot;medium\&quot;, \&quot;high\&quot;, \&quot;critical\&quot;. | [optional] 
**auto_scan** | **str** | Whether scan images automatically when pushing. The valid values are \&quot;true\&quot;, \&quot;false\&quot;. | [optional] 
**reuse_sys_cve_whitelist** | **str** | Whether this project reuse the system level CVE whitelist as the whitelist of its own.  The valid values are \&quot;true\&quot;, \&quot;false\&quot;. If it is set to \&quot;true\&quot; the actual whitelist associate with this project, if any, will be ignored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

