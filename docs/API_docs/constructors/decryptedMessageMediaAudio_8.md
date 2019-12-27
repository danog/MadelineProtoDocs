---
title: decryptedMessageMediaAudio
description: Audio file attached to a secret chat message.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaAudio\_8  
[Back to constructors index](index.md)



Audio file attached to a secret chat message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|duration|[int](../types/int.md) | Yes|Audio duration in seconds|
|size|[int](../types/int.md) | Yes|File size|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaAudio_8 = ['_' => 'decryptedMessageMediaAudio', 'duration' => int, 'size' => int];
```  


Or, if you're into Lua:

```lua
decryptedMessageMediaAudio_8={_='decryptedMessageMediaAudio', duration=int, size=int}

```


