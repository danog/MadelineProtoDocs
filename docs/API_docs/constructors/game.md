---
title: "game"
description: "Indicates an already sent game"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: game  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates an already sent game

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|ID of the game|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash of the game|
|short\_name|[string](/API_docs/types/string.html) | Yes|Short name for the game|
|title|[string](/API_docs/types/string.html) | Yes|Title of the game|
|description|[string](/API_docs/types/string.html) | Yes|Game description|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Game preview|
|document|[Document](/API_docs/types/Document.html) | Optional|Optional attached document|



### Type: [Game](/API_docs/types/Game.html)


### Example:

```
$game = ['_' => 'game', 'id' => long, 'access_hash' => long, 'short_name' => 'string', 'title' => 'string', 'description' => 'string', 'photo' => Photo, 'document' => Document];
```  
