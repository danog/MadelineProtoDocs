---
title: game
description: game attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: game  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|
|short\_name|[string](../types/string.md) | Yes|
|title|[string](../types/string.md) | Yes|
|description|[string](../types/string.md) | Yes|
|photo|[Photo](../types/Photo.md) | Optional|
|document|[Document](../types/Document.md) | Optional|



### Type: [Game](../types/Game.md)


### Example:

```php
$game = ['_' => 'game', 'id' => long, 'access_hash' => long, 'short_name' => 'string', 'title' => 'string', 'description' => 'string', 'photo' => Photo, 'document' => Document];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "game", "id": long, "access_hash": long, "short_name": "string", "title": "string", "description": "string", "photo": Photo, "document": Document}
```


Or, if you're into Lua:

```lua
game={_='game', id=long, access_hash=long, short_name='string', title='string', description='string', photo=Photo, document=Document}

```


