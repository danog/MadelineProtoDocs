---
title: updateChannelUserTyping
description: A user is typing in a [supergroup, channel](https://core.telegram.org/api/channel) or [message thread](https://core.telegram.org/api/threads)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelUserTyping  
[Back to constructors index](index.md)



A user is typing in a [supergroup, channel](https://core.telegram.org/api/channel) or [message thread](https://core.telegram.org/api/threads)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|top\_msg\_id|[int](../types/int.md) | Optional|[Thread ID](https://core.telegram.org/api/threads)|
|user\_id|[int](../types/int.md) | Yes|User ID|
|action|[SendMessageAction](../types/SendMessageAction.md) | Yes|Whether the user is typing, sending a media or doing something else|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelUserTyping = ['_' => 'updateChannelUserTyping', 'channel_id' => int, 'top_msg_id' => int, 'user_id' => int, 'action' => SendMessageAction];
```  


Or, if you're into Lua:

```lua
updateChannelUserTyping={_='updateChannelUserTyping', channel_id=int, top_msg_id=int, user_id=int, action=SendMessageAction}

```


