---
title: "help.countryCode"
description: "Country code and phone number pattern of a specific country"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_countryCode.html
---
# Constructor: help.countryCode  
[Back to constructors index](/API_docs/constructors/index.md)



Country code and phone number pattern of a specific country

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|country\_code|[string](/API_docs/types/string.md) | Yes|ISO country code|
|prefixes|Array of [string](/API_docs/types/string.md) | Optional|Possible phone prefixes|
|patterns|Array of [string](/API_docs/types/string.md) | Optional|Phone patterns: for example, `XXX XXX XXX`|



### Type: [help.CountryCode](/API_docs/types/help.CountryCode.md)


### Example:

```php
$help_countryCode = ['_' => 'help.countryCode', 'country_code' => 'string', 'prefixes' => ['string', 'string'], 'patterns' => ['string', 'string']];
```  
