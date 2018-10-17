---
title: inputMediaDocument
description: inputMediaDocument attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDocument  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|
|caption|[string](../types/string.md) | Yes|
|ttl\_seconds|[int](../types/int.md) | Optional|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaDocument = ['_' => 'inputMediaDocument', 'id' => InputDocument, 'caption' => 'string', 'ttl_seconds' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaDocument", "id": InputDocument, "caption": "string", "ttl_seconds": int}
```


Or, if you're into Lua:

```lua
inputMediaDocument={_='inputMediaDocument', id=InputDocument, caption='string', ttl_seconds=int}

```


