---
title: "contactStatus"
description: "Contact status: online / offline."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contactStatus  
[Back to constructors index](/API_docs/constructors/index.md)



Contact status: online / offline.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|status|[UserStatus](/API_docs/types/UserStatus.md) | Optional|Online status|



### Type: [ContactStatus](/API_docs/types/ContactStatus.md)


### Example:

```php
$contactStatus = ['_' => 'contactStatus', 'user_id' => long, 'status' => UserStatus];
```  
