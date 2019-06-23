---
title: privacyValueAllowChatParticipants
description: Allow chat participants?
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueAllowChatParticipants  
[Back to constructors index](index.md)



Allow chat participants?

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [int](../types/int.md) | Yes|Allowed chats|



### Type: [PrivacyRule](../types/PrivacyRule.md)


### Example:

```php
$privacyValueAllowChatParticipants = ['_' => 'privacyValueAllowChatParticipants', 'chats' => [int, int]];
```  


Or, if you're into Lua:

```lua
privacyValueAllowChatParticipants={_='privacyValueAllowChatParticipants', chats={int}}

```


