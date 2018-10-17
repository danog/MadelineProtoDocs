---
title: config
description: config attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: config  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|phonecalls\_enabled|[Bool](../types/Bool.md) | Optional|
|default\_p2p\_contacts|[Bool](../types/Bool.md) | Optional|
|preload\_featured\_stickers|[Bool](../types/Bool.md) | Optional|
|ignore\_phone\_entities|[Bool](../types/Bool.md) | Optional|
|revoke\_pm\_inbox|[Bool](../types/Bool.md) | Optional|
|blocked\_mode|[Bool](../types/Bool.md) | Optional|
|date|[int](../types/int.md) | Yes|
|expires|[int](../types/int.md) | Yes|
|test\_mode|[Bool](../types/Bool.md) | Yes|
|this\_dc|[int](../types/int.md) | Yes|
|dc\_options|Array of [DcOption](../types/DcOption.md) | Yes|
|dc\_txt\_domain\_name|[string](../types/string.md) | Yes|
|chat\_size\_max|[int](../types/int.md) | Yes|
|megagroup\_size\_max|[int](../types/int.md) | Yes|
|forwarded\_count\_max|[int](../types/int.md) | Yes|
|online\_update\_period\_ms|[int](../types/int.md) | Yes|
|offline\_blur\_timeout\_ms|[int](../types/int.md) | Yes|
|offline\_idle\_timeout\_ms|[int](../types/int.md) | Yes|
|online\_cloud\_timeout\_ms|[int](../types/int.md) | Yes|
|notify\_cloud\_delay\_ms|[int](../types/int.md) | Yes|
|notify\_default\_delay\_ms|[int](../types/int.md) | Yes|
|push\_chat\_period\_ms|[int](../types/int.md) | Yes|
|push\_chat\_limit|[int](../types/int.md) | Yes|
|saved\_gifs\_limit|[int](../types/int.md) | Yes|
|edit\_time\_limit|[int](../types/int.md) | Yes|
|revoke\_time\_limit|[int](../types/int.md) | Yes|
|revoke\_pm\_time\_limit|[int](../types/int.md) | Yes|
|rating\_e\_decay|[int](../types/int.md) | Yes|
|stickers\_recent\_limit|[int](../types/int.md) | Yes|
|stickers\_faved\_limit|[int](../types/int.md) | Yes|
|channels\_read\_media\_period|[int](../types/int.md) | Yes|
|tmp\_sessions|[int](../types/int.md) | Optional|
|pinned\_dialogs\_count\_max|[int](../types/int.md) | Yes|
|call\_receive\_timeout\_ms|[int](../types/int.md) | Yes|
|call\_ring\_timeout\_ms|[int](../types/int.md) | Yes|
|call\_connect\_timeout\_ms|[int](../types/int.md) | Yes|
|call\_packet\_timeout\_ms|[int](../types/int.md) | Yes|
|me\_url\_prefix|[string](../types/string.md) | Yes|
|autoupdate\_url\_prefix|[string](../types/string.md) | Optional|
|gif\_search\_username|[string](../types/string.md) | Optional|
|venue\_search\_username|[string](../types/string.md) | Optional|
|img\_search\_username|[string](../types/string.md) | Optional|
|static\_maps\_provider|[string](../types/string.md) | Optional|
|caption\_length\_max|[int](../types/int.md) | Yes|
|message\_length\_max|[int](../types/int.md) | Yes|
|webfile\_dc\_id|[int](../types/int.md) | Yes|
|suggested\_lang\_code|[string](../types/string.md) | Optional|
|lang\_pack\_version|[int](../types/int.md) | Optional|



### Type: [Config](../types/Config.md)


### Example:

```php
$config = ['_' => 'config', 'phonecalls_enabled' => Bool, 'default_p2p_contacts' => Bool, 'preload_featured_stickers' => Bool, 'ignore_phone_entities' => Bool, 'revoke_pm_inbox' => Bool, 'blocked_mode' => Bool, 'date' => int, 'expires' => int, 'test_mode' => Bool, 'this_dc' => int, 'dc_options' => [DcOption, DcOption], 'dc_txt_domain_name' => 'string', 'chat_size_max' => int, 'megagroup_size_max' => int, 'forwarded_count_max' => int, 'online_update_period_ms' => int, 'offline_blur_timeout_ms' => int, 'offline_idle_timeout_ms' => int, 'online_cloud_timeout_ms' => int, 'notify_cloud_delay_ms' => int, 'notify_default_delay_ms' => int, 'push_chat_period_ms' => int, 'push_chat_limit' => int, 'saved_gifs_limit' => int, 'edit_time_limit' => int, 'revoke_time_limit' => int, 'revoke_pm_time_limit' => int, 'rating_e_decay' => int, 'stickers_recent_limit' => int, 'stickers_faved_limit' => int, 'channels_read_media_period' => int, 'tmp_sessions' => int, 'pinned_dialogs_count_max' => int, 'call_receive_timeout_ms' => int, 'call_ring_timeout_ms' => int, 'call_connect_timeout_ms' => int, 'call_packet_timeout_ms' => int, 'me_url_prefix' => 'string', 'autoupdate_url_prefix' => 'string', 'gif_search_username' => 'string', 'venue_search_username' => 'string', 'img_search_username' => 'string', 'static_maps_provider' => 'string', 'caption_length_max' => int, 'message_length_max' => int, 'webfile_dc_id' => int, 'suggested_lang_code' => 'string', 'lang_pack_version' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "config", "phonecalls_enabled": Bool, "default_p2p_contacts": Bool, "preload_featured_stickers": Bool, "ignore_phone_entities": Bool, "revoke_pm_inbox": Bool, "blocked_mode": Bool, "date": int, "expires": int, "test_mode": Bool, "this_dc": int, "dc_options": [DcOption], "dc_txt_domain_name": "string", "chat_size_max": int, "megagroup_size_max": int, "forwarded_count_max": int, "online_update_period_ms": int, "offline_blur_timeout_ms": int, "offline_idle_timeout_ms": int, "online_cloud_timeout_ms": int, "notify_cloud_delay_ms": int, "notify_default_delay_ms": int, "push_chat_period_ms": int, "push_chat_limit": int, "saved_gifs_limit": int, "edit_time_limit": int, "revoke_time_limit": int, "revoke_pm_time_limit": int, "rating_e_decay": int, "stickers_recent_limit": int, "stickers_faved_limit": int, "channels_read_media_period": int, "tmp_sessions": int, "pinned_dialogs_count_max": int, "call_receive_timeout_ms": int, "call_ring_timeout_ms": int, "call_connect_timeout_ms": int, "call_packet_timeout_ms": int, "me_url_prefix": "string", "autoupdate_url_prefix": "string", "gif_search_username": "string", "venue_search_username": "string", "img_search_username": "string", "static_maps_provider": "string", "caption_length_max": int, "message_length_max": int, "webfile_dc_id": int, "suggested_lang_code": "string", "lang_pack_version": int}
```


Or, if you're into Lua:

```lua
config={_='config', phonecalls_enabled=Bool, default_p2p_contacts=Bool, preload_featured_stickers=Bool, ignore_phone_entities=Bool, revoke_pm_inbox=Bool, blocked_mode=Bool, date=int, expires=int, test_mode=Bool, this_dc=int, dc_options={DcOption}, dc_txt_domain_name='string', chat_size_max=int, megagroup_size_max=int, forwarded_count_max=int, online_update_period_ms=int, offline_blur_timeout_ms=int, offline_idle_timeout_ms=int, online_cloud_timeout_ms=int, notify_cloud_delay_ms=int, notify_default_delay_ms=int, push_chat_period_ms=int, push_chat_limit=int, saved_gifs_limit=int, edit_time_limit=int, revoke_time_limit=int, revoke_pm_time_limit=int, rating_e_decay=int, stickers_recent_limit=int, stickers_faved_limit=int, channels_read_media_period=int, tmp_sessions=int, pinned_dialogs_count_max=int, call_receive_timeout_ms=int, call_ring_timeout_ms=int, call_connect_timeout_ms=int, call_packet_timeout_ms=int, me_url_prefix='string', autoupdate_url_prefix='string', gif_search_username='string', venue_search_username='string', img_search_username='string', static_maps_provider='string', caption_length_max=int, message_length_max=int, webfile_dc_id=int, suggested_lang_code='string', lang_pack_version=int}

```


