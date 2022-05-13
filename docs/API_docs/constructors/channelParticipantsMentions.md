---
title: "channelParticipantsMentions"
description: "This filter is used when looking for supergroup members to mention.  "
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantsMentions  
[Back to constructors index](/API_docs/constructors/index.html)



This filter is used when looking for supergroup members to mention.  
This filter will automatically remove anonymous admins, and return even non-participant users that replied to a specific [thread](https://core.telegram.org/api/threads) through the [comment section](https://core.telegram.org/api/threads#channel-comments) of a channel.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|q|[string](/API_docs/types/string.html) | Optional|Filter by user name or username|
|top\_msg\_id|[int](/API_docs/types/int.html) | Optional|Look only for users that posted in this [thread](https://core.telegram.org/api/threads)|



### Type: [ChannelParticipantsFilter](/API_docs/types/ChannelParticipantsFilter.html)


### Example:

```
$channelParticipantsMentions = ['_' => 'channelParticipantsMentions', 'q' => 'string', 'top_msg_id' => int];
```  
