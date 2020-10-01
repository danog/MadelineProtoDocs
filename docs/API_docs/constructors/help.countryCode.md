---
title: help.countryCode
description: help.countryCode attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_countryCode.html
---
# Constructor: help.countryCode  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|country\_code|[string](../types/string.md) | Yes|
|prefixes|Array of [string](../types/string.md) | Optional|
|patterns|Array of [string](../types/string.md) | Optional|



### Type: [help.CountryCode](../types/help.CountryCode.md)


### Example:

```php
$help.countryCode = ['_' => 'help.countryCode', 'country_code' => 'string', 'prefixes' => ['string', 'string'], 'patterns' => ['string', 'string']];
```  


Or, if you're into Lua:

```lua
help.countryCode={_='help.countryCode', country_code='string', prefixes={'string'}, patterns={'string'}}

```


