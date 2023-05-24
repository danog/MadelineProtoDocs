---
title: "updateGroupInvitePrivacyForbidden"
description: "0-N updates of this type may be returned only when invoking messages.addChatUser, channels.inviteToChannel or messages.createChat: it indicates we couldn't add a user to a chat because of their privacy settings; if required, an invite link can be shared with the user, instead."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupInvitePrivacyForbidden  
[Back to constructors index](/API_docs/constructors/index.html)



0-N updates of this type may be returned only when invoking [messages.addChatUser](../methods/messages.addChatUser.html), [channels.inviteToChannel](../methods/channels.inviteToChannel.html) or [messages.createChat](../methods/messages.createChat.html): it indicates we couldn't add a user to a chat because of their privacy settings; if required, an [invite link](https://core.telegram.org/api/invites) can be shared with the user, instead.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|ID of the user we couldn't add.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGroupInvitePrivacyForbidden = ['_' => 'updateGroupInvitePrivacyForbidden', 'user_id' => long];
```  
