---
title: "messages.savedReactionTags"
description: "messages.savedReactionTags attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_savedReactionTags.html
---
# Constructor: messages.savedReactionTags  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|tags|Array of [SavedReactionTag](/API_docs/types/SavedReactionTag.html) | Yes|
|hash|[long](/API_docs/types/long.html) | Yes|



### Type: [messages.SavedReactionTags](/API_docs/types/messages.SavedReactionTags.html)


### Example:

```
$messages_savedReactionTags = ['_' => 'messages.savedReactionTags', 'tags' => [SavedReactionTag, SavedReactionTag], 'hash' => long];
```  
