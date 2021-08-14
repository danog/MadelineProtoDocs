---
title: messages.messageViews
description: View, forward counter + info about replies
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messageViews.html
---
# Constructor: messages.messageViews  
[Back to constructors index](index.md)



View, forward counter + info about replies

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|views|Array of [MessageViews](../types/MessageViews.md) | Yes|View, forward counter + info about replies|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats mentioned in constructor|
|users|Array of [User](../types/User.md) | Yes|Users mentioned in constructor|



### Type: [messages.MessageViews](../types/messages.MessageViews.md)


### Example:

```php
$messages_messageViews = ['_' => 'messages.messageViews', 'views' => [MessageViews, MessageViews], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_messageViews={_='messages.messageViews', views={MessageViews}, chats={Chat}, users={User}}

```


