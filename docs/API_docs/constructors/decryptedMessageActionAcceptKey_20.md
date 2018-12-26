---
title: decryptedMessageActionAcceptKey
description: Decrypted message action accept key
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionAcceptKey\_20  
[Back to constructors index](index.md)



Decrypted message action accept key

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exchange\_id|[long](../types/long.md) | Yes|Exchange ID|
|g\_b|[bytes](../types/bytes.md) | Yes|G b|
|key\_fingerprint|[long](../types/long.md) | Yes|Key fingerprint|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionAcceptKey_20 = ['_' => 'decryptedMessageActionAcceptKey', 'exchange_id' => long, 'g_b' => 'bytes', 'key_fingerprint' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageActionAcceptKey", "exchange_id": long, "g_b": {"_": "bytes", "bytes":"base64 encoded bytes"}, "key_fingerprint": long}
```


Or, if you're into Lua:

```lua
decryptedMessageActionAcceptKey_20={_='decryptedMessageActionAcceptKey', exchange_id=long, g_b='bytes', key_fingerprint=long}

```


