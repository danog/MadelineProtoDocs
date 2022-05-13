---
title: "inputGameID"
description: "Indicates an already sent game"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGameID  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates an already sent game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|game ID from [Game](../types/Game.html) constructor|
|access\_hash|[long](/API_docs/types/long.html) | Yes|access hash from [Game](../types/Game.html) constructor|



### Type: [InputGame](/API_docs/types/InputGame.html)


### Example:

```
$inputGameID = ['_' => 'inputGameID', 'id' => long, 'access_hash' => long];
```  
