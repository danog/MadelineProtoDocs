---
title: "phone.groupParticipants"
description: "phone.groupParticipants attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupParticipants.html
---
# Constructor: phone.groupParticipants  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.md) | Yes|
|participants|Array of [GroupCallParticipant](/API_docs/types/GroupCallParticipant.md) | Yes|
|next\_offset|[string](/API_docs/types/string.md) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.md) | Yes|
|users|Array of [User](/API_docs/types/User.md) | Yes|
|version|[int](/API_docs/types/int.md) | Yes|



### Type: [phone.GroupParticipants](/API_docs/types/phone.GroupParticipants.md)


### Example:

```php
$phone_groupParticipants = ['_' => 'phone.groupParticipants', 'count' => int, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User], 'version' => int];
```  
