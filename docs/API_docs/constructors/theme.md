---
title: theme
description: Theme
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: theme  
[Back to constructors index](index.md)



Theme

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](../types/Bool.md) | Optional|Whether the current user is the creator of this theme|
|default|[Bool](../types/Bool.md) | Optional|Whether this is the default theme|
|for\_chat|[Bool](../types/Bool.md) | Optional|
|id|[long](../types/long.md) | Yes|Theme ID|
|access\_hash|[long](../types/long.md) | Yes|Theme access hash|
|slug|[string](../types/string.md) | Yes|Unique theme ID|
|title|[string](../types/string.md) | Yes|Theme name|
|document|[Document](../types/Document.md) | Optional|Theme|
|settings|Array of [ThemeSettings](../types/ThemeSettings.md) | Optional|
|emoticon|[string](../types/string.md) | Optional|
|installs\_count|[int](../types/int.md) | Optional|Installation count|



### Type: [Theme](../types/Theme.md)


### Example:

```php
$theme = ['_' => 'theme', 'creator' => Bool, 'default' => Bool, 'for_chat' => Bool, 'id' => long, 'access_hash' => long, 'slug' => 'string', 'title' => 'string', 'document' => Document, 'settings' => [ThemeSettings, ThemeSettings], 'emoticon' => 'string', 'installs_count' => int];
```  


Or, if you're into Lua:

```lua
theme={_='theme', creator=Bool, default=Bool, for_chat=Bool, id=long, access_hash=long, slug='string', title='string', document=Document, settings={ThemeSettings}, emoticon='string', installs_count=int}

```


