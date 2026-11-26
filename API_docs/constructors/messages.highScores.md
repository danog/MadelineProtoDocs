# messages.highScores

> Highscores in a game

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
