---
title: "chatThemeUniqueGift"
description: "A chat theme based on a collectible gift »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatThemeUniqueGift  
[Back to constructors index](/API_docs/constructors/index.html)



A chat theme based on a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|The owned collectible gift on which this theme is based, as a [starGiftUnique](../constructors/starGiftUnique.html) constructor.|
|theme\_settings|Array of [ThemeSettings](/API_docs/types/ThemeSettings.html) | Yes|Theme settings.|



### Type: [ChatTheme](/API_docs/types/ChatTheme.html)


### Example:

```
$chatThemeUniqueGift = ['_' => 'chatThemeUniqueGift', 'gift' => StarGift, 'theme_settings' => [ThemeSettings, ThemeSettings]];
```  
