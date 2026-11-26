# geoPointAddress

> Address optionally associated to a geoPoint.

[Back to constructors index](/API_docs/constructors/index.html)



Address optionally associated to a [geoPoint](../constructors/geoPoint.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|country\_iso2|[string](/API_docs/types/string.html) | Yes|Two-letter ISO 3166-1 alpha-2 country code|
|state|[string](/API_docs/types/string.html) | Optional|State|
|city|[string](/API_docs/types/string.html) | Optional|City|
|street|[string](/API_docs/types/string.html) | Optional|Street|



### Type: [GeoPointAddress](/API_docs/types/GeoPointAddress.html)


### Example:

```
$geoPointAddress = ['_' => 'geoPointAddress', 'country_iso2' => 'string', 'state' => 'string', 'city' => 'string', 'street' => 'string'];
```
