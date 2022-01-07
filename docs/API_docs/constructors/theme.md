---
title: "theme"
description: "Theme"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: theme  
[Back to constructors index](/API_docs/constructors/index.md)



Theme

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](/API_docs/types/Bool.md) | Optional|Whether the current user is the creator of this theme|
|default|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is the default theme|
|for\_chat|[Bool](/API_docs/types/Bool.md) | Optional|
|id|[long](/API_docs/types/long.md) | Yes|Theme ID|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Theme access hash|
|slug|[string](/API_docs/types/string.md) | Yes|Unique theme ID|
|title|[string](/API_docs/types/string.md) | Yes|Theme name|
|document|[Document](/API_docs/types/Document.md) | Optional|Theme|
|settings|Array of [ThemeSettings](/API_docs/types/ThemeSettings.md) | Optional|
|emoticon|[string](/API_docs/types/string.md) | Optional|
|installs\_count|[int](/API_docs/types/int.md) | Optional|Installation count|



### Type: [Theme](/API_docs/types/Theme.md)


### Example:

```php
$theme = ['_' => 'theme', 'creator' => Bool, 'default' => Bool, 'for_chat' => Bool, 'id' => long, 'access_hash' => long, 'slug' => 'string', 'title' => 'string', 'document' => Document, 'settings' => [ThemeSettings, ThemeSettings], 'emoticon' => 'string', 'installs_count' => int];
```  
