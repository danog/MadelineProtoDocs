---
title: "contactStatus"
description: "Contact status: online / offline."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contactStatus  
[Back to constructors index](/API_docs/constructors/index.html)



Contact status: online / offline.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User identifier|
|status|[UserStatus](/API_docs/types/UserStatus.html) | Optional|Online status|



### Type: [ContactStatus](/API_docs/types/ContactStatus.html)


### Example:

```
$contactStatus = ['_' => 'contactStatus', 'user_id' => long, 'status' => UserStatus];
```  
