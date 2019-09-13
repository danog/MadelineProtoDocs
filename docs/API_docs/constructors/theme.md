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
|creator|[Bool](../types/Bool.md) | Optional|Creator?|
|default|[Bool](../types/Bool.md) | Optional|Default?|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|slug|[string](../types/string.md) | Yes|Slug|
|title|[string](../types/string.md) | Yes|Title|
|document|[Document](../types/Document.md) | Optional|Document|
|installs\_count|[int](../types/int.md) | Yes|Installs count|



### Type: [Theme](../types/Theme.md)


### Example:

```php
$theme = ['_' => 'theme', 'creator' => Bool, 'default' => Bool, 'id' => long, 'access_hash' => long, 'slug' => 'string', 'title' => 'string', 'document' => Document, 'installs_count' => int];
```  


Or, if you're into Lua:

```lua
theme={_='theme', creator=Bool, default=Bool, id=long, access_hash=long, slug='string', title='string', document=Document, installs_count=int}

```


