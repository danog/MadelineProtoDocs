---
title: "updateBotStopped"
description: "updateBotStopped attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotStopped  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|stopped|[Bool](/API_docs/types/Bool.html) | Yes|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```php
$updateBotStopped = ['_' => 'updateBotStopped', 'user_id' => long, 'date' => int, 'stopped' => Bool, 'qts' => int];
```  
