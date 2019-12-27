---
title: messages.dialogsSlice
description: Incomplete list of dialogs with messages and auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.dialogsSlice  
[Back to constructors index](index.md)



Incomplete list of dialogs with messages and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Total number of dialogs|
|dialogs|Array of [Dialog](../types/Dialog.md) | Yes|Dialogs|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages\_Dialogs](../types/messages_Dialogs.md)


### Example:

```php
$messages_dialogsSlice = ['_' => 'messages.dialogsSlice', 'count' => int, 'dialogs' => [Dialog, Dialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_dialogsSlice={_='messages.dialogsSlice', count=int, dialogs={Dialog}, messages={Message}, chats={Chat}, users={User}}

```


