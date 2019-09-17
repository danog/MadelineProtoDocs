---
title: Participant
description: PWRTelegram participant attributes, type and example
---
## Constructor: PWRTelegram chat participant  



### Attributes:

| Name     |    Type       | Required | Description|
|----------|---------------|----------|------------|
|user|[Chat](Chat.md) | Yes| The participant|
|inviter|[Chat](Chat.md) | Optional|The user that invited this participant|
|promoted_by|[Chat](Chat.md) | Optional|The user that promoted this participant|
|kicked_by|[Chat](Chat.md) | Optional|The user that kicked this participant|
|date|[int](API_docs/types/int.md) | Yes|When was the user invited|
|role|[string](API_docs/types/string.md) | Yes|user, admin, creator, banned|
|rank|[string](API_docs/types/string.md) | Optional|A custom rank string for admins and creators|
|can_edit|[Bool](API_docs/types/Bool.md) | Optional|Can the user edit messages in the channel|
|left|[Bool](API_docs/types/Bool.md) | Optional|Has this user left|
|admin_rights|[ChatAdminRights](API_docs/types/ChatAdminRights.md) | Optional|Admin rights|
|banned_rights|[ChatBannedRights](API_docs/types/ChatBannedRights.md) | Optional|Banned rights|
