---
title: upload.cdnFile
description: upload_cdnFile attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: upload.cdnFile  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bytes|[bytes](../types/bytes.md) | Yes|



### Type: [upload\_CdnFile](../types/upload_CdnFile.md)


### Example:

```
$upload_cdnFile = ['_' => 'upload.cdnFile', 'bytes' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "upload.cdnFile", "bytes": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:  


```
upload_cdnFile={_='upload.cdnFile', bytes='bytes'}

```


