---
title: "account.businessChatLinks"
description: "account.businessChatLinks attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_businessChatLinks.html
---
# Constructor: account.businessChatLinks  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|links|Array of [BusinessChatLink](/API_docs/types/BusinessChatLink.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [account.BusinessChatLinks](/API_docs/types/account.BusinessChatLinks.html)


### Example:

```
$account_businessChatLinks = ['_' => 'account.businessChatLinks', 'links' => [BusinessChatLink, BusinessChatLink], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
