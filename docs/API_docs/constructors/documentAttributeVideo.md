---
title: "documentAttributeVideo"
description: "Defines a video"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeVideo  
[Back to constructors index](/API_docs/constructors/index.html)



Defines a video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|round\_message|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a round video|
|supports\_streaming|[Bool](/API_docs/types/Bool.html) | Optional|Whether the video supports streaming|
|nosound|[Bool](/API_docs/types/Bool.html) | Optional|
|duration|[double](/API_docs/types/double.html) | Optional|
|w|[int](/API_docs/types/int.html) | Optional|Video width|
|h|[int](/API_docs/types/int.html) | Optional|Video height|
|preload\_prefix\_size|[int](/API_docs/types/int.html) | Optional|



### Type: [DocumentAttribute](/API_docs/types/DocumentAttribute.html)


### Example:

```
$documentAttributeVideo = ['_' => 'documentAttributeVideo', 'round_message' => Bool, 'supports_streaming' => Bool, 'nosound' => Bool, 'duration' => double, 'w' => int, 'h' => int, 'preload_prefix_size' => int];
```  
