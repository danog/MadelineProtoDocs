---
title: updateDraftMessage
description: Update draft message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDraftMessage  
[Back to constructors index](index.md)



Update draft message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|draft|[DraftMessage](../types/DraftMessage.md) | Optional|Draft|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDraftMessage = ['_' => 'updateDraftMessage', 'peer' => Peer, 'draft' => DraftMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateDraftMessage", "peer": Peer, "draft": DraftMessage}
```


Or, if you're into Lua:

```lua
updateDraftMessage={_='updateDraftMessage', peer=Peer, draft=DraftMessage}

```


