---
title: "peerSettings"
description: "List of actions that are possible when interacting with this user, to be shown as suggested actions in the chat action bar », see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerSettings  
[Back to constructors index](/API_docs/constructors/index.html)



List of actions that are possible when interacting with this user, to be shown as suggested actions in the [chat action bar »](https://core.telegram.org/api/action-bar), see [here »](https://core.telegram.org/api/action-bar) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|report\_spam|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can still report the user for spam|
|add\_contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can add the user as contact|
|block\_contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can block the user|
|share\_contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can share the user's contact|
|need\_contacts\_exception|[Bool](/API_docs/types/Bool.html) | Optional|Whether a special exception for contacts is needed|
|report\_geo|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can report a geogroup as irrelevant for this location|
|autoarchived|[Bool](/API_docs/types/Bool.html) | Optional|Whether this peer was automatically archived according to [privacy settings](../constructors/globalPrivacySettings.html) and can be unarchived|
|invite\_members|[Bool](/API_docs/types/Bool.html) | Optional|If set, this is a recently created group chat to which new members can be invited|
|request\_chat\_broadcast|[Bool](/API_docs/types/Bool.html) | Optional|This flag is set if `request_chat_title` and `request_chat_date` fields are set and the [join request »](https://core.telegram.org/api/invites#join-requests) is related to a channel (otherwise if only the request fields are set, the [join request »](https://core.telegram.org/api/invites#join-requests) is related to a chat).|
|business\_bot\_paused|[Bool](/API_docs/types/Bool.html) | Optional|This flag is set if both `business_bot_id` and `business_bot_manage_url` are set and all [connected business bots »](https://core.telegram.org/api/bots/connected-business-bots) were paused in this chat using [account.toggleConnectedBotPaused »](../methods/account.toggleConnectedBotPaused.html).|
|business\_bot\_can\_reply|[Bool](/API_docs/types/Bool.html) | Optional|This flag is set if both `business_bot_id` and `business_bot_manage_url` are set and [connected business bots »](https://core.telegram.org/api/bots/connected-business-bots) can reply to messages in this chat, as specified by the settings during [initial configuration](https://core.telegram.org/api/bots/connected-business-bots).|
|geo\_distance|[int](/API_docs/types/int.html) | Optional|Distance in meters between us and this peer|
|request\_chat\_title|[string](/API_docs/types/string.html) | Optional|If set, this is a private chat with an administrator of a chat or channel to which the user sent a join request, and this field contains the chat/channel's title.|
|request\_chat\_date|[int](/API_docs/types/int.html) | Optional|If set, this is a private chat with an administrator of a chat or channel to which the user sent a join request, and this field contains the timestamp when the [join request »](https://core.telegram.org/api/invites#join-requests) was sent.|
|business\_bot\_id|[long](/API_docs/types/long.html) | Optional|Contains the ID of the [business bot »](https://core.telegram.org/api/bots/connected-business-bots) managing this chat, used to display info about the bot in the action bar.|
|business\_bot\_manage\_url|[string](/API_docs/types/string.html) | Optional|Contains a [deep link »](https://core.telegram.org/api/links), used to open a management menu in the business bot. This flag is set if and only if `business_bot_id` is set.|
|charge\_paid\_message\_stars|[long](/API_docs/types/long.html) | Optional|All users that must [pay *us* »](https://core.telegram.org/api/paid-messages) to send us private messages will have this flag set *only for us*, containing the amount of required stars, see [here »](https://core.telegram.org/api/paid-messages) for more info on paid messages.|
|registration\_month|[string](/API_docs/types/string.html) | Optional|Used to display the user's registration year and month, the string is in `MM.YYYY` format, where `MM` is the registration month (`1-12`), and `YYYY` is the registration year.|
|phone\_country|[string](/API_docs/types/string.html) | Optional|The country code of the user's phone number.|
|name\_change\_date|[int](/API_docs/types/int.html) | Optional|When was the user's name last changed.|
|photo\_change\_date|[int](/API_docs/types/int.html) | Optional|When was the user's photo last changed.|



### Type: [PeerSettings](/API_docs/types/PeerSettings.html)


### Example:

```
$peerSettings = ['_' => 'peerSettings', 'report_spam' => Bool, 'add_contact' => Bool, 'block_contact' => Bool, 'share_contact' => Bool, 'need_contacts_exception' => Bool, 'report_geo' => Bool, 'autoarchived' => Bool, 'invite_members' => Bool, 'request_chat_broadcast' => Bool, 'business_bot_paused' => Bool, 'business_bot_can_reply' => Bool, 'geo_distance' => int, 'request_chat_title' => 'string', 'request_chat_date' => int, 'business_bot_id' => long, 'business_bot_manage_url' => 'string', 'charge_paid_message_stars' => long, 'registration_month' => 'string', 'phone_country' => 'string', 'name_change_date' => int, 'photo_change_date' => int];
```  
