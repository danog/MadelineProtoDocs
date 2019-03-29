---
title: updateNewChannelMessage
description: Update new channel message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewChannelMessage  
[Back to constructors index](index.md)



Update new channel message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|
|channel\_pts|[int](../types/int.md) | Yes|Channel pts|
|channel\_pts\_count|[int](../types/int.md) | Yes|Channel pts count|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewChannelMessage = ['_' => 'updateNewChannelMessage', 'message' => Message, 'channel_pts' => int, 'channel_pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateNewChannelMessage={_='updateNewChannelMessage', message=Message, channel_pts=int, channel_pts_count=int}

```


