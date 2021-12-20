---
title: "decryptedMessageMediaVenue"
description: "Venue"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaVenue\_46  
[Back to constructors index](index.md)



Venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lat|[double](../types/double.md) | Yes|Latitude of venue|
|long|[double](../types/double.md) | Yes|Longitude of venue|
|title|[string](../types/string.md) | Yes|Venue name|
|address|[string](../types/string.md) | Yes|Address|
|provider|[string](../types/string.md) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](../types/string.md) | Yes|Venue ID in the provider's database|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaVenue_46 = ['_' => 'decryptedMessageMediaVenue', 'lat' => double, 'long' => double, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string'];
```  


Or, if you're into Lua:

```lua
decryptedMessageMediaVenue_46={_='decryptedMessageMediaVenue', lat=double, long=double, title='string', address='string', provider='string', venue_id='string'}

```


