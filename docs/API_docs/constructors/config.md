---
title: "config"
description: "Current configuration"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: config  
[Back to constructors index](/API_docs/constructors/index.html)



Current configuration

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phonecalls\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|Whether phone calls can be used|
|default\_p2p\_contacts|[Bool](/API_docs/types/Bool.html) | Optional|Whether the client should use P2P by default for phone calls with contacts|
|preload\_featured\_stickers|[Bool](/API_docs/types/Bool.html) | Optional|Whether the client should preload featured stickers|
|ignore\_phone\_entities|[Bool](/API_docs/types/Bool.html) | Optional|Whether the client should ignore phone [entities](https://core.telegram.org/api/entities)|
|revoke\_pm\_inbox|[Bool](/API_docs/types/Bool.html) | Optional|Whether incoming private messages can be deleted for both participants|
|blocked\_mode|[Bool](/API_docs/types/Bool.html) | Optional|Indicates that telegram is *probably* censored by governments/ISPs in the current region|
|pfs\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|Whether [pfs](https://core.telegram.org/api/pfs) was used|
|force\_try\_ipv6|[Bool](/API_docs/types/Bool.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|Current date at the server|
|expires|[int](/API_docs/types/int.html) | Yes|Expiration date of this config: when it expires it'll have to be refetched using [help.getConfig](../methods/help.getConfig.html)|
|test\_mode|[Bool](/API_docs/types/Bool.html) | Yes|Whether we're connected to the test DCs|
|this\_dc|[int](/API_docs/types/int.html) | Yes|ID of the DC that returned the reply|
|dc\_options|Array of [DcOption](/API_docs/types/DcOption.html) | Yes|DC IP list|
|dc\_txt\_domain\_name|[string](/API_docs/types/string.html) | Yes|Domain name for fetching encrypted DC list from DNS TXT record|
|chat\_size\_max|[int](/API_docs/types/int.html) | Yes|Maximum member count for normal [groups](https://core.telegram.org/api/channel)|
|megagroup\_size\_max|[int](/API_docs/types/int.html) | Yes|Maximum member count for [supergroups](https://core.telegram.org/api/channel)|
|forwarded\_count\_max|[int](/API_docs/types/int.html) | Yes|Maximum number of messages that can be forwarded at once using [messages.forwardMessages](../methods/messages.forwardMessages.html).|
|online\_update\_period\_ms|[int](/API_docs/types/int.html) | Yes|The client should [update its online status](../methods/account.updateStatus.html) every N milliseconds|
|offline\_blur\_timeout\_ms|[int](/API_docs/types/int.html) | Yes|Delay before offline status needs to be sent to the server|
|offline\_idle\_timeout\_ms|[int](/API_docs/types/int.html) | Yes|Time without any user activity after which it should be treated offline|
|online\_cloud\_timeout\_ms|[int](/API_docs/types/int.html) | Yes|If we are offline, but were online from some other client in last `online_cloud_timeout_ms` milliseconds after we had gone offline, then delay offline notification for `notify_cloud_delay_ms` milliseconds.|
|notify\_cloud\_delay\_ms|[int](/API_docs/types/int.html) | Yes|If we are offline, but online from some other client then delay sending the offline notification for `notify_cloud_delay_ms` milliseconds.|
|notify\_default\_delay\_ms|[int](/API_docs/types/int.html) | Yes|If some other client is online, then delay notification for `notification_default_delay_ms` milliseconds|
|push\_chat\_period\_ms|[int](/API_docs/types/int.html) | Yes|Not for client use|
|push\_chat\_limit|[int](/API_docs/types/int.html) | Yes|Not for client use|
|saved\_gifs\_limit|[int](/API_docs/types/int.html) | Yes|Maximum count of saved gifs|
|edit\_time\_limit|[int](/API_docs/types/int.html) | Yes|Only messages with age smaller than the one specified can be edited|
|revoke\_time\_limit|[int](/API_docs/types/int.html) | Yes|Only channel/supergroup messages with age smaller than the specified can be deleted|
|revoke\_pm\_time\_limit|[int](/API_docs/types/int.html) | Yes|Only private messages with age smaller than the specified can be deleted|
|rating\_e\_decay|[int](/API_docs/types/int.html) | Yes|Exponential decay rate for computing [top peer rating](https://core.telegram.org/api/top-rating)|
|stickers\_recent\_limit|[int](/API_docs/types/int.html) | Yes|Maximum number of recent stickers|
|stickers\_faved\_limit|[int](/API_docs/types/int.html) | Yes|Maximum number of faved stickers|
|channels\_read\_media\_period|[int](/API_docs/types/int.html) | Yes|Indicates that round videos (video notes) and voice messages sent in channels and older than the specified period must be marked as read|
|tmp\_sessions|[int](/API_docs/types/int.html) | Optional|Temporary [passport](https://core.telegram.org/passport) sessions|
|pinned\_dialogs\_count\_max|[int](/API_docs/types/int.html) | Yes|Maximum count of pinned dialogs|
|pinned\_infolder\_count\_max|[int](/API_docs/types/int.html) | Yes|Maximum count of dialogs per folder|
|call\_receive\_timeout\_ms|[int](/API_docs/types/int.html) | Yes|Maximum allowed outgoing ring time in VoIP calls: if the user we're calling doesn't reply within the specified time (in milliseconds), we should hang up the call|
|call\_ring\_timeout\_ms|[int](/API_docs/types/int.html) | Yes|Maximum allowed incoming ring time in VoIP calls: if the current user doesn't reply within the specified time (in milliseconds), the call will be automatically refused|
|call\_connect\_timeout\_ms|[int](/API_docs/types/int.html) | Yes|VoIP connection timeout: if the instance of libtgvoip on the other side of the call doesn't connect to our instance of libtgvoip within the specified time (in milliseconds), the call must be aborted|
|call\_packet\_timeout\_ms|[int](/API_docs/types/int.html) | Yes|If during a VoIP call a packet isn't received for the specified period of time, the call must be aborted|
|me\_url\_prefix|[string](/API_docs/types/string.html) | Yes|The domain to use to parse in-app links.<br>For example t.me indicates that t.me/username links should parsed to @username, t.me/addsticker/name should be parsed to the appropriate stickerset and so on...|
|autoupdate\_url\_prefix|[string](/API_docs/types/string.html) | Optional|URL to use to auto-update the current app|
|gif\_search\_username|[string](/API_docs/types/string.html) | Optional|Username of the bot to use to search for GIFs|
|venue\_search\_username|[string](/API_docs/types/string.html) | Optional|Username of the bot to use to search for venues|
|img\_search\_username|[string](/API_docs/types/string.html) | Optional|Username of the bot to use for image search|
|static\_maps\_provider|[string](/API_docs/types/string.html) | Optional|ID of the map provider to use for venues|
|caption\_length\_max|[int](/API_docs/types/int.html) | Yes|Maximum length of caption (length in utf8 codepoints)|
|message\_length\_max|[int](/API_docs/types/int.html) | Yes|Maximum length of messages (length in utf8 codepoints)|
|webfile\_dc\_id|[int](/API_docs/types/int.html) | Yes|DC ID to use to download [webfiles](https://core.telegram.org/api/files)|
|suggested\_lang\_code|[string](/API_docs/types/string.html) | Optional|Suggested language code|
|lang\_pack\_version|[int](/API_docs/types/int.html) | Optional|Language pack version|
|base\_lang\_pack\_version|[int](/API_docs/types/int.html) | Optional|Basic language pack version|



### Type: [Config](/API_docs/types/Config.html)


### Example:

```
$config = ['_' => 'config', 'phonecalls_enabled' => Bool, 'default_p2p_contacts' => Bool, 'preload_featured_stickers' => Bool, 'ignore_phone_entities' => Bool, 'revoke_pm_inbox' => Bool, 'blocked_mode' => Bool, 'pfs_enabled' => Bool, 'force_try_ipv6' => Bool, 'date' => int, 'expires' => int, 'test_mode' => Bool, 'this_dc' => int, 'dc_options' => [DcOption, DcOption], 'dc_txt_domain_name' => 'string', 'chat_size_max' => int, 'megagroup_size_max' => int, 'forwarded_count_max' => int, 'online_update_period_ms' => int, 'offline_blur_timeout_ms' => int, 'offline_idle_timeout_ms' => int, 'online_cloud_timeout_ms' => int, 'notify_cloud_delay_ms' => int, 'notify_default_delay_ms' => int, 'push_chat_period_ms' => int, 'push_chat_limit' => int, 'saved_gifs_limit' => int, 'edit_time_limit' => int, 'revoke_time_limit' => int, 'revoke_pm_time_limit' => int, 'rating_e_decay' => int, 'stickers_recent_limit' => int, 'stickers_faved_limit' => int, 'channels_read_media_period' => int, 'tmp_sessions' => int, 'pinned_dialogs_count_max' => int, 'pinned_infolder_count_max' => int, 'call_receive_timeout_ms' => int, 'call_ring_timeout_ms' => int, 'call_connect_timeout_ms' => int, 'call_packet_timeout_ms' => int, 'me_url_prefix' => 'string', 'autoupdate_url_prefix' => 'string', 'gif_search_username' => 'string', 'venue_search_username' => 'string', 'img_search_username' => 'string', 'static_maps_provider' => 'string', 'caption_length_max' => int, 'message_length_max' => int, 'webfile_dc_id' => int, 'suggested_lang_code' => 'string', 'lang_pack_version' => int, 'base_lang_pack_version' => int];
```  
