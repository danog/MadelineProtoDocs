---
title: "updateReadMessagesContents"
description: "Contents of messages in the common message box were read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadMessagesContents  
[Back to constructors index](/API_docs/constructors/index.html)



Contents of messages in the common [message box](https://core.telegram.org/api/updates) were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [int](/API_docs/types/int.html) | Yes|IDs of read messages|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateReadMessagesContents = ['_' => 'updateReadMessagesContents', 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  
