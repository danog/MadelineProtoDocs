---
title: inputBotInlineMessageMediaVenue
description: Bot inline message media venue
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaVenue  
[Back to constructors index](index.md)



Bot inline message media venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geo point|
|title|[string](../types/string.md) | Yes|Title|
|address|[string](../types/string.md) | Yes|Address|
|provider|[string](../types/string.md) | Yes|Provider|
|venue\_id|[string](../types/string.md) | Yes|Venue ID|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Reply markup|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageMediaVenue = ['_' => 'inputBotInlineMessageMediaVenue', 'geo_point' => InputGeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'reply_markup' => ReplyMarkup];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputBotInlineMessageMediaVenue", "geo_point": InputGeoPoint, "title": "string", "address": "string", "provider": "string", "venue_id": "string", "reply_markup": ReplyMarkup}
```


Or, if you're into Lua:

```lua
inputBotInlineMessageMediaVenue={_='inputBotInlineMessageMediaVenue', geo_point=InputGeoPoint, title='string', address='string', provider='string', venue_id='string', reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


