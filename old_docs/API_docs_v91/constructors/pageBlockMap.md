---
title: pageBlockMap
description: Page block map
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockMap  
[Back to constructors index](index.md)



Page block map

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geo|
|zoom|[int](../types/int.md) | Yes|Zoom|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockMap = ['_' => 'pageBlockMap', 'geo' => GeoPoint, 'zoom' => int, 'w' => int, 'h' => int, 'caption' => PageCaption];
```  


Or, if you're into Lua:

```lua
pageBlockMap={_='pageBlockMap', geo=GeoPoint, zoom=int, w=int, h=int, caption=PageCaption}

```


