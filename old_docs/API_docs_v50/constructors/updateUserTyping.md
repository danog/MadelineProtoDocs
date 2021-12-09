---
title: updateUserTyping
description: The user is preparing a message; typing, recording, uploading, etc. This update is valid for 6 seconds. If no repeated update received after 6 seconds, it should be considered that the user stopped doing whatever he's been doing.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserTyping  
[Back to constructors index](index.md)



The user is preparing a message; typing, recording, uploading, etc. This update is valid for 6 seconds. If no repeated update received after 6 seconds, it should be considered that the user stopped doing whatever he's been doing.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|action|[SendMessageAction](../types/SendMessageAction.md) | Yes|Action type<br>Param added in [Layer 17](https://core.telegram.org/api/layers#layer-17).|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserTyping = ['_' => 'updateUserTyping', 'user_id' => long, 'action' => SendMessageAction];
```  


Or, if you're into Lua:

```lua
updateUserTyping={_='updateUserTyping', user_id=long, action=SendMessageAction}

```


