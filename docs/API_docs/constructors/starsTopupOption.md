---
title: "starsTopupOption"
description: "starsTopupOption attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsTopupOption  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|extended|[Bool](/API_docs/types/Bool.html) | Optional|
|stars|[long](/API_docs/types/long.html) | Yes|
|store\_product|[string](/API_docs/types/string.html) | Optional|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|



### Type: [StarsTopupOption](/API_docs/types/StarsTopupOption.html)


### Example:

```
$starsTopupOption = ['_' => 'starsTopupOption', 'extended' => Bool, 'stars' => long, 'store_product' => 'string', 'currency' => 'string', 'amount' => long];
```  
