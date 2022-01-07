---
title: "contact"
description: "A contact of the current user that is registered in the system."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contact  
[Back to constructors index](/API_docs/constructors/index.md)



A contact of the current user that is registered in the system.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|mutual|[Bool](/API_docs/types/Bool.md) | Yes|Current user is in the user's contact list|



### Type: [Contact](/API_docs/types/Contact.md)


### Example:

```php
$contact = ['_' => 'contact', 'user_id' => long, 'mutual' => Bool];
```  
