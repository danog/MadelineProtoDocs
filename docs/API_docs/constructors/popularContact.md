---
title: "popularContact"
description: "Popular contact"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: popularContact  
[Back to constructors index](/API_docs/constructors/index.md)



Popular contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|client\_id|[long](/API_docs/types/long.md) | Yes|Contact identifier|
|importers|[int](/API_docs/types/int.md) | Yes|How many people imported this contact|



### Type: [PopularContact](/API_docs/types/PopularContact.md)


### Example:

```php
$popularContact = ['_' => 'popularContact', 'client_id' => long, 'importers' => int];
```  
