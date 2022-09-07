---
description: "MadelineProto PHP API reference"
title: "MadelineProto API"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
has_children: "true"
has_toc: "false"
nav_order: "2"

---
# `danog/madelineproto`

PHP implementation of telegram's MTProto protocol.



## Abstract classes
* [\danog\MadelineProto\EventHandler: Event handler.](/PHP/danog/MadelineProto/EventHandler.md)
* [\danog\MadelineProto\FileCallbackInterface: File callback interface.](/PHP/danog/MadelineProto/FileCallbackInterface.md)
* [\danog\MadelineProto\StrTools: Some tools.](/PHP/danog/MadelineProto/StrTools.md)
* [\danog\MadelineProto\Tools: Some tools.](/PHP/danog/MadelineProto/Tools.md)
* [\danog\MadelineProto\Db\DbArray: DB array interface.](/PHP/danog/MadelineProto/Db/DbArray.md)
* [\danog\MadelineProto\Db\DbPropertiesFactory: This factory class initializes the correct database backend for MadelineProto.](/PHP/danog/MadelineProto/Db/DbPropertiesFactory.md)
* [\danog\MadelineProto\Db\DriverArray: Array caching trait.](/PHP/danog/MadelineProto/Db/DriverArray.md)
* [\danog\MadelineProto\Db\SqlArray: Generic SQL database backend.](/PHP/danog/MadelineProto/Db/SqlArray.md)
* [\danog\MadelineProto\Settings\DatabaseAbstract: Base class for storage backends.](/PHP/danog/MadelineProto/Settings/DatabaseAbstract.md)
* [\danog\MadelineProto\Settings\Database\DatabaseAbstract: Base class for database backends.](/PHP/danog/MadelineProto/Settings/Database/DatabaseAbstract.md)
* [\danog\MadelineProto\Settings\Database\SqlAbstract: Generic db backend settings.](/PHP/danog/MadelineProto/Settings/Database/SqlAbstract.md)
* [\danog\MadelineProto\TL\Conversion\Extension: Manages generation of extensions for files.](/PHP/danog/MadelineProto/TL/Conversion/Extension.md)

## Classes
* [\danog\MadelineProto\API: Main API wrapper for MadelineProto.](/PHP/danog/MadelineProto/API.md)
* [\danog\MadelineProto\Coroutine: Creates a promise from a generator function yielding promises.](/PHP/danog/MadelineProto/Coroutine.md)
* [\danog\MadelineProto\Exception: Basic exception.](/PHP/danog/MadelineProto/Exception.md)
* [\danog\MadelineProto\API: Main API wrapper for MadelineProto.](/PHP/danog/MadelineProto/API.md)
* [\danog\MadelineProto\FileCallback: File callback interface.](/PHP/danog/MadelineProto/FileCallback.md)
* [\danog\MadelineProto\Logger: Logger class.](/PHP/danog/MadelineProto/Logger.md)
* [\danog\MadelineProto\Lua: Lua interface.](/PHP/danog/MadelineProto/Lua.md)
* [\danog\MadelineProto\MyTelegramOrgWrapper: Wrapper for my.telegram.org.](/PHP/danog/MadelineProto/MyTelegramOrgWrapper.md)
* [\danog\MadelineProto\PTSException: Internal error indicating a problem with Telegram's servers.](/PHP/danog/MadelineProto/PTSException.md)
* [\danog\MadelineProto\PsrLogger: PSR-3 wrapper for MadelineProto's Logger.](/PHP/danog/MadelineProto/PsrLogger.md)
* [\danog\MadelineProto\RPCErrorException: Indicates an error returned by Telegram's API.](/PHP/danog/MadelineProto/RPCErrorException.md)
* [\danog\MadelineProto\ResponseException: Indicates an error thrown when an unexpected response is received from telegram's servers.](/PHP/danog/MadelineProto/ResponseException.md)
* [\danog\MadelineProto\SecurityException: Indicates a security error.](/PHP/danog/MadelineProto/SecurityException.md)
* [\danog\MadelineProto\Settings: Settings class used for configuring MadelineProto.](/PHP/danog/MadelineProto/Settings.md)
* [\danog\MadelineProto\Shutdown: Class that controls script shutdown.](/PHP/danog/MadelineProto/Shutdown.md)
* [\danog\MadelineProto\VoIPServerConfig: Manages storage of VoIP server config.](/PHP/danog/MadelineProto/VoIPServerConfig.md)
* [\danog\MadelineProto\Db\MemoryArray: Memory database backend.](/PHP/danog/MadelineProto/Db/MemoryArray.md)
* [\danog\MadelineProto\Db\MysqlArray: MySQL database backend.](/PHP/danog/MadelineProto/Db/MysqlArray.md)
* [\danog\MadelineProto\Db\PostgresArray: Postgres database backend.](/PHP/danog/MadelineProto/Db/PostgresArray.md)
* [\danog\MadelineProto\Db\RedisArray: Redis database backend.](/PHP/danog/MadelineProto/Db/RedisArray.md)
* [\danog\MadelineProto\Files\Server: MadelineProto fileserver.](/PHP/danog/MadelineProto/Files/Server.md)
* [\danog\MadelineProto\MTProtoTools\ResponseInfo: Obtain response information for file to server.](/PHP/danog/MadelineProto/MTProtoTools/ResponseInfo.md)
* [\danog\MadelineProto\Settings\AppInfo: App information.](/PHP/danog/MadelineProto/Settings/AppInfo.md)
* [\danog\MadelineProto\Settings\Auth: Cryptography settings.](/PHP/danog/MadelineProto/Settings/Auth.md)
* [\danog\MadelineProto\Settings\Connection: Connection settings.](/PHP/danog/MadelineProto/Settings/Connection.md)
* [\danog\MadelineProto\Settings\Files: File management settings.](/PHP/danog/MadelineProto/Settings/Files.md)
* [\danog\MadelineProto\Settings\Ipc: IPC server settings.](/PHP/danog/MadelineProto/Settings/Ipc.md)
* [\danog\MadelineProto\Settings\Logger: Logger settings.](/PHP/danog/MadelineProto/Settings/Logger.md)
* [\danog\MadelineProto\Settings\Peer: Peer database settings.](/PHP/danog/MadelineProto/Settings/Peer.md)
* [\danog\MadelineProto\Settings\Pwr: PWRTelegram settings.](/PHP/danog/MadelineProto/Settings/Pwr.md)
* [\danog\MadelineProto\Settings\RPC: RPC settings.](/PHP/danog/MadelineProto/Settings/RPC.md)
* [\danog\MadelineProto\Settings\SecretChats: Secret chat settings.](/PHP/danog/MadelineProto/Settings/SecretChats.md)
* [\danog\MadelineProto\Settings\Serialization: Serialization settings.](/PHP/danog/MadelineProto/Settings/Serialization.md)
* [\danog\MadelineProto\Settings\TLSchema: TL schema settings.](/PHP/danog/MadelineProto/Settings/TLSchema.md)
* [\danog\MadelineProto\Settings\Templates: Web and CLI template settings for login.](/PHP/danog/MadelineProto/Settings/Templates.md)
* [\danog\MadelineProto\Settings\VoIP: VoIP settings.](/PHP/danog/MadelineProto/Settings/VoIP.md)
* [\danog\MadelineProto\Settings\Database\Memory: Memory backend settings.](/PHP/danog/MadelineProto/Settings/Database/Memory.md)
* [\danog\MadelineProto\Settings\Database\Mysql: MySQL backend settings.](/PHP/danog/MadelineProto/Settings/Database/Mysql.md)
* [\danog\MadelineProto\Settings\Database\Postgres: Postgres backend settings.](/PHP/danog/MadelineProto/Settings/Database/Postgres.md)
* [\danog\MadelineProto\Settings\Database\Redis: Redis backend settings.](/PHP/danog/MadelineProto/Settings/Database/Redis.md)
* [\danog\MadelineProto\TL\Exception: TL deserialization exception.](/PHP/danog/MadelineProto/TL/Exception.md)
* [\danog\MadelineProto\TL\Conversion\Entities: Entities module.](/PHP/danog/MadelineProto/TL/Conversion/Entities.md)
* [\danog\MadelineProto\TL\Conversion\Exception: TL conversion exception.](/PHP/danog/MadelineProto/TL/Conversion/Exception.md)
* [\danog\MadelineProto\TL\Types\Button: Clickable button.](/PHP/danog/MadelineProto/TL/Types/Button.md)
* [\danog\MadelineProto\TL\Types\Bytes: Bytes wrapper.](/PHP/danog/MadelineProto/TL/Types/Bytes.md)
* [\danog\MadelineProto\TON\API: TON API.](/PHP/danog/MadelineProto/TON/API.md)

## Traits
* [\danog\MadelineProto\Db\DbPropertiesTrait: Include this trait and call DbPropertiesTrait::initDb to use MadelineProto's database backend for properties.](/PHP/danog/MadelineProto/Db/DbPropertiesTrait.md)


---
Generated by [danog/phpdoc](https://phpdoc.daniil.it).  