---
title: "botAppSettings"
description: "Mini app » settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botAppSettings  
[Back to constructors index](/API_docs/constructors/index.html)



[Mini app »](https://core.telegram.org/api/bots/webapps) settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|placeholder\_path|[bytes](/API_docs/types/bytes.html) | Optional|SVG placeholder logo, compressed using the same format used for [vector thumbnails »](https://core.telegram.org/api/files#vector-thumbnails).|
|background\_color|[int](/API_docs/types/int.html) | Optional|Default light mode background color|
|background\_dark\_color|[int](/API_docs/types/int.html) | Optional|Default dark mode background color|
|header\_color|[int](/API_docs/types/int.html) | Optional|Default light mode header color|
|header\_dark\_color|[int](/API_docs/types/int.html) | Optional|Default dark mode header color|



### Type: [BotAppSettings](/API_docs/types/BotAppSettings.html)


### Example:

```
$botAppSettings = ['_' => 'botAppSettings', 'placeholder_path' => 'bytes', 'background_color' => int, 'background_dark_color' => int, 'header_color' => int, 'header_dark_color' => int];
```  
