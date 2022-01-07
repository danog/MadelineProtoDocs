---
title: "groupCall"
description: "groupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCall  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|join\_muted|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_change\_join\_muted|[Bool](/API_docs/types/Bool.html) | Optional|
|join\_date\_asc|[Bool](/API_docs/types/Bool.html) | Optional|
|schedule\_start\_subscribed|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_start\_video|[Bool](/API_docs/types/Bool.html) | Optional|
|record\_video\_active|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|
|access\_hash|[long](/API_docs/types/long.html) | Yes|
|participants\_count|[int](/API_docs/types/int.html) | Yes|
|title|[string](/API_docs/types/string.html) | Optional|
|stream\_dc\_id|[int](/API_docs/types/int.html) | Optional|
|record\_start\_date|[int](/API_docs/types/int.html) | Optional|
|schedule\_date|[int](/API_docs/types/int.html) | Optional|
|unmuted\_video\_count|[int](/API_docs/types/int.html) | Optional|
|unmuted\_video\_limit|[int](/API_docs/types/int.html) | Yes|
|version|[int](/API_docs/types/int.html) | Yes|



### Type: [GroupCall](/API_docs/types/GroupCall.html)


### Example:

```php
$groupCall = ['_' => 'groupCall', 'join_muted' => Bool, 'can_change_join_muted' => Bool, 'join_date_asc' => Bool, 'schedule_start_subscribed' => Bool, 'can_start_video' => Bool, 'record_video_active' => Bool, 'id' => long, 'access_hash' => long, 'participants_count' => int, 'title' => 'string', 'stream_dc_id' => int, 'record_start_date' => int, 'schedule_date' => int, 'unmuted_video_count' => int, 'unmuted_video_limit' => int, 'version' => int];
```  
