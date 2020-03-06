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
|can\_not\_skip|[Bool](../types/Bool.md) | Optional|Unskippable, the new info must be shown to the user (with a popup or something else)|
|id|[int](../types/int.md) | Yes|Update ID|
|version|[string](../types/string.md) | Yes|New version name|
|text|[string](../types/string.md) | Yes|Text description of the update|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|Entities|
|document|[Document](../types/Document.md) | Optional|Attached document|
|url|[string](../types/string.md) | Optional|Application download URL|



### Type: [help.AppUpdate](../types/help.AppUpdate.md)


### Example:

```php
$help.appUpdate = ['_' => 'help.appUpdate', 'can_not_skip' => Bool, 'id' => int, 'version' => 'string', 'text' => 'string', 'entities' => [MessageEntity, MessageEntity], 'document' => Document, 'url' => 'string'];
```  


Or, if you're into Lua:

```lua
help.appUpdate={_='help.appUpdate', can_not_skip=Bool, id=int, version='string', text='string', entities={MessageEntity}, document=Document, url='string'}

```


