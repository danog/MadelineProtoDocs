---
title: "theme"
description: "Theme"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: theme  
[Back to constructors index](/API_docs/constructors/index.html)



Theme

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|Whether the current user is the creator of this theme|
|default|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is the default theme|
|for\_chat|[Bool](/API_docs/types/Bool.html) | Optional|Whether this theme is meant to be used as a [chat theme](https://telegram.org/blog/chat-themes-interactive-emoji-read-receipts)|
|id|[long](/API_docs/types/long.html) | Yes|Theme ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Theme access hash|
|slug|[string](/API_docs/types/string.html) | Yes|Unique theme ID|
|title|[string](/API_docs/types/string.html) | Yes|Theme name|
|document|[Document](/API_docs/types/Document.html) | Optional|Theme|
|settings|Array of [ThemeSettings](/API_docs/types/ThemeSettings.html) | Optional|Theme settings|
|emoticon|[string](/API_docs/types/string.html) | Optional|Theme emoji|
|installs\_count|[int](/API_docs/types/int.html) | Optional|Installation count|



### Type: [Theme](/API_docs/types/Theme.html)


### Example:

```
$theme = ['_' => 'theme', 'creator' => Bool, 'default' => Bool, 'for_chat' => Bool, 'id' => long, 'access_hash' => long, 'slug' => 'string', 'title' => 'string', 'document' => Document, 'settings' => [ThemeSettings, ThemeSettings], 'emoticon' => 'string', 'installs_count' => int];
```  
