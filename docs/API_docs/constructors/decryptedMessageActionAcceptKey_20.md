---
title: "decryptedMessageActionAcceptKey"
description: "Accept new key"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionAcceptKey\_20  
[Back to constructors index](index.md)



Accept new key

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exchange\_id|[long](../types/long.md) | Yes|Exchange ID|
|g\_b|[bytes](../types/bytes.md) | Yes|B parameter, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|
|key\_fingerprint|[long](../types/long.md) | Yes|Key fingerprint, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionAcceptKey_20 = ['_' => 'decryptedMessageActionAcceptKey', 'exchange_id' => long, 'g_b' => 'bytes', 'key_fingerprint' => long];
```  
