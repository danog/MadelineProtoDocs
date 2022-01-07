---
title: "documentAttributeVideo"
description: "Defines a video"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeVideo  
[Back to constructors index](/API_docs/constructors/index.md)



Defines a video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|round\_message|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is a round video|
|supports\_streaming|[Bool](/API_docs/types/Bool.md) | Optional|Whether the video supports streaming|
|duration|[int](/API_docs/types/int.md) | Optional|Duration in seconds|
|w|[int](/API_docs/types/int.md) | Optional|Video width|
|h|[int](/API_docs/types/int.md) | Optional|Video height|



### Type: [DocumentAttribute](/API_docs/types/DocumentAttribute.md)


### Example:

```php
$documentAttributeVideo = ['_' => 'documentAttributeVideo', 'round_message' => Bool, 'supports_streaming' => Bool, 'duration' => int, 'w' => int, 'h' => int];
```  
