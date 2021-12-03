---
title: chatInviteExported
description: Exported chat invite
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInviteExported  
[Back to constructors index](index.md)



Exported chat invite

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|revoked|[Bool](../types/Bool.md) | Optional|
|permanent|[Bool](../types/Bool.md) | Optional|
|request\_needed|[Bool](../types/Bool.md) | Optional|
|link|[string](../types/string.md) | Yes|Chat invitation link|
|admin\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|
|start\_date|[int](../types/int.md) | Optional|
|expire\_date|[int](../types/int.md) | Optional|
|usage\_limit|[int](../types/int.md) | Optional|
|usage|[int](../types/int.md) | Optional|
|requested|[int](../types/int.md) | Optional|
|title|[string](../types/string.md) | Optional|



### Type: [ExportedChatInvite](../types/ExportedChatInvite.md)


### Example:

```php
$chatInviteExported = ['_' => 'chatInviteExported', 'revoked' => Bool, 'permanent' => Bool, 'request_needed' => Bool, 'link' => 'string', 'admin_id' => long, 'date' => int, 'start_date' => int, 'expire_date' => int, 'usage_limit' => int, 'usage' => int, 'requested' => int, 'title' => 'string'];
```  


Or, if you're into Lua:

```lua
chatInviteExported={_='chatInviteExported', revoked=Bool, permanent=Bool, request_needed=Bool, link='string', admin_id=long, date=int, start_date=int, expire_date=int, usage_limit=int, usage=int, requested=int, title='string'}

```


