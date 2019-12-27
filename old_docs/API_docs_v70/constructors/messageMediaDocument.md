---
title: messageMediaDocument
description: Document (video, audio, voice, sticker, any media type except photo)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaDocument  
[Back to constructors index](index.md)



Document (video, audio, voice, sticker, any media type except photo)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document|[Document](../types/Document.md) | Optional|Attached document|
|caption|[string](../types/string.md) | Optional|Caption|
|ttl\_seconds|[int](../types/int.md) | Optional|Time to live of self-destructing document|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaDocument = ['_' => 'messageMediaDocument', 'document' => Document, 'caption' => 'string', 'ttl_seconds' => int];
```  


Or, if you're into Lua:

```lua
messageMediaDocument={_='messageMediaDocument', document=Document, caption='string', ttl_seconds=int}

```


