---
title: documentAttributeAudio
description: Document attribute audio
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeAudio  
[Back to constructors index](index.md)



Document attribute audio

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](../types/int.md) | Optional|Duration|
|title|[string](../types/string.md) | Yes|Title|
|performer|[string](../types/string.md) | Yes|Performer|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeAudio = ['_' => 'documentAttributeAudio', 'duration' => int, 'title' => 'string', 'performer' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "documentAttributeAudio", "duration": int, "title": "string", "performer": "string"}
```


Or, if you're into Lua:

```lua
documentAttributeAudio={_='documentAttributeAudio', duration=int, title='string', performer='string'}

```


