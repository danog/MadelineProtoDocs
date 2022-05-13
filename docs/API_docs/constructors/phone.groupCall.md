---
title: "phone.groupCall"
description: "Contains info about a group call, and partial info about its participants."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupCall.html
---
# Constructor: phone.groupCall  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a group call, and partial info about its participants.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|call|[GroupCall](/API_docs/types/GroupCall.html) | Yes|Info about the group call|
|participants|Array of [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|A partial list of participants.|
|participants\_next\_offset|[string](/API_docs/types/string.html) | Yes|Next offset to use when fetching the remaining participants using [phone.getGroupParticipants](../methods/phone.getGroupParticipants.html)|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in the participants vector|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the participants vector|



### Type: [phone.GroupCall](/API_docs/types/phone.GroupCall.html)


### Example:

```
$phone_groupCall = ['_' => 'phone.groupCall', 'call' => GroupCall, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'participants_next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
