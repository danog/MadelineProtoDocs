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
|voice|[Bool](../types/Bool.md) | Optional|Voice?|
|duration|[int](../types/int.md) | Optional|Duration|
|title|[string](../types/string.md) | Optional|Title|
|performer|[string](../types/string.md) | Optional|Performer|
|waveform|[bytes](../types/bytes.md) | Optional|Waveform|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeAudio = ['_' => 'documentAttributeAudio', 'voice' => Bool, 'duration' => int, 'title' => 'string', 'performer' => 'string', 'waveform' => 'bytes'];
```  


Or, if you're into Lua:

```lua
documentAttributeAudio={_='documentAttributeAudio', voice=Bool, duration=int, title='string', performer='string', waveform='bytes'}

```


