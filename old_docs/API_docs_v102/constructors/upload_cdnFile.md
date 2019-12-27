---
title: upload.cdnFile
description: Represent a chunk of a [CDN](https://core.telegram.org/cdn) file.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: upload.cdnFile  
[Back to constructors index](index.md)



Represent a chunk of a [CDN](https://core.telegram.org/cdn) file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bytes|[bytes](../types/bytes.md) | Yes|The data|



### Type: [upload\_CdnFile](../types/upload_CdnFile.md)


### Example:

```php
$upload_cdnFile = ['_' => 'upload.cdnFile', 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
upload_cdnFile={_='upload.cdnFile', bytes='bytes'}

```


