---
title: "help.appUpdate"
description: "An update is available for the application."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_appUpdate.html
---
# Constructor: help.appUpdate  
[Back to constructors index](/API_docs/constructors/index.html)



An update is available for the application.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_not\_skip|[Bool](/API_docs/types/Bool.html) | Optional|Unskippable, the new info must be shown to the user (with a popup or something else)|
|id|[int](/API_docs/types/int.html) | Yes|Update ID|
|version|[string](/API_docs/types/string.html) | Yes|New version name|
|text|[string](/API_docs/types/string.html) | Yes|Text description of the update|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Yes|[Message entities for styled text](https://core.telegram.org/api/entities)|
|document|[Document](/API_docs/types/Document.html) | Optional|Application binary|
|url|[string](/API_docs/types/string.html) | Optional|Application download URL|
|sticker|[Document](/API_docs/types/Document.html) | Optional|Associated sticker|



### Type: [help.AppUpdate](/API_docs/types/help.AppUpdate.html)


### Example:

```
$help_appUpdate = ['_' => 'help.appUpdate', 'can_not_skip' => Bool, 'id' => int, 'version' => 'string', 'text' => 'string', 'entities' => [MessageEntity, MessageEntity], 'document' => Document, 'url' => 'string', 'sticker' => Document];
```  
