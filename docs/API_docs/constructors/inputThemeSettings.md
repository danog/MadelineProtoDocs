---
title: "inputThemeSettings"
description: "Theme settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputThemeSettings  
[Back to constructors index](/API_docs/constructors/index.md)



Theme settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message\_colors\_animated|[Bool](/API_docs/types/Bool.md) | Optional|
|base\_theme|[BaseTheme](/API_docs/types/BaseTheme.md) | Yes|Default theme on which this theme is based|
|accent\_color|[int](/API_docs/types/int.md) | Yes|Accent color, RGB24 format|
|outbox\_accent\_color|[int](/API_docs/types/int.md) | Optional|
|message\_colors|Array of [int](/API_docs/types/int.md) | Optional|
|wallpaper|[InputWallPaper](/API_docs/types/InputWallPaper.md) | Optional|Wallpaper|
|wallpaper\_settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.md) | Optional|Wallpaper settings|



### Type: [InputThemeSettings](/API_docs/types/InputThemeSettings.md)


### Example:

```php
$inputThemeSettings = ['_' => 'inputThemeSettings', 'message_colors_animated' => Bool, 'base_theme' => BaseTheme, 'accent_color' => int, 'outbox_accent_color' => int, 'message_colors' => [int, int], 'wallpaper' => InputWallPaper, 'wallpaper_settings' => WallPaperSettings];
```  
