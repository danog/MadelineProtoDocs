---
title: "phoneCallAccepted"
description: "An accepted phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallAccepted  
[Back to constructors index](/API_docs/constructors/index.html)



An accepted phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a video call|
|id|[long](/API_docs/types/long.html) | Yes|ID of accepted phone call|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash of phone call|
|date|[int](/API_docs/types/int.html) | Yes|When was the call accepted|
|admin\_id|[long](/API_docs/types/long.html) | Yes|ID of the call creator|
|participant\_id|[long](/API_docs/types/long.html) | Yes|ID of the other user in the call|
|g\_b|[bytes](/API_docs/types/bytes.html) | Yes|B parameter for [secure E2E phone call key exchange](https://core.telegram.org/api/end-to-end/voice-calls)|
|protocol|[PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html) | Yes|Protocol to use for phone call|



### Type: [PhoneCall](/API_docs/types/PhoneCall.html)


### Example:

```
$phoneCallAccepted = ['_' => 'phoneCallAccepted', 'video' => Bool, 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long, 'g_b' => 'bytes', 'protocol' => PhoneCallProtocol];
```  
