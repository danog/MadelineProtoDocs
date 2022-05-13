---
title: "chatInviteExported"
description: "Exported chat invite"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInviteExported  
[Back to constructors index](/API_docs/constructors/index.html)



Exported chat invite

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|revoked|[Bool](/API_docs/types/Bool.html) | Optional|Whether this chat invite was revoked|
|permanent|[Bool](/API_docs/types/Bool.html) | Optional|Whether this chat invite has no expiration|
|request\_needed|[Bool](/API_docs/types/Bool.html) | Optional|Whether users importing this invite link will have to be approved to join the channel or group|
|link|[string](/API_docs/types/string.html) | Yes|Chat invitation link|
|admin\_id|[long](/API_docs/types/long.html) | Yes|ID of the admin that created this chat invite|
|date|[int](/API_docs/types/int.html) | Yes|When was this chat invite created|
|start\_date|[int](/API_docs/types/int.html) | Optional|When was this chat invite last modified|
|expire\_date|[int](/API_docs/types/int.html) | Optional|When does this chat invite expire|
|usage\_limit|[int](/API_docs/types/int.html) | Optional|Maximum number of users that can join using this link|
|usage|[int](/API_docs/types/int.html) | Optional|How many users joined using this link|
|requested|[int](/API_docs/types/int.html) | Optional|Number of users that have already used this link to join|
|title|[string](/API_docs/types/string.html) | Optional|Custom description for the invite link, visible only to admins|



### Type: [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html)


### Example:

```
$chatInviteExported = ['_' => 'chatInviteExported', 'revoked' => Bool, 'permanent' => Bool, 'request_needed' => Bool, 'link' => 'string', 'admin_id' => long, 'date' => int, 'start_date' => int, 'expire_date' => int, 'usage_limit' => int, 'usage' => int, 'requested' => int, 'title' => 'string'];
```  
