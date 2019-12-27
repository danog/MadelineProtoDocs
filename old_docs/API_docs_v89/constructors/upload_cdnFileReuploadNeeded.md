---
title: upload.cdnFileReuploadNeeded
description: The file was cleared from the temporary RAM cache of the [CDN](https://core.telegram.org/cdn) and has to be reuploaded.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: upload.cdnFileReuploadNeeded  
[Back to constructors index](index.md)



The file was cleared from the temporary RAM cache of the [CDN](https://core.telegram.org/cdn) and has to be reuploaded.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|request\_token|[bytes](../types/bytes.md) | Yes|Request token (see [CDN](https://core.telegram.org/cdn))|



### Type: [upload\_CdnFile](../types/upload_CdnFile.md)


### Example:

```php
$upload_cdnFileReuploadNeeded = ['_' => 'upload.cdnFileReuploadNeeded', 'request_token' => 'bytes'];
```  


Or, if you're into Lua:

```lua
upload_cdnFileReuploadNeeded={_='upload.cdnFileReuploadNeeded', request_token='bytes'}

```


