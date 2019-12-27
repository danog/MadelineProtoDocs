---
title: documentAttributeVideo
description: Defines a video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeVideo  
[Back to constructors index](index.md)



Defines a video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|round\_message|[Bool](../types/Bool.md) | Optional|Whether this is a round video|
|duration|[int](../types/int.md) | Optional|Duration in seconds|
|w|[int](../types/int.md) | Optional|Video width|
|h|[int](../types/int.md) | Optional|Video height|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeVideo = ['_' => 'documentAttributeVideo', 'round_message' => Bool, 'duration' => int, 'w' => int, 'h' => int];
```  


Or, if you're into Lua:

```lua
documentAttributeVideo={_='documentAttributeVideo', round_message=Bool, duration=int, w=int, h=int}

```


