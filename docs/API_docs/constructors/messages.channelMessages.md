---
title: "messages.channelMessages"
description: "Channel messages"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_channelMessages.html
---
# Constructor: messages.channelMessages  
[Back to constructors index](/API_docs/constructors/index.html)



Channel messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](/API_docs/types/Bool.html) | Optional|If set, returned results may be inexact|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results were found server-side (may not be all included here)|
|offset\_id\_offset|[int](/API_docs/types/int.html) | Optional|Indicates the absolute position of `messages[0]` within the total result set with count `count`. <br>This is useful, for example, if the result was fetched using `offset_id`, and we need to display a `progress/total` counter (like `photo 134 of 200`, for all media in a chat, we could simply use `photo ${offset_id_offset} of ${count}`.|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|Found messages|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [messages.Messages](/API_docs/types/messages.Messages.html)


### Example:

```
$messages_channelMessages = ['_' => 'messages.channelMessages', 'inexact' => Bool, 'pts' => int, 'count' => int, 'offset_id_offset' => int, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
