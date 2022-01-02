---
title: "decryptedMessageService"
description: "Contents of an encrypted service message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageService\_17  
[Back to constructors index](index.md)



Contents of an encrypted service message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|action|[DecryptedMessageAction](../types/DecryptedMessageAction.md) | Yes|Action relevant to the service message|



### Type: [DecryptedMessage](../types/DecryptedMessage.md)


### Example:

```php
$decryptedMessageService_17 = ['_' => 'decryptedMessageService', 'action' => DecryptedMessageAction];
```  


Or, if you're into Lua:

```lua
decryptedMessageService_17={_='decryptedMessageService', action=DecryptedMessageAction}

```


