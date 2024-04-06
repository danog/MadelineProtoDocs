---
title: "messages.invitedUsers"
description: "messages.invitedUsers attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_invitedUsers.html
---
# Constructor: messages.invitedUsers  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|updates|[Updates](/API_docs/types/Updates.html) | Yes|
|missing\_invitees|Array of [MissingInvitee](/API_docs/types/MissingInvitee.html) | Yes|



### Type: [messages.InvitedUsers](/API_docs/types/messages.InvitedUsers.html)


### Example:

```
$messages_invitedUsers = ['_' => 'messages.invitedUsers', 'updates' => Updates, 'missing_invitees' => [MissingInvitee, MissingInvitee]];
```  
