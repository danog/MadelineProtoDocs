---
title: Participant
description: PWRTelegram participant attributes, type and example
nav_exclude: true
---
## Constructor: PWRTelegram chat participant  



### Attributes:

| Name     |    Type       | Required | Description|
|----------|---------------|----------|------------|
|user|[Chat](Chat.html) | Yes| The participant|
|inviter|[Chat](Chat.html) | Optional|The user that invited this participant|
|promoted_by|[Chat](Chat.html) | Optional|The user that promoted this participant|
|kicked_by|[Chat](Chat.html) | Optional|The user that kicked this participant|
|date|[int](API_docs/types/int.html) | Yes|When was the user invited|
|role|[string](API_docs/types/string.html) | Yes|user, admin, creator, banned|
|rank|[string](API_docs/types/string.html) | Optional|A custom rank string for admins and creators|
|can_edit|[Bool](API_docs/types/Bool.html) | Optional|Can the user edit messages in the channel|
|left|[Bool](API_docs/types/Bool.html) | Optional|Has this user left|
|admin_rights|[ChatAdminRights](API_docs/types/ChatAdminRights.html) | Optional|Admin rights|
|banned_rights|[ChatBannedRights](API_docs/types/ChatBannedRights.html) | Optional|Banned rights|
