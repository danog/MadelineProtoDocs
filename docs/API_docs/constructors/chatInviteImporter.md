---
title: "chatInviteImporter"
description: "chatInviteImporter attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInviteImporter  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|requested|[Bool](/API_docs/types/Bool.md) | Optional|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|
|about|[string](/API_docs/types/string.md) | Optional|
|approved\_by|[long](/API_docs/types/long.md) | Optional|



### Type: [ChatInviteImporter](/API_docs/types/ChatInviteImporter.md)


### Example:

```php
$chatInviteImporter = ['_' => 'chatInviteImporter', 'requested' => Bool, 'user_id' => long, 'date' => int, 'about' => 'string', 'approved_by' => long];
```  
