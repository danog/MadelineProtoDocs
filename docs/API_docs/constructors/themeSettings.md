---
title: "themeSettings"
description: "Theme settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: themeSettings  
[Back to constructors index](index.md)



Theme settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message\_colors\_animated|[Bool](../types/Bool.md) | Optional|
|base\_theme|[BaseTheme](../types/BaseTheme.md) | Yes|Base theme|
|accent\_color|[int](../types/int.md) | Yes|Accent color, RGB24 format|
|outbox\_accent\_color|[int](../types/int.md) | Optional|
|message\_colors|Array of [int](../types/int.md) | Optional|
|wallpaper|[WallPaper](../types/WallPaper.md) | Optional|Wallpaper|



### Type: [ThemeSettings](../types/ThemeSettings.md)


### Example:

```php
$themeSettings = ['_' => 'themeSettings', 'message_colors_animated' => Bool, 'base_theme' => BaseTheme, 'accent_color' => int, 'outbox_accent_color' => int, 'message_colors' => [int, int], 'wallpaper' => WallPaper];
```  


Or, if you're into Lua:

```lua
themeSettings={_='themeSettings', message_colors_animated=Bool, base_theme=BaseTheme, accent_color=int, outbox_accent_color=int, message_colors={int}, wallpaper=WallPaper}

```


