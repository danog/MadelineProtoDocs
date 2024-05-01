---
title: "updateNewScheduledMessage"
description: "A message was added to the schedule queue of a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewScheduledMessage  
[Back to constructors index](/API_docs/constructors/index.html)



A message was added to the [schedule queue of a chat](https://core.telegram.org/api/scheduled-messages)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.html) | Optional|Message|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNewScheduledMessage = ['_' => 'updateNewScheduledMessage', 'message' => Message];
```  
