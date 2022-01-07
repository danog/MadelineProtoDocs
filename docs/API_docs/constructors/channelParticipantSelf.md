---
title: "channelParticipantSelf"
description: "Myself"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantSelf  
[Back to constructors index](index.md)



Myself

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|via\_request|[Bool](../types/Bool.md) | Optional|
|user\_id|[long](../types/long.md) | Yes|
|inviter\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|When did I join the channel/supergroup|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantSelf = ['_' => 'channelParticipantSelf', 'via_request' => Bool, 'user_id' => long, 'inviter_id' => long, 'date' => int];
```  
