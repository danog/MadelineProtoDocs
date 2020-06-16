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
|date|[int](../types/int.md) | Yes|Current date at the server|
|expires|[int](../types/int.md) | Yes|Expiration date of this config: when it expires it'll have to be refetched using [help.getConfig](../methods/help.getConfig.md)|
|test\_mode|[Bool](../types/Bool.md) | Yes|Whether we're connected to the test DCs|
|this\_dc|[int](../types/int.md) | Yes|ID of the DC that returned the reply|
|dc\_options|Array of [DcOption](../types/DcOption.md) | Yes|DC IP list|
|chat\_size\_max|[int](../types/int.md) | Yes|Maximum member count for normal [groups](https://core.telegram.org/api/channel)|
|megagroup\_size\_max|[int](../types/int.md) | Yes|Maximum member count for [supergroups](https://core.telegram.org/api/channel)|
|forwarded\_count\_max|[int](../types/int.md) | Yes|Maximum number of messages that can be forwarded at once using [messages.forwardMessages](../methods/messages.forwardMessages.md).|
|online\_update\_period\_ms|[int](../types/int.md) | Yes|The client should [update its online status](../methods/account.updateStatus.md) every N milliseconds|
|offline\_blur\_timeout\_ms|[int](../types/int.md) | Yes|Delay before offline status needs to be sent to the server|
|offline\_idle\_timeout\_ms|[int](../types/int.md) | Yes|Time without any user activity after which it should be treated offline|
|online\_cloud\_timeout\_ms|[int](../types/int.md) | Yes|If we are offline, but were online from some other client in last `online_cloud_timeout_ms` milliseconds after we had gone offline, then delay offline notification for `notify_cloud_delay_ms` milliseconds.|
|notify\_cloud\_delay\_ms|[int](../types/int.md) | Yes|If we are offline, but online from some other client then delay sending the offline notification for `notify_cloud_delay_ms` milliseconds.|
|notify\_default\_delay\_ms|[int](../types/int.md) | Yes|If some other client is online, then delay notification for `notification_default_delay_ms` milliseconds|
|chat\_big\_size|[int](../types/int.md) | Yes|
|push\_chat\_period\_ms|[int](../types/int.md) | Yes|Not for client use|
|push\_chat\_limit|[int](../types/int.md) | Yes|Not for client use|
|saved\_gifs\_limit|[int](../types/int.md) | Yes|Maximum count of saved gifs|
|disabled\_features|Array of [DisabledFeature](../types/DisabledFeature.md) | Yes|



### Type: [Config](../types/Config.md)


### Example:

```php
$config = ['_' => 'config', 'date' => int, 'expires' => int, 'test_mode' => Bool, 'this_dc' => int, 'dc_options' => [DcOption, DcOption], 'chat_size_max' => int, 'megagroup_size_max' => int, 'forwarded_count_max' => int, 'online_update_period_ms' => int, 'offline_blur_timeout_ms' => int, 'offline_idle_timeout_ms' => int, 'online_cloud_timeout_ms' => int, 'notify_cloud_delay_ms' => int, 'notify_default_delay_ms' => int, 'chat_big_size' => int, 'push_chat_period_ms' => int, 'push_chat_limit' => int, 'saved_gifs_limit' => int, 'disabled_features' => [DisabledFeature, DisabledFeature]];
```  


Or, if you're into Lua:

```lua
config={_='config', date=int, expires=int, test_mode=Bool, this_dc=int, dc_options={DcOption}, chat_size_max=int, megagroup_size_max=int, forwarded_count_max=int, online_update_period_ms=int, offline_blur_timeout_ms=int, offline_idle_timeout_ms=int, online_cloud_timeout_ms=int, notify_cloud_delay_ms=int, notify_default_delay_ms=int, chat_big_size=int, push_chat_period_ms=int, push_chat_limit=int, saved_gifs_limit=int, disabled_features={DisabledFeature}}

```


