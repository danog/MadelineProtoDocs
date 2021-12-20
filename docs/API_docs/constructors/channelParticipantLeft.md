---
title: "channelParticipantLeft"
description: "A participant that left the channel/supergroup"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantLeft  
[Back to constructors index](index.md)



A participant that left the channel/supergroup

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantLeft = ['_' => 'channelParticipantLeft', 'peer' => Peer];
```  


Or, if you're into Lua:

```lua
channelParticipantLeft={_='channelParticipantLeft', peer=Peer}

```


