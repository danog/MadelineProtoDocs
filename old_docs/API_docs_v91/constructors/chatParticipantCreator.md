---
title: chatParticipantCreator
description: Represents the creator of the group
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantCreator  
[Back to constructors index](index.md)



Represents the creator of the group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|ID of the user that created the group|



### Type: [ChatParticipant](../types/ChatParticipant.md)


### Example:

```php
$chatParticipantCreator = ['_' => 'chatParticipantCreator', 'user_id' => int];
```  


Or, if you're into Lua:

```lua
chatParticipantCreator={_='chatParticipantCreator', user_id=int}

```


