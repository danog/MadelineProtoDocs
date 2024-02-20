---
title: "inputReplyToStory"
description: "inputReplyToStory attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputReplyToStory  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|story\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [InputReplyTo](/API_docs/types/InputReplyTo.html)


### Example:

```
$inputReplyToStory = ['_' => 'inputReplyToStory', 'peer' => InputPeer, 'story_id' => int];
```  
