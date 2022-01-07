---
title: "inputThemeSettings"
description: "Theme settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputThemeSettings  
[Back to constructors index](index.md)



Theme settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message\_colors\_animated|[Bool](../types/Bool.md) | Optional|
|base\_theme|[BaseTheme](../types/BaseTheme.md) | Yes|Default theme on which this theme is based|
|accent\_color|[int](../types/int.md) | Yes|Accent color, RGB24 format|
|outbox\_accent\_color|[int](../types/int.md) | Optional|
|message\_colors|Array of [int](../types/int.md) | Optional|
|wallpaper|[InputWallPaper](../types/InputWallPaper.md) | Optional|Wallpaper|
|wallpaper\_settings|[WallPaperSettings](../types/WallPaperSettings.md) | Optional|Wallpaper settings|



### Type: [InputThemeSettings](../types/InputThemeSettings.md)


### Example:

```php
$inputThemeSettings = ['_' => 'inputThemeSettings', 'message_colors_animated' => Bool, 'base_theme' => BaseTheme, 'accent_color' => int, 'outbox_accent_color' => int, 'message_colors' => [int, int], 'wallpaper' => InputWallPaper, 'wallpaper_settings' => WallPaperSettings];
```  
