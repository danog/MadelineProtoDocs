---
title: "missingInvitee"
description: "Info about why a specific user could not be invited »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: missingInvitee  
[Back to constructors index](/API_docs/constructors/index.html)



Info about why a specific user could not be [invited »](https://core.telegram.org/api/invites#direct-invites).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|premium\_would\_allow\_invite|[Bool](/API_docs/types/Bool.html) | Optional|If set, we could not add the user *only because* the current account needs to purchase a [Telegram Premium](https://core.telegram.org/api/premium) subscription to complete the operation.|
|premium\_required\_for\_pm|[Bool](/API_docs/types/Bool.html) | Optional|If set, we could not add the user because of their privacy settings, and additionally, the current account needs to purchase a [Telegram Premium](https://core.telegram.org/api/premium) subscription to directly share an invite link with the user via a private message.|
|user\_id|[long](/API_docs/types/long.html) | Yes|ID of the user. If neither of the flags below are set, we could not add the user because of their privacy settings, and we can create and directly share an [invite link](https://core.telegram.org/api/invites#invite-links) with them using a normal message, instead.|



### Type: [MissingInvitee](/API_docs/types/MissingInvitee.html)


### Example:

```
$missingInvitee = ['_' => 'missingInvitee', 'premium_would_allow_invite' => Bool, 'premium_required_for_pm' => Bool, 'user_id' => long];
```  
