---
title: webPage
description: webPage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|url|[string](../types/string.md) | Yes|
|display\_url|[string](../types/string.md) | Yes|
|type|[string](../types/string.md) | Optional|
|site\_name|[string](../types/string.md) | Optional|
|title|[string](../types/string.md) | Optional|
|description|[string](../types/string.md) | Optional|
|photo|[Photo](../types/Photo.md) | Optional|
|embed\_url|[string](../types/string.md) | Optional|
|embed\_type|[string](../types/string.md) | Optional|
|embed\_width|[int](../types/int.md) | Optional|
|embed\_height|[int](../types/int.md) | Optional|
|duration|[int](../types/int.md) | Optional|
|author|[string](../types/string.md) | Optional|
|document|[Document](../types/Document.md) | Optional|



### Type: [WebPage](../types/WebPage.md)


### Example:

```php
$webPage = ['_' => 'webPage', 'id' => long, 'url' => 'string', 'display_url' => 'string', 'type' => 'string', 'site_name' => 'string', 'title' => 'string', 'description' => 'string', 'photo' => Photo, 'embed_url' => 'string', 'embed_type' => 'string', 'embed_width' => int, 'embed_height' => int, 'duration' => int, 'author' => 'string', 'document' => Document];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "webPage", "id": long, "url": "string", "display_url": "string", "type": "string", "site_name": "string", "title": "string", "description": "string", "photo": Photo, "embed_url": "string", "embed_type": "string", "embed_width": int, "embed_height": int, "duration": int, "author": "string", "document": Document}
```


Or, if you're into Lua:

```lua
webPage={_='webPage', id=long, url='string', display_url='string', type='string', site_name='string', title='string', description='string', photo=Photo, embed_url='string', embed_type='string', embed_width=int, embed_height=int, duration=int, author='string', document=Document}

```


