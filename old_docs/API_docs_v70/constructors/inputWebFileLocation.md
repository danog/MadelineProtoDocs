---
title: inputWebFileLocation
description: Web file location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebFileLocation  
[Back to constructors index](index.md)



Web file location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputWebFileLocation](../types/InputWebFileLocation.md)


### Example:

```php
$inputWebFileLocation = ['_' => 'inputWebFileLocation', 'url' => 'string', 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputWebFileLocation", "url": "string", "access_hash": long}
```


Or, if you're into Lua:

```lua
inputWebFileLocation={_='inputWebFileLocation', url='string', access_hash=long}

```


