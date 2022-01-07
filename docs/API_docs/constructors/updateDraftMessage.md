---
title: "updateDraftMessage"
description: "Notifies a change of a message draft."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDraftMessage  
[Back to constructors index](/API_docs/constructors/index.md)



Notifies a change of a message [draft](https://core.telegram.org/api/drafts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|The peer to which the draft is associated|
|draft|[DraftMessage](/API_docs/types/DraftMessage.md) | Optional|The draft|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateDraftMessage = ['_' => 'updateDraftMessage', 'peer' => Peer, 'draft' => DraftMessage];
```  
