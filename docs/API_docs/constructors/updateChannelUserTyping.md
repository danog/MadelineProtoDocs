---
title: updateChannelUserTyping
description: updateChannelUserTyping attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelUserTyping  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[int](../types/int.md) | Yes|
|top\_msg\_id|[int](../types/int.md) | Optional|
|user\_id|[int](../types/int.md) | Yes|
|action|[SendMessageAction](../types/SendMessageAction.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelUserTyping = ['_' => 'updateChannelUserTyping', 'channel_id' => int, 'top_msg_id' => int, 'user_id' => int, 'action' => SendMessageAction];
```  


Or, if you're into Lua:

```lua
updateChannelUserTyping={_='updateChannelUserTyping', channel_id=int, top_msg_id=int, user_id=int, action=SendMessageAction}

```


