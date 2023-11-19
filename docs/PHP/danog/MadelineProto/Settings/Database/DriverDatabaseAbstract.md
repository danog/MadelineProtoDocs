---
title: "danog\\MadelineProto\\Settings\\Database\\DriverDatabaseAbstract: Base class for database backends."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Settings\Database\DriverDatabaseAbstract`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Base class for database backends.  




## Method list:
* [`getEphemeralFilesystemPrefix(): ?string`](#getephemeralfilesystemprefix-string)
* [`setEphemeralFilesystemPrefix(?string $ephemeralFilesystemPrefix): static`](#setephemeralfilesystemprefix-string-ephemeralfilesystemprefix-static)
* [`getCacheTtl(): int`](#getcachettl-int)
* [`setCacheTtl(int|string $cacheTtl): static`](#setcachettl-int-string-cachettl-static)
* [`getPassword(): string`](#getpassword-string)
* [`setPassword(string $password): static`](#setpassword-string-password-static)
* [`getDatabase(): string|int`](#getdatabase-string-int)
* [`getUri(): string`](#geturi-string)
* [`setUri(string $uri): static`](#seturi-string-uri-static)
* [`getSerializer(): ?\danog\MadelineProto\Settings\Database\SerializerType`](#getserializer-danog-madelineproto-settings-database-serializertype)
* [`setSerializer(?\danog\MadelineProto\Settings\Database\SerializerType $serializer): static`](#setserializer-danog-madelineproto-settings-database-serializertype-serializer-static)
* [`getEnableFileReferenceDb(): bool`](#getenablefilereferencedb-bool)
* [`setEnableFileReferenceDb(bool $enableFileReferenceDb): static`](#setenablefilereferencedb-bool-enablefilereferencedb-static)
* [`getEnableMinDb(): bool`](#getenablemindb-bool)
* [`setEnableMinDb(bool $enableMinDb): static`](#setenablemindb-bool-enablemindb-static)
* [`getEnableUsernameDb(): bool`](#getenableusernamedb-bool)
* [`setEnableUsernameDb(bool $enableUsernameDb): static`](#setenableusernamedb-bool-enableusernamedb-static)
* [`getEnableFullPeerDb(): bool`](#getenablefullpeerdb-bool)
* [`setEnableFullPeerDb(bool $enableFullPeerDb): static`](#setenablefullpeerdb-bool-enablefullpeerdb-static)
* [`getEnablePeerInfoDb(): bool`](#getenablepeerinfodb-bool)
* [`setEnablePeerInfoDb(bool $enablePeerInfoDb): static`](#setenablepeerinfodb-bool-enablepeerinfodb-static)
* [`getDriverClass(): class-string<\danog\MadelineProto\Db\DbArray>`](#getdriverclass-class-string-danog-madelineproto-db-dbarray)

## Methods:
### `getEphemeralFilesystemPrefix(): ?string`

If set, indicates that the filesystem is ephemeral, and thus session files will not be used to store persistent data.
Must contain a unique string, used as prefix for database tables, different for every session.  
The prefix may be the same if different databases are used.  
  
This is useful when running MadelineProto inside docker containers without volumes, using just a database.  
  
Note that the session folder must still NEVER be deleted *if* MadelineProto is running,  
or else the session will be dropped from the database due to AUTH_KEY_DUPLICATED errors.  
  
Stopping the container and then deleting the session folder is 100%% OK though.


### `setEphemeralFilesystemPrefix(?string $ephemeralFilesystemPrefix): static`

If set, indicates that the filesystem is ephemeral, and thus session files will not be used to store persistent data.
Must contain a unique string, used as prefix for database tables, different for every session.  
The prefix may be the same if different databases are used.  
  
This is useful when running MadelineProto inside docker containers without volumes, using just a database.  
  
Note that the session folder must still NEVER be deleted *if* MadelineProto is running,  
or else the session will be dropped from the database due to AUTH_KEY_DUPLICATED errors.  
  
Stopping the container and then deleting the session folder is 100%% OK though.

Parameters:

* `$ephemeralFilesystemPrefix`: `?string` The database prefix  



### `getCacheTtl(): int`

Get for how long to keep records in memory after last read, for cached backends.



### `setCacheTtl(int|string $cacheTtl): static`

Set for how long to keep records in memory after last read, for cached backends.
The cache TTL identifier can be a string like '+5 minutes'.  
When data is retrieved from a database it is stored in memory.  
This helps to reduce latency, improve speed and reduce mysql/postgres/redis load.  
Data will be removed from the cache if last access was more than this amount of time.  
Clean up is done once per minute.

Parameters:

* `$cacheTtl`: `int|string` For how long to keep records in memory after last read, for cached backends.  



### `getPassword(): string`

Get password.



### `setPassword(string $password): static`

Set password.


Parameters:

* `$password`: `string` Password.  



### `getDatabase(): string|int`

Get database name/ID.



### `getUri(): string`

Get database URI.



### `setUri(string $uri): static`

Set database URI.


Parameters:

* `$uri`: `string`   



### `getSerializer(): ?\danog\MadelineProto\Settings\Database\SerializerType`




#### See also: 
* [\danog\MadelineProto\Settings\Database\SerializerType](../../../../danog/MadelineProto/Settings/Database/SerializerType.html)




### `setSerializer(?\danog\MadelineProto\Settings\Database\SerializerType $serializer): static`

Which serializer to use by default.
If null, the best serializer is chosen.

Parameters:

* `$serializer`: `?\danog\MadelineProto\Settings\Database\SerializerType`   


#### See also: 
* [\danog\MadelineProto\Settings\Database\SerializerType](../../../../danog/MadelineProto/Settings/Database/SerializerType.html)




### `getEnableFileReferenceDb(): bool`

Get whether to enable the file reference database. If disabled, will break file downloads.



### `setEnableFileReferenceDb(bool $enableFileReferenceDb): static`

Set whether to enable the file reference database. If disabled, will break file downloads.


Parameters:

* `$enableFileReferenceDb`: `bool` Whether to enable the file reference database. If disabled, will break file downloads.  



### `getEnableMinDb(): bool`

Get whether to enable the min database. If disabled, will break sendMessage (and other methods) in certain conditions.



### `setEnableMinDb(bool $enableMinDb): static`

Set whether to enable the min database. If disabled, will break sendMessage (and other methods) in certain conditions.


Parameters:

* `$enableMinDb`: `bool` Whether to enable the min database. If disabled, will break sendMessage (and other methods) in certain conditions.  



### `getEnableUsernameDb(): bool`

Get whether to enable the username database. If disabled, will break sendMessage (and other methods) with usernames.



### `setEnableUsernameDb(bool $enableUsernameDb): static`

Set whether to enable the username database. If disabled, will break sendMessage (and other methods) with usernames.


Parameters:

* `$enableUsernameDb`: `bool` Whether to enable the username database. If disabled, will break sendMessage (and other methods) with usernames.  



### `getEnableFullPeerDb(): bool`

Get whether to enable the full peer info database. If disabled, will break getFullInfo.



### `setEnableFullPeerDb(bool $enableFullPeerDb): static`

Set whether to enable the full peer info database. If disabled, will break getFullInfo.


Parameters:

* `$enableFullPeerDb`: `bool` Whether to enable the full peer info database. If disabled, will break getFullInfo.  



### `getEnablePeerInfoDb(): bool`

Get whether to enable the peer info database. If disabled, will break getInfo.



### `setEnablePeerInfoDb(bool $enablePeerInfoDb): static`

Set whether to enable the peer info database. If disabled, will break getInfo.


Parameters:

* `$enablePeerInfoDb`: `bool` Whether to enable the peer info database. If disabled, will break getInfo.  



### `getDriverClass(): class-string<\danog\MadelineProto\Db\DbArray>`




#### See also: 
* [`\danog\MadelineProto\Db\DbArray`: DB array interface.](../../../../danog/MadelineProto/Db/DbArray.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
