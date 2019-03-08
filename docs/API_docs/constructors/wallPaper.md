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
|id|[long](../types/long.md) | Yes||
|creator|[Bool](../types/Bool.md) | Optional||
|default|[Bool](../types/Bool.md) | Optional||
|pattern|[Bool](../types/Bool.md) | Optional||
|dark|[Bool](../types/Bool.md) | Optional||
|access\_hash|[long](../types/long.md) | Yes||
|slug|[string](../types/string.md) | Yes||
|document|[Document](../types/Document.md) | Optional||
|settings|[WallPaperSettings](../types/WallPaperSettings.md) | Optional||



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


