---
title: "chatAdminWithInvites"
description: "chatAdminWithInvites attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatAdminWithInvites  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|admin\_id|[long](../types/long.md) | Yes|
|invites\_count|[int](../types/int.md) | Yes|
|revoked\_invites\_count|[int](../types/int.md) | Yes|



### Type: [ChatAdminWithInvites](../types/ChatAdminWithInvites.md)


### Example:

```php
$chatAdminWithInvites = ['_' => 'chatAdminWithInvites', 'admin_id' => long, 'invites_count' => int, 'revoked_invites_count' => int];
```  


Or, if you're into Lua:

```lua
chatAdminWithInvites={_='chatAdminWithInvites', admin_id=long, invites_count=int, revoked_invites_count=int}

```


