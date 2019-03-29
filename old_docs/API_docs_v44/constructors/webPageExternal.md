---
title: webPageExternal
description: Web page external
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPageExternal  
[Back to constructors index](index.md)



Web page external

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|display\_url|[string](../types/string.md) | Yes|Display URL|
|type|[string](../types/string.md) | Optional|Type|
|title|[string](../types/string.md) | Optional|Title|
|description|[string](../types/string.md) | Optional|Description|
|thumb\_url|[string](../types/string.md) | Optional|Thumbnail URL|
|content\_url|[string](../types/string.md) | Optional|Content URL|
|w|[int](../types/int.md) | Optional|Width|
|h|[int](../types/int.md) | Optional|Height|
|duration|[int](../types/int.md) | Optional|Duration|



### Type: [WebPage](../types/WebPage.md)


### Example:

```php
$webPageExternal = ['_' => 'webPageExternal', 'url' => 'string', 'display_url' => 'string', 'type' => 'string', 'title' => 'string', 'description' => 'string', 'thumb_url' => 'string', 'content_url' => 'string', 'w' => int, 'h' => int, 'duration' => int];
```  


Or, if you're into Lua:

```lua
webPageExternal={_='webPageExternal', url='string', display_url='string', type='string', title='string', description='string', thumb_url='string', content_url='string', w=int, h=int, duration=int}

```


