---
title: "chatInviteImporter"
description: "chatInviteImporter attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInviteImporter  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|requested|[Bool](../types/Bool.md) | Optional|
|user\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|
|about|[string](../types/string.md) | Optional|
|approved\_by|[long](../types/long.md) | Optional|



### Type: [ChatInviteImporter](../types/ChatInviteImporter.md)


### Example:

```php
$chatInviteImporter = ['_' => 'chatInviteImporter', 'requested' => Bool, 'user_id' => long, 'date' => int, 'about' => 'string', 'approved_by' => long];
```  
