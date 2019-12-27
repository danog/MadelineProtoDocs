---
title: inputGameID
description: Indicates an already sent game
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGameID  
[Back to constructors index](index.md)



Indicates an already sent game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Game ID from [Game](../types/Game.md) constructor|
|access\_hash|[long](../types/long.md) | Yes|Access hash from [Game](../types/Game.md) constructor|



### Type: [InputGame](../types/InputGame.md)


### Example:

```php
$inputGameID = ['_' => 'inputGameID', 'id' => long, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputGameID={_='inputGameID', id=long, access_hash=long}

```


