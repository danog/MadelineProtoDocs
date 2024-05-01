---
title: "cdnPublicKey"
description: "Public key to use only during handshakes to CDN DCs."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: cdnPublicKey  
[Back to constructors index](/API_docs/constructors/index.html)



Public key to use **only** during handshakes to [CDN](https://core.telegram.org/cdn) DCs.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](/API_docs/types/int.html) | Yes|[CDN DC](https://core.telegram.org/cdn) ID|
|public\_key|[string](/API_docs/types/string.html) | Yes|RSA public key|



### Type: [CdnPublicKey](/API_docs/types/CdnPublicKey.html)


### Example:

```
$cdnPublicKey = ['_' => 'cdnPublicKey', 'dc_id' => int, 'public_key' => 'string'];
```  
