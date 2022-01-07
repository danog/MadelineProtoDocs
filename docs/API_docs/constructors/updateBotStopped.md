---
title: "updateBotStopped"
description: "updateBotStopped attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotStopped  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|
|stopped|[Bool](/API_docs/types/Bool.md) | Yes|
|qts|[int](/API_docs/types/int.md) | Yes|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateBotStopped = ['_' => 'updateBotStopped', 'user_id' => long, 'date' => int, 'stopped' => Bool, 'qts' => int];
```  
