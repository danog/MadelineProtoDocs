---
title: updateDialogFilter
description: updateDialogFilter attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogFilter  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[int](../types/int.md) | Yes|
|filter|[DialogFilter](../types/DialogFilter.md) | Optional|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDialogFilter = ['_' => 'updateDialogFilter', 'id' => int, 'filter' => DialogFilter];
```  


Or, if you're into Lua:

```lua
updateDialogFilter={_='updateDialogFilter', id=int, filter=DialogFilter}

```


