---
title: "messages.highScores"
description: "Highscores in a game"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_highScores.html
---
# Constructor: messages.highScores  
[Back to constructors index](/API_docs/constructors/index.html)



Highscores in a game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|scores|Array of [HighScore](/API_docs/types/HighScore.html) | Yes|Highscores|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users, associated to the highscores|



### Type: [messages.HighScores](/API_docs/types/messages.HighScores.html)


### Example:

```
$messages_highScores = ['_' => 'messages.highScores', 'scores' => [HighScore, HighScore], 'users' => [User, User]];
```  
