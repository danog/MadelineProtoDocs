---
title: "botInlineMessageMediaGeo"
description: "Send a geolocation"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaGeo  
[Back to constructors index](index.md)



Send a geolocation

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geolocation|
|heading|[int](../types/int.md) | Optional|For [live locations](https://core.telegram.org/api/live-location), a direction in which the location moves, in degrees; 1-360.|
|period|[int](../types/int.md) | Optional|Validity period|
|proximity\_notification\_radius|[int](../types/int.md) | Optional|For [live locations](https://core.telegram.org/api/live-location), a maximum distance to another chat member for proximity alerts, in meters (0-100000).|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Inline keyboard|



### Type: [BotInlineMessage](../types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageMediaGeo = ['_' => 'botInlineMessageMediaGeo', 'geo' => GeoPoint, 'heading' => int, 'period' => int, 'proximity_notification_radius' => int, 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
botInlineMessageMediaGeo={_='botInlineMessageMediaGeo', geo=GeoPoint, heading=int, period=int, proximity_notification_radius=int, reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


