---
title: themeSettings
description: Theme settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: themeSettings  
[Back to constructors index](index.md)



Theme settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|base\_theme|[BaseTheme](../types/BaseTheme.md) | Yes|Base theme|
|accent\_color|[int](../types/int.md) | Yes|Accent color, RGB24 format|
|message\_top\_color|[int](../types/int.md) | Optional|Message gradient color (top), RGB24 format|
|message\_bottom\_color|[int](../types/int.md) | Optional|Message gradient color (bottom), RGB24 format|
|wallpaper|[WallPaper](../types/WallPaper.md) | Optional|Wallpaper|



### Type: [ThemeSettings](../types/ThemeSettings.md)


### Example:

```php
$themeSettings = ['_' => 'themeSettings', 'base_theme' => BaseTheme, 'accent_color' => int, 'message_top_color' => int, 'message_bottom_color' => int, 'wallpaper' => WallPaper];
```  


Or, if you're into Lua:

```lua
themeSettings={_='themeSettings', base_theme=BaseTheme, accent_color=int, message_top_color=int, message_bottom_color=int, wallpaper=WallPaper}

```


