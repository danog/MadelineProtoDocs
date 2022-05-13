---
title: "updateUserPhone"
description: "A user's phone number was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPhone  
[Back to constructors index](/API_docs/constructors/index.html)



A user's phone number was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|phone|[string](/API_docs/types/string.html) | Yes|New phone number|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateUserPhone = ['_' => 'updateUserPhone', 'user_id' => long, 'phone' => 'string'];
```  
