---
title: upload.cdnFile
description: Cdn file
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: upload.cdnFile  
[Back to constructors index](index.md)



Cdn file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bytes|[bytes](../types/bytes.md) | Yes|Bytes|



### Type: [upload\_CdnFile](../types/upload_CdnFile.md)


### Example:

```php
$upload_cdnFile = ['_' => 'upload.cdnFile', 'bytes' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "upload.cdnFile", "bytes": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
upload_cdnFile={_='upload.cdnFile', bytes='bytes'}

```


