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
|popup|[Bool](../types/Bool.md) | Optional|Popup?|
|id|[int](../types/int.md) | Yes|ID|
|version|[string](../types/string.md) | Yes|Version|
|text|[string](../types/string.md) | Yes|Text|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|Entities|
|document|[Document](../types/Document.md) | Optional|Document|
|url|[string](../types/string.md) | Optional|URL|



### Type: [help\_AppUpdate](../types/help_AppUpdate.md)


### Example:

```php
$help_appUpdate = ['_' => 'help.appUpdate', 'popup' => Bool, 'id' => int, 'version' => 'string', 'text' => 'string', 'entities' => [MessageEntity, MessageEntity], 'document' => Document, 'url' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.appUpdate", "popup": Bool, "id": int, "version": "string", "text": "string", "entities": [MessageEntity], "document": Document, "url": "string"}
```


Or, if you're into Lua:

```lua
help_appUpdate={_='help.appUpdate', popup=Bool, id=int, version='string', text='string', entities={MessageEntity}, document=Document, url='string'}

```


