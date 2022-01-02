---
title: "decryptedMessageActionRequestKey"
description: "Request rekeying, see rekeying process"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionRequestKey\_20  
[Back to constructors index](index.md)



Request rekeying, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exchange\_id|[long](../types/long.md) | Yes|Exchange ID|
|g\_a|[bytes](../types/bytes.md) | Yes|g\_a, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionRequestKey_20 = ['_' => 'decryptedMessageActionRequestKey', 'exchange_id' => long, 'g_a' => 'bytes'];
```  


Or, if you're into Lua:

```lua
decryptedMessageActionRequestKey_20={_='decryptedMessageActionRequestKey', exchange_id=long, g_a='bytes'}

```


