---
title: "help.countryCode"
description: "Country code and phone number pattern of a specific country"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_countryCode.html
---
# Constructor: help.countryCode  
[Back to constructors index](index.md)



Country code and phone number pattern of a specific country

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|country\_code|[string](../types/string.md) | Yes|ISO country code|
|prefixes|Array of [string](../types/string.md) | Optional|Possible phone prefixes|
|patterns|Array of [string](../types/string.md) | Optional|Phone patterns: for example, `XXX XXX XXX`|



### Type: [help.CountryCode](../types/help.CountryCode.md)


### Example:

```php
$help_countryCode = ['_' => 'help.countryCode', 'country_code' => 'string', 'prefixes' => ['string', 'string'], 'patterns' => ['string', 'string']];
```  


Or, if you're into Lua:

```lua
help_countryCode={_='help.countryCode', country_code='string', prefixes={'string'}, patterns={'string'}}

```


