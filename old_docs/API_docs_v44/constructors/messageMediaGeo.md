---
title: messageMediaGeo
description: messageMediaGeo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: messageMediaGeo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```
$messageMediaGeo = ['_' => 'messageMediaGeo', 'geo' => GeoPoint];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageMediaGeo", "geo": GeoPoint}
```


Or, if you're into Lua:  


```
messageMediaGeo={_='messageMediaGeo', geo=GeoPoint}

```


