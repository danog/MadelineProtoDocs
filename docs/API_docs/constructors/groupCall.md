---
title: "groupCall"
description: "groupCall attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCall  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|join\_muted|[Bool](../types/Bool.md) | Optional|
|can\_change\_join\_muted|[Bool](../types/Bool.md) | Optional|
|join\_date\_asc|[Bool](../types/Bool.md) | Optional|
|schedule\_start\_subscribed|[Bool](../types/Bool.md) | Optional|
|can\_start\_video|[Bool](../types/Bool.md) | Optional|
|record\_video\_active|[Bool](../types/Bool.md) | Optional|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|
|participants\_count|[int](../types/int.md) | Yes|
|title|[string](../types/string.md) | Optional|
|stream\_dc\_id|[int](../types/int.md) | Optional|
|record\_start\_date|[int](../types/int.md) | Optional|
|schedule\_date|[int](../types/int.md) | Optional|
|unmuted\_video\_count|[int](../types/int.md) | Optional|
|unmuted\_video\_limit|[int](../types/int.md) | Yes|
|version|[int](../types/int.md) | Yes|



### Type: [GroupCall](../types/GroupCall.md)


### Example:

```php
$groupCall = ['_' => 'groupCall', 'join_muted' => Bool, 'can_change_join_muted' => Bool, 'join_date_asc' => Bool, 'schedule_start_subscribed' => Bool, 'can_start_video' => Bool, 'record_video_active' => Bool, 'id' => long, 'access_hash' => long, 'participants_count' => int, 'title' => 'string', 'stream_dc_id' => int, 'record_start_date' => int, 'schedule_date' => int, 'unmuted_video_count' => int, 'unmuted_video_limit' => int, 'version' => int];
```  


Or, if you're into Lua:

```lua
groupCall={_='groupCall', join_muted=Bool, can_change_join_muted=Bool, join_date_asc=Bool, schedule_start_subscribed=Bool, can_start_video=Bool, record_video_active=Bool, id=long, access_hash=long, participants_count=int, title='string', stream_dc_id=int, record_start_date=int, schedule_date=int, unmuted_video_count=int, unmuted_video_limit=int, version=int}

```


