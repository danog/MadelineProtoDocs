---
title: PWRTelegram chat
description: chat attributes, type and example
nav_exclude: true
---
## Constructor: PWRTelegram chat  



### Attributes:

| Name     |    Type       | Required |Description|
|----------|---------------|----------|-----------|
|type|[string](API_docs/types/string.html) | Yes|bot, user, channel, supergroup or chat|
|id|[long](API_docs/types/long.html) | Yes|bot API chat id|
|access\_hash|[long](API_docs/types/long.html) | Optional|access hash of peer|
|first\_name|[string](API_docs/types/string.html) | Optional|First name of the user|
|last\_name|[string](API_docs/types/string.html) | Optional|Last name of the user|
|lang\_code|[string](API_docs/types/string.html) | Optional|Language of the user|
|username|[string](API_docs/types/string.html) | Optional|Username|
|verified|[Bool](API_docs/types/Bool.html) | Optional|Is the peer official?|
|restricted|[Bool](API_docs/types/Bool.html) | Optional|Is the peer restricted to the current user?|
|restriction\_reason|[string](API_docs/types/string.html) | Optional|Restriction reason|
|status|[UserStatus](API_docs/types/UserStatus.html) | Optional|Describes last time user was online|
|bot\_inline\_placeholder|[string](API_docs/types/string.html) | Optional|Inline placeholder of inline bot|
|bot\_nochats|[Bool](API_docs/types/Bool.html) | Optional|Can the bot be added to a group|
|about|[string](API_docs/types/string.html) | Optional|Description of supergroups/channels or bios of users|
|bot\_info|[BotInfo](API_docs/types/BotInfo.html) | Optional|Bot info of bots|
|phone\_calls\_available|[Bool](API_docs/types/Bool.html) | Optional|Are phone calls available for that user?|
|phone\_calls\_private|[Bool](API_docs/types/Bool.html) | Optional||
|common\_chats\_count|[int](API_docs/types/int.html) | Optional|Number of chats in common with that user|
|photo|[string](API_docs/types/string.html) | Optional|bot API file object the profile picture|
|title|[string](API_docs/types/string.html) | Optional|Chat title|
|participants\_count|[int](API_docs/types/int.html) | Optional|Number of participants in the chat.|
|kicked\_count|[int](API_docs/types/int.html) | Optional|Number of users kicked from the chat.|
|admin\_count|[int](API_docs/types/int.html) | Optional|Number of admins in the chat.|
|admin|[Bool](API_docs/types/Bool.html) | Optional|Are you an admin in this chat?|
|all\_members\_are\_administrators|[Bool](API_docs/types/Bool.html) | Optional|True if a group has ‘All Members Are Admins’ enabled.|
|invite|[string](API_docs/types/string.html) | Optional|Invite link of the chat|
|participants|Array of [Participant](Participant.html) | Yes|Chat participants|
|democracy|[Bool](API_docs/types/Bool.html) | Optional|Can everyone add users to this chat?|
|signatures|[Bool](API_docs/types/Bool.html) | Optional|Are channel signatures enabled?|
|can\_view\_participants|[Bool](API_docs/types/Bool.html) | Optional|Can you view participants (you can still view the bots in channels even if this is false)|
|can\_set\_username|[Bool](API_docs/types/Bool.html) | Optional|Can you set the username of this channel/supergroup?|
|can\_set\_stickers|[Bool](API_docs/types/Bool.html) | Optional|Can you set the associated stickerpack of this channel/supergroup?|
|stickerset|[StickerSet](API_docs/types/StickerSet.html) | Optional|StickerSet associtaed to this channel/supergroup|
|migrated\_from\_chat\_id|[int](API_docs/types/int.html) | Optional|MTProto chat id of the original chat (render it negative to make it a bot API chat id)|
|migrated\_from\_max\_id|[int](API_docs/types/int.html) | Optional|Last message id before migration|
|pinned\_msg\_id|[int](API_docs/types/int.html) | Optional|Message id of pinned message|


