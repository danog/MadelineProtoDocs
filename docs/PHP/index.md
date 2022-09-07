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
* [\danog\MadelineProto\EventHandler: Event handler.](/PHP/danog/MadelineProto/EventHandler.html)
* [\danog\MadelineProto\FileCallbackInterface: File callback interface.](/PHP/danog/MadelineProto/FileCallbackInterface.html)
* [\danog\MadelineProto\StrTools: Some tools.](/PHP/danog/MadelineProto/StrTools.html)
* [\danog\MadelineProto\Tools: Some tools.](/PHP/danog/MadelineProto/Tools.html)
* [\danog\MadelineProto\Db\DbArray: DB array interface.](/PHP/danog/MadelineProto/Db/DbArray.html)
* [\danog\MadelineProto\Db\DbPropertiesFactory: This factory class initializes the correct database backend for MadelineProto.](/PHP/danog/MadelineProto/Db/DbPropertiesFactory.html)
* [\danog\MadelineProto\Db\DriverArray: Array caching trait.](/PHP/danog/MadelineProto/Db/DriverArray.html)
* [\danog\MadelineProto\Db\SqlArray: Generic SQL database backend.](/PHP/danog/MadelineProto/Db/SqlArray.html)
* [\danog\MadelineProto\Settings\DatabaseAbstract: Base class for storage backends.](/PHP/danog/MadelineProto/Settings/DatabaseAbstract.html)
* [\danog\MadelineProto\Settings\Database\DatabaseAbstract: Base class for database backends.](/PHP/danog/MadelineProto/Settings/Database/DatabaseAbstract.html)
* [\danog\MadelineProto\Settings\Database\SqlAbstract: Generic db backend settings.](/PHP/danog/MadelineProto/Settings/Database/SqlAbstract.html)
* [\danog\MadelineProto\TL\Conversion\Extension: Manages generation of extensions for files.](/PHP/danog/MadelineProto/TL/Conversion/Extension.html)

## Classes
* [\danog\MadelineProto\API: Main API wrapper for MadelineProto.](/PHP/danog/MadelineProto/API.html)
* [\danog\MadelineProto\Coroutine: Creates a promise from a generator function yielding promises.](/PHP/danog/MadelineProto/Coroutine.html)
* [\danog\MadelineProto\Exception: Basic exception.](/PHP/danog/MadelineProto/Exception.html)
* [\danog\MadelineProto\API: Main API wrapper for MadelineProto.](/PHP/danog/MadelineProto/API.html)
* [\danog\MadelineProto\FileCallback: File callback interface.](/PHP/danog/MadelineProto/FileCallback.html)
* [\danog\MadelineProto\Logger: Logger class.](/PHP/danog/MadelineProto/Logger.html)
* [\danog\MadelineProto\Lua: Lua interface.](/PHP/danog/MadelineProto/Lua.html)
* [\danog\MadelineProto\MyTelegramOrgWrapper: Wrapper for my.telegram.org.](/PHP/danog/MadelineProto/MyTelegramOrgWrapper.html)
* [\danog\MadelineProto\PTSException: Internal error indicating a problem with Telegram's servers.](/PHP/danog/MadelineProto/PTSException.html)
* [\danog\MadelineProto\PsrLogger: PSR-3 wrapper for MadelineProto's Logger.](/PHP/danog/MadelineProto/PsrLogger.html)
* [\danog\MadelineProto\RPCErrorException: Indicates an error returned by Telegram's API.](/PHP/danog/MadelineProto/RPCErrorException.html)
* [\danog\MadelineProto\ResponseException: Indicates an error thrown when an unexpected response is received from telegram's servers.](/PHP/danog/MadelineProto/ResponseException.html)
* [\danog\MadelineProto\SecurityException: Indicates a security error.](/PHP/danog/MadelineProto/SecurityException.html)
* [\danog\MadelineProto\Settings: Settings class used for configuring MadelineProto.](/PHP/danog/MadelineProto/Settings.html)
* [\danog\MadelineProto\Shutdown: Class that controls script shutdown.](/PHP/danog/MadelineProto/Shutdown.html)
* [\danog\MadelineProto\VoIPServerConfig: Manages storage of VoIP server config.](/PHP/danog/MadelineProto/VoIPServerConfig.html)
* [\danog\MadelineProto\Db\MemoryArray: Memory database backend.](/PHP/danog/MadelineProto/Db/MemoryArray.html)
* [\danog\MadelineProto\Db\MysqlArray: MySQL database backend.](/PHP/danog/MadelineProto/Db/MysqlArray.html)
* [\danog\MadelineProto\Db\PostgresArray: Postgres database backend.](/PHP/danog/MadelineProto/Db/PostgresArray.html)
* [\danog\MadelineProto\Db\RedisArray: Redis database backend.](/PHP/danog/MadelineProto/Db/RedisArray.html)
* [\danog\MadelineProto\Files\Server: MadelineProto fileserver.](/PHP/danog/MadelineProto/Files/Server.html)
* [\danog\MadelineProto\MTProtoTools\ResponseInfo: Obtain response information for file to server.](/PHP/danog/MadelineProto/MTProtoTools/ResponseInfo.html)
* [\danog\MadelineProto\Settings\AppInfo: App information.](/PHP/danog/MadelineProto/Settings/AppInfo.html)
* [\danog\MadelineProto\Settings\Auth: Cryptography settings.](/PHP/danog/MadelineProto/Settings/Auth.html)
* [\danog\MadelineProto\Settings\Connection: Connection settings.](/PHP/danog/MadelineProto/Settings/Connection.html)
* [\danog\MadelineProto\Settings\Files: File management settings.](/PHP/danog/MadelineProto/Settings/Files.html)
* [\danog\MadelineProto\Settings\Ipc: IPC server settings.](/PHP/danog/MadelineProto/Settings/Ipc.html)
* [\danog\MadelineProto\Settings\Logger: Logger settings.](/PHP/danog/MadelineProto/Settings/Logger.html)
* [\danog\MadelineProto\Settings\Peer: Peer database settings.](/PHP/danog/MadelineProto/Settings/Peer.html)
* [\danog\MadelineProto\Settings\Pwr: PWRTelegram settings.](/PHP/danog/MadelineProto/Settings/Pwr.html)
* [\danog\MadelineProto\Settings\RPC: RPC settings.](/PHP/danog/MadelineProto/Settings/RPC.html)
* [\danog\MadelineProto\Settings\SecretChats: Secret chat settings.](/PHP/danog/MadelineProto/Settings/SecretChats.html)
* [\danog\MadelineProto\Settings\Serialization: Serialization settings.](/PHP/danog/MadelineProto/Settings/Serialization.html)
* [\danog\MadelineProto\Settings\TLSchema: TL schema settings.](/PHP/danog/MadelineProto/Settings/TLSchema.html)
* [\danog\MadelineProto\Settings\Templates: Web and CLI template settings for login.](/PHP/danog/MadelineProto/Settings/Templates.html)
* [\danog\MadelineProto\Settings\VoIP: VoIP settings.](/PHP/danog/MadelineProto/Settings/VoIP.html)
* [\danog\MadelineProto\Settings\Database\Memory: Memory backend settings.](/PHP/danog/MadelineProto/Settings/Database/Memory.html)
* [\danog\MadelineProto\Settings\Database\Mysql: MySQL backend settings.](/PHP/danog/MadelineProto/Settings/Database/Mysql.html)
* [\danog\MadelineProto\Settings\Database\Postgres: Postgres backend settings.](/PHP/danog/MadelineProto/Settings/Database/Postgres.html)
* [\danog\MadelineProto\Settings\Database\Redis: Redis backend settings.](/PHP/danog/MadelineProto/Settings/Database/Redis.html)
* [\danog\MadelineProto\TL\Exception: TL deserialization exception.](/PHP/danog/MadelineProto/TL/Exception.html)
* [\danog\MadelineProto\TL\Conversion\Entities: Entities module.](/PHP/danog/MadelineProto/TL/Conversion/Entities.html)
* [\danog\MadelineProto\TL\Conversion\Exception: TL conversion exception.](/PHP/danog/MadelineProto/TL/Conversion/Exception.html)
* [\danog\MadelineProto\TL\Types\Button: Clickable button.](/PHP/danog/MadelineProto/TL/Types/Button.html)
* [\danog\MadelineProto\TL\Types\Bytes: Bytes wrapper.](/PHP/danog/MadelineProto/TL/Types/Bytes.html)
* [\danog\MadelineProto\TON\API: TON API.](/PHP/danog/MadelineProto/TON/API.html)

## Traits
* [\danog\MadelineProto\Db\DbPropertiesTrait: Include this trait and call DbPropertiesTrait::initDb to use MadelineProto's database backend for properties.](/PHP/danog/MadelineProto/Db/DbPropertiesTrait.html)


---
Generated by [danog/phpdoc](https://phpdoc.daniil.it).  