---
title: inputThemeSettings
description: inputThemeSettings attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputThemeSettings  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|base\_theme|[BaseTheme](../types/BaseTheme.md) | Yes|
|accent\_color|[int](../types/int.md) | Yes|
|message\_top\_color|[int](../types/int.md) | Optional|
|message\_bottom\_color|[int](../types/int.md) | Optional|
|wallpaper|[InputWallPaper](../types/InputWallPaper.md) | Optional|
|wallpaper\_settings|[WallPaperSettings](../types/WallPaperSettings.md) | Optional|



### Type: [InputThemeSettings](../types/InputThemeSettings.md)


### Example:

```php
$inputThemeSettings = ['_' => 'inputThemeSettings', 'base_theme' => BaseTheme, 'accent_color' => int, 'message_top_color' => int, 'message_bottom_color' => int, 'wallpaper' => InputWallPaper, 'wallpaper_settings' => WallPaperSettings];
```  


Or, if you're into Lua:

```lua
inputThemeSettings={_='inputThemeSettings', base_theme=BaseTheme, accent_color=int, message_top_color=int, message_bottom_color=int, wallpaper=InputWallPaper, wallpaper_settings=WallPaperSettings}

```


