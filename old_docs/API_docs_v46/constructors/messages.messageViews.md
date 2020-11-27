---
title: messages.messageViews
description: messages.messageViews attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messageViews.html
---
# Constructor: messages.messageViews  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|views|Array of [MessageViews](../types/MessageViews.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.MessageViews](../types/messages.MessageViews.md)


### Example:

```php
$messages_messageViews = ['_' => 'messages.messageViews', 'views' => [MessageViews, MessageViews], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_messageViews={_='messages.messageViews', views={MessageViews}, chats={Chat}, users={User}}

```


