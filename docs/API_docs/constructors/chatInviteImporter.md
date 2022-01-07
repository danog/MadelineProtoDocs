---
title: "chatInviteImporter"
description: "chatInviteImporter attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInviteImporter  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|requested|[Bool](/API_docs/types/Bool.html) | Optional|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|about|[string](/API_docs/types/string.html) | Optional|
|approved\_by|[long](/API_docs/types/long.html) | Optional|



### Type: [ChatInviteImporter](/API_docs/types/ChatInviteImporter.html)


### Example:

```php
$chatInviteImporter = ['_' => 'chatInviteImporter', 'requested' => Bool, 'user_id' => long, 'date' => int, 'about' => 'string', 'approved_by' => long];
```  
