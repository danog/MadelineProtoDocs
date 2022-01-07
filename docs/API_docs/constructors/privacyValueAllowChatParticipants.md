---
title: "privacyValueAllowChatParticipants"
description: "Allow all participants of certain chats"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueAllowChatParticipants  
[Back to constructors index](index.md)



Allow all participants of certain chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [long](../types/long.md) | Yes|Allowed chats|



### Type: [PrivacyRule](../types/PrivacyRule.md)


### Example:

```php
$privacyValueAllowChatParticipants = ['_' => 'privacyValueAllowChatParticipants', 'chats' => [long, long]];
```  
