---
title: "privacyValueDisallowChatParticipants"
description: "Disallow only participants of certain chats"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: privacyValueDisallowChatParticipants  
[Back to constructors index](index.md)



Disallow only participants of certain chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [long](../types/long.md) | Yes|Disallowed chats|



### Type: [PrivacyRule](../types/PrivacyRule.md)


### Example:

```php
$privacyValueDisallowChatParticipants = ['_' => 'privacyValueDisallowChatParticipants', 'chats' => [long, long]];
```  


Or, if you're into Lua:

```lua
privacyValueDisallowChatParticipants={_='privacyValueDisallowChatParticipants', chats={long}}

```


