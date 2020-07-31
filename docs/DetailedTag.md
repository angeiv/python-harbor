# DetailedTag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | The digest of the tag. | [optional] 
**name** | **str** | The name of the tag. | [optional] 
**size** | **int** | The size of the image. | [optional] 
**architecture** | **str** | The architecture of the image. | [optional] 
**os** | **str** | The os of the image. | [optional] 
**docker_version** | **str** | The version of docker which builds the image. | [optional] 
**author** | **str** | The author of the image. | [optional] 
**created** | **str** | The build time of the image. | [optional] 
**signature** | **object** | The signature of image, defined by RepoSignature. If it is null, the image is unsigned. | [optional] 
**scan_overview** | [**ScanOverview**](ScanOverview.md) |  | [optional] 
**labels** | [**list[Label]**](Label.md) | The label list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

