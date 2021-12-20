---
title: "decryptedMessageMediaGeoPoint"
description: "GeoPont attached to an encrypted message."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaGeoPoint\_8  
[Back to constructors index](index.md)



GeoPont attached to an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lat|[double](../types/double.md) | Yes|Latitude of point|
|long|[double](../types/double.md) | Yes|Longtitude of point|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaGeoPoint_8 = ['_' => 'decryptedMessageMediaGeoPoint', 'lat' => double, 'long' => double];
```  


Or, if you're into Lua:

```lua
decryptedMessageMediaGeoPoint_8={_='decryptedMessageMediaGeoPoint', lat=double, long=double}

```


