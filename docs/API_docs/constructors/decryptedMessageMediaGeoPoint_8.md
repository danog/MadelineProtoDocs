---
title: decryptedMessageMediaGeoPoint
description: Decrypted message media geo point
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaGeoPoint\_8  
[Back to constructors index](index.md)



Decrypted message media geo point

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lat|[double](../types/double.md) | Yes|Lat|
|long|[double](../types/double.md) | Yes|Long|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaGeoPoint_8 = ['_' => 'decryptedMessageMediaGeoPoint', 'lat' => double, 'long' => double];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaGeoPoint", "lat": double, "long": double}
```


Or, if you're into Lua:

```lua
decryptedMessageMediaGeoPoint_8={_='decryptedMessageMediaGeoPoint', lat=double, long=double}

```


