---
title: "inputSecureFileLocation"
description: "Location of encrypted telegram passport file."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFileLocation  
[Back to constructors index](index.md)



Location of encrypted telegram [passport](https://core.telegram.org/passport) file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|File ID, **id** parameter value from [secureFile](../constructors/secureFile.md)|
|access\_hash|[long](../types/long.md) | Yes|Checksum, **access\_hash** parameter value from [secureFile](../constructors/secureFile.md)|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputSecureFileLocation = ['_' => 'inputSecureFileLocation', 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputSecureFileLocation={_='inputSecureFileLocation', id=long, access_hash=long}

```


