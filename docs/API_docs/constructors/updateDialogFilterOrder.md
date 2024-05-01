---
title: "updateDialogFilterOrder"
description: "New folder order"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogFilterOrder  
[Back to constructors index](/API_docs/constructors/index.html)



New [folder](https://core.telegram.org/api/folders) order

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|order|Array of [int](/API_docs/types/int.html) | Yes|Ordered [folder IDs](https://core.telegram.org/api/folders)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDialogFilterOrder = ['_' => 'updateDialogFilterOrder', 'order' => [int, int]];
```  
