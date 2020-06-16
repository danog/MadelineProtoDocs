---
title: inputBotInlineMessageMediaGeo
description: Geolocation
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaGeo  
[Back to constructors index](index.md)



Geolocation

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geolocation|
|period|[int](../types/int.md) | Yes|Validity period|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Reply markup for bot/inline keyboards|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageMediaGeo = ['_' => 'inputBotInlineMessageMediaGeo', 'geo_point' => InputGeoPoint, 'period' => int, 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
inputBotInlineMessageMediaGeo={_='inputBotInlineMessageMediaGeo', geo_point=InputGeoPoint, period=int, reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


