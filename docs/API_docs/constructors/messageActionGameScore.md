---
title: "messageActionGameScore"
description: "Someone scored in a game"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGameScore  
[Back to constructors index](/API_docs/constructors/index.md)



Someone scored in a game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|game\_id|[long](/API_docs/types/long.md) | Yes|Game ID|
|score|[int](/API_docs/types/int.md) | Yes|Score|



### Type: [MessageAction](/API_docs/types/MessageAction.md)


### Example:

```php
$messageActionGameScore = ['_' => 'messageActionGameScore', 'game_id' => long, 'score' => int];
```  
