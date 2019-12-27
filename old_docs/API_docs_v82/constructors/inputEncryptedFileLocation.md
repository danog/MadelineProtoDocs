---
title: inputEncryptedFileLocation
description: Location of encrypted secret chat file.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFileLocation  
[Back to constructors index](index.md)



Location of encrypted secret chat file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|File ID, **id** parameter value from [encryptedFile](../constructors/encryptedFile.md)|
|access\_hash|[long](../types/long.md) | Yes|Checksum, **access\_hash** parameter value from [encryptedFile](../constructors/encryptedFile.md)|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputEncryptedFileLocation = ['_' => 'inputEncryptedFileLocation', 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputEncryptedFileLocation={_='inputEncryptedFileLocation', id=long, access_hash=long}

```


