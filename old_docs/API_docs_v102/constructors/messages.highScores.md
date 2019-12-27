---
title: messages.highScores
description: Highscores in a game
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.highScores  
[Back to constructors index](index.md)



Highscores in a game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|scores|Array of [HighScore](../types/HighScore.md) | Yes|Scores|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages.HighScores](../types/messages.HighScores.md)


### Example:

```php
$messages.highScores = ['_' => 'messages.highScores', 'scores' => [HighScore, HighScore], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages.highScores={_='messages.highScores', scores={HighScore}, users={User}}

```


