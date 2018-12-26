---
title: botInlineMessageMediaGeo
description: Bot inline message media geo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaGeo  
[Back to constructors index](index.md)



Bot inline message media geo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geo|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|Reply markup|



### Type: [BotInlineMessage](../types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageMediaGeo = ['_' => 'botInlineMessageMediaGeo', 'geo' => GeoPoint, 'reply_markup' => ReplyMarkup];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "botInlineMessageMediaGeo", "geo": GeoPoint, "reply_markup": ReplyMarkup}
```


Or, if you're into Lua:

```lua
botInlineMessageMediaGeo={_='botInlineMessageMediaGeo', geo=GeoPoint, reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


