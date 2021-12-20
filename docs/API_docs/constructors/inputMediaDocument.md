---
title: "inputMediaDocument"
description: "Forwarded document"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDocument  
[Back to constructors index](index.md)



Forwarded document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|The document to be forwarded.|
|ttl\_seconds|[int](../types/int.md) | Optional|Time to live of self-destructing document|
|query|[string](../types/string.md) | Optional|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaDocument = ['_' => 'inputMediaDocument', 'id' => InputDocument, 'ttl_seconds' => int, 'query' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaDocument={_='inputMediaDocument', id=InputDocument, ttl_seconds=int, query='string'}

```


