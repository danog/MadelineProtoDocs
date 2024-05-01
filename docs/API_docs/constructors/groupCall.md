---
title: "groupCall"
description: "Info about a group call or livestream"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCall  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a group call or livestream

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|join\_muted|[Bool](/API_docs/types/Bool.html) | Optional|Whether the user should be muted upon joining the call|
|can\_change\_join\_muted|[Bool](/API_docs/types/Bool.html) | Optional|Whether the current user can change the value of the `join_muted` flag using [phone.toggleGroupCallSettings](../methods/phone.toggleGroupCallSettings.html)|
|join\_date\_asc|[Bool](/API_docs/types/Bool.html) | Optional|Specifies the ordering to use when locally sorting by date and displaying in the UI group call participants.|
|schedule\_start\_subscribed|[Bool](/API_docs/types/Bool.html) | Optional|Whether we subscribed to the scheduled call|
|can\_start\_video|[Bool](/API_docs/types/Bool.html) | Optional|Whether you can start streaming video into the call|
|record\_video\_active|[Bool](/API_docs/types/Bool.html) | Optional|Whether the group call is currently being recorded|
|rtmp\_stream|[Bool](/API_docs/types/Bool.html) | Optional|Whether RTMP streams are allowed|
|listeners\_hidden|[Bool](/API_docs/types/Bool.html) | Optional|Whether the listeners list is hidden and cannot be fetched using [phone.getGroupParticipants](../methods/phone.getGroupParticipants.html). The `phone.groupParticipants.count` and `groupCall.participants_count` counters will still include listeners.|
|id|[long](/API_docs/types/long.html) | Yes|Group call ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Group call access hash|
|participants\_count|[int](/API_docs/types/int.html) | Yes|Participant count|
|title|[string](/API_docs/types/string.html) | Optional|Group call title|
|stream\_dc\_id|[int](/API_docs/types/int.html) | Optional|DC ID to be used for livestream chunks|
|record\_start\_date|[int](/API_docs/types/int.html) | Optional|When was the recording started|
|schedule\_date|[int](/API_docs/types/int.html) | Optional|When is the call scheduled to start|
|unmuted\_video\_count|[int](/API_docs/types/int.html) | Optional|Number of people currently streaming video into the call|
|unmuted\_video\_limit|[int](/API_docs/types/int.html) | Yes|Maximum number of people allowed to stream video into the call|
|version|[int](/API_docs/types/int.html) | Yes|Version|



### Type: [GroupCall](/API_docs/types/GroupCall.html)


### Example:

```
$groupCall = ['_' => 'groupCall', 'join_muted' => Bool, 'can_change_join_muted' => Bool, 'join_date_asc' => Bool, 'schedule_start_subscribed' => Bool, 'can_start_video' => Bool, 'record_video_active' => Bool, 'rtmp_stream' => Bool, 'listeners_hidden' => Bool, 'id' => long, 'access_hash' => long, 'participants_count' => int, 'title' => 'string', 'stream_dc_id' => int, 'record_start_date' => int, 'schedule_date' => int, 'unmuted_video_count' => int, 'unmuted_video_limit' => int, 'version' => int];
```  
