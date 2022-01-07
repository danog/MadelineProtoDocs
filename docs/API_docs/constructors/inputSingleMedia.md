---
title: "inputSingleMedia"
description: "A single media in an album or grouped media sent with messages.sendMultiMedia."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSingleMedia  
[Back to constructors index](/API_docs/constructors/index.md)



A single media in an [album or grouped media](https://core.telegram.org/api/files#albums-grouped-media) sent with [messages.sendMultiMedia](../methods/messages.sendMultiMedia.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|media|[MessageMedia, Message, Update or InputMedia](/API_docs/types/InputMedia.md) | Optional|The media|
|message|[string](/API_docs/types/string.md) | Yes|A caption for the media|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.md) | Optional|Message [entities](https://core.telegram.org/api/entities) for styled text|



### Type: [InputSingleMedia](/API_docs/types/InputSingleMedia.md)


### Example:

```php
$inputSingleMedia = ['_' => 'inputSingleMedia', 'media' => InputMedia, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  
