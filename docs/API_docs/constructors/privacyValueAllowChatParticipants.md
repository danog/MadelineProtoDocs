---
title: "privacyValueAllowChatParticipants"
description: "Allow all participants of certain chats"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueAllowChatParticipants  
[Back to constructors index](/API_docs/constructors/index.html)



Allow all participants of certain chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [long](/API_docs/types/long.html) | Yes|Allowed chats|



### Type: [PrivacyRule](/API_docs/types/PrivacyRule.html)


### Example:

```
$privacyValueAllowChatParticipants = ['_' => 'privacyValueAllowChatParticipants', 'chats' => [long, long]];
```  
