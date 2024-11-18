---
title: "messages.preparedInlineMessage"
description: "messages.preparedInlineMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_preparedInlineMessage.html
---
# Constructor: messages.preparedInlineMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|query\_id|[long](/API_docs/types/long.html) | Yes|
|result|[BotInlineResult](/API_docs/types/BotInlineResult.html) | Yes|
|peer\_types|Array of [InlineQueryPeerType](/API_docs/types/InlineQueryPeerType.html) | Yes|
|cache\_time|[int](/API_docs/types/int.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.PreparedInlineMessage](/API_docs/types/messages.PreparedInlineMessage.html)


### Example:

```
$messages_preparedInlineMessage = ['_' => 'messages.preparedInlineMessage', 'query_id' => long, 'result' => BotInlineResult, 'peer_types' => [InlineQueryPeerType, InlineQueryPeerType], 'cache_time' => int, 'users' => [User, User]];
```  
