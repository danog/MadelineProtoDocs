---
title: "phoneCallDiscarded"
description: "Indicates a discarded phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallDiscarded  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates a discarded phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|need\_rating|[Bool](/API_docs/types/Bool.html) | Optional|Whether the server required the user to [rate](../methods/phone.setCallRating.html) the call|
|need\_debug|[Bool](/API_docs/types/Bool.html) | Optional|Whether the server required the client to [send](../methods/phone.saveCallDebug.html) the libtgvoip call debug data|
|video|[Bool](/API_docs/types/Bool.html) | Optional|Whether the call was a video call|
|id|[long](/API_docs/types/long.html) | Yes|Call ID|
|reason|[PhoneCallDiscardReason](/API_docs/types/PhoneCallDiscardReason.html) | Optional|Why was the phone call discarded|
|duration|[int](/API_docs/types/int.html) | Optional|Duration of the phone call in seconds|



### Type: [PhoneCall](/API_docs/types/PhoneCall.html)


### Example:

```
$phoneCallDiscarded = ['_' => 'phoneCallDiscarded', 'need_rating' => Bool, 'need_debug' => Bool, 'video' => Bool, 'id' => long, 'reason' => PhoneCallDiscardReason, 'duration' => int];
```  
