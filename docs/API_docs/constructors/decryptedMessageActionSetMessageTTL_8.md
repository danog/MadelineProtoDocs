---
title: decryptedMessageActionSetMessageTTL
description: Setting of a message lifetime after reading.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageActionSetMessageTTL\_8  
[Back to constructors index](index.md)



Setting of a message lifetime after reading.

Upon receiving such message the client shall start deleting of all messages of an encrypted chat **ttl\_seconds** seconds after the messages were read by user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ttl\_seconds|[int](../types/int.md) | Yes|Lifetime in seconds|



### Type: [DecryptedMessageAction](../types/DecryptedMessageAction.md)


### Example:

```php
$decryptedMessageActionSetMessageTTL_8 = ['_' => 'decryptedMessageActionSetMessageTTL', 'ttl_seconds' => int];
```  


Or, if you're into Lua:

```lua
decryptedMessageActionSetMessageTTL_8={_='decryptedMessageActionSetMessageTTL', ttl_seconds=int}

```


