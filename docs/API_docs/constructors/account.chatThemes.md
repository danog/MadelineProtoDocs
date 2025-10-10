---
title: "account.chatThemes"
description: "Available chat themes"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_chatThemes.html
---
# Constructor: account.chatThemes  
[Back to constructors index](/API_docs/constructors/index.html)



Available [chat themes](https://core.telegram.org/api/themes#chat-themes)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|Hash to pass to the method that returned this constructor, to avoid refetching the result if it hasn't changed.|
|themes|Array of [ChatTheme](/API_docs/types/ChatTheme.html) | Yes|Themes.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in the `themes` field.|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the `themes` field.|
|next\_offset|[string](/API_docs/types/string.html) | Optional|



### Type: [account.ChatThemes](/API_docs/types/account.ChatThemes.html)


### Example:

```
$account_chatThemes = ['_' => 'account.chatThemes', 'hash' => long, 'themes' => [ChatTheme, ChatTheme], 'chats' => [Chat, Chat], 'users' => [User, User], 'next_offset' => 'string'];
```  
