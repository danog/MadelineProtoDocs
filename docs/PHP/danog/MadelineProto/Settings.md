---
title: "danog\\MadelineProto\\Settings: Settings class used for configuring MadelineProto."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Settings`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Settings class used for configuring MadelineProto.  




## Method list:
* `merge(\danog\MadelineProto\SettingsAbstract $settings)`
* `getAppInfo()`
* `setAppInfo(\danog\MadelineProto\Settings\AppInfo $appInfo)`
* `getAuth()`
* `setAuth(\danog\MadelineProto\Settings\Auth $auth)`
* `getConnection()`
* `setConnection(\danog\MadelineProto\Settings\Connection $connection)`
* `getFiles()`
* `setFiles(\danog\MadelineProto\Settings\Files $files)`
* `getLogger()`
* `setLogger(\danog\MadelineProto\Settings\Logger $logger)`
* `getPeer()`
* `setPeer(\danog\MadelineProto\Settings\Peer $peer)`
* `getRpc()`
* `setRpc(\danog\MadelineProto\Settings\RPC $rpc)`
* `getSecretChats()`
* `setSecretChats(\danog\MadelineProto\Settings\SecretChats $secretChats)`
* `getSerialization()`
* `setSerialization(\danog\MadelineProto\Settings\Serialization $serialization)`
* `getSchema()`
* `setSchema(\danog\MadelineProto\Settings\TLSchema $schema)`
* `getDb()`
* `setDb(\danog\MadelineProto\Settings\DatabaseAbstract $db)`
* `getIpc()`
* `setIpc(\danog\MadelineProto\Settings\Ipc $ipc)`
* `getTemplates()`
* `setTemplates(\danog\MadelineProto\Settings\Templates $templates)`
* `getVoip()`
* `setVoip(\danog\MadelineProto\Settings\VoIP $voip)`

## Methods:
### `merge(\danog\MadelineProto\SettingsAbstract $settings)`

Merge another instance of settings.


Parameters:

* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### `getAppInfo()`

Get app information.



### `setAppInfo(\danog\MadelineProto\Settings\AppInfo $appInfo)`

Set app information.


Parameters:

* `$appInfo`: `\danog\MadelineProto\Settings\AppInfo` App information.  


#### See also: 
* [`\danog\MadelineProto\Settings\AppInfo`: App information.](../../danog/MadelineProto/Settings/AppInfo.html)




### `getAuth()`

Get cryptography settings.



### `setAuth(\danog\MadelineProto\Settings\Auth $auth)`

Set cryptography settings.


Parameters:

* `$auth`: `\danog\MadelineProto\Settings\Auth` Cryptography settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Auth`: Cryptography settings.](../../danog/MadelineProto/Settings/Auth.html)




### `getConnection()`

Get connection settings.



### `setConnection(\danog\MadelineProto\Settings\Connection $connection)`

Set connection settings.


Parameters:

* `$connection`: `\danog\MadelineProto\Settings\Connection` Connection settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Connection`: Connection settings.](../../danog/MadelineProto/Settings/Connection.html)




### `getFiles()`

Get file management settings.



### `setFiles(\danog\MadelineProto\Settings\Files $files)`

Set file management settings.


Parameters:

* `$files`: `\danog\MadelineProto\Settings\Files` File management settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Files`: File management settings.](../../danog/MadelineProto/Settings/Files.html)




### `getLogger()`

Get logger settings.



### `setLogger(\danog\MadelineProto\Settings\Logger $logger)`

Set logger settings.


Parameters:

* `$logger`: `\danog\MadelineProto\Settings\Logger` Logger settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Logger`: Logger settings.](../../danog/MadelineProto/Settings/Logger.html)




### `getPeer()`

Get peer database settings.



### `setPeer(\danog\MadelineProto\Settings\Peer $peer)`

Set peer database settings.


Parameters:

* `$peer`: `\danog\MadelineProto\Settings\Peer` Peer database settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Peer`: Peer database settings.](../../danog/MadelineProto/Settings/Peer.html)




### `getRpc()`

Get RPC settings.



### `setRpc(\danog\MadelineProto\Settings\RPC $rpc)`

Set RPC settings.


Parameters:

* `$rpc`: `\danog\MadelineProto\Settings\RPC` RPC settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\RPC`: RPC settings.](../../danog/MadelineProto/Settings/RPC.html)




### `getSecretChats()`

Get secret chat settings.



### `setSecretChats(\danog\MadelineProto\Settings\SecretChats $secretChats)`

Set secret chat settings.


Parameters:

* `$secretChats`: `\danog\MadelineProto\Settings\SecretChats` Secret chat settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\SecretChats`: Secret chat settings.](../../danog/MadelineProto/Settings/SecretChats.html)




### `getSerialization()`

Get serialization settings.



### `setSerialization(\danog\MadelineProto\Settings\Serialization $serialization)`

Set serialization settings.


Parameters:

* `$serialization`: `\danog\MadelineProto\Settings\Serialization` Serialization settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Serialization`: Serialization settings.](../../danog/MadelineProto/Settings/Serialization.html)




### `getSchema()`

Get TL schema settings.



### `setSchema(\danog\MadelineProto\Settings\TLSchema $schema)`

Set TL schema settings.


Parameters:

* `$schema`: `\danog\MadelineProto\Settings\TLSchema` TL schema settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\TLSchema`: TL schema settings.](../../danog/MadelineProto/Settings/TLSchema.html)




### `getDb()`

Get database settings.



### `setDb(\danog\MadelineProto\Settings\DatabaseAbstract $db)`

Set database settings.


Parameters:

* `$db`: `\danog\MadelineProto\Settings\DatabaseAbstract` DatabaseAbstract settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\DatabaseAbstract`: Base class for storage backends.](../../danog/MadelineProto/Settings/DatabaseAbstract.html)




### `getIpc()`

Get IPC server settings.



### `setIpc(\danog\MadelineProto\Settings\Ipc $ipc)`

Set IPC server settings.


Parameters:

* `$ipc`: `\danog\MadelineProto\Settings\Ipc` IPC server settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Ipc`: IPC server settings.](../../danog/MadelineProto/Settings/Ipc.html)




### `getTemplates()`

Get template settings.



### `setTemplates(\danog\MadelineProto\Settings\Templates $templates)`

Set template settings.


Parameters:

* `$templates`: `\danog\MadelineProto\Settings\Templates` Template settings  


#### See also: 
* [`\danog\MadelineProto\Settings\Templates`: Web and CLI template settings for login.](../../danog/MadelineProto/Settings/Templates.html)




### `getVoip()`

Get voIP settings.



### `setVoip(\danog\MadelineProto\Settings\VoIP $voip)`

Set voIP settings.


Parameters:

* `$voip`: `\danog\MadelineProto\Settings\VoIP` VoIP settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\VoIP`: VoIP settings.](../../danog/MadelineProto/Settings/VoIP.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
