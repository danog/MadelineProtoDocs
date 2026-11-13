# cdnConfig

> Configuration for CDN file downloads.

[Back to constructors index](/API_docs/constructors/index.html)



Configuration for [CDN](https://core.telegram.org/cdn) file downloads.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|public\_keys|Array of [CdnPublicKey](/API_docs/types/CdnPublicKey.html) | Yes|Vector of public keys to use **only** during handshakes to [CDN](https://core.telegram.org/cdn) DCs.|



### Type: [CdnConfig](/API_docs/types/CdnConfig.html)


### Example:

```
$cdnConfig = ['_' => 'cdnConfig', 'public_keys' => [CdnPublicKey, CdnPublicKey]];
```
