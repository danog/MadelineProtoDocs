---
title: help.country
description: help.country attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_country.html
---
# Constructor: help.country  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hidden|[Bool](../types/Bool.md) | Optional|
|iso2|[string](../types/string.md) | Yes|
|default\_name|[string](../types/string.md) | Yes|
|name|[string](../types/string.md) | Optional|
|country\_codes|Array of [help.CountryCode](../constructors/help.CountryCode.md) | Yes|



### Type: [help.Country](../types/help.Country.md)


### Example:

```php
$help.country = ['_' => 'help.country', 'hidden' => Bool, 'iso2' => 'string', 'default_name' => 'string', 'name' => 'string', 'country_codes' => [help.CountryCode, help.CountryCode]];
```  


Or, if you're into Lua:

```lua
help.country={_='help.country', hidden=Bool, iso2='string', default_name='string', name='string', country_codes={help.CountryCode}}

```


