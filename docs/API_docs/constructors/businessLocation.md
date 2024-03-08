---
title: "businessLocation"
description: "businessLocation attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessLocation  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|geo\_point|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|
|address|[string](/API_docs/types/string.html) | Yes|



### Type: [BusinessLocation](/API_docs/types/BusinessLocation.html)


### Example:

```
$businessLocation = ['_' => 'businessLocation', 'geo_point' => GeoPoint, 'address' => 'string'];
```  
