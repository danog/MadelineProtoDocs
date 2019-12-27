---
title: config
description: Current configuration
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: config  
[Back to constructors index](index.md)



Current configuration

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phonecalls\_enabled|[Bool](../types/Bool.md) | Optional|Whether phone calls can be used|
|date|[int](../types/int.md) | Yes|Current date at the server|
|expires|[int](../types/int.md) | Yes|Expiration date of this config: when it expires it'll have to be refetched using [help.getConfig](../methods/help.getConfig.md)|
|test\_mode|[Bool](../types/Bool.md) | Yes|Whether we're connected to the test DCs|
|this\_dc|[int](../types/int.md) | Yes|ID of the DC that returned the reply|
|dc\_options|Array of [DcOption](../types/DcOption.md) | Yes|DC options|
|chat\_size\_max|[int](../types/int.md) | Yes|Maximum member count for normal [groups](https://core.telegram.org/api/channel)|
|megagroup\_size\_max|[int](../types/int.md) | Yes|Maximum member count for [supergroups](https://core.telegram.org/api/channel)|
|forwarded\_count\_max|[int](../types/int.md) | Yes|Maximum number of messages that can be forwarded at once using [messages.forwardMessages](../methods/messages.forwardMessages.md).|
|online\_update\_period\_ms|[int](../types/int.md) | Yes|The client should [update its online status](../methods/account.updateStatus.md) every N milliseconds|
|offline\_blur\_timeout\_ms|[int](../types/int.md) | Yes|Delay before offline status needs to be sent to the server|
|offline\_idle\_timeout\_ms|[int](../types/int.md) | Yes|Time without any user activity after which it should be treated offline|
|online\_cloud\_timeout\_ms|[int](../types/int.md) | Yes|If we are offline, but were online from some other client in last `online_cloud_timeout_ms` milliseconds after we had gone offline, then delay offline notification for `notify_cloud_delay_ms` milliseconds.|
|notify\_cloud\_delay\_ms|[int](../types/int.md) | Yes|If we are offline, but online from some other client then delay sending the offline notification for `notify_cloud_delay_ms` milliseconds.|
|notify\_default\_delay\_ms|[int](../types/int.md) | Yes|If some other client is online, then delay notification for `notification_default_delay_ms` milliseconds|
|chat\_big\_size|[int](../types/int.md) | Yes|Chat big size|
|push\_chat\_period\_ms|[int](../types/int.md) | Yes|Not for client use|
|push\_chat\_limit|[int](../types/int.md) | Yes|Not for client use|
|saved\_gifs\_limit|[int](../types/int.md) | Yes|Maximum count of saved gifs|
|edit\_time\_limit|[int](../types/int.md) | Yes|Only messages with age smaller than the one specified can be edited|
|rating\_e\_decay|[int](../types/int.md) | Yes|Exponential decay rate for computing [top peer rating](https://core.telegram.org/api/top-rating)|
|stickers\_recent\_limit|[int](../types/int.md) | Yes|Maximum number of recent stickers|
|tmp\_sessions|[int](../types/int.md) | Optional|Temporary [passport](https://core.telegram.org/passport) sessions|
|pinned\_dialogs\_count\_max|[int](../types/int.md) | Yes|Maximum count of pinned dialogs|
|call\_receive\_timeout\_ms|[int](../types/int.md) | Yes|Maximum allowed outgoing ring time in VoIP calls: if the user we're calling doesn't reply within the specified time (in milliseconds), we should hang up the call|
|call\_ring\_timeout\_ms|[int](../types/int.md) | Yes|Maximum allowed incoming ring time in VoIP calls: if the current user doesn't reply within the specified time (in milliseconds), the call will be automatically refused|
|call\_connect\_timeout\_ms|[int](../types/int.md) | Yes|VoIP connection timeout: if the instance of libtgvoip on the other side of the call doesn't connect to our instance of libtgvoip within the specified time (in milliseconds), the call must be aborted|
|call\_packet\_timeout\_ms|[int](../types/int.md) | Yes|If during a VoIP call a packet isn't received for the specified period of time, the call must be aborted|
|me\_url\_prefix|[string](../types/string.md) | Yes|The domain to use to parse in-app links.<br>For example t.me indicates that t.me/username links should parsed to @username, t.me/addsticker/name should be parsed to the appropriate stickerset and so on...|
|suggested\_lang\_code|[string](../types/string.md) | Optional|Suggested language code|
|lang\_pack\_version|[int](../types/int.md) | Optional|Language pack version|
|disabled\_features|Array of [DisabledFeature](../types/DisabledFeature.md) | Yes|Disabled features|



### Type: [Config](../types/Config.md)


### Example:

```php
$config = ['_' => 'config', 'phonecalls_enabled' => Bool, 'date' => int, 'expires' => int, 'test_mode' => Bool, 'this_dc' => int, 'dc_options' => [DcOption, DcOption], 'chat_size_max' => int, 'megagroup_size_max' => int, 'forwarded_count_max' => int, 'online_update_period_ms' => int, 'offline_blur_timeout_ms' => int, 'offline_idle_timeout_ms' => int, 'online_cloud_timeout_ms' => int, 'notify_cloud_delay_ms' => int, 'notify_default_delay_ms' => int, 'chat_big_size' => int, 'push_chat_period_ms' => int, 'push_chat_limit' => int, 'saved_gifs_limit' => int, 'edit_time_limit' => int, 'rating_e_decay' => int, 'stickers_recent_limit' => int, 'tmp_sessions' => int, 'pinned_dialogs_count_max' => int, 'call_receive_timeout_ms' => int, 'call_ring_timeout_ms' => int, 'call_connect_timeout_ms' => int, 'call_packet_timeout_ms' => int, 'me_url_prefix' => 'string', 'suggested_lang_code' => 'string', 'lang_pack_version' => int, 'disabled_features' => [DisabledFeature, DisabledFeature]];
```  


Or, if you're into Lua:

```lua
config={_='config', phonecalls_enabled=Bool, date=int, expires=int, test_mode=Bool, this_dc=int, dc_options={DcOption}, chat_size_max=int, megagroup_size_max=int, forwarded_count_max=int, online_update_period_ms=int, offline_blur_timeout_ms=int, offline_idle_timeout_ms=int, online_cloud_timeout_ms=int, notify_cloud_delay_ms=int, notify_default_delay_ms=int, chat_big_size=int, push_chat_period_ms=int, push_chat_limit=int, saved_gifs_limit=int, edit_time_limit=int, rating_e_decay=int, stickers_recent_limit=int, tmp_sessions=int, pinned_dialogs_count_max=int, call_receive_timeout_ms=int, call_ring_timeout_ms=int, call_connect_timeout_ms=int, call_packet_timeout_ms=int, me_url_prefix='string', suggested_lang_code='string', lang_pack_version=int, disabled_features={DisabledFeature}}

```


