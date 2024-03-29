---
title: "danog\\MadelineProto\\Conversion: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Conversion`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  



## Properties
* `$tdesktop_base_path`: `mixed` 
* `$tdesktop_user_base_path`: `mixed` 
* `$tdesktop_key`: `mixed` 

## Method list:
* [`importAuthorization(array<int, string> $authorization, int $main_dc_id, string $session, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): \danog\MadelineProto\API`](#importauthorization-array-int-string-authorization-int-main_dc_id-string-session-danog-madelineproto-settingsabstract-settings-null-danog-madelineproto-api)
* [`telethon(string $session, string $new_session, \danog\MadelineProto\SettingsAbstract|null $settings = NULL): \danog\MadelineProto\API`](#telethon-string-session-string-new_session-danog-madelineproto-settingsabstract-null-settings-null-danog-madelineproto-api)
* [`pyrogram(string $session, string $new_session, \danog\MadelineProto\SettingsAbstract|null $settings = NULL): \danog\MadelineProto\API`](#pyrogram-string-session-string-new_session-danog-madelineproto-settingsabstract-null-settings-null-danog-madelineproto-api)
* [`zerobias(array|string $session, string $new_session, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): \danog\MadelineProto\API`](#zerobias-array-string-session-string-new_session-danog-madelineproto-settingsabstract-settings-null-danog-madelineproto-api)

## Methods:
### `importAuthorization(array<int, string> $authorization, int $main_dc_id, string $session, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): \danog\MadelineProto\API`

Prepare API instance.


Parameters:

* `$authorization`: `array<int, string>` Authorization info  
* `$main_dc_id`: `int`   
* `$session`: `string`   
* `$settings`: `?\danog\MadelineProto\SettingsAbstract`   


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`
* [`\danog\MadelineProto\API`: Main API wrapper for MadelineProto.](../../danog/MadelineProto/API.html)




### `telethon(string $session, string $new_session, \danog\MadelineProto\SettingsAbstract|null $settings = NULL): \danog\MadelineProto\API`

Convert telethon session.


Parameters:

* `$session`: `string` Telethon session file  
* `$new_session`: `string` MadelineProto session directory to create  
* `$settings`: `\danog\MadelineProto\SettingsAbstract|null` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`
* [`\danog\MadelineProto\API`: Main API wrapper for MadelineProto.](../../danog/MadelineProto/API.html)




### `pyrogram(string $session, string $new_session, \danog\MadelineProto\SettingsAbstract|null $settings = NULL): \danog\MadelineProto\API`

Convert pyrogram session.


Parameters:

* `$session`: `string` Pyrogram session file  
* `$new_session`: `string` MadelineProto session directory to create  
* `$settings`: `\danog\MadelineProto\SettingsAbstract|null` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`
* [`\danog\MadelineProto\API`: Main API wrapper for MadelineProto.](../../danog/MadelineProto/API.html)




### `zerobias(array|string $session, string $new_session, ?\danog\MadelineProto\SettingsAbstract $settings = NULL): \danog\MadelineProto\API`




Parameters:

* `$session`: `array|string`   
* `$new_session`: `string`   
* `$settings`: `?\danog\MadelineProto\SettingsAbstract`   


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`
* [`\danog\MadelineProto\API`: Main API wrapper for MadelineProto.](../../danog/MadelineProto/API.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
