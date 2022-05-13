---
title: "updateEditMessage"
description: "A message was edited"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEditMessage  
[Back to constructors index](/API_docs/constructors/index.html)



A message was edited

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.html) | Optional|The new edited message|
|pts|[int](/API_docs/types/int.html) | Yes|[PTS](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[PTS count](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateEditMessage = ['_' => 'updateEditMessage', 'message' => Message, 'pts' => int, 'pts_count' => int];
```  
