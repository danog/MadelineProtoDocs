---
title: "messages.savedReactionTags"
description: "List of reaction tag » names assigned by the user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_savedReactionTags.html
---
# Constructor: messages.savedReactionTags  
[Back to constructors index](/API_docs/constructors/index.html)



List of [reaction tag »](https://core.telegram.org/api/saved-messages#tags) names assigned by the user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|tags|Array of [SavedReactionTag](/API_docs/types/SavedReactionTag.html) | Yes|Saved reaction tags.|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|



### Type: [messages.SavedReactionTags](/API_docs/types/messages.SavedReactionTags.html)


### Example:

```
$messages_savedReactionTags = ['_' => 'messages.savedReactionTags', 'tags' => [SavedReactionTag, SavedReactionTag], 'hash' => long];
```  
