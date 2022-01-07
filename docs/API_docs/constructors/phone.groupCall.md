---
title: "phone.groupCall"
description: "phone.groupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupCall.html
---
# Constructor: phone.groupCall  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[GroupCall](/API_docs/types/GroupCall.html) | Yes|
|participants|Array of [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|
|participants\_next\_offset|[string](/API_docs/types/string.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [phone.GroupCall](/API_docs/types/phone.GroupCall.html)


### Example:

```php
$phone_groupCall = ['_' => 'phone.groupCall', 'call' => GroupCall, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'participants_next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
