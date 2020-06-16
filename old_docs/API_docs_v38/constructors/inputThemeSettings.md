---
title: inputThemeSettings
description: Theme settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputThemeSettings  
[Back to constructors index](index.md)



Theme settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|base\_theme|[BaseTheme](../types/BaseTheme.md) | Yes|Default theme on which this theme is based|
|accent\_color|[int](../types/int.md) | Yes|Accent color, RGB24 format|
|message\_top\_color|[int](../types/int.md) | Optional|Message gradient color (top), RGB24 format|
|message\_bottom\_color|[int](../types/int.md) | Optional|Message gradient color (bottom), RGB24 format|
|wallpaper|[InputWallPaper](../types/InputWallPaper.md) | Optional|Wallpaper|
|wallpaper\_settings|[WallPaperSettings](../types/WallPaperSettings.md) | Optional|Wallpaper settings|



### Type: [InputThemeSettings](../types/InputThemeSettings.md)


### Example:

```php
$inputThemeSettings = ['_' => 'inputThemeSettings', 'base_theme' => BaseTheme, 'accent_color' => int, 'message_top_color' => int, 'message_bottom_color' => int, 'wallpaper' => InputWallPaper, 'wallpaper_settings' => WallPaperSettings];
```  


Or, if you're into Lua:

```lua
inputThemeSettings={_='inputThemeSettings', base_theme=BaseTheme, accent_color=int, message_top_color=int, message_bottom_color=int, wallpaper=InputWallPaper, wallpaper_settings=WallPaperSettings}

```


