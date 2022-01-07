---
title: "chatInvite"
description: "Chat invite info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInvite  
[Back to constructors index](/API_docs/constructors/index.md)



Chat invite info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is a [channel/supergroup](https://core.telegram.org/api/channel) or a [normal group](https://core.telegram.org/api/channel)|
|broadcast|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is a [channel](https://core.telegram.org/api/channel)|
|public|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is a public [channel/supergroup](https://core.telegram.org/api/channel)|
|megagroup|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is a [supergroup](https://core.telegram.org/api/channel)|
|request\_needed|[Bool](/API_docs/types/Bool.md) | Optional|
|title|[string](/API_docs/types/string.md) | Yes|Chat/supergroup/channel title|
|about|[string](/API_docs/types/string.md) | Optional|
|photo|[Photo](/API_docs/types/Photo.md) | Optional|Chat/supergroup/channel photo|
|participants\_count|[int](/API_docs/types/int.md) | Yes|Participant count|
|participants|Array of [User](/API_docs/types/User.md) | Optional|A few of the participants that are in the group|



### Type: [ChatInvite](/API_docs/types/ChatInvite.md)


### Example:

```php
$chatInvite = ['_' => 'chatInvite', 'channel' => Bool, 'broadcast' => Bool, 'public' => Bool, 'megagroup' => Bool, 'request_needed' => Bool, 'title' => 'string', 'about' => 'string', 'photo' => Photo, 'participants_count' => int, 'participants' => [User, User]];
```  
