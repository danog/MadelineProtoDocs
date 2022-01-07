---
title: "postAddress"
description: "Shipping address"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: postAddress  
[Back to constructors index](index.md)



Shipping address

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|street\_line1|[string](../types/string.md) | Yes|First line for the address|
|street\_line2|[string](../types/string.md) | Yes|Second line for the address|
|city|[string](../types/string.md) | Yes|City|
|state|[string](../types/string.md) | Yes|State, if applicable (empty otherwise)|
|country\_iso2|[string](../types/string.md) | Yes|ISO 3166-1 alpha-2 country code|
|post\_code|[string](../types/string.md) | Yes|Address post code|



### Type: [PostAddress](../types/PostAddress.md)


### Example:

```php
$postAddress = ['_' => 'postAddress', 'street_line1' => 'string', 'street_line2' => 'string', 'city' => 'string', 'state' => 'string', 'country_iso2' => 'string', 'post_code' => 'string'];
```  
