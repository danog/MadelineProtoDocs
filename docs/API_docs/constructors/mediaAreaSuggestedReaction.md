---
title: "mediaAreaSuggestedReaction"
description: "mediaAreaSuggestedReaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaSuggestedReaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dark|[Bool](/API_docs/types/Bool.html) | Optional|
|flipped|[Bool](/API_docs/types/Bool.html) | Optional|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaSuggestedReaction = ['_' => 'mediaAreaSuggestedReaction', 'dark' => Bool, 'flipped' => Bool, 'coordinates' => MediaAreaCoordinates, 'reaction' => Reaction];
```  
