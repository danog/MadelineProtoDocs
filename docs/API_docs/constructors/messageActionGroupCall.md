---
title: "messageActionGroupCall"
description: "messageActionGroupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGroupCall  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|duration|[int](/API_docs/types/int.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```php
$messageActionGroupCall = ['_' => 'messageActionGroupCall', 'call' => InputGroupCall, 'duration' => int];
```  
