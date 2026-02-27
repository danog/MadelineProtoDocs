---
title: "danog\\MadelineProto\\Settings\\Database\\Redis: Redis backend settings."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Settings\Database\Redis`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Redis backend settings.  




## Method list:
* [`getOrmSettings(): \danog\AsyncOrm\Settings`](#getOrmSettings)
* [`getDatabase(): int`](#getDatabase)
* [`setDatabase(int $database): \danog\MadelineProto\Settings\Database\Redis`](#setDatabase)
* [`getUri(): string`](#getUri)
* [`setUri(string $uri): static`](#setUri)
* [`getEphemeralFilesystemPrefix(): ?string`](#getEphemeralFilesystemPrefix)
* [`setEphemeralFilesystemPrefix(?string $ephemeralFilesystemPrefix): static`](#setEphemeralFilesystemPrefix)
* [`getCacheTtl(): int`](#getCacheTtl)
* [`setCacheTtl((int|string) $cacheTtl): static`](#setCacheTtl)
* [`getPassword(): string`](#getPassword)
* [`setPassword(string $password): static`](#setPassword)
* [`getSerializer(): ?\danog\MadelineProto\Settings\Database\SerializerType`](#getSerializer)
* [`setSerializer(?\danog\MadelineProto\Settings\Database\SerializerType $serializer): static`](#setSerializer)
* [`getEnableFileReferenceDb(): bool`](#getEnableFileReferenceDb)
* [`setEnableFileReferenceDb(bool $enableFileReferenceDb): static`](#setEnableFileReferenceDb)
* [`getEnableMinDb(): bool`](#getEnableMinDb)
* [`setEnableMinDb(bool $enableMinDb): static`](#setEnableMinDb)
* [`getEnableUsernameDb(): bool`](#getEnableUsernameDb)
* [`setEnableUsernameDb(bool $enableUsernameDb): static`](#setEnableUsernameDb)
* [`getEnableFullPeerDb(): bool`](#getEnableFullPeerDb)
* [`setEnableFullPeerDb(bool $enableFullPeerDb): static`](#setEnableFullPeerDb)
* [`getEnablePeerInfoDb(): bool`](#getEnablePeerInfoDb)
* [`setEnablePeerInfoDb(bool $enablePeerInfoDb): static`](#setEnablePeerInfoDb)

## Methods:
### <a name="getOrmSettings"></a> `getOrmSettings(): \danog\AsyncOrm\Settings`




#### See also: 
* `\danog\AsyncOrm\Settings`




### <a name="getDatabase"></a> `getDatabase(): int`

Get database number.



### <a name="setDatabase"></a> `setDatabase(int $database): \danog\MadelineProto\Settings\Database\Redis`

Set database number.


Parameters:

* `$database`: `int` Database number.  



### <a name="getUri"></a> `getUri(): string`

Get database URI.



### <a name="setUri"></a> `setUri(string $uri): static`

Set database URI.


Parameters:

* `$uri`: `string` Database URI.  



### <a name="getEphemeralFilesystemPrefix"></a> `getEphemeralFilesystemPrefix(): ?string`

If set, indicates that the filesystem is ephemeral, and thus session files will not be used to store persistent data.
  
Must contain a unique string, used as prefix for database tables, different for every session.  
The prefix may be the same if different databases are used.  
  
This is useful when running MadelineProto inside docker containers without volumes, using just a database.  
  
Note that the session folder must still NEVER be deleted *if* MadelineProto is running,  
or else the session will be dropped from the database due to AUTH_KEY_DUPLICATED errors.  
  
Stopping the container and then deleting the session folder is 100% OK though.  



### <a name="setEphemeralFilesystemPrefix"></a> `setEphemeralFilesystemPrefix(?string $ephemeralFilesystemPrefix): static`

If set, indicates that the filesystem is ephemeral, and thus session files will not be used to store persistent data.
  
Must contain a unique string, used as prefix for database tables, different for every session.  
The prefix may be the same if different databases are used.  
  
This is useful when running MadelineProto inside docker containers without volumes, using just a database.  
  
Note that the session folder must still NEVER be deleted *if* MadelineProto is running,  
or else the session will be dropped from the database due to AUTH_KEY_DUPLICATED errors.  
  
Stopping the container and then deleting the session folder is 100% OK though.  


Parameters:

* `$ephemeralFilesystemPrefix`: `?string` The database prefix  



### <a name="getCacheTtl"></a> `getCacheTtl(): int`

Get for how long to keep records in memory after last read, for cached backends.



### <a name="setCacheTtl"></a> `setCacheTtl((int|string) $cacheTtl): static`

Set for how long to keep records in memory after last read, for cached backends.
  
The cache TTL identifier can be a string like '+5 minutes'.  
When data is retrieved from a database it is stored in memory.  
This helps to reduce latency, improve speed and reduce mysql/postgres/redis load.  
Data will be removed from the cache if last access was more than this amount of time.  
Clean up is done once per minute.  


Parameters:

* `$cacheTtl`: `(int|string)` For how long to keep records in memory after last read, for cached backends.  



### <a name="getPassword"></a> `getPassword(): string`

Get password.



### <a name="setPassword"></a> `setPassword(string $password): static`

Set password.


Parameters:

* `$password`: `string` Password.  



### <a name="getSerializer"></a> `getSerializer(): ?\danog\MadelineProto\Settings\Database\SerializerType`




#### See also: 
* [\danog\MadelineProto\Settings\Database\SerializerType](../../../../danog/MadelineProto/Settings/Database/SerializerType.html)




### <a name="setSerializer"></a> `setSerializer(?\danog\MadelineProto\Settings\Database\SerializerType $serializer): static`

Which serializer to use by default.
  
If null, the best serializer is chosen.  


Parameters:

* `$serializer`: `?\danog\MadelineProto\Settings\Database\SerializerType`   


#### See also: 
* [\danog\MadelineProto\Settings\Database\SerializerType](../../../../danog/MadelineProto/Settings/Database/SerializerType.html)




### <a name="getEnableFileReferenceDb"></a> `getEnableFileReferenceDb(): bool`

Get whether to enable the file reference database. If disabled, will break file downloads.



### <a name="setEnableFileReferenceDb"></a> `setEnableFileReferenceDb(bool $enableFileReferenceDb): static`

Set whether to enable the file reference database. If disabled, will break file downloads.


Parameters:

* `$enableFileReferenceDb`: `bool` Whether to enable the file reference database. If disabled, will break file downloads.  



### <a name="getEnableMinDb"></a> `getEnableMinDb(): bool`

Get whether to enable the min database. If disabled, will break sendMessage (and other methods) in certain conditions.



### <a name="setEnableMinDb"></a> `setEnableMinDb(bool $enableMinDb): static`

Set whether to enable the min database. If disabled, will break sendMessage (and other methods) in certain conditions.


Parameters:

* `$enableMinDb`: `bool` Whether to enable the min database. If disabled, will break sendMessage (and other methods) in certain conditions.  



### <a name="getEnableUsernameDb"></a> `getEnableUsernameDb(): bool`

Get whether to enable the username database. If disabled, will break sendMessage (and other methods) with usernames.



### <a name="setEnableUsernameDb"></a> `setEnableUsernameDb(bool $enableUsernameDb): static`

Set whether to enable the username database. If disabled, will break sendMessage (and other methods) with usernames.


Parameters:

* `$enableUsernameDb`: `bool` Whether to enable the username database. If disabled, will break sendMessage (and other methods) with usernames.  



### <a name="getEnableFullPeerDb"></a> `getEnableFullPeerDb(): bool`

Get whether to enable the full peer info database. If disabled, will break getFullInfo.



### <a name="setEnableFullPeerDb"></a> `setEnableFullPeerDb(bool $enableFullPeerDb): static`

Set whether to enable the full peer info database. If disabled, will break getFullInfo.


Parameters:

* `$enableFullPeerDb`: `bool` Whether to enable the full peer info database. If disabled, will break getFullInfo.  



### <a name="getEnablePeerInfoDb"></a> `getEnablePeerInfoDb(): bool`

Get whether to enable the peer info database. If disabled, will break getInfo.



### <a name="setEnablePeerInfoDb"></a> `setEnablePeerInfoDb(bool $enablePeerInfoDb): static`

Set whether to enable the peer info database. If disabled, will break getInfo.


Parameters:

* `$enablePeerInfoDb`: `bool` Whether to enable the peer info database. If disabled, will break getInfo.  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
