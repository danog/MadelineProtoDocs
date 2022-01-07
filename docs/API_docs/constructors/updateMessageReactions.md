---
title: "updateMessageReactions"
description: "New message reactions are available"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageReactions  
[Back to constructors index](/API_docs/constructors/index.md)



New message reactions are available

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|Peer|
|msg\_id|[int](/API_docs/types/int.md) | Yes|Message ID|
|reactions|[MessageReactions](/API_docs/types/MessageReactions.md) | Yes|Reactions|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateMessageReactions = ['_' => 'updateMessageReactions', 'peer' => Peer, 'msg_id' => int, 'reactions' => MessageReactions];
```  
