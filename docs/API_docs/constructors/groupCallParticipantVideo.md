---
title: "groupCallParticipantVideo"
description: "groupCallParticipantVideo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipantVideo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|paused|[Bool](../types/Bool.md) | Optional|
|endpoint|[string](../types/string.md) | Yes|
|source\_groups|Array of [GroupCallParticipantVideoSourceGroup](../types/GroupCallParticipantVideoSourceGroup.md) | Yes|
|audio\_source|[int](../types/int.md) | Optional|



### Type: [GroupCallParticipantVideo](../types/GroupCallParticipantVideo.md)


### Example:

```php
$groupCallParticipantVideo = ['_' => 'groupCallParticipantVideo', 'paused' => Bool, 'endpoint' => 'string', 'source_groups' => [GroupCallParticipantVideoSourceGroup, GroupCallParticipantVideoSourceGroup], 'audio_source' => int];
```  


Or, if you're into Lua:

```lua
groupCallParticipantVideo={_='groupCallParticipantVideo', paused=Bool, endpoint='string', source_groups={GroupCallParticipantVideoSourceGroup}, audio_source=int}

```


