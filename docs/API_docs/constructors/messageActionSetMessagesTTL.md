---
title: "messageActionSetMessagesTTL"
description: "The Time-To-Live of messages in this chat was changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSetMessagesTTL  
[Back to constructors index](/API_docs/constructors/index.html)



The Time-To-Live of messages in this chat was changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|period|[int](/API_docs/types/int.html) | Yes|New Time-To-Live|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSetMessagesTTL = ['_' => 'messageActionSetMessagesTTL', 'period' => int];
```  
