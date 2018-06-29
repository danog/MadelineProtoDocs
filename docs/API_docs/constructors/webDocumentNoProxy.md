---
title: webDocumentNoProxy
description: webDocumentNoProxy attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webDocumentNoProxy  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|url|[string](../types/string.md) | Yes|
|size|[int](../types/int.md) | Yes|
|mime\_type|[string](../types/string.md) | Yes|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|



### Type: [WebDocument](../types/WebDocument.md)


### Example:

```
$webDocumentNoProxy = ['_' => 'webDocumentNoProxy', 'url' => 'string', 'size' => int, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "webDocumentNoProxy", "url": "string", "size": int, "mime_type": "string", "attributes": [DocumentAttribute]}
```


Or, if you're into Lua:  


```
webDocumentNoProxy={_='webDocumentNoProxy', url='string', size=int, mime_type='string', attributes={DocumentAttribute}}

```


