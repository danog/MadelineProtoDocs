---
title: "inputGameID"
description: "Indicates an already sent game"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGameID  
[Back to constructors index](/API_docs/constructors/index.md)



Indicates an already sent game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|game ID from [Game](../types/Game.md) constructor|
|access\_hash|[long](/API_docs/types/long.md) | Yes|access hash from [Game](../types/Game.md) constructor|



### Type: [InputGame](/API_docs/types/InputGame.md)


### Example:

```php
$inputGameID = ['_' => 'inputGameID', 'id' => long, 'access_hash' => long];
```  
