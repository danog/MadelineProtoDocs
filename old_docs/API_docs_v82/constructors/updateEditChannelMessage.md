---
title: updateEditChannelMessage
description: Update edit channel message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEditChannelMessage  
[Back to constructors index](index.md)



Update edit channel message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateEditChannelMessage = ['_' => 'updateEditChannelMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateEditChannelMessage={_='updateEditChannelMessage', message=Message, pts=int, pts_count=int}

```


