---
title: "messageActionGroupCallScheduled"
description: "messageActionGroupCallScheduled attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGroupCallScheduled  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|schedule\_date|[int](/API_docs/types/int.html) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```php
$messageActionGroupCallScheduled = ['_' => 'messageActionGroupCallScheduled', 'call' => InputGroupCall, 'schedule_date' => int];
```  
