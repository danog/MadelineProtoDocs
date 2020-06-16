---
title: webPageExternal
description: webPageExternal attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageExternal  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|url|[string](../types/string.md) | Yes|
|display\_url|[string](../types/string.md) | Yes|
|type|[string](../types/string.md) | Optional|
|title|[string](../types/string.md) | Optional|
|description|[string](../types/string.md) | Optional|
|thumb\_url|[string](../types/string.md) | Optional|
|content\_url|[string](../types/string.md) | Optional|
|w|[int](../types/int.md) | Optional|
|h|[int](../types/int.md) | Optional|
|duration|[int](../types/int.md) | Optional|



### Type: [WebPage](../types/WebPage.md)


### Example:

```php
$webPageExternal = ['_' => 'webPageExternal', 'url' => 'string', 'display_url' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'thumb_url' => 'string', 'content_url' => 'string', 'w' => int, 'h' => int, 'duration' => int];
```  


Or, if you're into Lua:

```lua
webPageExternal={_='webPageExternal', url='string', display_url='string', type='string', title='string', description='string', thumb_url='string', content_url='string', w=int, h=int, duration=int}

```


