---
title: "autoSaveSettings"
description: "Media autosave settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: autoSaveSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Media autosave settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photos|[Bool](/API_docs/types/Bool.html) | Optional|Whether photos should be autosaved to the gallery.|
|videos|[Bool](/API_docs/types/Bool.html) | Optional|Whether videos should be autosaved to the gallery.|
|video\_max\_size|[long](/API_docs/types/long.html) | Optional|If set, specifies a size limit for autosavable videos|



### Type: [AutoSaveSettings](/API_docs/types/AutoSaveSettings.html)


### Example:

```
$autoSaveSettings = ['_' => 'autoSaveSettings', 'photos' => Bool, 'videos' => Bool, 'video_max_size' => long];
```  
