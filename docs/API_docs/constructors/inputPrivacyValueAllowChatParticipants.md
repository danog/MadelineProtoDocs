---
title: "inputPrivacyValueAllowChatParticipants"
description: "Allow only participants of certain chats"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPrivacyValueAllowChatParticipants  
[Back to constructors index](index.md)



Allow only participants of certain chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [long](../types/long.md) | Yes|Allowed chat IDs|



### Type: [InputPrivacyRule](../types/InputPrivacyRule.md)


### Example:

```php
$inputPrivacyValueAllowChatParticipants = ['_' => 'inputPrivacyValueAllowChatParticipants', 'chats' => [long, long]];
```  


Or, if you're into Lua:

```lua
inputPrivacyValueAllowChatParticipants={_='inputPrivacyValueAllowChatParticipants', chats={long}}

```


