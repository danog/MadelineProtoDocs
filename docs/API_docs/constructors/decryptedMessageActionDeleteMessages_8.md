---
title: decryptedMessageActionDeleteMessages
description: Deleted messages.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionDeleteMessages\_8  
[Back to constructors index](index.md)



Deleted messages.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|random\_ids|Array of [long](../types/long.md) | Yes|List of deleted message IDs|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionDeleteMessages_8 = ['_' => 'decryptedMessageActionDeleteMessages', 'random_ids' => [long, long]];
```  


Or, if you're into Lua:

```lua
decryptedMessageActionDeleteMessages_8={_='decryptedMessageActionDeleteMessages', random_ids={long}}

```


