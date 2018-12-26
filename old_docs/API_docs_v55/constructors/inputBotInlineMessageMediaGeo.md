---
title: inputBotInlineMessageMediaGeo
description: Bot inline message media geo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaGeo  
[Back to constructors index](index.md)



Bot inline message media geo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geo point|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Reply markup|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageMediaGeo = ['_' => 'inputBotInlineMessageMediaGeo', 'geo_point' => InputGeoPoint, 'reply_markup' => ReplyMarkup];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputBotInlineMessageMediaGeo", "geo_point": InputGeoPoint, "reply_markup": ReplyMarkup}
```


Or, if you're into Lua:

```lua
inputBotInlineMessageMediaGeo={_='inputBotInlineMessageMediaGeo', geo_point=InputGeoPoint, reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


