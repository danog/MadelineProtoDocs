---
title: "autoDownloadSettings"
description: "Autodownload settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: autoDownloadSettings  
[Back to constructors index](index.md)



Autodownload settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|disabled|[Bool](../types/Bool.md) | Optional|Disable automatic media downloads?|
|video\_preload\_large|[Bool](../types/Bool.md) | Optional|Whether to preload the first seconds of videos larger than the specified limit|
|audio\_preload\_next|[Bool](../types/Bool.md) | Optional|Whether to preload the next audio track when you're listening to music|
|phonecalls\_less\_data|[Bool](../types/Bool.md) | Optional|Whether to enable data saving mode in phone calls|
|photo\_size\_max|[int](../types/int.md) | Yes|Maximum size of photos to preload|
|video\_size\_max|[int](../types/int.md) | Yes|Maximum size of videos to preload|
|file\_size\_max|[int](../types/int.md) | Yes|Maximum size of other files to preload|
|video\_upload\_maxbitrate|[int](../types/int.md) | Yes|Maximum suggested bitrate for **uploading** videos|



### Type: [AutoDownloadSettings](../types/AutoDownloadSettings.md)


### Example:

```php
$autoDownloadSettings = ['_' => 'autoDownloadSettings', 'disabled' => Bool, 'video_preload_large' => Bool, 'audio_preload_next' => Bool, 'phonecalls_less_data' => Bool, 'photo_size_max' => int, 'video_size_max' => int, 'file_size_max' => int, 'video_upload_maxbitrate' => int];
```  
