---
title: inputWebFileLocation
description: Location of a remote HTTP(s) file
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebFileLocation  
[Back to constructors index](index.md)



Location of a remote HTTP(s) file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|HTTP URL of file|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputWebFileLocation](../types/InputWebFileLocation.md)


### Example:

```php
$inputWebFileLocation = ['_' => 'inputWebFileLocation', 'url' => 'string', 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputWebFileLocation={_='inputWebFileLocation', url='string', access_hash=long}

```


