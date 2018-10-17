---
title: messageMediaVenue
description: messageMediaVenue attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaVenue  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|
|title|[string](../types/string.md) | Yes|
|address|[string](../types/string.md) | Yes|
|provider|[string](../types/string.md) | Yes|
|venue\_id|[string](../types/string.md) | Yes|
|venue\_type|[string](../types/string.md) | Yes|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaVenue = ['_' => 'messageMediaVenue', 'geo' => GeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageMediaVenue", "geo": GeoPoint, "title": "string", "address": "string", "provider": "string", "venue_id": "string", "venue_type": "string"}
```


Or, if you're into Lua:

```lua
messageMediaVenue={_='messageMediaVenue', geo=GeoPoint, title='string', address='string', provider='string', venue_id='string', venue_type='string'}

```


