---
title: game
description: Game
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: game  
[Back to constructors index](index.md)



Game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|short\_name|[string](../types/string.md) | Yes|Short name|
|title|[string](../types/string.md) | Yes|Title|
|description|[string](../types/string.md) | Yes|Description|
|photo|[Photo](../types/Photo.md) | Optional|Photo|
|document|[Document](../types/Document.md) | Optional|Document|



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


