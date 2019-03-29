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
|id|[int](../types/int.md) | Yes|ID|
|title|[string](../types/string.md) | Yes|Title|
|sizes|Array of [PhotoSize](../types/PhotoSize.md) | Yes|Sizes|
|color|[int](../types/int.md) | Yes|Color|



### Type: [WallPaper](../types/WallPaper.md)


### Example:

```php
$wallPaper = ['_' => 'wallPaper', 'id' => int, 'title' => 'string', 'sizes' => [PhotoSize, PhotoSize], 'color' => int];
```  


Or, if you're into Lua:

```lua
wallPaper={_='wallPaper', id=int, title='string', sizes={PhotoSize}, color=int}

```


