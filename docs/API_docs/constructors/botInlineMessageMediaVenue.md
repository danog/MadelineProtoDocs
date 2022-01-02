---
title: "botInlineMessageMediaVenue"
description: "Send a venue"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaVenue  
[Back to constructors index](index.md)



Send a venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geolocation of venue|
|title|[string](../types/string.md) | Yes|Venue name|
|address|[string](../types/string.md) | Yes|Address|
|provider|[string](../types/string.md) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](../types/string.md) | Yes|Venue ID in the provider's database|
|venue\_type|[string](../types/string.md) | Yes|Venue type in the provider's database|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Inline keyboard|



### Type: [BotInlineMessage](../types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageMediaVenue = ['_' => 'botInlineMessageMediaVenue', 'geo' => GeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string', 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
botInlineMessageMediaVenue={_='botInlineMessageMediaVenue', geo=GeoPoint, title='string', address='string', provider='string', venue_id='string', venue_type='string', reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


