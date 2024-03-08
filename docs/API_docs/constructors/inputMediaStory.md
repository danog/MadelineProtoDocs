---
title: "inputMediaStory"
description: "Forwarded story"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaStory  
[Back to constructors index](/API_docs/constructors/index.html)



Forwarded story

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|Peer where the story was posted|
|id|[int](/API_docs/types/int.html) | Yes|Story ID|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaStory = ['_' => 'inputMediaStory', 'peer' => InputPeer, 'id' => int];
```  
