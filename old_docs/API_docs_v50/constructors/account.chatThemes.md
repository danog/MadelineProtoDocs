---
title: account.chatThemes
description: account.chatThemes attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_chatThemes.html
---
# Constructor: account.chatThemes  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](../types/int.md) | Yes|
|themes|Array of [ChatTheme](../types/ChatTheme.md) | Yes|



### Type: [account.ChatThemes](../types/account.ChatThemes.md)


### Example:

```php
$account_chatThemes = ['_' => 'account.chatThemes', 'hash' => int, 'themes' => [ChatTheme, ChatTheme]];
```  


Or, if you're into Lua:

```lua
account_chatThemes={_='account.chatThemes', hash=int, themes={ChatTheme}}

```


