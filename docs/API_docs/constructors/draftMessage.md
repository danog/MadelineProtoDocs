---
title: "draftMessage"
description: "Represents a message draft."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: draftMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a message [draft](https://core.telegram.org/api/drafts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|no\_webpage|[Bool](/API_docs/types/Bool.html) | Optional|Whether no webpage preview will be generated|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | Optional|The message this message will reply to|
|message|[string](/API_docs/types/string.html) | Yes|The draft|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Optional|Message [entities](https://core.telegram.org/api/entities) for styled text.|
|date|[int](/API_docs/types/int.html) | Yes|Date of last update of the draft.|



### Type: [DraftMessage](/API_docs/types/DraftMessage.html)


### Example:

```
$draftMessage = ['_' => 'draftMessage', 'no_webpage' => Bool, 'reply_to_msg_id' => int, 'message' => 'string', 'entities' => [MessageEntity, MessageEntity], 'date' => int];
```  
