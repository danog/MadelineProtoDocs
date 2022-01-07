---
title: "privacyValueDisallowChatParticipants"
description: "Disallow only participants of certain chats"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueDisallowChatParticipants  
[Back to constructors index](/API_docs/constructors/index.md)



Disallow only participants of certain chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [long](/API_docs/types/long.md) | Yes|Disallowed chats|



### Type: [PrivacyRule](/API_docs/types/PrivacyRule.md)


### Example:

```php
$privacyValueDisallowChatParticipants = ['_' => 'privacyValueDisallowChatParticipants', 'chats' => [long, long]];
```  
