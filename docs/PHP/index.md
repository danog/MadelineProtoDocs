---
title: danog/madelineproto
description: PHP implementation of telegram's MTProto protocol.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# `danog/madelineproto`

PHP implementation of telegram's MTProto protocol.



## Abstract classes
* [\danog\MadelineProto\EventHandler: Event handler.](danog/MadelineProto/EventHandler.md)
* [\danog\MadelineProto\FileCallbackInterface: File callback interface.](danog/MadelineProto/FileCallbackInterface.md)
* [\danog\MadelineProto\StrTools: Some tools.](danog/MadelineProto/StrTools.md)
* [\danog\MadelineProto\Tools: Some tools.](danog/MadelineProto/Tools.md)
* [\danog\MadelineProto\Db\DbArray: DB array interface.](danog/MadelineProto/Db/DbArray.md)
* [\danog\MadelineProto\Db\DbPropertiesFactory: This factory class initializes the correct database backend for MadelineProto.](danog/MadelineProto/Db/DbPropertiesFactory.md)
* [\danog\MadelineProto\Db\DriverArray: Array caching trait.](danog/MadelineProto/Db/DriverArray.md)
* [\danog\MadelineProto\Db\SqlArray: Generic SQL database backend.](danog/MadelineProto/Db/SqlArray.md)
* [\danog\MadelineProto\Settings\DatabaseAbstract: Base class for storage backends.](danog/MadelineProto/Settings/DatabaseAbstract.md)
* [\danog\MadelineProto\Settings\Database\DatabaseAbstract: Base class for database backends.](danog/MadelineProto/Settings/Database/DatabaseAbstract.md)
* [\danog\MadelineProto\Settings\Database\SqlAbstract: Generic db backend settings.](danog/MadelineProto/Settings/Database/SqlAbstract.md)
* [\danog\MadelineProto\TL\Conversion\Extension: Manages generation of extensions for files.](danog/MadelineProto/TL/Conversion/Extension.md)

## Classes
* [\danog\MadelineProto\API: Main API wrapper for MadelineProto.](danog/MadelineProto/API.md)
* [\danog\MadelineProto\Coroutine: Creates a promise from a generator function yielding promises.](danog/MadelineProto/Coroutine.md)
* [\danog\MadelineProto\Exception: Basic exception.](danog/MadelineProto/Exception.md)
* [\danog\MadelineProto\API: Main API wrapper for MadelineProto.](danog/MadelineProto/API.md)
* [\danog\MadelineProto\FileCallback: File callback interface.](danog/MadelineProto/FileCallback.md)
* [\danog\MadelineProto\Logger: Logger class.](danog/MadelineProto/Logger.md)
* [\danog\MadelineProto\Lua: Lua interface.](danog/MadelineProto/Lua.md)
* [\danog\MadelineProto\MyTelegramOrgWrapper: Wrapper for my.telegram.org.](danog/MadelineProto/MyTelegramOrgWrapper.md)
* [\danog\MadelineProto\PTSException: Internal error indicating a problem with Telegram's servers.](danog/MadelineProto/PTSException.md)
* [\danog\MadelineProto\PsrLogger: PSR-3 wrapper for MadelineProto's Logger.](danog/MadelineProto/PsrLogger.md)
* [\danog\MadelineProto\RPCErrorException: Indicates an error returned by Telegram's API.](danog/MadelineProto/RPCErrorException.md)
* [\danog\MadelineProto\ResponseException: Indicates an error thrown when an unexpected response is received from telegram's servers.](danog/MadelineProto/ResponseException.md)
* [\danog\MadelineProto\SecurityException: Indicates a security error.](danog/MadelineProto/SecurityException.md)
* [\danog\MadelineProto\Settings: Settings class used for configuring MadelineProto.](danog/MadelineProto/Settings.md)
* [\danog\MadelineProto\Shutdown: Class that controls script shutdown.](danog/MadelineProto/Shutdown.md)
* [\danog\MadelineProto\VoIPServerConfig: Manages storage of VoIP server config.](danog/MadelineProto/VoIPServerConfig.md)
* [\danog\MadelineProto\Db\MemoryArray: Memory database backend.](danog/MadelineProto/Db/MemoryArray.md)
* [\danog\MadelineProto\Db\MysqlArray: MySQL database backend.](danog/MadelineProto/Db/MysqlArray.md)
* [\danog\MadelineProto\Db\PostgresArray: Postgres database backend.](danog/MadelineProto/Db/PostgresArray.md)
* [\danog\MadelineProto\Db\RedisArray: Redis database backend.](danog/MadelineProto/Db/RedisArray.md)
* [\danog\MadelineProto\Files\Server: MadelineProto fileserver.](danog/MadelineProto/Files/Server.md)
* [\danog\MadelineProto\MTProtoTools\ResponseInfo: Obtain response information for file to server.](danog/MadelineProto/MTProtoTools/ResponseInfo.md)
* [\danog\MadelineProto\Settings\AppInfo: App information.](danog/MadelineProto/Settings/AppInfo.md)
* [\danog\MadelineProto\Settings\Auth: Cryptography settings.](danog/MadelineProto/Settings/Auth.md)
* [\danog\MadelineProto\Settings\Connection: Connection settings.](danog/MadelineProto/Settings/Connection.md)
* [\danog\MadelineProto\Settings\Files: File management settings.](danog/MadelineProto/Settings/Files.md)
* [\danog\MadelineProto\Settings\Ipc: IPC server settings.](danog/MadelineProto/Settings/Ipc.md)
* [\danog\MadelineProto\Settings\Logger: Logger settings.](danog/MadelineProto/Settings/Logger.md)
* [\danog\MadelineProto\Settings\Peer: Peer database settings.](danog/MadelineProto/Settings/Peer.md)
* [\danog\MadelineProto\Settings\Pwr: PWRTelegram settings.](danog/MadelineProto/Settings/Pwr.md)
* [\danog\MadelineProto\Settings\RPC: RPC settings.](danog/MadelineProto/Settings/RPC.md)
* [\danog\MadelineProto\Settings\SecretChats: Secret chat settings.](danog/MadelineProto/Settings/SecretChats.md)
* [\danog\MadelineProto\Settings\Serialization: Serialization settings.](danog/MadelineProto/Settings/Serialization.md)
* [\danog\MadelineProto\Settings\TLSchema: TL schema settings.](danog/MadelineProto/Settings/TLSchema.md)
* [\danog\MadelineProto\Settings\Templates: Web and CLI template settings for login.](danog/MadelineProto/Settings/Templates.md)
* [\danog\MadelineProto\Settings\VoIP: VoIP settings.](danog/MadelineProto/Settings/VoIP.md)
* [\danog\MadelineProto\Settings\Database\Memory: Memory backend settings.](danog/MadelineProto/Settings/Database/Memory.md)
* [\danog\MadelineProto\Settings\Database\Mysql: MySQL backend settings.](danog/MadelineProto/Settings/Database/Mysql.md)
* [\danog\MadelineProto\Settings\Database\Postgres: Postgres backend settings.](danog/MadelineProto/Settings/Database/Postgres.md)
* [\danog\MadelineProto\Settings\Database\Redis: Redis backend settings.](danog/MadelineProto/Settings/Database/Redis.md)
* [\danog\MadelineProto\TL\Exception: TL deserialization exception.](danog/MadelineProto/TL/Exception.md)
* [\danog\MadelineProto\TL\Conversion\Exception: TL conversion exception.](danog/MadelineProto/TL/Conversion/Exception.md)
* [\danog\MadelineProto\TL\Types\Button: Clickable button.](danog/MadelineProto/TL/Types/Button.md)
* [\danog\MadelineProto\TL\Types\Bytes: Bytes wrapper.](danog/MadelineProto/TL/Types/Bytes.md)
* [\danog\MadelineProto\TON\API: TON API.](danog/MadelineProto/TON/API.md)

## Traits
* [\danog\MadelineProto\Db\DbPropertiesTrait: Include this trait and call DbPropertiesTrait::initDb to use MadelineProto's database backend for properties.](danog/MadelineProto/Db/DbPropertiesTrait.md)


---
Generated by [danog/phpdoc](https://phpdoc.daniil.it).  