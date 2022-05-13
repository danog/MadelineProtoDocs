---
title: "themeSettings"
description: "Theme settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: themeSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Theme settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message\_colors\_animated|[Bool](/API_docs/types/Bool.html) | Optional|If set, the freeform gradient fill needs to be animated on every sent message.|
|base\_theme|[BaseTheme](/API_docs/types/BaseTheme.html) | Yes|Base theme|
|accent\_color|[int](/API_docs/types/int.html) | Yes|Accent color, ARGB format|
|outbox\_accent\_color|[int](/API_docs/types/int.html) | Optional|Accent color of outgoing messages in ARGB format|
|message\_colors|Array of [int](/API_docs/types/int.html) | Optional|The fill to be used as a background for outgoing messages, in RGB24 format. <br>If just one or two equal colors are provided, describes a solid fill of a background. <br>If two different colors are provided, describes the top and bottom colors of a 0-degree gradient.<br>If three or four colors are provided, describes a freeform gradient fill of a background.|
|wallpaper|[WallPaper](/API_docs/types/WallPaper.html) | Optional|Wallpaper|



### Type: [ThemeSettings](/API_docs/types/ThemeSettings.html)


### Example:

```
$themeSettings = ['_' => 'themeSettings', 'message_colors_animated' => Bool, 'base_theme' => BaseTheme, 'accent_color' => int, 'outbox_accent_color' => int, 'message_colors' => [int, int], 'wallpaper' => WallPaper];
```  
