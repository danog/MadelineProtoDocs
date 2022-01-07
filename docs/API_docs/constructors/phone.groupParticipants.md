---
title: "phone.groupParticipants"
description: "phone.groupParticipants attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupParticipants.html
---
# Constructor: phone.groupParticipants  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|participants|Array of [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|version|[int](/API_docs/types/int.html) | Yes|



### Type: [phone.GroupParticipants](/API_docs/types/phone.GroupParticipants.html)


### Example:

```php
$phone_groupParticipants = ['_' => 'phone.groupParticipants', 'count' => int, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User], 'version' => int];
```  
