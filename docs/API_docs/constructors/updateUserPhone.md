---
title: "updateUserPhone"
description: "A user's phone number was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPhone  
[Back to constructors index](/API_docs/constructors/index.md)



A user's phone number was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|phone|[string](/API_docs/types/string.md) | Yes|New phone number|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateUserPhone = ['_' => 'updateUserPhone', 'user_id' => long, 'phone' => 'string'];
```  
