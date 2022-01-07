---
title: "phone.groupCall"
description: "phone.groupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupCall.html
---
# Constructor: phone.groupCall  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[GroupCall](/API_docs/types/GroupCall.md) | Yes|
|participants|Array of [GroupCallParticipant](/API_docs/types/GroupCallParticipant.md) | Yes|
|participants\_next\_offset|[string](/API_docs/types/string.md) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.md) | Yes|
|users|Array of [User](/API_docs/types/User.md) | Yes|



### Type: [phone.GroupCall](/API_docs/types/phone.GroupCall.md)


### Example:

```php
$phone_groupCall = ['_' => 'phone.groupCall', 'call' => GroupCall, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'participants_next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
