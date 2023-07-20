---
title: "autoDownloadSettings"
description: "Autodownload settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: autoDownloadSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Autodownload settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|disabled|[Bool](/API_docs/types/Bool.html) | Optional|Disable automatic media downloads?|
|video\_preload\_large|[Bool](/API_docs/types/Bool.html) | Optional|Whether to preload the first seconds of videos larger than the specified limit|
|audio\_preload\_next|[Bool](/API_docs/types/Bool.html) | Optional|Whether to preload the next audio track when you're listening to music|
|phonecalls\_less\_data|[Bool](/API_docs/types/Bool.html) | Optional|Whether to enable data saving mode in phone calls|
|stories\_preload|[Bool](/API_docs/types/Bool.html) | Optional|
|photo\_size\_max|[int](/API_docs/types/int.html) | Yes|Maximum size of photos to preload|
|video\_size\_max|[long](/API_docs/types/long.html) | Yes|Maximum size of videos to preload|
|file\_size\_max|[long](/API_docs/types/long.html) | Yes|Maximum size of other files to preload|
|video\_upload\_maxbitrate|[int](/API_docs/types/int.html) | Yes|Maximum suggested bitrate for **uploading** videos|
|small\_queue\_active\_operations\_max|[int](/API_docs/types/int.html) | Yes|
|large\_queue\_active\_operations\_max|[int](/API_docs/types/int.html) | Yes|



### Type: [AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.html)


### Example:

```
$autoDownloadSettings = ['_' => 'autoDownloadSettings', 'disabled' => Bool, 'video_preload_large' => Bool, 'audio_preload_next' => Bool, 'phonecalls_less_data' => Bool, 'stories_preload' => Bool, 'photo_size_max' => int, 'video_size_max' => long, 'file_size_max' => long, 'video_upload_maxbitrate' => int, 'small_queue_active_operations_max' => int, 'large_queue_active_operations_max' => int];
```  
