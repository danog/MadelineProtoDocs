---
title: "pageBlockMap"
description: "A map"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockMap  
[Back to constructors index](index.md)



A map

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Location of the map center|
|zoom|[int](../types/int.md) | Yes|Map zoom level; 13-20|
|w|[int](../types/int.md) | Yes|Map width in pixels before applying scale; 16-102|
|h|[int](../types/int.md) | Yes|Map height in pixels before applying scale; 16-1024|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockMap = ['_' => 'pageBlockMap', 'geo' => GeoPoint, 'zoom' => int, 'w' => int, 'h' => int, 'caption' => PageCaption];
```  
