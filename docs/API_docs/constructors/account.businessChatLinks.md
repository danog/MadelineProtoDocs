---
title: "account.businessChatLinks"
description: "Contains info about business chat deep links » created by the current account."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_businessChatLinks.html
---
# Constructor: account.businessChatLinks  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about [business chat deep links »](https://core.telegram.org/api/business#business-chat-links) created by the current account.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|links|Array of [BusinessChatLink](/API_docs/types/BusinessChatLink.html) | Yes|Links|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [account.BusinessChatLinks](/API_docs/types/account.BusinessChatLinks.html)


### Example:

```
$account_businessChatLinks = ['_' => 'account.businessChatLinks', 'links' => [BusinessChatLink, BusinessChatLink], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
