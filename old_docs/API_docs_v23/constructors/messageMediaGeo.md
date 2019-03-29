---
title: messageMediaGeo
description: Message media geo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGeo  
[Back to constructors index](index.md)



Message media geo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geo|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaGeo = ['_' => 'messageMediaGeo', 'geo' => GeoPoint];
```  


Or, if you're into Lua:

```lua
messageMediaGeo={_='messageMediaGeo', geo=GeoPoint}

```


