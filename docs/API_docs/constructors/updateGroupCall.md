---
title: "updateGroupCall"
description: "updateGroupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCall  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[long](../types/long.md) | Yes|
|call|[GroupCall](../types/GroupCall.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateGroupCall = ['_' => 'updateGroupCall', 'chat_id' => long, 'call' => GroupCall];
```  
