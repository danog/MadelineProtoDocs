---
title: phoneCallDiscarded
description: Indicates a discarded phone call
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallDiscarded  
[Back to constructors index](index.md)



Indicates a discarded phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Call ID|
|reason|[PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md) | Optional|Why was the phone call discarded|
|duration|[int](../types/int.md) | Optional|Duration of the phone call in seconds|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCallDiscarded = ['_' => 'phoneCallDiscarded', 'id' => long, 'reason' => PhoneCallDiscardReason, 'duration' => int];
```  


Or, if you're into Lua:

```lua
phoneCallDiscarded={_='phoneCallDiscarded', id=long, reason=PhoneCallDiscardReason, duration=int}

```


