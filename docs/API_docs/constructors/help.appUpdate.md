---
title: "help.appUpdate"
description: "An update is available for the application."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_appUpdate.html
---
# Constructor: help.appUpdate  
[Back to constructors index](/API_docs/constructors/index.md)



An update is available for the application.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_not\_skip|[Bool](/API_docs/types/Bool.md) | Optional|Unskippable, the new info must be shown to the user (with a popup or something else)|
|id|[int](/API_docs/types/int.md) | Yes|Update ID|
|version|[string](/API_docs/types/string.md) | Yes|New version name|
|text|[string](/API_docs/types/string.md) | Yes|Text description of the update|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.md) | Yes|[Message entities for styled text](https://core.telegram.org/api/entities)|
|document|[Document](/API_docs/types/Document.md) | Optional|Application binary|
|url|[string](/API_docs/types/string.md) | Optional|Application download URL|
|sticker|[Document](/API_docs/types/Document.md) | Optional|



### Type: [help.AppUpdate](/API_docs/types/help.AppUpdate.md)


### Example:

```php
$help_appUpdate = ['_' => 'help.appUpdate', 'can_not_skip' => Bool, 'id' => int, 'version' => 'string', 'text' => 'string', 'entities' => [MessageEntity, MessageEntity], 'document' => Document, 'url' => 'string', 'sticker' => Document];
```  
