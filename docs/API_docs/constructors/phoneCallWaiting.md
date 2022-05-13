---
title: "phoneCallWaiting"
description: "Incoming phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallWaiting  
[Back to constructors index](/API_docs/constructors/index.html)



Incoming phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[Bool](/API_docs/types/Bool.html) | Optional|Is this a video call|
|id|[long](/API_docs/types/long.html) | Yes|Call ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|date|[int](/API_docs/types/int.html) | Yes|Date|
|admin\_id|[long](/API_docs/types/long.html) | Yes|Admin ID|
|participant\_id|[long](/API_docs/types/long.html) | Yes|Participant ID|
|protocol|[PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html) | Yes|Phone call protocol info|
|receive\_date|[int](/API_docs/types/int.html) | Optional|When was the phone call received|



### Type: [PhoneCall](/API_docs/types/PhoneCall.html)


### Example:

```
$phoneCallWaiting = ['_' => 'phoneCallWaiting', 'video' => Bool, 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long, 'protocol' => PhoneCallProtocol, 'receive_date' => int];
```  
