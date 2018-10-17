---
title: documentAttributeVideo
description: documentAttributeVideo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeVideo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|round\_message|[Bool](../types/Bool.md) | Optional|
|supports\_streaming|[Bool](../types/Bool.md) | Optional|
|duration|[int](../types/int.md) | Optional|
|w|[int](../types/int.md) | Optional|
|h|[int](../types/int.md) | Optional|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeVideo = ['_' => 'documentAttributeVideo', 'round_message' => Bool, 'supports_streaming' => Bool, 'duration' => int, 'w' => int, 'h' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "documentAttributeVideo", "round_message": Bool, "supports_streaming": Bool, "duration": int, "w": int, "h": int}
```


Or, if you're into Lua:

```lua
documentAttributeVideo={_='documentAttributeVideo', round_message=Bool, supports_streaming=Bool, duration=int, w=int, h=int}

```


