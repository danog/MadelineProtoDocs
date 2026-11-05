# phoneCallRequested

> Requested phone call

[Back to constructors index](/API_docs/constructors/index.html)



Requested phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a video call|
|id|[long](/API_docs/types/long.html) | Yes|Phone call ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|date|[int](/API_docs/types/int.html) | Yes|When was the phone call created|
|admin\_id|[long](/API_docs/types/long.html) | Yes|ID of the creator of the phone call|
|participant\_id|[long](/API_docs/types/long.html) | Yes|ID of the other participant of the phone call|
|g\_a\_hash|[bytes](/API_docs/types/bytes.html) | Yes|[Parameter for key exchange](https://core.telegram.org/api/end-to-end/voice-calls)|
|protocol|[PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html) | Yes|Call protocol info to be passed to libtgvoip|



### Type: [PhoneCall](/API_docs/types/PhoneCall.html)


### Example:

```
$phoneCallRequested = ['_' => 'phoneCallRequested', 'video' => Bool, 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long, 'g_a_hash' => 'bytes', 'protocol' => PhoneCallProtocol];
```
