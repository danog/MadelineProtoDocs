---
title: "documentAttributeVideo"
description: "Defines a video"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeVideo\_23  
[Back to constructors index](index.md)



Defines a video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](../types/int.md) | Optional|Duration in seconds|
|w|[int](../types/int.md) | Optional|Video width|
|h|[int](../types/int.md) | Optional|Video height|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeVideo_23 = ['_' => 'documentAttributeVideo', 'duration' => int, 'w' => int, 'h' => int];
```  


Or, if you're into Lua:

```lua
documentAttributeVideo_23={_='documentAttributeVideo', duration=int, w=int, h=int}

```


