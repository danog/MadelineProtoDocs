---
title: updateDeleteChannelMessages
description: updateDeleteChannelMessages attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteChannelMessages  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[int](../types/int.md) | Yes|
|messages|Array of [int](../types/int.md) | Yes|
|channel\_pts|[int](../types/int.md) | Yes|
|channel\_pts\_count|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDeleteChannelMessages = ['_' => 'updateDeleteChannelMessages', 'channel_id' => int, 'messages' => [int, int], 'channel_pts' => int, 'channel_pts_count' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateDeleteChannelMessages", "channel_id": int, "messages": [int], "channel_pts": int, "channel_pts_count": int}
```


Or, if you're into Lua:

```lua
updateDeleteChannelMessages={_='updateDeleteChannelMessages', channel_id=int, messages={int}, channel_pts=int, channel_pts_count=int}

```


