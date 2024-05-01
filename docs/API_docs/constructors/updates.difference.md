---
title: "updates.difference"
description: "Full list of occurred events."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/updates_difference.html
---
# Constructor: updates.difference  
[Back to constructors index](/API_docs/constructors/index.html)



Full list of occurred events.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|new\_messages|Array of [Message](/API_docs/types/Message.html) | Yes|List of new messages|
|new\_encrypted\_messages|Array of [EncryptedMessage](/API_docs/types/EncryptedMessage.html) | Yes|List of new encrypted secret chat messages|
|other\_updates|Array of [Update](/API_docs/types/Update.html) | Yes|List of updates|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|List of chats mentioned in events|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of users mentioned in events|
|state|[updates.State](/API_docs/constructors/updates.State.html) | Yes|Current state|



### Type: [updates.Difference](/API_docs/types/updates.Difference.html)


### Example:

```
$updates_difference = ['_' => 'updates.difference', 'new_messages' => [Message, Message], 'new_encrypted_messages' => [EncryptedMessage, EncryptedMessage], 'other_updates' => [Update, Update], 'chats' => [Chat, Chat], 'users' => [User, User], 'state' => updates.State];
```  
