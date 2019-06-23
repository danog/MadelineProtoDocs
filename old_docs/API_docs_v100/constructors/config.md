---
title: config
description: Config
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: config  
[Back to constructors index](index.md)



Config

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phonecalls\_enabled|[Bool](../types/Bool.md) | Optional|Phonecalls enabled?|
|default\_p2p\_contacts|[Bool](../types/Bool.md) | Optional|Default p2p contacts?|
|preload\_featured\_stickers|[Bool](../types/Bool.md) | Optional|Preload featured stickers?|
|ignore\_phone\_entities|[Bool](../types/Bool.md) | Optional|Ignore phone entities?|
|revoke\_pm\_inbox|[Bool](../types/Bool.md) | Optional|Revoke pm inbox?|
|blocked\_mode|[Bool](../types/Bool.md) | Optional|Blocked mode?|
|pfs\_enabled|[Bool](../types/Bool.md) | Optional|Pfs enabled?|
|date|[int](../types/int.md) | Yes|Date|
|expires|[int](../types/int.md) | Yes|Expires|
|test\_mode|[Bool](../types/Bool.md) | Yes|Test mode?|
|this\_dc|[int](../types/int.md) | Yes|This DC|
|dc\_options|Array of [DcOption](../types/DcOption.md) | Yes|DC options|
|dc\_txt\_domain\_name|[string](../types/string.md) | Yes|DC txt domain name|
|chat\_size\_max|[int](../types/int.md) | Yes|Chat size max|
|megagroup\_size\_max|[int](../types/int.md) | Yes|Megagroup size max|
|forwarded\_count\_max|[int](../types/int.md) | Yes|Forwarded count max|
|online\_update\_period\_ms|[int](../types/int.md) | Yes|Online update period ms|
|offline\_blur\_timeout\_ms|[int](../types/int.md) | Yes|Offline blur timeout ms|
|offline\_idle\_timeout\_ms|[int](../types/int.md) | Yes|Offline IDle timeout ms|
|online\_cloud\_timeout\_ms|[int](../types/int.md) | Yes|Online cloud timeout ms|
|notify\_cloud\_delay\_ms|[int](../types/int.md) | Yes|Notify cloud delay ms|
|notify\_default\_delay\_ms|[int](../types/int.md) | Yes|Notify default delay ms|
|push\_chat\_period\_ms|[int](../types/int.md) | Yes|Push chat period ms|
|push\_chat\_limit|[int](../types/int.md) | Yes|Push chat limit|
|saved\_gifs\_limit|[int](../types/int.md) | Yes|Saved gifs limit|
|edit\_time\_limit|[int](../types/int.md) | Yes|Edit time limit|
|revoke\_time\_limit|[int](../types/int.md) | Yes|Revoke time limit|
|revoke\_pm\_time\_limit|[int](../types/int.md) | Yes|Revoke pm time limit|
|rating\_e\_decay|[int](../types/int.md) | Yes|Rating e decay|
|stickers\_recent\_limit|[int](../types/int.md) | Yes|Stickers recent limit|
|stickers\_faved\_limit|[int](../types/int.md) | Yes|Stickers faved limit|
|channels\_read\_media\_period|[int](../types/int.md) | Yes|Channels read media period|
|tmp\_sessions|[int](../types/int.md) | Optional|Tmp sessions|
|pinned\_dialogs\_count\_max|[int](../types/int.md) | Yes|Pinned dialogs count max|
|pinned\_infolder\_count\_max|[int](../types/int.md) | Yes|Pinned infolder count max_type|
|call\_receive\_timeout\_ms|[int](../types/int.md) | Yes|Call receive timeout ms|
|call\_ring\_timeout\_ms|[int](../types/int.md) | Yes|Call ring timeout ms|
|call\_connect\_timeout\_ms|[int](../types/int.md) | Yes|Call connect timeout ms|
|call\_packet\_timeout\_ms|[int](../types/int.md) | Yes|Call packet timeout ms|
|me\_url\_prefix|[string](../types/string.md) | Yes|Me URL prefix|
|autoupdate\_url\_prefix|[string](../types/string.md) | Optional|Autoupdate URL prefix|
|gif\_search\_username|[string](../types/string.md) | Optional|Gif search username|
|venue\_search\_username|[string](../types/string.md) | Optional|Venue search username|
|img\_search\_username|[string](../types/string.md) | Optional|Img search username|
|static\_maps\_provider|[string](../types/string.md) | Optional|Static maps provider|
|caption\_length\_max|[int](../types/int.md) | Yes|Caption length max|
|message\_length\_max|[int](../types/int.md) | Yes|Message length max|
|webfile\_dc\_id|[int](../types/int.md) | Yes|Webfile DC ID|
|suggested\_lang\_code|[string](../types/string.md) | Optional|Suggested lang code|
|lang\_pack\_version|[int](../types/int.md) | Optional|Lang pack version|
|base\_lang\_pack\_version|[int](../types/int.md) | Optional|Base lang pack version|



### Type: [Config](../types/Config.md)


### Example:

```php
$config = ['_' => 'config', 'phonecalls_enabled' => Bool, 'default_p2p_contacts' => Bool, 'preload_featured_stickers' => Bool, 'ignore_phone_entities' => Bool, 'revoke_pm_inbox' => Bool, 'blocked_mode' => Bool, 'pfs_enabled' => Bool, 'date' => int, 'expires' => int, 'test_mode' => Bool, 'this_dc' => int, 'dc_options' => [DcOption, DcOption], 'dc_txt_domain_name' => 'string', 'chat_size_max' => int, 'megagroup_size_max' => int, 'forwarded_count_max' => int, 'online_update_period_ms' => int, 'offline_blur_timeout_ms' => int, 'offline_idle_timeout_ms' => int, 'online_cloud_timeout_ms' => int, 'notify_cloud_delay_ms' => int, 'notify_default_delay_ms' => int, 'push_chat_period_ms' => int, 'push_chat_limit' => int, 'saved_gifs_limit' => int, 'edit_time_limit' => int, 'revoke_time_limit' => int, 'revoke_pm_time_limit' => int, 'rating_e_decay' => int, 'stickers_recent_limit' => int, 'stickers_faved_limit' => int, 'channels_read_media_period' => int, 'tmp_sessions' => int, 'pinned_dialogs_count_max' => int, 'pinned_infolder_count_max' => int, 'call_receive_timeout_ms' => int, 'call_ring_timeout_ms' => int, 'call_connect_timeout_ms' => int, 'call_packet_timeout_ms' => int, 'me_url_prefix' => 'string', 'autoupdate_url_prefix' => 'string', 'gif_search_username' => 'string', 'venue_search_username' => 'string', 'img_search_username' => 'string', 'static_maps_provider' => 'string', 'caption_length_max' => int, 'message_length_max' => int, 'webfile_dc_id' => int, 'suggested_lang_code' => 'string', 'lang_pack_version' => int, 'base_lang_pack_version' => int];
```  


Or, if you're into Lua:

```lua
config={_='config', phonecalls_enabled=Bool, default_p2p_contacts=Bool, preload_featured_stickers=Bool, ignore_phone_entities=Bool, revoke_pm_inbox=Bool, blocked_mode=Bool, pfs_enabled=Bool, date=int, expires=int, test_mode=Bool, this_dc=int, dc_options={DcOption}, dc_txt_domain_name='string', chat_size_max=int, megagroup_size_max=int, forwarded_count_max=int, online_update_period_ms=int, offline_blur_timeout_ms=int, offline_idle_timeout_ms=int, online_cloud_timeout_ms=int, notify_cloud_delay_ms=int, notify_default_delay_ms=int, push_chat_period_ms=int, push_chat_limit=int, saved_gifs_limit=int, edit_time_limit=int, revoke_time_limit=int, revoke_pm_time_limit=int, rating_e_decay=int, stickers_recent_limit=int, stickers_faved_limit=int, channels_read_media_period=int, tmp_sessions=int, pinned_dialogs_count_max=int, pinned_infolder_count_max=int, call_receive_timeout_ms=int, call_ring_timeout_ms=int, call_connect_timeout_ms=int, call_packet_timeout_ms=int, me_url_prefix='string', autoupdate_url_prefix='string', gif_search_username='string', venue_search_username='string', img_search_username='string', static_maps_provider='string', caption_length_max=int, message_length_max=int, webfile_dc_id=int, suggested_lang_code='string', lang_pack_version=int, base_lang_pack_version=int}

```


