---
title: "phoneCallWaiting"
description: "Incoming phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallWaiting  
[Back to constructors index](/API_docs/constructors/index.md)



Incoming phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[Bool](/API_docs/types/Bool.md) | Optional|Is this a video call|
|id|[long](/API_docs/types/long.md) | Yes|Call ID|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Access hash|
|date|[int](/API_docs/types/int.md) | Yes|Date|
|admin\_id|[long](/API_docs/types/long.md) | Yes|
|participant\_id|[long](/API_docs/types/long.md) | Yes|
|protocol|[PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.md) | Yes|Phone call protocol info|
|receive\_date|[int](/API_docs/types/int.md) | Optional|When was the phone call received|



### Type: [PhoneCall](/API_docs/types/PhoneCall.md)


### Example:

```php
$phoneCallWaiting = ['_' => 'phoneCallWaiting', 'video' => Bool, 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long, 'protocol' => PhoneCallProtocol, 'receive_date' => int];
```  
