---
title: inputVideoFileLocation
description: inputVideoFileLocation attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputVideoFileLocation  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|



### Type: [InputFileLocation](../types/InputFileLocation.md)


### Example:

```php
$inputVideoFileLocation = ['_' => 'inputVideoFileLocation', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputVideoFileLocation", "id": long, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputVideoFileLocation={_='inputVideoFileLocation', id=long, access_hash=long}

```


