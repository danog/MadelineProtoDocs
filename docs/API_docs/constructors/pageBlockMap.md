---
title: "pageBlockMap"
description: "A map"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockMap  
[Back to constructors index](/API_docs/constructors/index.md)



A map

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](/API_docs/types/GeoPoint.md) | Optional|Location of the map center|
|zoom|[int](/API_docs/types/int.md) | Yes|Map zoom level; 13-20|
|w|[int](/API_docs/types/int.md) | Yes|Map width in pixels before applying scale; 16-102|
|h|[int](/API_docs/types/int.md) | Yes|Map height in pixels before applying scale; 16-1024|
|caption|[PageCaption](/API_docs/types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](/API_docs/types/PageBlock.md)


### Example:

```php
$pageBlockMap = ['_' => 'pageBlockMap', 'geo' => GeoPoint, 'zoom' => int, 'w' => int, 'h' => int, 'caption' => PageCaption];
```  
