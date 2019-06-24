---
title: privacyValueDisallowChatParticipants
description: Diallowed chats
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueDisallowChatParticipants  
[Back to constructors index](index.md)



Diallowed chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [int](../types/int.md) | Yes|Disallowed chats|



### Type: [PrivacyRule](../types/PrivacyRule.md)


### Example:

```php
$privacyValueDisallowChatParticipants = ['_' => 'privacyValueDisallowChatParticipants', 'chats' => [int, int]];
```  


Or, if you're into Lua:

```lua
privacyValueDisallowChatParticipants={_='privacyValueDisallowChatParticipants', chats={int}}

```


