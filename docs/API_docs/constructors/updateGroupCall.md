---
title: "updateGroupCall"
description: "updateGroupCall attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCall  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|
|call|[GroupCall](/API_docs/types/GroupCall.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```php
$updateGroupCall = ['_' => 'updateGroupCall', 'chat_id' => long, 'call' => GroupCall];
```  
