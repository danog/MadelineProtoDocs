---
title: "phone.groupParticipants"
description: "Info about the participants of a group call or livestream"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupParticipants.html
---
# Constructor: phone.groupParticipants  
[Back to constructors index](/API_docs/constructors/index.html)



Info about the participants of a group call or livestream

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Number of participants|
|participants|Array of [GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|List of participants|
|next\_offset|[string](/API_docs/types/string.html) | Yes|If not empty, the specified list of participants is partial, and more participants can be fetched specifying this parameter as `offset` in [phone.getGroupParticipants](../methods/phone.getGroupParticipants.html).|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|
|version|[int](/API_docs/types/int.html) | Yes|Version info|



### Type: [phone.GroupParticipants](/API_docs/types/phone.GroupParticipants.html)


### Example:

```
$phone_groupParticipants = ['_' => 'phone.groupParticipants', 'count' => int, 'participants' => [GroupCallParticipant, GroupCallParticipant], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User], 'version' => int];
```  
