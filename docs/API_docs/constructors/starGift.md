---
title: "starGift"
description: "starGift attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGift  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|limited|[Bool](/API_docs/types/Bool.html) | Optional|
|sold\_out|[Bool](/API_docs/types/Bool.html) | Optional|
|birthday|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|
|sticker|[Document](/API_docs/types/Document.html) | Optional|
|stars|[long](/API_docs/types/long.html) | Yes|
|availability\_remains|[int](/API_docs/types/int.html) | Optional|
|availability\_total|[int](/API_docs/types/int.html) | Optional|
|convert\_stars|[long](/API_docs/types/long.html) | Yes|
|first\_sale\_date|[int](/API_docs/types/int.html) | Optional|
|last\_sale\_date|[int](/API_docs/types/int.html) | Optional|



### Type: [StarGift](/API_docs/types/StarGift.html)


### Example:

```
$starGift = ['_' => 'starGift', 'limited' => Bool, 'sold_out' => Bool, 'birthday' => Bool, 'id' => long, 'sticker' => Document, 'stars' => long, 'availability_remains' => int, 'availability_total' => int, 'convert_stars' => long, 'first_sale_date' => int, 'last_sale_date' => int];
```  
