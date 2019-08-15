---
title: inputSecureFile
description: Secure file
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFile  
[Back to constructors index](index.md)



Secure file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputSecureFile](../types/InputSecureFile.md)


### Example:

```php
$inputSecureFile = ['_' => 'inputSecureFile', 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputSecureFile={_='inputSecureFile', id=long, access_hash=long}

```


