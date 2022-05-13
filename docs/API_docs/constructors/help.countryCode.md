---
title: "help.countryCode"
description: "Country code and phone number pattern of a specific country"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_countryCode.html
---
# Constructor: help.countryCode  
[Back to constructors index](/API_docs/constructors/index.html)



Country code and phone number pattern of a specific country

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|country\_code|[string](/API_docs/types/string.html) | Yes|ISO country code|
|prefixes|Array of [string](/API_docs/types/string.html) | Optional|Possible phone prefixes|
|patterns|Array of [string](/API_docs/types/string.html) | Optional|Phone patterns: for example, `XXX XXX XXX`|



### Type: [help.CountryCode](/API_docs/types/help.CountryCode.html)


### Example:

```
$help_countryCode = ['_' => 'help.countryCode', 'country_code' => 'string', 'prefixes' => ['string', 'string'], 'patterns' => ['string', 'string']];
```  
