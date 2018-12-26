---
title: inputMediaDocumentExternal
description: Media document external
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDocumentExternal  
[Back to constructors index](index.md)



Media document external

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaDocumentExternal = ['_' => 'inputMediaDocumentExternal', 'url' => 'string', 'caption' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaDocumentExternal", "url": "string", "caption": "string"}
```


Or, if you're into Lua:

```lua
inputMediaDocumentExternal={_='inputMediaDocumentExternal', url='string', caption='string'}

```


