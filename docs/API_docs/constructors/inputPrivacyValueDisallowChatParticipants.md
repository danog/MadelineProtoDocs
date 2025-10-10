---
title: "inputPrivacyValueDisallowChatParticipants"
description: "Disallow only participants of certain chats"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyValueDisallowChatParticipants  
[Back to constructors index](/API_docs/constructors/index.html)



Disallow only participants of certain chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [long](/API_docs/types/long.html) | Yes|Disallowed chat IDs (either a [chat](../constructors/chat.html) or a [supergroup](../constructors/channel.html) ID, verbatim the way it is received in the constructor (i.e. unlike with bot API IDs, here group and supergroup IDs should be treated in the same way)).|



### Type: [InputPrivacyRule](/API_docs/types/InputPrivacyRule.html)


### Example:

```
$inputPrivacyValueDisallowChatParticipants = ['_' => 'inputPrivacyValueDisallowChatParticipants', 'chats' => [long, long]];
```  
