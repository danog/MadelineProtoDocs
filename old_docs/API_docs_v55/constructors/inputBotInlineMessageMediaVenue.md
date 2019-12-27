---
title: inputBotInlineMessageMediaVenue
description: Venue
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaVenue  
[Back to constructors index](index.md)



Venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geolocation|
|title|[string](../types/string.md) | Yes|Venue name|
|address|[string](../types/string.md) | Yes|Address|
|provider|[string](../types/string.md) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](../types/string.md) | Yes|Venue ID in the provider's database|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Inline keyboard|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageMediaVenue = ['_' => 'inputBotInlineMessageMediaVenue', 'geo_point' => InputGeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
inputBotInlineMessageMediaVenue={_='inputBotInlineMessageMediaVenue', geo_point=InputGeoPoint, title='string', address='string', provider='string', venue_id='string', reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


