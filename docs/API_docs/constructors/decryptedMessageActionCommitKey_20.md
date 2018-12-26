---
title: decryptedMessageActionCommitKey
description: Decrypted message action commit key
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionCommitKey\_20  
[Back to constructors index](index.md)



Decrypted message action commit key

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exchange\_id|[long](../types/long.md) | Yes|Exchange ID|
|key\_fingerprint|[long](../types/long.md) | Yes|Key fingerprint|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionCommitKey_20 = ['_' => 'decryptedMessageActionCommitKey', 'exchange_id' => long, 'key_fingerprint' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageActionCommitKey", "exchange_id": long, "key_fingerprint": long}
```


Or, if you're into Lua:

```lua
decryptedMessageActionCommitKey_20={_='decryptedMessageActionCommitKey', exchange_id=long, key_fingerprint=long}

```


