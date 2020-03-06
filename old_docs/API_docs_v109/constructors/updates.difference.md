---
title: updates.difference
description: Full list of occurred events.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_difference.html
---
# Constructor: updates.difference  
[Back to constructors index](index.md)



Full list of occurred events.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_messages|Array of [Message](../types/Message.md) | Yes|New messages|
|new\_encrypted\_messages|Array of [EncryptedMessage](../types/EncryptedMessage.md) | Yes|New encrypted messages|
|other\_updates|Array of [Update](../types/Update.md) | Yes|Other updates|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|
|state|[updates.State](../constructors/updates.State.md) | Yes|Current state|



### Type: [updates.Difference](../types/updates.Difference.md)


### Example:

```php
$updates.difference = ['_' => 'updates.difference', 'new_messages' => [Message, Message], 'new_encrypted_messages' => [EncryptedMessage, EncryptedMessage], 'other_updates' => [Update, Update], 'chats' => [Chat, Chat], 'users' => [User, User], 'state' => updates.State];
```  


Or, if you're into Lua:

```lua
updates.difference={_='updates.difference', new_messages={Message}, new_encrypted_messages={EncryptedMessage}, other_updates={Update}, chats={Chat}, users={User}, state=updates.State}

```


