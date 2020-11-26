---
title: updateDeleteScheduledMessages
description: Some scheduled messages were deleted
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteScheduledMessages  
[Back to constructors index](index.md)



Some scheduled messages were deleted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|messages|Array of [int](../types/int.md) | Yes|Deleted scheduled messages|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDeleteScheduledMessages = ['_' => 'updateDeleteScheduledMessages', 'peer' => Peer, 'messages' => [int, int]];
```  


Or, if you're into Lua:

```lua
updateDeleteScheduledMessages={_='updateDeleteScheduledMessages', peer=Peer, messages={int}}

```


