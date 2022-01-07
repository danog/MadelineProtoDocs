---
title: "messageActionGroupCall"
description: "messageActionGroupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGroupCall  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.md) | Yes|
|duration|[int](/API_docs/types/int.md) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.md)


### Example:

```php
$messageActionGroupCall = ['_' => 'messageActionGroupCall', 'call' => InputGroupCall, 'duration' => int];
```  
