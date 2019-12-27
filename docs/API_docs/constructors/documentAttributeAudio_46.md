---
title: documentAttributeAudio
description: Represents an audio file
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeAudio\_46  
[Back to constructors index](index.md)



Represents an audio file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](../types/int.md) | Optional|Duration in seconds|
|title|[string](../types/string.md) | Yes|Name of song|
|performer|[string](../types/string.md) | Yes|Performer|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeAudio_46 = ['_' => 'documentAttributeAudio', 'duration' => int, 'title' => 'string', 'performer' => 'string'];
```  


Or, if you're into Lua:

```lua
documentAttributeAudio_46={_='documentAttributeAudio', duration=int, title='string', performer='string'}

```


