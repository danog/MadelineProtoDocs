---
title: "popularContact"
description: "Popular contact"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: popularContact  
[Back to constructors index](/API_docs/constructors/index.html)



Popular contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|client\_id|[long](/API_docs/types/long.html) | Yes|Contact identifier|
|importers|[int](/API_docs/types/int.html) | Yes|How many people imported this contact|



### Type: [PopularContact](/API_docs/types/PopularContact.html)


### Example:

```
$popularContact = ['_' => 'popularContact', 'client_id' => long, 'importers' => int];
```  
