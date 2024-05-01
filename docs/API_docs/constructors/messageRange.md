---
title: "messageRange"
description: "Indicates a range of chat messages"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageRange  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates a range of chat messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min\_id|[int](/API_docs/types/int.html) | Yes|Start of range (message ID)|
|max\_id|[int](/API_docs/types/int.html) | Yes|End of range (message ID)|



### Type: [MessageRange](/API_docs/types/MessageRange.html)


### Example:

```
$messageRange = ['_' => 'messageRange', 'min_id' => int, 'max_id' => int];
```  
