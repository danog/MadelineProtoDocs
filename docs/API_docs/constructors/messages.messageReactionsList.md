---
title: "messages.messageReactionsList"
description: "messages.messageReactionsList attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messageReactionsList.html
---
# Constructor: messages.messageReactionsList  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|reactions|Array of [MessageUserReaction](/API_docs/types/MessageUserReaction.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|



### Type: [messages.MessageReactionsList](/API_docs/types/messages.MessageReactionsList.html)


### Example:

```php
$messages_messageReactionsList = ['_' => 'messages.messageReactionsList', 'count' => int, 'reactions' => [MessageUserReaction, MessageUserReaction], 'users' => [User, User], 'next_offset' => 'string'];
```  
