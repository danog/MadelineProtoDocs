---
title: "phone.groupParticipants"
description: "phone.groupParticipants attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupParticipants.html
---
# Constructor: phone.groupParticipants  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](../types/int.md) | Yes|
|participants|Array of [GroupCallParticipant](../types/GroupCallParticipant.md) | Yes|
|next\_offset|[string](../types/string.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|
|version|[int](../types/int.md) | Yes|



### Type: [phone.GroupParticipants](../types/phone.GroupParticipants.md)


### Example:

```php
$phone_groupParticipants = ['_' => 'phone.groupParticipants', 'count' => int, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User], 'version' => int];
```  


Or, if you're into Lua:

```lua
phone_groupParticipants={_='phone.groupParticipants', count=int, participants={GroupCallParticipant}, next_offset='string', chats={Chat}, users={User}, version=int}

```


