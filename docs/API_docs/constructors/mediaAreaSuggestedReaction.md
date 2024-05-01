---
title: "mediaAreaSuggestedReaction"
description: "Represents a reaction bubble."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaSuggestedReaction  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a reaction bubble.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dark|[Bool](/API_docs/types/Bool.html) | Optional|Whether the reaction bubble has a dark background.|
|flipped|[Bool](/API_docs/types/Bool.html) | Optional|Whether the reaction bubble is mirrored (see [here »](https://core.telegram.org/api/stories#reactions) for more info).|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|The coordinates of the media area corresponding to the reaction button.|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|The reaction that should be sent when this area is clicked.|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaSuggestedReaction = ['_' => 'mediaAreaSuggestedReaction', 'dark' => Bool, 'flipped' => Bool, 'coordinates' => MediaAreaCoordinates, 'reaction' => Reaction];
```  
