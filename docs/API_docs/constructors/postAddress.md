---
title: "postAddress"
description: "Shipping address"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: postAddress  
[Back to constructors index](/API_docs/constructors/index.html)



Shipping address

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|street\_line1|[string](/API_docs/types/string.html) | Yes|First line for the address|
|street\_line2|[string](/API_docs/types/string.html) | Yes|Second line for the address|
|city|[string](/API_docs/types/string.html) | Yes|City|
|state|[string](/API_docs/types/string.html) | Yes|State, if applicable (empty otherwise)|
|country\_iso2|[string](/API_docs/types/string.html) | Yes|ISO 3166-1 alpha-2 country code|
|post\_code|[string](/API_docs/types/string.html) | Yes|Address post code|



### Type: [PostAddress](/API_docs/types/PostAddress.html)


### Example:

```
$postAddress = ['_' => 'postAddress', 'street_line1' => 'string', 'street_line2' => 'string', 'city' => 'string', 'state' => 'string', 'country_iso2' => 'string', 'post_code' => 'string'];
```  
