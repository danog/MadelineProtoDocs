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
|need\_rating|[Bool](../types/Bool.md) | Optional|Need rating?|
|need\_debug|[Bool](../types/Bool.md) | Optional|Need debug?|
|video|[Bool](../types/Bool.md) | Optional|Video call?|
|id|[long](../types/long.md) | Yes|ID|
|reason|[PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md) | Optional|Reason|
|duration|[int](../types/int.md) | Optional|Duration|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCallDiscarded = ['_' => 'phoneCallDiscarded', 'need_rating' => Bool, 'need_debug' => Bool, 'video' => Bool, 'id' => long, 'reason' => PhoneCallDiscardReason, 'duration' => int];
```  


Or, if you're into Lua:

```lua
phoneCallDiscarded={_='phoneCallDiscarded', need_rating=Bool, need_debug=Bool, video=Bool, id=long, reason=PhoneCallDiscardReason, duration=int}

```


