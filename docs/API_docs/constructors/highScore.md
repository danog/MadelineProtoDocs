---
title: "highScore"
description: "Game highscore"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: highScore  
[Back to constructors index](index.md)



Game highscore

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pos|[int](../types/int.md) | Yes|Position in highscore list|
|user\_id|[long](../types/long.md) | Yes|
|score|[int](../types/int.md) | Yes|Score|



### Type: [HighScore](../types/HighScore.md)


### Example:

```php
$highScore = ['_' => 'highScore', 'pos' => int, 'user_id' => long, 'score' => int];
```  


Or, if you're into Lua:

```lua
highScore={_='highScore', pos=int, user_id=long, score=int}

```


