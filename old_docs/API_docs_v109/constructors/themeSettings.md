---
title: themeSettings
description: themeSettings attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: themeSettings  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|base\_theme|[BaseTheme](../types/BaseTheme.md) | Yes|
|accent\_color|[int](../types/int.md) | Yes|
|message\_top\_color|[int](../types/int.md) | Optional|
|message\_bottom\_color|[int](../types/int.md) | Optional|
|wallpaper|[WallPaper](../types/WallPaper.md) | Optional|



### Type: [ThemeSettings](../types/ThemeSettings.md)


### Example:

```php
$themeSettings = ['_' => 'themeSettings', 'base_theme' => BaseTheme, 'accent_color' => int, 'message_top_color' => int, 'message_bottom_color' => int, 'wallpaper' => WallPaper];
```  


Or, if you're into Lua:

```lua
themeSettings={_='themeSettings', base_theme=BaseTheme, accent_color=int, message_top_color=int, message_bottom_color=int, wallpaper=WallPaper}

```


