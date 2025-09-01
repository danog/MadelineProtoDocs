---
title: "account.chatThemes"
description: "account.chatThemes attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_chatThemes.html
---
# Constructor: account.chatThemes  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Yes|
|themes|Array of [ChatTheme](/API_docs/types/ChatTheme.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|next\_offset|[int](/API_docs/types/int.html) | Optional|



### Type: [account.ChatThemes](/API_docs/types/account.ChatThemes.html)


### Example:

```
$account_chatThemes = ['_' => 'account.chatThemes', 'hash' => long, 'themes' => [ChatTheme, ChatTheme], 'chats' => [Chat, Chat], 'users' => [User, User], 'next_offset' => int];
```  
