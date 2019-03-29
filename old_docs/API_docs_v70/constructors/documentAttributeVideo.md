---
title: documentAttributeVideo
description: Document attribute video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeVideo  
[Back to constructors index](index.md)



Document attribute video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|round\_message|[Bool](../types/Bool.md) | Optional|Round message?|
|duration|[int](../types/int.md) | Optional|Duration|
|w|[int](../types/int.md) | Optional|Width|
|h|[int](../types/int.md) | Optional|Height|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeVideo = ['_' => 'documentAttributeVideo', 'round_message' => Bool, 'duration' => int, 'w' => int, 'h' => int];
```  


Or, if you're into Lua:

```lua
documentAttributeVideo={_='documentAttributeVideo', round_message=Bool, duration=int, w=int, h=int}

```


