---
title: inputSecureFileLocation
description: Secure file location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFileLocation  
[Back to constructors index](index.md)



Secure file location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputSecureFileLocation = ['_' => 'inputSecureFileLocation', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputSecureFileLocation", "id": long, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputSecureFileLocation={_='inputSecureFileLocation', id=long, access_hash=long}

```


