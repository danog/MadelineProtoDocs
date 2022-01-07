---
title: "help.appUpdate"
description: "An update is available for the application."
nav_exclude: true
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
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Yes|[Message entities for styled text](https://core.telegram.org/api/entities)|
|document|[Document](../types/Document.md) | Optional|Application binary|
|url|[string](../types/string.md) | Optional|Application download URL|
|sticker|[Document](../types/Document.md) | Optional|



### Type: [help.AppUpdate](../types/help.AppUpdate.md)


### Example:

```php
$help_appUpdate = ['_' => 'help.appUpdate', 'can_not_skip' => Bool, 'id' => int, 'version' => 'string', 'text' => 'string', 'entities' => [MessageEntity, MessageEntity], 'document' => Document, 'url' => 'string', 'sticker' => Document];
```  
