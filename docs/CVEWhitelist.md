# CVEWhitelist

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the whitelist | [optional] 
**project_id** | **int** | ID of the project which the whitelist belongs to.  For system level whitelist this attribute is zero. | [optional] 
**expires_at** | **int** | the time for expiration of the whitelist, in the form of seconds since epoch.  This is an optional attribute, if it&#x27;s not set the CVE whitelist does not expire. | [optional] 
**items** | [**list[CVEWhitelistItem]**](CVEWhitelistItem.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

