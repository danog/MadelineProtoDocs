---
title: "messageActionGameScore"
description: "Someone scored in a game"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGameScore  
[Back to constructors index](/API_docs/constructors/index.html)



Someone scored in a game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|game\_id|[long](/API_docs/types/long.html) | Yes|Game ID|
|score|[int](/API_docs/types/int.html) | Yes|Score|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGameScore = ['_' => 'messageActionGameScore', 'game_id' => long, 'score' => int];
```  
