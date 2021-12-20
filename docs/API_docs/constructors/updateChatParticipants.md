---
title: "updateChatParticipants"
description: "Composition of chat participants changed."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipants  
[Back to constructors index](index.md)



Composition of chat participants changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participants|[ChatParticipants](../types/ChatParticipants.md) | Yes|Updated chat participants|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipants = ['_' => 'updateChatParticipants', 'participants' => ChatParticipants];
```  


Or, if you're into Lua:

```lua
updateChatParticipants={_='updateChatParticipants', participants=ChatParticipants}

```


