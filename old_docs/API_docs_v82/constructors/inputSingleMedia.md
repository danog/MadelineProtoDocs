---
title: inputSingleMedia
description: Single media
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSingleMedia  
[Back to constructors index](index.md)



Single media

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|media|[MessageMedia, Message, Update or InputMedia](../types/InputMedia.md) | Optional|Media|
|message|[string](../types/string.md) | Yes|Message|
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


