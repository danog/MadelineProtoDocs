---
title: chatTheme
description: chatTheme attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatTheme  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|emoticon|[string](../types/string.md) | Yes|
|theme|[Theme](../types/Theme.md) | Yes|
|dark\_theme|[Theme](../types/Theme.md) | Yes|



### Type: [ChatTheme](../types/ChatTheme.md)


### Example:

```php
$chatTheme = ['_' => 'chatTheme', 'emoticon' => 'string', 'theme' => Theme, 'dark_theme' => Theme];
```  


Or, if you're into Lua:

```lua
chatTheme={_='chatTheme', emoticon='string', theme=Theme, dark_theme=Theme}

```


