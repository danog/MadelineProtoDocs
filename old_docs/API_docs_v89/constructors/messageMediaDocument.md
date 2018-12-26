---
title: messageMediaDocument
description: Message media document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaDocument  
[Back to constructors index](index.md)



Message media document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document|[Document](../types/Document.md) | Optional|Document|
|ttl\_seconds|[int](../types/int.md) | Optional|Ttl seconds|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaDocument = ['_' => 'messageMediaDocument', 'document' => Document, 'ttl_seconds' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageMediaDocument", "document": Document, "ttl_seconds": int}
```


Or, if you're into Lua:

```lua
messageMediaDocument={_='messageMediaDocument', document=Document, ttl_seconds=int}

```


