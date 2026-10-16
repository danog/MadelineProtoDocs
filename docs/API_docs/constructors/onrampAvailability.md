---
title: "onrampAvailability"
description: "onrampAvailability attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: onrampAvailability  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|allowed|[Bool](/API_docs/types/Bool.html) | Optional|
|buy\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|
|country\_code|[string](/API_docs/types/string.html) | Yes|
|state|[string](/API_docs/types/string.html) | Optional|
|methods|Array of [OnrampMethodAvailability](/API_docs/types/OnrampMethodAvailability.html) | Yes|



### Type: [OnrampAvailability](/API_docs/types/OnrampAvailability.html)


### Example:

```
$onrampAvailability = ['_' => 'onrampAvailability', 'allowed' => Bool, 'buy_allowed' => Bool, 'country_code' => 'string', 'state' => 'string', 'methods' => [OnrampMethodAvailability, OnrampMethodAvailability]];
```  
