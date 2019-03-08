---
title: inputDocumentFileLocation
description: Document file location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputDocumentFileLocation  
[Back to constructors index](index.md)



Document file location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|file\_reference|[bytes](../types/bytes.md) | Yes|File reference|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputDocumentFileLocation = ['_' => 'inputDocumentFileLocation', 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputDocumentFileLocation", "id": long, "access_hash": long, "file_reference": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
inputDocumentFileLocation={_='inputDocumentFileLocation', id=long, access_hash=long, file_reference='bytes'}

```


