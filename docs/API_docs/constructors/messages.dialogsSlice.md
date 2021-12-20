---
title: "messages.dialogsSlice"
description: "Incomplete list of dialogs with messages and auxiliary data."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dialogsSlice.html
---
# Constructor: messages.dialogsSlice  
[Back to constructors index](index.md)



Incomplete list of dialogs with messages and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Total number of dialogs|
|dialogs|Array of [Dialog](../types/Dialog.md) | Yes|List of dialogs|
|messages|Array of [Message](../types/Message.md) | Yes|List of last messages from dialogs|
|chats|Array of [Chat](../types/Chat.md) | Yes|List of chats mentioned in dialogs|
|users|Array of [User](../types/User.md) | Yes|List of users mentioned in messages and chats|



### Type: [messages.Dialogs](../types/messages.Dialogs.md)


### Example:

```php
$messages_dialogsSlice = ['_' => 'messages.dialogsSlice', 'count' => int, 'dialogs' => [Dialog, Dialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_dialogsSlice={_='messages.dialogsSlice', count=int, dialogs={Dialog}, messages={Message}, chats={Chat}, users={User}}

```


