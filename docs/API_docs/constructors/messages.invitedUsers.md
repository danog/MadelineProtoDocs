---
title: "messages.invitedUsers"
description: "Contains info about successfully or unsuccessfully invited » users."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_invitedUsers.html
---
# Constructor: messages.invitedUsers  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about successfully or unsuccessfully [invited »](https://core.telegram.org/api/invites#direct-invites) users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|updates|[Updates](/API_docs/types/Updates.html) | Yes|List of updates about successfully invited users (and eventually info about the created group)|
|missing\_invitees|Array of [MissingInvitee](/API_docs/types/MissingInvitee.html) | Yes|A list of users that could not be invited, along with the reason why they couldn't be invited.|



### Type: [messages.InvitedUsers](/API_docs/types/messages.InvitedUsers.html)


### Example:

```
$messages_invitedUsers = ['_' => 'messages.invitedUsers', 'updates' => Updates, 'missing_invitees' => [MissingInvitee, MissingInvitee]];
```  
