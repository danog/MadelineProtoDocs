---
title: "messageInteractionCounters"
description: "Message interaction counters"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageInteractionCounters  
[Back to constructors index](/API_docs/constructors/index.md)



Message interaction counters

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_id|[int](/API_docs/types/int.md) | Yes|Message ID|
|views|[int](/API_docs/types/int.md) | Yes|Views|
|forwards|[int](/API_docs/types/int.md) | Yes|Number of times this message was forwarded|



### Type: [MessageInteractionCounters](/API_docs/types/MessageInteractionCounters.md)


### Example:

```php
$messageInteractionCounters = ['_' => 'messageInteractionCounters', 'msg_id' => int, 'views' => int, 'forwards' => int];
```  
