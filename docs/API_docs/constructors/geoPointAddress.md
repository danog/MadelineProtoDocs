---
title: "geoPointAddress"
description: "geoPointAddress attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geoPointAddress  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|country\_iso2|[string](/API_docs/types/string.html) | Yes|
|state|[string](/API_docs/types/string.html) | Optional|
|city|[string](/API_docs/types/string.html) | Optional|
|street|[string](/API_docs/types/string.html) | Optional|



### Type: [GeoPointAddress](/API_docs/types/GeoPointAddress.html)


### Example:

```
$geoPointAddress = ['_' => 'geoPointAddress', 'country_iso2' => 'string', 'state' => 'string', 'city' => 'string', 'street' => 'string'];
```  
