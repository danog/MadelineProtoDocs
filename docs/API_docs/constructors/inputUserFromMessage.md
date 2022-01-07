---
title: "inputUserFromMessage"
description: "Defines a min user that was seen in a certain message of a certain chat."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputUserFromMessage  
[Back to constructors index](index.md)



Defines a [min](https://core.telegram.org/api/min) user that was seen in a certain message of a certain chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|The chat where the user was seen|
|msg\_id|[int](../types/int.md) | Yes|The message ID|
|user\_id|[long](../types/long.md) | Yes|



### Type: [InputUser](../types/InputUser.md)


### Example:

```php
$inputUserFromMessage = ['_' => 'inputUserFromMessage', 'peer' => InputPeer, 'msg_id' => int, 'user_id' => long];
```  
