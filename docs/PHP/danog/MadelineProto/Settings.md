---
title: danog\MadelineProto\Settings: Settings class used for configuring MadelineProto.
description: 

---
# `danog\MadelineProto\Settings`
[Back to index](../../index.md)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Settings class used for configuring MadelineProto.  




## Method list:
* `merge(\danog\MadelineProto\SettingsAbstract $settings): void`
* `getDefaultDc(): int`
* `getDefaultDcParams(): array`
* `setDefaultDc(int $dc): self`
* `getAppInfo(): \danog\MadelineProto\Settings\AppInfo`
* `setAppInfo(\danog\MadelineProto\Settings\AppInfo $appInfo): self`
* `getAuth(): \danog\MadelineProto\Settings\Auth`
* `setAuth(\danog\MadelineProto\Settings\Auth $auth): self`
* `getConnection(): \danog\MadelineProto\Settings\Connection`
* `setConnection(\danog\MadelineProto\Settings\Connection $connection): self`
* `getFiles(): \danog\MadelineProto\Settings\Files`
* `setFiles(\danog\MadelineProto\Settings\Files $files): self`
* `getLogger(): \danog\MadelineProto\Settings\Logger`
* `setLogger(\danog\MadelineProto\Settings\Logger $logger): self`
* `getPeer(): \danog\MadelineProto\Settings\Peer`
* `setPeer(\danog\MadelineProto\Settings\Peer $peer): self`
* `getPwr(): \danog\MadelineProto\Settings\Pwr`
* `setPwr(\danog\MadelineProto\Settings\Pwr $pwr): self`
* `getRpc(): \danog\MadelineProto\Settings\RPC`
* `setRpc(\danog\MadelineProto\Settings\RPC $rpc): self`
* `getSecretChats(): \danog\MadelineProto\Settings\SecretChats`
* `setSecretChats(\danog\MadelineProto\Settings\SecretChats $secretChats): self`
* `getSerialization(): \danog\MadelineProto\Settings\Serialization`
* `setSerialization(\danog\MadelineProto\Settings\Serialization $serialization): self`
* `getSchema(): \danog\MadelineProto\Settings\TLSchema`
* `setSchema(\danog\MadelineProto\Settings\TLSchema $schema): self`
* `getDb(): \danog\MadelineProto\Settings\DatabaseAbstract`
* `setDb(\danog\MadelineProto\Settings\DatabaseAbstract $db): self`
* `getIpc(): \danog\MadelineProto\Settings\Ipc`
* `setIpc(\danog\MadelineProto\Settings\Ipc $ipc): self`
* `getTemplates(): \danog\MadelineProto\Settings\Templates`
* `setTemplates(\danog\MadelineProto\Settings\Templates $templates): self`
* `hasChanged(): bool`

## Methods:
### `merge(\danog\MadelineProto\SettingsAbstract $settings): void`

Merge another instance of settings.


Parameters:
* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### `getDefaultDc(): int`

Get default DC ID.



### `getDefaultDcParams(): array`

Get default DC params.



### `setDefaultDc(int $dc): self`

Set default DC ID.


Parameters:
* `$dc`: `int` DC ID  



### `getAppInfo(): \danog\MadelineProto\Settings\AppInfo`

Get app information.


#### See also: 
* [`\danog\MadelineProto\Settings\AppInfo`: App information.](./Settings/AppInfo.md)




### `setAppInfo(\danog\MadelineProto\Settings\AppInfo $appInfo): self`

Set app information.


Parameters:
* `$appInfo`: `\danog\MadelineProto\Settings\AppInfo` App information.  


#### See also: 
* [`\danog\MadelineProto\Settings\AppInfo`: App information.](./Settings/AppInfo.md)




### `getAuth(): \danog\MadelineProto\Settings\Auth`

Get cryptography settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Auth`: Cryptography settings.](./Settings/Auth.md)




### `setAuth(\danog\MadelineProto\Settings\Auth $auth): self`

Set cryptography settings.


Parameters:
* `$auth`: `\danog\MadelineProto\Settings\Auth` Cryptography settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Auth`: Cryptography settings.](./Settings/Auth.md)




### `getConnection(): \danog\MadelineProto\Settings\Connection`

Get connection settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Connection`: Connection settings.](./Settings/Connection.md)




### `setConnection(\danog\MadelineProto\Settings\Connection $connection): self`

Set connection settings.


Parameters:
* `$connection`: `\danog\MadelineProto\Settings\Connection` Connection settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Connection`: Connection settings.](./Settings/Connection.md)




### `getFiles(): \danog\MadelineProto\Settings\Files`

Get file management settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Files`: File management settings.](./Settings/Files.md)




### `setFiles(\danog\MadelineProto\Settings\Files $files): self`

Set file management settings.


Parameters:
* `$files`: `\danog\MadelineProto\Settings\Files` File management settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Files`: File management settings.](./Settings/Files.md)




### `getLogger(): \danog\MadelineProto\Settings\Logger`

Get logger settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Logger`: Logger settings.](./Settings/Logger.md)




### `setLogger(\danog\MadelineProto\Settings\Logger $logger): self`

Set logger settings.


Parameters:
* `$logger`: `\danog\MadelineProto\Settings\Logger` Logger settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Logger`: Logger settings.](./Settings/Logger.md)




### `getPeer(): \danog\MadelineProto\Settings\Peer`

Get peer database settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Peer`: Peer database settings.](./Settings/Peer.md)




### `setPeer(\danog\MadelineProto\Settings\Peer $peer): self`

Set peer database settings.


Parameters:
* `$peer`: `\danog\MadelineProto\Settings\Peer` Peer database settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Peer`: Peer database settings.](./Settings/Peer.md)




### `getPwr(): \danog\MadelineProto\Settings\Pwr`

Get PWRTelegram settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Pwr`: PWRTelegram settings.](./Settings/Pwr.md)




### `setPwr(\danog\MadelineProto\Settings\Pwr $pwr): self`

Set PWRTelegram settings.


Parameters:
* `$pwr`: `\danog\MadelineProto\Settings\Pwr` PWRTelegram settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Pwr`: PWRTelegram settings.](./Settings/Pwr.md)




### `getRpc(): \danog\MadelineProto\Settings\RPC`

Get RPC settings.


#### See also: 
* [`\danog\MadelineProto\Settings\RPC`: RPC settings.](./Settings/RPC.md)




### `setRpc(\danog\MadelineProto\Settings\RPC $rpc): self`

Set RPC settings.


Parameters:
* `$rpc`: `\danog\MadelineProto\Settings\RPC` RPC settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\RPC`: RPC settings.](./Settings/RPC.md)




### `getSecretChats(): \danog\MadelineProto\Settings\SecretChats`

Get secret chat settings.


#### See also: 
* [`\danog\MadelineProto\Settings\SecretChats`: Secret chat settings.](./Settings/SecretChats.md)




### `setSecretChats(\danog\MadelineProto\Settings\SecretChats $secretChats): self`

Set secret chat settings.


Parameters:
* `$secretChats`: `\danog\MadelineProto\Settings\SecretChats` Secret chat settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\SecretChats`: Secret chat settings.](./Settings/SecretChats.md)




### `getSerialization(): \danog\MadelineProto\Settings\Serialization`

Get serialization settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Serialization`: Serialization settings.](./Settings/Serialization.md)




### `setSerialization(\danog\MadelineProto\Settings\Serialization $serialization): self`

Set serialization settings.


Parameters:
* `$serialization`: `\danog\MadelineProto\Settings\Serialization` Serialization settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Serialization`: Serialization settings.](./Settings/Serialization.md)




### `getSchema(): \danog\MadelineProto\Settings\TLSchema`

Get TL schema settings.


#### See also: 
* [`\danog\MadelineProto\Settings\TLSchema`: TL schema settings.](./Settings/TLSchema.md)




### `setSchema(\danog\MadelineProto\Settings\TLSchema $schema): self`

Set TL schema settings.


Parameters:
* `$schema`: `\danog\MadelineProto\Settings\TLSchema` TL schema settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\TLSchema`: TL schema settings.](./Settings/TLSchema.md)




### `getDb(): \danog\MadelineProto\Settings\DatabaseAbstract`

Get database settings.


#### See also: 
* [`\danog\MadelineProto\Settings\DatabaseAbstract`: Base class for storage backends.](./Settings/DatabaseAbstract.md)




### `setDb(\danog\MadelineProto\Settings\DatabaseAbstract $db): self`

Set database settings.


Parameters:
* `$db`: `\danog\MadelineProto\Settings\DatabaseAbstract` DatabaseAbstract settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\DatabaseAbstract`: Base class for storage backends.](./Settings/DatabaseAbstract.md)




### `getIpc(): \danog\MadelineProto\Settings\Ipc`

Get IPC server settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Ipc`: IPC server settings.](./Settings/Ipc.md)




### `setIpc(\danog\MadelineProto\Settings\Ipc $ipc): self`

Set IPC server settings.


Parameters:
* `$ipc`: `\danog\MadelineProto\Settings\Ipc` IPC server settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Ipc`: IPC server settings.](./Settings/Ipc.md)




### `getTemplates(): \danog\MadelineProto\Settings\Templates`

Get template settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Templates`: Web and CLI template settings for login.](./Settings/Templates.md)




### `setTemplates(\danog\MadelineProto\Settings\Templates $templates): self`

Set template settings.


Parameters:
* `$templates`: `\danog\MadelineProto\Settings\Templates` Template settings  


#### See also: 
* [`\danog\MadelineProto\Settings\Templates`: Web and CLI template settings for login.](./Settings/Templates.md)




### `hasChanged(): bool`

Get whether this setting was changed, also applies changes.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
