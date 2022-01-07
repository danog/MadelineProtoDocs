---
title: "inputPrivacyValueAllowChatParticipants"
description: "Allow only participants of certain chats"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyValueAllowChatParticipants  
[Back to constructors index](/API_docs/constructors/index.md)



Allow only participants of certain chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [long](/API_docs/types/long.md) | Yes|Allowed chat IDs|



### Type: [InputPrivacyRule](/API_docs/types/InputPrivacyRule.md)


### Example:

```php
$inputPrivacyValueAllowChatParticipants = ['_' => 'inputPrivacyValueAllowChatParticipants', 'chats' => [long, long]];
```  
