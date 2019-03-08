---
title: wallPaper
description: Wall paper
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaper  
[Back to constructors index](index.md)



Wall paper

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|creator|[Bool](../types/Bool.md) | Optional|Am I the creator?|
|default|[Bool](../types/Bool.md) | Optional|Default?|
|pattern|[Bool](../types/Bool.md) | Optional|Pattern|
|dark|[Bool](../types/Bool.md) | Optional|Dark?|
|access\_hash|[long](../types/long.md) | Yes|Hash|
|slug|[string](../types/string.md) | Yes|Slug?|
|document|[Document](../types/Document.md) | Optional|Wallpaper|
|settings|[WallPaperSettings](../types/WallPaperSettings.md) | Optional|Wallpaper settings|



### Type: [WallPaper](../types/WallPaper.md)


### Example:

```php
$wallPaper = ['_' => 'wallPaper', 'id' => long, 'creator' => Bool, 'default' => Bool, 'pattern' => Bool, 'dark' => Bool, 'access_hash' => long, 'slug' => 'string', 'document' => Document, 'settings' => WallPaperSettings];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "wallPaper", "id": long, "creator": Bool, "default": Bool, "pattern": Bool, "dark": Bool, "access_hash": long, "slug": "string", "document": Document, "settings": WallPaperSettings}
```


Or, if you're into Lua:

```lua
wallPaper={_='wallPaper', id=long, creator=Bool, default=Bool, pattern=Bool, dark=Bool, access_hash=long, slug='string', document=Document, settings=WallPaperSettings}

```


