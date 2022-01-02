---
title: "updateGroupCallParticipants"
description: "updateGroupCallParticipants attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCallParticipants  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](../types/InputGroupCall.md) | Yes|
|participants|Array of [GroupCallParticipant](../types/GroupCallParticipant.md) | Yes|
|version|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateGroupCallParticipants = ['_' => 'updateGroupCallParticipants', 'call' => InputGroupCall, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'version' => int];
```  


Or, if you're into Lua:

```lua
updateGroupCallParticipants={_='updateGroupCallParticipants', call=InputGroupCall, participants={GroupCallParticipant}, version=int}

```


