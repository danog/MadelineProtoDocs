---
title: "businessLocation"
description: "Represents the location of a Telegram Business »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessLocation  
[Back to constructors index](/API_docs/constructors/index.html)



Represents the location of a [Telegram Business »](https://core.telegram.org/api/business#location).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|Geographical coordinates (optional).|
|address|[string](/API_docs/types/string.html) | Yes|Textual description of the address (mandatory).|



### Type: [BusinessLocation](/API_docs/types/BusinessLocation.html)


### Example:

```
$businessLocation = ['_' => 'businessLocation', 'geo_point' => GeoPoint, 'address' => 'string'];
```  
