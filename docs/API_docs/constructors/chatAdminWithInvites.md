---
title: "chatAdminWithInvites"
description: "chatAdminWithInvites attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatAdminWithInvites  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|admin\_id|[long](/API_docs/types/long.html) | Yes|
|invites\_count|[int](/API_docs/types/int.html) | Yes|
|revoked\_invites\_count|[int](/API_docs/types/int.html) | Yes|



### Type: [ChatAdminWithInvites](/API_docs/types/ChatAdminWithInvites.html)


### Example:

```php
$chatAdminWithInvites = ['_' => 'chatAdminWithInvites', 'admin_id' => long, 'invites_count' => int, 'revoked_invites_count' => int];
```  
