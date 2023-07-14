---
title: "danog\\MadelineProto\\Conversion: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Conversion`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Constants
* `danog\MadelineProto\Conversion::FILEOPTION_SAFE`: 

* `danog\MadelineProto\Conversion::FILEOPTION_USER`: 

* `danog\MadelineProto\Conversion::dbiKey`: 

* `danog\MadelineProto\Conversion::dbiUser`: 

* `danog\MadelineProto\Conversion::dbiDcOptionOldOld`: 

* `danog\MadelineProto\Conversion::dbiChatSizeMax`: 

* `danog\MadelineProto\Conversion::dbiMutePeer`: 

* `danog\MadelineProto\Conversion::dbiSendKey`: 

* `danog\MadelineProto\Conversion::dbiAutoStart`: 

* `danog\MadelineProto\Conversion::dbiStartMinimized`: 

* `danog\MadelineProto\Conversion::dbiSoundNotify`: 

* `danog\MadelineProto\Conversion::dbiWorkMode`: 

* `danog\MadelineProto\Conversion::dbiSeenTrayTooltip`: 

* `danog\MadelineProto\Conversion::dbiDesktopNotify`: 

* `danog\MadelineProto\Conversion::dbiAutoUpdate`: 

* `danog\MadelineProto\Conversion::dbiLastUpdateCheck`: 

* `danog\MadelineProto\Conversion::dbiWindowPosition`: 

* `danog\MadelineProto\Conversion::dbiConnectionTypeOld`: 

* `danog\MadelineProto\Conversion::dbiDefaultAttach`: 

* `danog\MadelineProto\Conversion::dbiCatsAndDogs`: 

* `danog\MadelineProto\Conversion::dbiReplaceEmojis`: 

* `danog\MadelineProto\Conversion::dbiAskDownloadPath`: 

* `danog\MadelineProto\Conversion::dbiDownloadPathOld`: 

* `danog\MadelineProto\Conversion::dbiScale`: 

* `danog\MadelineProto\Conversion::dbiEmojiTabOld`: 

* `danog\MadelineProto\Conversion::dbiRecentEmojiOldOld`: 

* `danog\MadelineProto\Conversion::dbiLoggedPhoneNumber`: 

* `danog\MadelineProto\Conversion::dbiMutedPeers`: 

* `danog\MadelineProto\Conversion::dbiNotifyView`: 

* `danog\MadelineProto\Conversion::dbiSendToMenu`: 

* `danog\MadelineProto\Conversion::dbiCompressPastedImage`: 

* `danog\MadelineProto\Conversion::dbiLangOld`: 

* `danog\MadelineProto\Conversion::dbiLangFileOld`: 

* `danog\MadelineProto\Conversion::dbiTileBackground`: 

* `danog\MadelineProto\Conversion::dbiAutoLock`: 

* `danog\MadelineProto\Conversion::dbiDialogLastPath`: 

* `danog\MadelineProto\Conversion::dbiRecentEmojiOld`: 

* `danog\MadelineProto\Conversion::dbiEmojiVariantsOld`: 

* `danog\MadelineProto\Conversion::dbiRecentStickers`: 

* `danog\MadelineProto\Conversion::dbiDcOptionOld`: 

* `danog\MadelineProto\Conversion::dbiTryIPv6`: 

* `danog\MadelineProto\Conversion::dbiSongVolume`: 

* `danog\MadelineProto\Conversion::dbiWindowsNotificationsOld`: 

* `danog\MadelineProto\Conversion::dbiIncludeMuted`: 

* `danog\MadelineProto\Conversion::dbiMegagroupSizeMax`: 

* `danog\MadelineProto\Conversion::dbiDownloadPath`: 

* `danog\MadelineProto\Conversion::dbiAutoDownload`: 

* `danog\MadelineProto\Conversion::dbiSavedGifsLimit`: 

* `danog\MadelineProto\Conversion::dbiShowingSavedGifsOld`: 

* `danog\MadelineProto\Conversion::dbiAutoPlay`: 

* `danog\MadelineProto\Conversion::dbiAdaptiveForWide`: 

* `danog\MadelineProto\Conversion::dbiHiddenPinnedMessages`: 

* `danog\MadelineProto\Conversion::dbiRecentEmoji`: 

* `danog\MadelineProto\Conversion::dbiEmojiVariants`: 

* `danog\MadelineProto\Conversion::dbiDialogsMode`: 

* `danog\MadelineProto\Conversion::dbiModerateMode`: 

* `danog\MadelineProto\Conversion::dbiVideoVolume`: 

* `danog\MadelineProto\Conversion::dbiStickersRecentLimit`: 

* `danog\MadelineProto\Conversion::dbiNativeNotifications`: 

* `danog\MadelineProto\Conversion::dbiNotificationsCount`: 

* `danog\MadelineProto\Conversion::dbiNotificationsCorner`: 

* `danog\MadelineProto\Conversion::dbiThemeKey`: 

* `danog\MadelineProto\Conversion::dbiDialogsWidthRatioOld`: 

* `danog\MadelineProto\Conversion::dbiUseExternalVideoPlayer`: 

* `danog\MadelineProto\Conversion::dbiDcOptions`: 

* `danog\MadelineProto\Conversion::dbiMtpAuthorization`: 

* `danog\MadelineProto\Conversion::dbiLastSeenWarningSeenOld`: 

* `danog\MadelineProto\Conversion::dbiAuthSessionSettings`: 

* `danog\MadelineProto\Conversion::dbiLangPackKey`: 

* `danog\MadelineProto\Conversion::dbiConnectionType`: 

* `danog\MadelineProto\Conversion::dbiStickersFavedLimit`: 

* `danog\MadelineProto\Conversion::dbiSuggestStickersByEmoji`: 

* `danog\MadelineProto\Conversion::dbiEncryptedWithSalt`: 

* `danog\MadelineProto\Conversion::dbiEncrypted`: 

* `danog\MadelineProto\Conversion::dbiVersion`: 

## Properties
* `$tdesktop_base_path`: `mixed` 
* `$tdesktop_user_base_path`: `mixed` 
* `$tdesktop_key`: `mixed` 

## Method list:
* [`importAuthorization(array<int, string> $authorization, int $main_dc_id, string $session, \danog\MadelineProto\SettingsAbstract|array $settings): \danog\MadelineProto\API`](#importauthorization-array-int-string-authorization-int-main_dc_id-string-session-danog-madelineproto-settingsabstract-array-settings-danog-madelineproto-api)
* [`telethon(string $session, string $new_session, mixed $settings = []): mixed`](#telethon-string-session-string-new_session-mixed-settings-mixed)
* [`pyrogram(string $session, string $new_session, mixed $settings = []): mixed`](#pyrogram-string-session-string-new_session-mixed-settings-mixed)
* [`zerobias(mixed $session, mixed $new_session, mixed $settings = []): mixed`](#zerobias-mixed-session-mixed-new_session-mixed-settings-mixed)
* [`tdesktop_md5(mixed $data): mixed`](#tdesktop_md5-mixed-data-mixed)
* [`tdesktop_fopen(mixed $fileName, mixed $options = 3): mixed`](#tdesktop_fopen-mixed-filename-mixed-options-3-mixed)
* [`tdesktop_fopen_encrypted(mixed $fileName, mixed $options = 3): mixed`](#tdesktop_fopen_encrypted-mixed-filename-mixed-options-3-mixed)
* [`tdesktop_read_bytearray(mixed $fp, bool $asString = false): mixed`](#tdesktop_read_bytearray-mixed-fp-bool-asstring-false-mixed)
* [`tdesktop_decrypt(mixed $data, mixed $auth_key): mixed`](#tdesktop_decrypt-mixed-data-mixed-auth_key-mixed)
* [`tdesktop(string $session, string $new_session, mixed $settings = []): mixed`](#tdesktop-string-session-string-new_session-mixed-settings-mixed)

## Methods:
### `importAuthorization(array<int, string> $authorization, int $main_dc_id, string $session, \danog\MadelineProto\SettingsAbstract|array $settings): \danog\MadelineProto\API`

Prepare API instance.


Parameters:

* `$authorization`: `array<int, string>` Authorization info  
* `$main_dc_id`: `int`   
* `$session`: `string`   
* `$settings`: `\danog\MadelineProto\SettingsAbstract|array`   


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`
* [`\danog\MadelineProto\API`: Main API wrapper for MadelineProto.](../../danog/MadelineProto/API.html)




### `telethon(string $session, string $new_session, mixed $settings = []): mixed`




Parameters:

* `$session`: `string`   
* `$new_session`: `string`   
* `$settings`: `mixed`   



### `pyrogram(string $session, string $new_session, mixed $settings = []): mixed`




Parameters:

* `$session`: `string`   
* `$new_session`: `string`   
* `$settings`: `mixed`   



### `zerobias(mixed $session, mixed $new_session, mixed $settings = []): mixed`




Parameters:

* `$session`: `mixed`   
* `$new_session`: `mixed`   
* `$settings`: `mixed`   



### `tdesktop_md5(mixed $data): mixed`




Parameters:

* `$data`: `mixed`   



### `tdesktop_fopen(mixed $fileName, mixed $options = 3): mixed`




Parameters:

* `$fileName`: `mixed`   
* `$options`: `mixed`   



### `tdesktop_fopen_encrypted(mixed $fileName, mixed $options = 3): mixed`




Parameters:

* `$fileName`: `mixed`   
* `$options`: `mixed`   



### `tdesktop_read_bytearray(mixed $fp, bool $asString = false): mixed`




Parameters:

* `$fp`: `mixed`   
* `$asString`: `bool`   



### `tdesktop_decrypt(mixed $data, mixed $auth_key): mixed`




Parameters:

* `$data`: `mixed`   
* `$auth_key`: `mixed`   



### `tdesktop(string $session, string $new_session, mixed $settings = []): mixed`




Parameters:

* `$session`: `string`   
* `$new_session`: `string`   
* `$settings`: `mixed`   



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
