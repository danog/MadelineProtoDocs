---
title: "botInlineMessageMediaGeo"
description: "Send a geolocation"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaGeo  
[Back to constructors index](/API_docs/constructors/index.html)



Send a geolocation

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|Geolocation|
|heading|[int](/API_docs/types/int.html) | Optional|For [live locations](https://core.telegram.org/api/live-location), a direction in which the location moves, in degrees; 1-360.|
|period|[int](/API_docs/types/int.html) | Optional|Validity period|
|proximity\_notification\_radius|[int](/API_docs/types/int.html) | Optional|For [live locations](https://core.telegram.org/api/live-location), a maximum distance to another chat member for proximity alerts, in meters (0-100000).|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|Inline keyboard|



### Type: [BotInlineMessage](/API_docs/types/BotInlineMessage.html)



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


### Example:

```
$botInlineMessageMediaGeo = ['_' => 'botInlineMessageMediaGeo', 'geo' => GeoPoint, 'heading' => int, 'period' => int, 'proximity_notification_radius' => int, 'reply_markup' => ReplyMarkup];
```  
