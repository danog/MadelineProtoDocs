---
title: "documentAttributeVideo"
description: "Defines a video"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeVideo  
[Back to constructors index](index.md)



Defines a video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|round\_message|[Bool](../types/Bool.md) | Optional|Whether this is a round video|
|supports\_streaming|[Bool](../types/Bool.md) | Optional|Whether the video supports streaming|
|duration|[int](../types/int.md) | Optional|Duration in seconds|
|w|[int](../types/int.md) | Optional|Video width|
|h|[int](../types/int.md) | Optional|Video height|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeVideo = ['_' => 'documentAttributeVideo', 'round_message' => Bool, 'supports_streaming' => Bool, 'duration' => int, 'w' => int, 'h' => int];
```  
