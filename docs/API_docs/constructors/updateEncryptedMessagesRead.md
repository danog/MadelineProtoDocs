---
title: "updateEncryptedMessagesRead"
description: "Communication history in an encrypted chat was marked as read."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateEncryptedMessagesRead  
[Back to constructors index](/API_docs/constructors/index.html)



Communication history in an encrypted chat was marked as read.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](/API_docs/types/int.html) | Yes|Chat ID|
|max\_date|[int](/API_docs/types/int.html) | Yes|Maximum value of data for read messages|
|date|[int](/API_docs/types/int.html) | Yes|Time when messages were read|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateEncryptedMessagesRead = ['_' => 'updateEncryptedMessagesRead', 'chat_id' => int, 'max_date' => int, 'date' => int];
```  
