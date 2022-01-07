---
title: "updateChatParticipants"
description: "Composition of chat participants changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipants  
[Back to constructors index](/API_docs/constructors/index.md)



Composition of chat participants changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participants|[ChatParticipants](/API_docs/types/ChatParticipants.md) | Yes|Updated chat participants|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateChatParticipants = ['_' => 'updateChatParticipants', 'participants' => ChatParticipants];
```  
