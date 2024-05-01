---
title: "inputReplyToStory"
description: "Reply to a story."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputReplyToStory  
[Back to constructors index](/API_docs/constructors/index.html)



Reply to a story.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|story\_id|[int](/API_docs/types/int.html) | Yes|ID of the story to reply to.|



### Type: [InputReplyTo](/API_docs/types/InputReplyTo.html)


### Example:

```
$inputReplyToStory = ['_' => 'inputReplyToStory', 'peer' => InputPeer, 'story_id' => int];
```  
