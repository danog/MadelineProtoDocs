---
title: "channelParticipantsMentions"
description: "This filter is used when looking for supergroup members to mention.  "
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsMentions  
[Back to constructors index](index.md)



This filter is used when looking for supergroup members to mention.  
This filter will automatically remove anonymous admins, and return even non-participant users that replied to a specific [thread](https://core.telegram.org/api/threads) through the [comment section](https://core.telegram.org/api/threads#channel-comments) of a channel.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](../types/string.md) | Optional|Filter by user name or username|
|top\_msg\_id|[int](../types/int.md) | Optional|Look only for users that posted in this [thread](https://core.telegram.org/api/threads)|



### Type: [ChannelParticipantsFilter](../types/ChannelParticipantsFilter.md)


### Example:

```php
$channelParticipantsMentions = ['_' => 'channelParticipantsMentions', 'q' => 'string', 'top_msg_id' => int];
```  


Or, if you're into Lua:

```lua
channelParticipantsMentions={_='channelParticipantsMentions', q='string', top_msg_id=int}

```


