# help.country

> Name, ISO code, localized name and phone codes/patterns of a specific country

[Back to constructors index](/API_docs/constructors/index.html)



Name, ISO code, localized name and phone codes/patterns of a specific country

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hidden|[Bool](/API_docs/types/Bool.html) | Optional|Whether this country should not be shown in the list|
|iso2|[string](/API_docs/types/string.html) | Yes|ISO code of country|
|default\_name|[string](/API_docs/types/string.html) | Yes|Name of the country in the country's language|
|name|[string](/API_docs/types/string.html) | Optional|Name of the country in the user's language, if different from the original name|
|country\_codes|Array of [help.CountryCode](/API_docs/constructors/help.CountryCode.html) | Yes|Phone codes/patterns|



### Type: [help.Country](/API_docs/types/help.Country.html)


### Example:

```
$help_country = ['_' => 'help.country', 'hidden' => Bool, 'iso2' => 'string', 'default_name' => 'string', 'name' => 'string', 'country_codes' => [help.CountryCode, help.CountryCode]];
```
