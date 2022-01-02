---
title: "phone.groupCall"
description: "phone.groupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupCall.html
---
# Constructor: phone.groupCall  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[GroupCall](../types/GroupCall.md) | Yes|
|participants|Array of [GroupCallParticipant](../types/GroupCallParticipant.md) | Yes|
|participants\_next\_offset|[string](../types/string.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [phone.GroupCall](../types/phone.GroupCall.md)


### Example:

```php
$phone_groupCall = ['_' => 'phone.groupCall', 'call' => GroupCall, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'participants_next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
phone_groupCall={_='phone.groupCall', call=GroupCall, participants={GroupCallParticipant}, participants_next_offset='string', chats={Chat}, users={User}}

```


