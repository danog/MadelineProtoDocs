---
title: inputPhoto
description: Photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhoto  
[Back to constructors index](index.md)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputPhoto](../types/InputPhoto.md)


### Example:

```php
$inputPhoto = ['_' => 'inputPhoto', 'id' => long, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPhoto", "id": long, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputPhoto={_='inputPhoto', id=long, access_hash=long}

```


