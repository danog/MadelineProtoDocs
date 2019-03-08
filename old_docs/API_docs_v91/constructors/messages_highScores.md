---
title: messages.highScores
description: High scores
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.highScores  
[Back to constructors index](index.md)



High scores

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|scores|Array of [HighScore](../types/HighScore.md) | Yes|Scores|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages\_HighScores](../types/messages_HighScores.md)


### Example:

```php
$messages_highScores = ['_' => 'messages.highScores', 'scores' => [HighScore, HighScore], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.highScores", "scores": [HighScore], "users": [User]}
```


Or, if you're into Lua:

```lua
messages_highScores={_='messages.highScores', scores={HighScore}, users={User}}

```


