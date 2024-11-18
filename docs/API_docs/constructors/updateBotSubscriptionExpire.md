---
title: "updateBotSubscriptionExpire"
description: "updateBotSubscriptionExpire attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotSubscriptionExpire  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|payload|[string](/API_docs/types/string.html) | Yes|
|invoice\_slug|[string](/API_docs/types/string.html) | Yes|
|until\_date|[int](/API_docs/types/int.html) | Yes|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotSubscriptionExpire = ['_' => 'updateBotSubscriptionExpire', 'user_id' => long, 'payload' => 'string', 'invoice_slug' => 'string', 'until_date' => int, 'qts' => int];
```  
