---
title: upload.cdnFileReuploadNeeded
description: upload_cdnFileReuploadNeeded attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: upload.cdnFileReuploadNeeded  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|request\_token|[bytes](../types/bytes.md) | Yes|



### Type: [upload\_CdnFile](../types/upload_CdnFile.md)


### Example:

```
$upload_cdnFileReuploadNeeded = ['_' => 'upload.cdnFileReuploadNeeded', 'request_token' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "upload.cdnFileReuploadNeeded", "request_token": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:  


```
upload_cdnFileReuploadNeeded={_='upload.cdnFileReuploadNeeded', request_token='bytes'}

```


