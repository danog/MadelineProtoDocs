---
title: "updateUserStatus"
description: "Contact status update."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserStatus  
[Back to constructors index](/API_docs/constructors/index.md)



Contact status update.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|status|[UserStatus](/API_docs/types/UserStatus.md) | Optional|New status|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateUserStatus = ['_' => 'updateUserStatus', 'user_id' => long, 'status' => UserStatus];
```  
