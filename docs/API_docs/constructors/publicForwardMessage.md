---
title: "publicForwardMessage"
description: "Contains info about a forward of a story as a message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: publicForwardMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a forward of a [story](https://core.telegram.org/api/stories) as a message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.html) | Optional|Info about the message with the reposted story.|



### Type: [PublicForward](/API_docs/types/PublicForward.html)


### Example:

```
$publicForwardMessage = ['_' => 'publicForwardMessage', 'message' => Message];
```  
