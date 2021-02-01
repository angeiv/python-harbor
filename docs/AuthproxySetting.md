# AuthproxySetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | The fully qualified URI of login endpoint of authproxy, such as &#x27;https://192.168.1.2:8443/login&#x27; | [optional] 
**tokenreivew_endpoint** | **str** | The fully qualified URI of token review endpoint of authproxy, such as &#x27;https://192.168.1.2:8443/tokenreview&#x27; | [optional] 
**skip_search** | **bool** | The flag to determine whether Harbor can skip search the user/group when adding him as a member. | [optional] 
**verify_cert** | **bool** | The flag to determine whether Harbor should verify the certificate when connecting to the auth proxy. | [optional] 
**server_certificate** | **str** | The certificate to be pinned when connecting auth proxy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

