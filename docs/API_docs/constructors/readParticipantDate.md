---
title: "readParticipantDate"
description: "Contains info about when a certain participant has read a message"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: readParticipantDate  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about when a certain participant has read a message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|date|[int](/API_docs/types/int.html) | Yes|When the user read the message|



### Type: [ReadParticipantDate](/API_docs/types/ReadParticipantDate.html)


### Example:

```
$readParticipantDate = ['_' => 'readParticipantDate', 'user_id' => long, 'date' => int];
```  
