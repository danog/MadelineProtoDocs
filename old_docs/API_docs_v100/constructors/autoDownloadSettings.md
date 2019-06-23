---
title: autoDownloadSettings
description: Autodownload settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: autoDownloadSettings  
[Back to constructors index](index.md)



Autodownload settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|disabled|[Bool](../types/Bool.md) | Optional|Disabled?|
|video\_preload\_large|[Bool](../types/Bool.md) | Optional|Preload large videos?|
|audio\_preload\_next|[Bool](../types/Bool.md) | Optional|Preload audios?|
|phonecalls\_less\_data|[Bool](../types/Bool.md) | Optional|Use less data in phonecalls?|
|photo\_size\_max|[int](../types/int.md) | Yes|Maximum photo file size to preload|
|video\_size\_max|[int](../types/int.md) | Yes|Maximum video file size to preload|
|file\_size\_max|[int](../types/int.md) | Yes|Maximum file size to preload|



### Type: [AutoDownloadSettings](../types/AutoDownloadSettings.md)


### Example:

```php
$autoDownloadSettings = ['_' => 'autoDownloadSettings', 'disabled' => Bool, 'video_preload_large' => Bool, 'audio_preload_next' => Bool, 'phonecalls_less_data' => Bool, 'photo_size_max' => int, 'video_size_max' => int, 'file_size_max' => int];
```  


Or, if you're into Lua:

```lua
autoDownloadSettings={_='autoDownloadSettings', disabled=Bool, video_preload_large=Bool, audio_preload_next=Bool, phonecalls_less_data=Bool, photo_size_max=int, video_size_max=int, file_size_max=int}

```


