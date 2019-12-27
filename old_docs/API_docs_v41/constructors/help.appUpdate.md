---
title: help.appUpdate
description: An update is available for the application.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_appUpdate.html
---
# Constructor: help.appUpdate  
[Back to constructors index](index.md)



An update is available for the application.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|Update ID|
|critical|[Bool](../types/Bool.md) | Yes|Critical?|
|url|[string](../types/string.md) | Yes|Application download URL|
|text|[string](../types/string.md) | Yes|Text description of the update|



### Type: [help.AppUpdate](../types/help.AppUpdate.md)


### Example:

```php
$help.appUpdate = ['_' => 'help.appUpdate', 'id' => int, 'critical' => Bool, 'url' => 'string', 'text' => 'string'];
```  


Or, if you're into Lua:

```lua
help.appUpdate={_='help.appUpdate', id=int, critical=Bool, url='string', text='string'}

```


