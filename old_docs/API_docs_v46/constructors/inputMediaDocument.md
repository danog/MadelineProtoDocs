---
title: inputMediaDocument
description: Media document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDocument  
[Back to constructors index](index.md)



Media document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document\_id|[MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|Document ID|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaDocument = ['_' => 'inputMediaDocument', 'document_id' => InputDocument, 'caption' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaDocument", "document_id": InputDocument, "caption": "string"}
```


Or, if you're into Lua:

```lua
inputMediaDocument={_='inputMediaDocument', document_id=InputDocument, caption='string'}

```


