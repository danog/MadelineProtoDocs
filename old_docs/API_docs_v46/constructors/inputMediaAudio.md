---
title: inputMediaAudio
description: Media audio
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaAudio  
[Back to constructors index](index.md)



Media audio

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|audio|[InputAudio](../types/InputAudio.md) | Optional|Audio|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaAudio = ['_' => 'inputMediaAudio', 'audio' => InputAudio];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaAudio", "audio": InputAudio}
```


Or, if you're into Lua:

```lua
inputMediaAudio={_='inputMediaAudio', audio=InputAudio}

```


