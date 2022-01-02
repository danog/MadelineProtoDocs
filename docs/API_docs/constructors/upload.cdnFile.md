---
title: "upload.cdnFile"
description: "Represent a chunk of a CDN file."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/upload_cdnFile.html
---
# Constructor: upload.cdnFile  
[Back to constructors index](index.md)



Represent a chunk of a [CDN](https://core.telegram.org/cdn) file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bytes|[bytes](../types/bytes.md) | Yes|The data|



### Type: [upload.CdnFile](../types/upload.CdnFile.md)


### Example:

```php
$upload_cdnFile = ['_' => 'upload.cdnFile', 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
upload_cdnFile={_='upload.cdnFile', bytes='bytes'}

```


