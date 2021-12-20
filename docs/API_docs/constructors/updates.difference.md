---
title: "updates.difference"
description: "Full list of occurred events."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_difference.html
---
# Constructor: updates.difference  
[Back to constructors index](index.md)



Full list of occurred events.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_messages|Array of [Message](../types/Message.md) | Yes|List of new messages|
|new\_encrypted\_messages|Array of [EncryptedMessage](../types/EncryptedMessage.md) | Yes|List of new encrypted secret chat messages|
|other\_updates|Array of [Update](../types/Update.md) | Yes|List of updates|
|chats|Array of [Chat](../types/Chat.md) | Yes|List of chats mentioned in events|
|users|Array of [User](../types/User.md) | Yes|List of users mentioned in events|
|state|[updates.State](../constructors/updates.State.md) | Yes|Current state|



### Type: [updates.Difference](../types/updates.Difference.md)


### Example:

```php
$updates_difference = ['_' => 'updates.difference', 'new_messages' => [Message, Message], 'new_encrypted_messages' => [EncryptedMessage, EncryptedMessage], 'other_updates' => [Update, Update], 'chats' => [Chat, Chat], 'users' => [User, User], 'state' => updates.State];
```  


Or, if you're into Lua:

```lua
updates_difference={_='updates.difference', new_messages={Message}, new_encrypted_messages={EncryptedMessage}, other_updates={Update}, chats={Chat}, users={User}, state=updates.State}

```


