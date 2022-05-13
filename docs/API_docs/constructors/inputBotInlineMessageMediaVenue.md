---
title: "inputBotInlineMessageMediaVenue"
description: "Venue"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaVenue  
[Back to constructors index](/API_docs/constructors/index.html)



Venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.html) | Optional|Geolocation|
|title|[string](/API_docs/types/string.html) | Yes|Venue name|
|address|[string](/API_docs/types/string.html) | Yes|Address|
|provider|[string](/API_docs/types/string.html) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](/API_docs/types/string.html) | Yes|Venue ID in the provider's database|
|venue\_type|[string](/API_docs/types/string.html) | Yes|Venue type in the provider's database|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|Inline keyboard|



### Type: [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html)



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


### Example:

```
$inputBotInlineMessageMediaVenue = ['_' => 'inputBotInlineMessageMediaVenue', 'geo_point' => InputGeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string', 'reply_markup' => ReplyMarkup];
```  
