---
title: inputSingleMedia
description: A single media in an album sent with [messages.sendMultiMedia](../methods/messages.sendMultiMedia.md).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSingleMedia  
[Back to constructors index](index.md)



A single media in an album sent with [messages.sendMultiMedia](../methods/messages.sendMultiMedia.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|media|[MessageMedia, Message, Update or InputMedia](../types/InputMedia.md) | Optional|The media|
|message|[string](../types/string.md) | Yes|A caption for the media|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|Entities|



### Type: [InputSingleMedia](../types/InputSingleMedia.md)


### Example:

```php
$inputSingleMedia = ['_' => 'inputSingleMedia', 'media' => InputMedia, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
inputSingleMedia={_='inputSingleMedia', media=InputMedia, message='string', entities={MessageEntity}}

```


