---
title: "nearestDc"
description: "Nearest data centre, according to geo-ip."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: nearestDc  
[Back to constructors index](/API_docs/constructors/index.md)



Nearest data centre, according to geo-ip.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|country|[string](/API_docs/types/string.md) | Yes|Country code determined by geo-ip|
|this\_dc|[int](/API_docs/types/int.md) | Yes|Number of current data centre|
|nearest\_dc|[int](/API_docs/types/int.md) | Yes|Number of nearest data centre|



### Type: [NearestDc](/API_docs/types/NearestDc.md)


### Example:

```php
$nearestDc = ['_' => 'nearestDc', 'country' => 'string', 'this_dc' => int, 'nearest_dc' => int];
```  
