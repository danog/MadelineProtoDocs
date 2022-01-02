---
title: "updateDraftMessage"
description: "Notifies a change of a message draft."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDraftMessage  
[Back to constructors index](index.md)



Notifies a change of a message [draft](https://core.telegram.org/api/drafts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|The peer to which the draft is associated|
|draft|[DraftMessage](../types/DraftMessage.md) | Optional|The draft|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDraftMessage = ['_' => 'updateDraftMessage', 'peer' => Peer, 'draft' => DraftMessage];
```  


Or, if you're into Lua:

```lua
updateDraftMessage={_='updateDraftMessage', peer=Peer, draft=DraftMessage}

```


