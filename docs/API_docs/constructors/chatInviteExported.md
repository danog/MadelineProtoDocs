---
title: "chatInviteExported"
description: "Exported chat invite"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInviteExported  
[Back to constructors index](/API_docs/constructors/index.md)



Exported chat invite

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|revoked|[Bool](/API_docs/types/Bool.md) | Optional|
|permanent|[Bool](/API_docs/types/Bool.md) | Optional|
|request\_needed|[Bool](/API_docs/types/Bool.md) | Optional|
|link|[string](/API_docs/types/string.md) | Yes|Chat invitation link|
|admin\_id|[long](/API_docs/types/long.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|
|start\_date|[int](/API_docs/types/int.md) | Optional|
|expire\_date|[int](/API_docs/types/int.md) | Optional|
|usage\_limit|[int](/API_docs/types/int.md) | Optional|
|usage|[int](/API_docs/types/int.md) | Optional|
|requested|[int](/API_docs/types/int.md) | Optional|
|title|[string](/API_docs/types/string.md) | Optional|



### Type: [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md)


### Example:

```php
$chatInviteExported = ['_' => 'chatInviteExported', 'revoked' => Bool, 'permanent' => Bool, 'request_needed' => Bool, 'link' => 'string', 'admin_id' => long, 'date' => int, 'start_date' => int, 'expire_date' => int, 'usage_limit' => int, 'usage' => int, 'requested' => int, 'title' => 'string'];
```  
