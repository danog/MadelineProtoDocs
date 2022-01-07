---
title: "messageActionInviteToGroupCall"
description: "messageActionInviteToGroupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionInviteToGroupCall  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.md) | Yes|
|users|Array of [long](/API_docs/types/long.md) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.md)


### Example:

```php
$messageActionInviteToGroupCall = ['_' => 'messageActionInviteToGroupCall', 'call' => InputGroupCall, 'users' => [long, long]];
```  
