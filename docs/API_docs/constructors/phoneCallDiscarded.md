---
title: "phoneCallDiscarded"
description: "Indicates a discarded phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallDiscarded  
[Back to constructors index](index.md)



Indicates a discarded phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|need\_rating|[Bool](../types/Bool.md) | Optional|Whether the server required the user to [rate](../methods/phone.setCallRating.md) the call|
|need\_debug|[Bool](../types/Bool.md) | Optional|Whether the server required the client to [send](../methods/phone.saveCallDebug.md) the libtgvoip call debug data|
|video|[Bool](../types/Bool.md) | Optional|Whether the call was a video call|
|id|[long](../types/long.md) | Yes|Call ID|
|reason|[PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md) | Optional|Why was the phone call discarded|
|duration|[int](../types/int.md) | Optional|Duration of the phone call in seconds|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCallDiscarded = ['_' => 'phoneCallDiscarded', 'need_rating' => Bool, 'need_debug' => Bool, 'video' => Bool, 'id' => long, 'reason' => PhoneCallDiscardReason, 'duration' => int];
```  
