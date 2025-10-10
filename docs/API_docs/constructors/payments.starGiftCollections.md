---
title: "payments.starGiftCollections"
description: "Represents a list of star gift collections »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGiftCollections.html
---
# Constructor: payments.starGiftCollections  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a list of [star gift collections »](https://core.telegram.org/api/gifts#gift-collections).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|collections|Array of [StarGiftCollection](/API_docs/types/StarGiftCollection.html) | Yes|Star gift collections.|



### Type: [payments.StarGiftCollections](/API_docs/types/payments.StarGiftCollections.html)


### Example:

```
$payments_starGiftCollections = ['_' => 'payments.starGiftCollections', 'collections' => [StarGiftCollection, StarGiftCollection]];
```  
