---
title: messages.dialogs
description: Full list of chats with messages and auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dialogs.html
---
# Constructor: messages.dialogs  
[Back to constructors index](index.md)



Full list of chats with messages and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dialogs|Array of [Dialog](../types/Dialog.md) | Yes|Dialogs|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages.Dialogs](../types/messages.Dialogs.md)


### Example:

```php
$messages.dialogs = ['_' => 'messages.dialogs', 'dialogs' => [Dialog, Dialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages.dialogs={_='messages.dialogs', dialogs={Dialog}, messages={Message}, chats={Chat}, users={User}}

```


