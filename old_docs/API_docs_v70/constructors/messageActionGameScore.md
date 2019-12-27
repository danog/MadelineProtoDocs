---
title: messageActionGameScore
description: Someone scored in a game
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGameScore  
[Back to constructors index](index.md)



Someone scored in a game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|game\_id|[long](../types/long.md) | Yes|Game ID|
|score|[int](../types/int.md) | Yes|Score|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionGameScore = ['_' => 'messageActionGameScore', 'game_id' => long, 'score' => int];
```  


Or, if you're into Lua:

```lua
messageActionGameScore={_='messageActionGameScore', game_id=long, score=int}

```


