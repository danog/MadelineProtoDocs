---
title: "updateShort"
description: "Shortened constructor containing info on one update not requiring auxiliary data"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateShort  
[Back to constructors index](/API_docs/constructors/index.md)



Shortened constructor containing info on one update not requiring auxiliary data

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|update|[Update](/API_docs/types/Update.md) | Yes|Update|
|date|[int](/API_docs/types/int.md) | Yes|Date of event|



### Type: [Updates](/API_docs/types/Updates.md)


### Example:

```php
$updateShort = ['_' => 'updateShort', 'update' => Update, 'date' => int];
```  
