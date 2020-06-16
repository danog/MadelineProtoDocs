---
title: updateDialogFilterOrder
description: New [folder](https://core.telegram.org/api/folders) order
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogFilterOrder  
[Back to constructors index](index.md)



New [folder](https://core.telegram.org/api/folders) order

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|order|Array of [int](../types/int.md) | Yes|Ordered [folder IDs](https://core.telegram.org/api/folders)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDialogFilterOrder = ['_' => 'updateDialogFilterOrder', 'order' => [int, int]];
```  


Or, if you're into Lua:

```lua
updateDialogFilterOrder={_='updateDialogFilterOrder', order={int}}

```


