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
* [`__construct()`](#__construct)
* [`merge(\danog\MadelineProto\SettingsAbstract $settings): void`](#merge)
* [`getAppInfo(): \danog\MadelineProto\Settings\AppInfo`](#getAppInfo)
* [`setAppInfo(\danog\MadelineProto\Settings\AppInfo $appInfo): self`](#setAppInfo)
* [`getAuth(): \danog\MadelineProto\Settings\Auth`](#getAuth)
* [`setAuth(\danog\MadelineProto\Settings\Auth $auth): self`](#setAuth)
* [`getConnection(): \danog\MadelineProto\Settings\Connection`](#getConnection)
* [`setConnection(\danog\MadelineProto\Settings\Connection $connection): self`](#setConnection)
* [`getFiles(): \danog\MadelineProto\Settings\Files`](#getFiles)
* [`setFiles(\danog\MadelineProto\Settings\Files $files): self`](#setFiles)
* [`getMetrics(): \danog\MadelineProto\Settings\Metrics`](#getMetrics)
* [`setMetrics(\danog\MadelineProto\Settings\Metrics $metrics): self`](#setMetrics)
* [`getLogger(): \danog\MadelineProto\Settings\Logger`](#getLogger)
* [`setLogger(\danog\MadelineProto\Settings\Logger $logger): self`](#setLogger)
* [`getPeer(): \danog\MadelineProto\Settings\Peer`](#getPeer)
* [`setPeer(\danog\MadelineProto\Settings\Peer $peer): self`](#setPeer)
* [`getRpc(): \danog\MadelineProto\Settings\RPC`](#getRpc)
* [`setRpc(\danog\MadelineProto\Settings\RPC $rpc): self`](#setRpc)
* [`getSecretChats(): \danog\MadelineProto\Settings\SecretChats`](#getSecretChats)
* [`setSecretChats(\danog\MadelineProto\Settings\SecretChats $secretChats): self`](#setSecretChats)
* [`getSerialization(): \danog\MadelineProto\Settings\Serialization`](#getSerialization)
* [`setSerialization(\danog\MadelineProto\Settings\Serialization $serialization): self`](#setSerialization)
* [`getSchema(): \danog\MadelineProto\Settings\TLSchema`](#getSchema)
* [`setSchema(\danog\MadelineProto\Settings\TLSchema $schema): self`](#setSchema)
* [`getDb(): \danog\MadelineProto\Settings\DatabaseAbstract`](#getDb)
* [`setDb(\danog\MadelineProto\Settings\DatabaseAbstract $db): self`](#setDb)
* [`getIpc(): \danog\MadelineProto\Settings\Ipc`](#getIpc)
* [`setIpc(\danog\MadelineProto\Settings\Ipc $ipc): self`](#setIpc)
* [`applyChanges(): \danog\MadelineProto\SettingsAbstract`](#applyChanges)
* [`getTemplates(): \danog\MadelineProto\Settings\Templates`](#getTemplates)
* [`setTemplates(\danog\MadelineProto\Settings\Templates $templates): self`](#setTemplates)
* [`getVoip(): \danog\MadelineProto\Settings\VoIP`](#getVoip)
* [`setVoip(\danog\MadelineProto\Settings\VoIP $voip): self`](#setVoip)

## Methods:
### <a name="__construct"></a> `__construct()`

Constructor.



### <a name="merge"></a> `merge(\danog\MadelineProto\SettingsAbstract $settings): void`

Merge another instance of settings.


Parameters:

* `$settings`: `\danog\MadelineProto\SettingsAbstract` Settings  


#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### <a name="getAppInfo"></a> `getAppInfo(): \danog\MadelineProto\Settings\AppInfo`

Get app information.


#### See also: 
* [`\danog\MadelineProto\Settings\AppInfo`: App information.](../../danog/MadelineProto/Settings/AppInfo.html)




### <a name="setAppInfo"></a> `setAppInfo(\danog\MadelineProto\Settings\AppInfo $appInfo): self`

Set app information.


Parameters:

* `$appInfo`: `\danog\MadelineProto\Settings\AppInfo` App information.  


#### See also: 
* [`\danog\MadelineProto\Settings\AppInfo`: App information.](../../danog/MadelineProto/Settings/AppInfo.html)




### <a name="getAuth"></a> `getAuth(): \danog\MadelineProto\Settings\Auth`

Get cryptography settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Auth`: Cryptography settings.](../../danog/MadelineProto/Settings/Auth.html)




### <a name="setAuth"></a> `setAuth(\danog\MadelineProto\Settings\Auth $auth): self`

Set cryptography settings.


Parameters:

* `$auth`: `\danog\MadelineProto\Settings\Auth` Cryptography settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Auth`: Cryptography settings.](../../danog/MadelineProto/Settings/Auth.html)




### <a name="getConnection"></a> `getConnection(): \danog\MadelineProto\Settings\Connection`

Get connection settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Connection`: Connection settings.](../../danog/MadelineProto/Settings/Connection.html)




### <a name="setConnection"></a> `setConnection(\danog\MadelineProto\Settings\Connection $connection): self`

Set connection settings.


Parameters:

* `$connection`: `\danog\MadelineProto\Settings\Connection` Connection settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Connection`: Connection settings.](../../danog/MadelineProto/Settings/Connection.html)




### <a name="getFiles"></a> `getFiles(): \danog\MadelineProto\Settings\Files`

Get file management settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Files`: File management settings.](../../danog/MadelineProto/Settings/Files.html)




### <a name="setFiles"></a> `setFiles(\danog\MadelineProto\Settings\Files $files): self`

Set file management settings.


Parameters:

* `$files`: `\danog\MadelineProto\Settings\Files` File management settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Files`: File management settings.](../../danog/MadelineProto/Settings/Files.html)




### <a name="getMetrics"></a> `getMetrics(): \danog\MadelineProto\Settings\Metrics`

Get metrics settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Metrics`: Metric settings.](../../danog/MadelineProto/Settings/Metrics.html)




### <a name="setMetrics"></a> `setMetrics(\danog\MadelineProto\Settings\Metrics $metrics): self`

Set metrics settings.


Parameters:

* `$metrics`: `\danog\MadelineProto\Settings\Metrics` File management settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Metrics`: Metric settings.](../../danog/MadelineProto/Settings/Metrics.html)




### <a name="getLogger"></a> `getLogger(): \danog\MadelineProto\Settings\Logger`

Get logger settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Logger`: Logger settings.](../../danog/MadelineProto/Settings/Logger.html)




### <a name="setLogger"></a> `setLogger(\danog\MadelineProto\Settings\Logger $logger): self`

Set logger settings.


Parameters:

* `$logger`: `\danog\MadelineProto\Settings\Logger` Logger settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Logger`: Logger settings.](../../danog/MadelineProto/Settings/Logger.html)




### <a name="getPeer"></a> `getPeer(): \danog\MadelineProto\Settings\Peer`

Get peer database settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Peer`: Peer database settings.](../../danog/MadelineProto/Settings/Peer.html)




### <a name="setPeer"></a> `setPeer(\danog\MadelineProto\Settings\Peer $peer): self`

Set peer database settings.


Parameters:

* `$peer`: `\danog\MadelineProto\Settings\Peer` Peer database settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Peer`: Peer database settings.](../../danog/MadelineProto/Settings/Peer.html)




### <a name="getRpc"></a> `getRpc(): \danog\MadelineProto\Settings\RPC`

Get RPC settings.


#### See also: 
* [`\danog\MadelineProto\Settings\RPC`: RPC settings.](../../danog/MadelineProto/Settings/RPC.html)




### <a name="setRpc"></a> `setRpc(\danog\MadelineProto\Settings\RPC $rpc): self`

Set RPC settings.


Parameters:

* `$rpc`: `\danog\MadelineProto\Settings\RPC` RPC settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\RPC`: RPC settings.](../../danog/MadelineProto/Settings/RPC.html)




### <a name="getSecretChats"></a> `getSecretChats(): \danog\MadelineProto\Settings\SecretChats`

Get secret chat settings.


#### See also: 
* [`\danog\MadelineProto\Settings\SecretChats`: Secret chat settings.](../../danog/MadelineProto/Settings/SecretChats.html)




### <a name="setSecretChats"></a> `setSecretChats(\danog\MadelineProto\Settings\SecretChats $secretChats): self`

Set secret chat settings.


Parameters:

* `$secretChats`: `\danog\MadelineProto\Settings\SecretChats` Secret chat settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\SecretChats`: Secret chat settings.](../../danog/MadelineProto/Settings/SecretChats.html)




### <a name="getSerialization"></a> `getSerialization(): \danog\MadelineProto\Settings\Serialization`

Get serialization settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Serialization`: Serialization settings.](../../danog/MadelineProto/Settings/Serialization.html)




### <a name="setSerialization"></a> `setSerialization(\danog\MadelineProto\Settings\Serialization $serialization): self`

Set serialization settings.


Parameters:

* `$serialization`: `\danog\MadelineProto\Settings\Serialization` Serialization settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Serialization`: Serialization settings.](../../danog/MadelineProto/Settings/Serialization.html)




### <a name="getSchema"></a> `getSchema(): \danog\MadelineProto\Settings\TLSchema`

Get TL schema settings.


#### See also: 
* [`\danog\MadelineProto\Settings\TLSchema`: TL schema settings.](../../danog/MadelineProto/Settings/TLSchema.html)




### <a name="setSchema"></a> `setSchema(\danog\MadelineProto\Settings\TLSchema $schema): self`

Set TL schema settings.


Parameters:

* `$schema`: `\danog\MadelineProto\Settings\TLSchema` TL schema settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\TLSchema`: TL schema settings.](../../danog/MadelineProto/Settings/TLSchema.html)




### <a name="getDb"></a> `getDb(): \danog\MadelineProto\Settings\DatabaseAbstract`

Get database settings.


#### See also: 
* [`\danog\MadelineProto\Settings\DatabaseAbstract`: Base class for storage backends.](../../danog/MadelineProto/Settings/DatabaseAbstract.html)




### <a name="setDb"></a> `setDb(\danog\MadelineProto\Settings\DatabaseAbstract $db): self`

Set database settings.


Parameters:

* `$db`: `\danog\MadelineProto\Settings\DatabaseAbstract` DatabaseAbstract settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\DatabaseAbstract`: Base class for storage backends.](../../danog/MadelineProto/Settings/DatabaseAbstract.html)




### <a name="getIpc"></a> `getIpc(): \danog\MadelineProto\Settings\Ipc`

Get IPC server settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Ipc`: IPC server settings.](../../danog/MadelineProto/Settings/Ipc.html)




### <a name="setIpc"></a> `setIpc(\danog\MadelineProto\Settings\Ipc $ipc): self`

Set IPC server settings.


Parameters:

* `$ipc`: `\danog\MadelineProto\Settings\Ipc` IPC server settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\Ipc`: IPC server settings.](../../danog/MadelineProto/Settings/Ipc.html)




### <a name="applyChanges"></a> `applyChanges(): \danog\MadelineProto\SettingsAbstract`




#### See also: 
* `\danog\MadelineProto\SettingsAbstract`




### <a name="getTemplates"></a> `getTemplates(): \danog\MadelineProto\Settings\Templates`

Get template settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Templates`: Web and CLI template settings for login.](../../danog/MadelineProto/Settings/Templates.html)




### <a name="setTemplates"></a> `setTemplates(\danog\MadelineProto\Settings\Templates $templates): self`

Set template settings.


Parameters:

* `$templates`: `\danog\MadelineProto\Settings\Templates` Template settings  


#### See also: 
* [`\danog\MadelineProto\Settings\Templates`: Web and CLI template settings for login.](../../danog/MadelineProto/Settings/Templates.html)




### <a name="getVoip"></a> `getVoip(): \danog\MadelineProto\Settings\VoIP`

Get voIP settings.


#### See also: 
* [`\danog\MadelineProto\Settings\VoIP`: VoIP settings.](../../danog/MadelineProto/Settings/VoIP.html)




### <a name="setVoip"></a> `setVoip(\danog\MadelineProto\Settings\VoIP $voip): self`

Set voIP settings.


Parameters:

* `$voip`: `\danog\MadelineProto\Settings\VoIP` VoIP settings.  


#### See also: 
* [`\danog\MadelineProto\Settings\VoIP`: VoIP settings.](../../danog/MadelineProto/Settings/VoIP.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
