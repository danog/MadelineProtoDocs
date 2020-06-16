---
title: updateDialogFilter
description: A new [folder](https://core.telegram.org/api/folders) was added
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDialogFilter  
[Back to constructors index](index.md)



A new [folder](https://core.telegram.org/api/folders) was added

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|[Folder](https://core.telegram.org/api/folders) ID|
|filter|[DialogFilter](../types/DialogFilter.md) | Optional|[Folder](https://core.telegram.org/api/folders) info|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDialogFilter = ['_' => 'updateDialogFilter', 'id' => int, 'filter' => DialogFilter];
```  


Or, if you're into Lua:

```lua
updateDialogFilter={_='updateDialogFilter', id=int, filter=DialogFilter}

```


