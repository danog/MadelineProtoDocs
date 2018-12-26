---
title: decryptedMessageActionDeleteMessages
description: Decrypted message action delete messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionDeleteMessages\_8  
[Back to constructors index](index.md)



Decrypted message action delete messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|random\_ids|Array of [long](../types/long.md) | Yes|Random IDs|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionDeleteMessages_8 = ['_' => 'decryptedMessageActionDeleteMessages', 'random_ids' => [long, long]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageActionDeleteMessages", "random_ids": [long]}
```


Or, if you're into Lua:

```lua
decryptedMessageActionDeleteMessages_8={_='decryptedMessageActionDeleteMessages', random_ids={long}}

```


