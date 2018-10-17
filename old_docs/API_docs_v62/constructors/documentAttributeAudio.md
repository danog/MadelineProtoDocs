---
title: documentAttributeAudio
description: documentAttributeAudio attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeAudio  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|voice|[Bool](../types/Bool.md) | Optional|
|duration|[int](../types/int.md) | Optional|
|title|[string](../types/string.md) | Optional|
|performer|[string](../types/string.md) | Optional|
|waveform|[bytes](../types/bytes.md) | Optional|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeAudio = ['_' => 'documentAttributeAudio', 'voice' => Bool, 'duration' => int, 'title' => 'string', 'performer' => 'string', 'waveform' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "documentAttributeAudio", "voice": Bool, "duration": int, "title": "string", "performer": "string", "waveform": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
documentAttributeAudio={_='documentAttributeAudio', voice=Bool, duration=int, title='string', performer='string', waveform='bytes'}

```


