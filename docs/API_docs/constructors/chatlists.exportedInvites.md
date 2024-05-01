---
title: "chatlists.exportedInvites"
description: "Info about multiple chat folder deep links »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/chatlists_exportedInvites.html
---
# Constructor: chatlists.exportedInvites  
[Back to constructors index](/API_docs/constructors/index.html)



Info about multiple [chat folder deep links »](https://core.telegram.org/api/links#chat-folder-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|invites|Array of [ExportedChatlistInvite](/API_docs/types/ExportedChatlistInvite.html) | Yes|The [chat folder deep links »](https://core.telegram.org/api/links#chat-folder-links).|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Related chat information|
|users|Array of [User](/API_docs/types/User.html) | Yes|Related user information|



### Type: [chatlists.ExportedInvites](/API_docs/types/chatlists.ExportedInvites.html)


### Example:

```
$chatlists_exportedInvites = ['_' => 'chatlists.exportedInvites', 'invites' => [ExportedChatlistInvite, ExportedChatlistInvite], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
