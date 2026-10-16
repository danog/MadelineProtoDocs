---
title: "onrampProviderInfo"
description: "onrampProviderInfo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: onrampProviderInfo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|supports\_base\_currencies|[Bool](/API_docs/types/Bool.html) | Optional|
|supports\_limits|[Bool](/API_docs/types/Bool.html) | Optional|
|supports\_quote|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[string](/API_docs/types/string.html) | Yes|
|name|[string](/API_docs/types/string.html) | Yes|
|crypto\_currencies|Array of [string](/API_docs/types/string.html) | Yes|



### Type: [OnrampProviderInfo](/API_docs/types/OnrampProviderInfo.html)


### Example:

```
$onrampProviderInfo = ['_' => 'onrampProviderInfo', 'supports_base_currencies' => Bool, 'supports_limits' => Bool, 'supports_quote' => Bool, 'id' => 'string', 'name' => 'string', 'crypto_currencies' => ['string', 'string']];
```  
