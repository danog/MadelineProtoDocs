---
title: "starsTransaction"
description: "starsTransaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsTransaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|refund|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[string](/API_docs/types/string.html) | Yes|
|stars|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|peer|[StarsTransactionPeer](/API_docs/types/StarsTransactionPeer.html) | Yes|
|title|[string](/API_docs/types/string.html) | Optional|
|description|[string](/API_docs/types/string.html) | Optional|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|



### Type: [StarsTransaction](/API_docs/types/StarsTransaction.html)


### Example:

```
$starsTransaction = ['_' => 'starsTransaction', 'refund' => Bool, 'id' => 'string', 'stars' => long, 'date' => int, 'peer' => StarsTransactionPeer, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument];
```  
