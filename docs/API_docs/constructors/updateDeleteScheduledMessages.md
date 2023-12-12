---
title: "updateDeleteScheduledMessages"
description: "Some scheduled messages were deleted from the schedule queue of a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteScheduledMessages  
[Back to constructors index](/API_docs/constructors/index.html)



Some [scheduled messages](https://core.telegram.org/api/scheduled-messages) were deleted from the schedule queue of a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|
|messages|Array of [int](/API_docs/types/int.html) | Yes|Deleted scheduled messages|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDeleteScheduledMessages = ['_' => 'updateDeleteScheduledMessages', 'peer' => long, 'messages' => [int, int]];
```  
