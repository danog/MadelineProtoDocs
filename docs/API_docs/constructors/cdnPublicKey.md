---
title: "cdnPublicKey"
description: "Public key to use only during handshakes to CDN DCs."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: cdnPublicKey  
[Back to constructors index](index.md)



Public key to use **only** during handshakes to [CDN](https://core.telegram.org/cdn) DCs.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](../types/int.md) | Yes|[CDN DC](https://core.telegram.org/cdn) ID|
|public\_key|[string](../types/string.md) | Yes|RSA public key|



### Type: [CdnPublicKey](../types/CdnPublicKey.md)


### Example:

```php
$cdnPublicKey = ['_' => 'cdnPublicKey', 'dc_id' => int, 'public_key' => 'string'];
```  
