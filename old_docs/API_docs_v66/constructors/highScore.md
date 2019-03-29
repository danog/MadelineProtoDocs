---
title: highScore
description: High score
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: highScore  
[Back to constructors index](index.md)



High score

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pos|[int](../types/int.md) | Yes|Pos|
|user\_id|[int](../types/int.md) | Yes|User ID|
|score|[int](../types/int.md) | Yes|Score|



### Type: [HighScore](../types/HighScore.md)


### Example:

```php
$highScore = ['_' => 'highScore', 'pos' => int, 'user_id' => int, 'score' => int];
```  


Or, if you're into Lua:

```lua
highScore={_='highScore', pos=int, user_id=int, score=int}

```


