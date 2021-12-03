---
title: help.country
description: Name, ISO code, localized name and phone codes/patterns of a specific country
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_country.html
---
# Constructor: help.country  
[Back to constructors index](index.md)



Name, ISO code, localized name and phone codes/patterns of a specific country

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hidden|[Bool](../types/Bool.md) | Optional|Whether this country should not be shown in the list|
|iso2|[string](../types/string.md) | Yes|ISO code of country|
|default\_name|[string](../types/string.md) | Yes|Name of the country in the country's language|
|name|[string](../types/string.md) | Optional|Name of the country in the user's language, if different from the original name|
|country\_codes|Array of [help.CountryCode](../constructors/help.CountryCode.md) | Yes|Phone codes/patterns|



### Type: [help.Country](../types/help.Country.md)


### Example:

```php
$help_country = ['_' => 'help.country', 'hidden' => Bool, 'iso2' => 'string', 'default_name' => 'string', 'name' => 'string', 'country_codes' => [help.CountryCode, help.CountryCode]];
```  


Or, if you're into Lua:

```lua
help_country={_='help.country', hidden=Bool, iso2='string', default_name='string', name='string', country_codes={help.CountryCode}}

```


