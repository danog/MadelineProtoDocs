---
title: "highScore"
description: "Game highscore"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: highScore  
[Back to constructors index](/API_docs/constructors/index.html)



Game highscore

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pos|[int](/API_docs/types/int.html) | Yes|Position in highscore list|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|score|[int](/API_docs/types/int.html) | Yes|Score|



### Type: [HighScore](/API_docs/types/HighScore.html)


### Example:

```
$highScore = ['_' => 'highScore', 'pos' => int, 'user_id' => long, 'score' => int];
```  
