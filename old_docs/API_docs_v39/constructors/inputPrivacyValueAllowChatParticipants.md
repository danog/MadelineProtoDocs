---
title: inputPrivacyValueAllowChatParticipants
description: Allow only participants of certain chats
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyValueAllowChatParticipants  
[Back to constructors index](index.md)



Allow only participants of certain chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [int](../types/int.md) | Yes|Allowed chat IDs|



### Type: [InputPrivacyRule](../types/InputPrivacyRule.md)


### Example:

```php
$inputPrivacyValueAllowChatParticipants = ['_' => 'inputPrivacyValueAllowChatParticipants', 'chats' => [int, int]];
```  


Or, if you're into Lua:

```lua
inputPrivacyValueAllowChatParticipants={_='inputPrivacyValueAllowChatParticipants', chats={int}}

```


