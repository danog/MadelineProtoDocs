---
title: "messages.messagesSlice"
description: "Incomplete list of messages and auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messagesSlice.html
---
# Constructor: messages.messagesSlice  
[Back to constructors index](index.md)



Incomplete list of messages and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](../types/Bool.md) | Optional|If set, indicates that the results may be inexact|
|count|[int](../types/int.md) | Yes|Total number of messages in the list|
|next\_rate|[int](../types/int.md) | Optional|Rate to use in the `offset_rate` parameter in the next call to [messages.searchGlobal](../methods/messages.searchGlobal.md)|
|offset\_id\_offset|[int](../types/int.md) | Optional|Indicates the absolute position of `messages[0]` within the total result set with count `count`. <br>This is useful, for example, if the result was fetched using `offset_id`, and we need to display a `progress/total` counter (like `photo 134 of 200`, for all media in a chat, we could simply use `photo ${offset_id_offset} of ${count}`.|
|messages|Array of [Message](../types/Message.md) | Yes|List of messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|List of chats mentioned in messages|
|users|Array of [User](../types/User.md) | Yes|List of users mentioned in messages and chats|



### Type: [messages.Messages](../types/messages.Messages.md)


### Example:

```php
$messages_messagesSlice = ['_' => 'messages.messagesSlice', 'inexact' => Bool, 'count' => int, 'next_rate' => int, 'offset_id_offset' => int, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_messagesSlice={_='messages.messagesSlice', inexact=Bool, count=int, next_rate=int, offset_id_offset=int, messages={Message}, chats={Chat}, users={User}}

```


