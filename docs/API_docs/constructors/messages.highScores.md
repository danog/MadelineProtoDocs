---
title: "messages.highScores"
description: "Highscores in a game"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_highScores.html
---
# Constructor: messages.highScores  
[Back to constructors index](index.md)



Highscores in a game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|scores|Array of [HighScore](../types/HighScore.md) | Yes|Highscores|
|users|Array of [User](../types/User.md) | Yes|Users, associated to the highscores|



### Type: [messages.HighScores](../types/messages.HighScores.md)


### Example:

```php
$messages_highScores = ['_' => 'messages.highScores', 'scores' => [HighScore, HighScore], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_highScores={_='messages.highScores', scores={HighScore}, users={User}}

```


