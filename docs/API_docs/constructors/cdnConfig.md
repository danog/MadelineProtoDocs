---
title: "cdnConfig"
description: "Configuration for CDN file downloads."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: cdnConfig  
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
