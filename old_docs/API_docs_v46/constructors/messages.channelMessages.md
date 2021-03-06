---
title: messages.channelMessages
description: Channel messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_channelMessages.html
---
# Constructor: messages.channelMessages  
[Back to constructors index](index.md)



Channel messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](../types/Bool.md) | Optional|If set, returned results may be inexact|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|count|[int](../types/int.md) | Yes|Total number of results were found server-side (may not be all included here)|
|offset\_id\_offset|[int](../types/int.md) | Optional|Indicates the absolute position of `messages[0]` within the total result set with count `count`. <br>This is useful, for example, if the result was fetched using `offset_id`, and we need to display a `progress/total` counter (like `photo 134 of 200`, for all media in a chat, we could simply use `photo ${offset_id_offset} of ${count}`.|
|messages|Array of [Message](../types/Message.md) | Yes|Found messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages.Messages](../types/messages.Messages.md)


### Example:

```php
$messages_channelMessages = ['_' => 'messages.channelMessages', 'inexact' => Bool, 'pts' => int, 'count' => int, 'offset_id_offset' => int, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_channelMessages={_='messages.channelMessages', inexact=Bool, pts=int, count=int, offset_id_offset=int, messages={Message}, chats={Chat}, users={User}}

```


