---
title: "help.countriesList"
description: "Name, ISO code, localized name and phone codes/patterns of all available countries"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_countriesList.html
---
# Constructor: help.countriesList  
[Back to constructors index](/API_docs/constructors/index.html)



Name, ISO code, localized name and phone codes/patterns of all available countries

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|countries|Array of [help.Country](/API_docs/constructors/help.Country.html) | Yes|Name, ISO code, localized name and phone codes/patterns of all available countries|
|hash|[int](/API_docs/types/int.html) | Yes|



### Type: [help.CountriesList](/API_docs/types/help.CountriesList.html)


### Example:

```
$help_countriesList = ['_' => 'help.countriesList', 'countries' => [help.Country, help.Country], 'hash' => int];
```  
