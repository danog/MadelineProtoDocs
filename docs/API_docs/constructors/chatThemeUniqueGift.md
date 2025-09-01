---
title: "chatThemeUniqueGift"
description: "chatThemeUniqueGift attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatThemeUniqueGift  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|theme\_settings|Array of [ThemeSettings](/API_docs/types/ThemeSettings.html) | Yes|



### Type: [ChatTheme](/API_docs/types/ChatTheme.html)


### Example:

```
$chatThemeUniqueGift = ['_' => 'chatThemeUniqueGift', 'gift' => StarGift, 'theme_settings' => [ThemeSettings, ThemeSettings]];
```  
