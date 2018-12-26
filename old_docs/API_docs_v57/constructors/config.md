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
|date|[int](../types/int.md) | Yes|Date|
|expires|[int](../types/int.md) | Yes|Expires|
|test\_mode|[Bool](../types/Bool.md) | Yes|Test mode?|
|this\_dc|[int](../types/int.md) | Yes|This DC|
|dc\_options|Array of [DcOption](../types/DcOption.md) | Yes|DC options|
|chat\_size\_max|[int](../types/int.md) | Yes|Chat size max|
|megagroup\_size\_max|[int](../types/int.md) | Yes|Megagroup size max|
|forwarded\_count\_max|[int](../types/int.md) | Yes|Forwarded count max|
|online\_update\_period\_ms|[int](../types/int.md) | Yes|Online update period ms|
|offline\_blur\_timeout\_ms|[int](../types/int.md) | Yes|Offline blur timeout ms|
|offline\_idle\_timeout\_ms|[int](../types/int.md) | Yes|Offline IDle timeout ms|
|online\_cloud\_timeout\_ms|[int](../types/int.md) | Yes|Online cloud timeout ms|
|notify\_cloud\_delay\_ms|[int](../types/int.md) | Yes|Notify cloud delay ms|
|notify\_default\_delay\_ms|[int](../types/int.md) | Yes|Notify default delay ms|
|chat\_big\_size|[int](../types/int.md) | Yes|Chat big size|
|push\_chat\_period\_ms|[int](../types/int.md) | Yes|Push chat period ms|
|push\_chat\_limit|[int](../types/int.md) | Yes|Push chat limit|
|saved\_gifs\_limit|[int](../types/int.md) | Yes|Saved gifs limit|
|edit\_time\_limit|[int](../types/int.md) | Yes|Edit time limit|
|rating\_e\_decay|[int](../types/int.md) | Yes|Rating e decay|
|stickers\_recent\_limit|[int](../types/int.md) | Yes|Stickers recent limit|
|tmp\_sessions|[int](../types/int.md) | Optional|Tmp sessions|
|disabled\_features|Array of [DisabledFeature](../types/DisabledFeature.md) | Yes|Disabled features|



### Type: [Config](../types/Config.md)


### Example:

```php
$config = ['_' => 'config', 'date' => int, 'expires' => int, 'test_mode' => Bool, 'this_dc' => int, 'dc_options' => [DcOption, DcOption], 'chat_size_max' => int, 'megagroup_size_max' => int, 'forwarded_count_max' => int, 'online_update_period_ms' => int, 'offline_blur_timeout_ms' => int, 'offline_idle_timeout_ms' => int, 'online_cloud_timeout_ms' => int, 'notify_cloud_delay_ms' => int, 'notify_default_delay_ms' => int, 'chat_big_size' => int, 'push_chat_period_ms' => int, 'push_chat_limit' => int, 'saved_gifs_limit' => int, 'edit_time_limit' => int, 'rating_e_decay' => int, 'stickers_recent_limit' => int, 'tmp_sessions' => int, 'disabled_features' => [DisabledFeature, DisabledFeature]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "config", "date": int, "expires": int, "test_mode": Bool, "this_dc": int, "dc_options": [DcOption], "chat_size_max": int, "megagroup_size_max": int, "forwarded_count_max": int, "online_update_period_ms": int, "offline_blur_timeout_ms": int, "offline_idle_timeout_ms": int, "online_cloud_timeout_ms": int, "notify_cloud_delay_ms": int, "notify_default_delay_ms": int, "chat_big_size": int, "push_chat_period_ms": int, "push_chat_limit": int, "saved_gifs_limit": int, "edit_time_limit": int, "rating_e_decay": int, "stickers_recent_limit": int, "tmp_sessions": int, "disabled_features": [DisabledFeature]}
```


Or, if you're into Lua:

```lua
config={_='config', date=int, expires=int, test_mode=Bool, this_dc=int, dc_options={DcOption}, chat_size_max=int, megagroup_size_max=int, forwarded_count_max=int, online_update_period_ms=int, offline_blur_timeout_ms=int, offline_idle_timeout_ms=int, online_cloud_timeout_ms=int, notify_cloud_delay_ms=int, notify_default_delay_ms=int, chat_big_size=int, push_chat_period_ms=int, push_chat_limit=int, saved_gifs_limit=int, edit_time_limit=int, rating_e_decay=int, stickers_recent_limit=int, tmp_sessions=int, disabled_features={DisabledFeature}}

```


