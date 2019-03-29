---
title: updateChatParticipants
description: Update chat participants
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipants  
[Back to constructors index](index.md)



Update chat participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participants|[ChatParticipants](../types/ChatParticipants.md) | Yes|Participants|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipants = ['_' => 'updateChatParticipants', 'participants' => ChatParticipants];
```  


Or, if you're into Lua:

```lua
updateChatParticipants={_='updateChatParticipants', participants=ChatParticipants}

```


