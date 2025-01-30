---
title: "savedReactionTag"
description: "Info about a saved message reaction tag »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: savedReactionTag  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a [saved message reaction tag »](https://core.telegram.org/api/saved-messages#tags).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|[Reaction](https://core.telegram.org/api/reactions) associated to the tag.|
|title|[string](/API_docs/types/string.html) | Optional|Custom tag name assigned by the user (max 12 UTF-8 chars).|
|count|[int](/API_docs/types/int.html) | Yes|Number of messages tagged with this tag.|



### Type: [SavedReactionTag](/API_docs/types/SavedReactionTag.html)


### Example:

```
$savedReactionTag = ['_' => 'savedReactionTag', 'reaction' => Reaction, 'title' => 'string', 'count' => int];
```  
