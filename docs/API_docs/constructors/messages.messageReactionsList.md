---
title: "messages.messageReactionsList"
description: "messages.messageReactionsList attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messageReactionsList.html
---
# Constructor: messages.messageReactionsList  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](../types/int.md) | Yes|
|reactions|Array of [MessageUserReaction](../types/MessageUserReaction.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|
|next\_offset|[string](../types/string.md) | Optional|



### Type: [messages.MessageReactionsList](../types/messages.MessageReactionsList.md)


### Example:

```php
$messages_messageReactionsList = ['_' => 'messages.messageReactionsList', 'count' => int, 'reactions' => [MessageUserReaction, MessageUserReaction], 'users' => [User, User], 'next_offset' => 'string'];
```  


Or, if you're into Lua:

```lua
messages_messageReactionsList={_='messages.messageReactionsList', count=int, reactions={MessageUserReaction}, users={User}, next_offset='string'}

```


