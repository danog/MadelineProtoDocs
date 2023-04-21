---
title: "chatlists.exportedInvites"
description: "chatlists.exportedInvites attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/chatlists_exportedInvites.html
---
# Constructor: chatlists.exportedInvites  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|invites|Array of [ExportedChatlistInvite](/API_docs/types/ExportedChatlistInvite.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [chatlists.ExportedInvites](/API_docs/types/chatlists.ExportedInvites.html)


### Example:

```
$chatlists_exportedInvites = ['_' => 'chatlists.exportedInvites', 'invites' => [ExportedChatlistInvite, ExportedChatlistInvite], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
