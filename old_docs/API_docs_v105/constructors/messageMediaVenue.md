---
title: messageMediaVenue
description: Message media venue
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaVenue  
[Back to constructors index](index.md)



Message media venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geo|
|title|[string](../types/string.md) | Yes|Title|
|address|[string](../types/string.md) | Yes|Address|
|provider|[string](../types/string.md) | Yes|Provider|
|venue\_id|[string](../types/string.md) | Yes|Venue ID|
|venue\_type|[string](../types/string.md) | Yes|Venue type|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaVenue = ['_' => 'messageMediaVenue', 'geo' => GeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string'];
```  


Or, if you're into Lua:

```lua
messageMediaVenue={_='messageMediaVenue', geo=GeoPoint, title='string', address='string', provider='string', venue_id='string', venue_type='string'}

```


