---
title: "help.countriesList"
description: "Name, ISO code, localized name and phone codes/patterns of all available countries"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_countriesList.html
---
# Constructor: help.countriesList  
[Back to constructors index](index.md)



Name, ISO code, localized name and phone codes/patterns of all available countries

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|countries|Array of [help.Country](../constructors/help.Country.md) | Yes|Name, ISO code, localized name and phone codes/patterns of all available countries|
|hash|[int](../types/int.md) | Yes|



### Type: [help.CountriesList](../types/help.CountriesList.md)


### Example:

```php
$help_countriesList = ['_' => 'help.countriesList', 'countries' => [help.Country, help.Country], 'hash' => int];
```  


Or, if you're into Lua:

```lua
help_countriesList={_='help.countriesList', countries={help.Country}, hash=int}

```


