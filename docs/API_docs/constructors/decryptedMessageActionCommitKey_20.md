---
title: "decryptedMessageActionCommitKey"
description: "Commit new key, see rekeying process"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionCommitKey\_20  
[Back to constructors index](index.md)



Commit new key, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exchange\_id|[long](../types/long.md) | Yes|Exchange ID, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|
|key\_fingerprint|[long](../types/long.md) | Yes|Key fingerprint, see [rekeying process](https://core.telegram.org/api/end-to-end/pfs)|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionCommitKey_20 = ['_' => 'decryptedMessageActionCommitKey', 'exchange_id' => long, 'key_fingerprint' => long];
```  


Or, if you're into Lua:

```lua
decryptedMessageActionCommitKey_20={_='decryptedMessageActionCommitKey', exchange_id=long, key_fingerprint=long}

```


