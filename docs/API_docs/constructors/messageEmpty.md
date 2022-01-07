---
title: "messageEmpty"
description: "Empty constructor, non-existent message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEmpty  
[Back to constructors index](/API_docs/constructors/index.md)



Empty constructor, non-existent message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.md) | Yes|Message identifier|
|peer\_id|[Peer](/API_docs/types/Peer.md) | Optional|



### Type: [Message](/API_docs/types/Message.md)


### Example:

```php
$messageEmpty = ['_' => 'messageEmpty', 'id' => int, 'peer_id' => Peer];
```  
