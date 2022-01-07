---
title: "messageActionPhoneCall"
description: "A phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPhoneCall  
[Back to constructors index](index.md)



A phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[Bool](../types/Bool.md) | Optional|Is this a video call?|
|call\_id|[long](../types/long.md) | Yes|Call ID|
|reason|[PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md) | Optional|If the call has ended, the reason why it ended|
|duration|[int](../types/int.md) | Optional|Duration of the call in seconds|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionPhoneCall = ['_' => 'messageActionPhoneCall', 'video' => Bool, 'call_id' => long, 'reason' => PhoneCallDiscardReason, 'duration' => int];
```  
