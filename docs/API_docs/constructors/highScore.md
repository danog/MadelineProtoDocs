---
title: "highScore"
description: "Game highscore"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: highScore  
[Back to constructors index](/API_docs/constructors/index.md)



Game highscore

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pos|[int](/API_docs/types/int.md) | Yes|Position in highscore list|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|score|[int](/API_docs/types/int.md) | Yes|Score|



### Type: [HighScore](/API_docs/types/HighScore.md)


### Example:

```php
$highScore = ['_' => 'highScore', 'pos' => int, 'user_id' => long, 'score' => int];
```  
