---
title: phoneCallDiscarded
description: Phone call discarded
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallDiscarded  
[Back to constructors index](index.md)



Phone call discarded

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|reason|[PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md) | Optional|Reason|
|duration|[int](../types/int.md) | Optional|Duration|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCallDiscarded = ['_' => 'phoneCallDiscarded', 'id' => long, 'reason' => PhoneCallDiscardReason, 'duration' => int];
```  


Or, if you're into Lua:

```lua
phoneCallDiscarded={_='phoneCallDiscarded', id=long, reason=PhoneCallDiscardReason, duration=int}

```


