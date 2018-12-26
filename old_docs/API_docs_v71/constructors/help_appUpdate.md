---
title: help.appUpdate
description: App update
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.appUpdate  
[Back to constructors index](index.md)



App update

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|critical|[Bool](../types/Bool.md) | Yes|Critical?|
|url|[string](../types/string.md) | Yes|URL|
|text|[string](../types/string.md) | Yes|Text|



### Type: [help\_AppUpdate](../types/help_AppUpdate.md)


### Example:

```php
$help_appUpdate = ['_' => 'help.appUpdate', 'id' => int, 'critical' => Bool, 'url' => 'string', 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.appUpdate", "id": int, "critical": Bool, "url": "string", "text": "string"}
```


Or, if you're into Lua:

```lua
help_appUpdate={_='help.appUpdate', id=int, critical=Bool, url='string', text='string'}

```


