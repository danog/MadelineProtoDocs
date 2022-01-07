---
title: "help.promoDataEmpty"
description: "No PSA/MTProxy info is available"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_promoDataEmpty.html
---
# Constructor: help.promoDataEmpty  
[Back to constructors index](/API_docs/constructors/index.md)



No PSA/MTProxy info is available

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](/API_docs/types/int.md) | Yes|Re-fetch PSA/MTProxy info after the specified number of seconds|



### Type: [help.PromoData](/API_docs/types/help.PromoData.md)


### Example:

```php
$help_promoDataEmpty = ['_' => 'help.promoDataEmpty', 'expires' => int];
```  
