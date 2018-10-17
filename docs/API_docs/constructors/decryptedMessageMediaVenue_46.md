---
title: decryptedMessageMediaVenue
description: decryptedMessageMediaVenue attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaVenue\_46  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|lat|[double](../types/double.md) | Yes|
|long|[double](../types/double.md) | Yes|
|title|[string](../types/string.md) | Yes|
|address|[string](../types/string.md) | Yes|
|provider|[string](../types/string.md) | Yes|
|venue\_id|[string](../types/string.md) | Yes|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaVenue_46 = ['_' => 'decryptedMessageMediaVenue', 'lat' => double, 'long' => double, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaVenue", "lat": double, "long": double, "title": "string", "address": "string", "provider": "string", "venue_id": "string"}
```


Or, if you're into Lua:

```lua
decryptedMessageMediaVenue_46={_='decryptedMessageMediaVenue', lat=double, long=double, title='string', address='string', provider='string', venue_id='string'}

```


