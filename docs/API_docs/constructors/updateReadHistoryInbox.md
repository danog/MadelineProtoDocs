---
title: "updateReadHistoryInbox"
description: "Incoming messages were read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadHistoryInbox  
[Back to constructors index](/API_docs/constructors/index.md)



Incoming messages were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](/API_docs/types/int.md) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|Peer|
|max\_id|[int](/API_docs/types/int.md) | Yes|Maximum ID of messages read|
|still\_unread\_count|[int](/API_docs/types/int.md) | Yes|Number of messages that are still unread|
|pts|[int](/API_docs/types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateReadHistoryInbox = ['_' => 'updateReadHistoryInbox', 'folder_id' => int, 'peer' => Peer, 'max_id' => int, 'still_unread_count' => int, 'pts' => int, 'pts_count' => int];
```  
