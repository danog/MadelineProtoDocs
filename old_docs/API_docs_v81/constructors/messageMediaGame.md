---
title: messageMediaGame
description: messageMediaGame attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGame  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|game|[Game](../types/Game.md) | Yes|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaGame = ['_' => 'messageMediaGame', 'game' => Game];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageMediaGame", "game": Game}
```


Or, if you're into Lua:

```lua
messageMediaGame={_='messageMediaGame', game=Game}

```


