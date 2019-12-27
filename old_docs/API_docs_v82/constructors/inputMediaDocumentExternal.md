---
title: inputMediaDocumentExternal
description: Document that will be downloaded by the telegram servers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDocumentExternal  
[Back to constructors index](index.md)



Document that will be downloaded by the telegram servers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL of the document|
|ttl\_seconds|[int](../types/int.md) | Optional|Self-destruct time to live of document|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaDocumentExternal = ['_' => 'inputMediaDocumentExternal', 'url' => 'string', 'ttl_seconds' => int];
```  


Or, if you're into Lua:

```lua
inputMediaDocumentExternal={_='inputMediaDocumentExternal', url='string', ttl_seconds=int}

```


