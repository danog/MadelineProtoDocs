# secureSecretSettings

> Secure settings

[Back to constructors index](/API_docs/constructors/index.html)



Secure settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|secure\_algo|[SecurePasswordKdfAlgo](/API_docs/types/SecurePasswordKdfAlgo.html) | Yes|Secure KDF algo|
|secure\_secret|[bytes](/API_docs/types/bytes.html) | Yes|Secure secret|
|secure\_secret\_id|[long](/API_docs/types/long.html) | Yes|Secret ID|



### Type: [SecureSecretSettings](/API_docs/types/SecureSecretSettings.html)


### Example:

```
$secureSecretSettings = ['_' => 'secureSecretSettings', 'secure_algo' => SecurePasswordKdfAlgo, 'secure_secret' => 'bytes', 'secure_secret_id' => long];
```
