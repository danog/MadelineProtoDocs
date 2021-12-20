---
title: "game"
description: "Indicates an already sent game"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: game  
[Back to constructors index](index.md)



Indicates an already sent game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID of the game|
|access\_hash|[long](../types/long.md) | Yes|Access hash of the game|
|short\_name|[string](../types/string.md) | Yes|Short name for the game|
|title|[string](../types/string.md) | Yes|Title of the game|
|description|[string](../types/string.md) | Yes|Game description|
|photo|[Photo](../types/Photo.md) | Optional|Game preview|
|document|[Document](../types/Document.md) | Optional|Optional attached document|



### Type: [Game](../types/Game.md)


### Example:

```php
$game = ['_' => 'game', 'id' => long, 'access_hash' => long, 'short_name' => 'string', 'title' => 'string', 'description' => 'string', 'photo' => Photo, 'document' => Document];
```  


Or, if you're into Lua:

```lua
game={_='game', id=long, access_hash=long, short_name='string', title='string', description='string', photo=Photo, document=Document}

```


