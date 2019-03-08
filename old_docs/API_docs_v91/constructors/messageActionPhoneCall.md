---
title: messageActionPhoneCall
description: Message action phone call
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPhoneCall  
[Back to constructors index](index.md)



Message action phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|call\_id|[long](../types/long.md) | Yes|Call ID|
|reason|[PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md) | Optional|Reason|
|duration|[int](../types/int.md) | Optional|Duration|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionPhoneCall = ['_' => 'messageActionPhoneCall', 'call_id' => long, 'reason' => PhoneCallDiscardReason, 'duration' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionPhoneCall", "call_id": long, "reason": PhoneCallDiscardReason, "duration": int}
```


Or, if you're into Lua:

```lua
messageActionPhoneCall={_='messageActionPhoneCall', call_id=long, reason=PhoneCallDiscardReason, duration=int}

```


