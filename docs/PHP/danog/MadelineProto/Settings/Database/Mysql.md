---
title: "danog\\MadelineProto\\Settings\\Database\\Mysql: MySQL backend settings."
description: "MariaDb 10.2+ or Mysql 5.6+ required."
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Settings\Database\Mysql`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

MySQL backend settings.  

MariaDb 10.2+ or Mysql 5.6+ required.


## Method list:
* [`getDriverClass(): string`](#getdriverclass-string)
* [`getMaxConnections(): int`](#getmaxconnections-int)
* [`setMaxConnections(int $maxConnections): static`](#setmaxconnections-int-maxconnections-static)
* [`getIdleTimeout(): int`](#getidletimeout-int)
* [`setIdleTimeout(int $idleTimeout): static`](#setidletimeout-int-idletimeout-static)
* [`getDatabase(): string`](#getdatabase-string)
* [`setDatabase(string $database): static`](#setdatabase-string-database-static)
* [`getUsername(): string`](#getusername-string)
* [`setUsername(string $username): static`](#setusername-string-username-static)
* [`getUri(): string`](#geturi-string)
* [`setUri(string $uri): static`](#seturi-string-uri-static)
* [`getKey(): string`](#getkey-string)
* [`getCacheTtl(): int`](#getcachettl-int)
* [`setCacheTtl(int|string $cacheTtl): static`](#setcachettl-int-string-cachettl-static)
* [`getPassword(): string`](#getpassword-string)
* [`setPassword(string $password): static`](#setpassword-string-password-static)
* [`getSerializer(): ?\danog\MadelineProto\Settings\Database\SerializerType`](#getserializer-danog-madelineproto-settings-database-serializertype)
* [`setSerializer(?\danog\MadelineProto\Settings\Database\SerializerType $serializer): static`](#setserializer-danog-madelineproto-settings-database-serializertype-serializer-static)
* [`getEnableFileReferenceDb(): bool`](#getenablefilereferencedb-bool)
* [`setEnableFileReferenceDb(bool $enableFileReferenceDb): self`](#setenablefilereferencedb-bool-enablefilereferencedb-self)
* [`getEnableMinDb(): bool`](#getenablemindb-bool)
* [`setEnableMinDb(bool $enableMinDb): self`](#setenablemindb-bool-enablemindb-self)
* [`getEnableUsernameDb(): bool`](#getenableusernamedb-bool)
* [`setEnableUsernameDb(bool $enableUsernameDb): self`](#setenableusernamedb-bool-enableusernamedb-self)
* [`getEnableFullPeerDb(): bool`](#getenablefullpeerdb-bool)
* [`setEnableFullPeerDb(bool $enableFullPeerDb): self`](#setenablefullpeerdb-bool-enablefullpeerdb-self)
* [`getEnablePeerInfoDb(): bool`](#getenablepeerinfodb-bool)
* [`setEnablePeerInfoDb(bool $enablePeerInfoDb): self`](#setenablepeerinfodb-bool-enablepeerinfodb-self)

## Methods:
### `getDriverClass(): string`





### `getMaxConnections(): int`

Get maximum connection limit.



### `setMaxConnections(int $maxConnections): static`

Set maximum connection limit.


Parameters:

* `$maxConnections`: `int` Maximum connection limit.  



### `getIdleTimeout(): int`

Get idle timeout.



### `setIdleTimeout(int $idleTimeout): static`

Set idle timeout.


Parameters:

* `$idleTimeout`: `int` Idle timeout.  



### `getDatabase(): string`

Get database name.



### `setDatabase(string $database): static`

Set database name.


Parameters:

* `$database`: `string` Database name.  



### `getUsername(): string`

Get username.



### `setUsername(string $username): static`

Set username.


Parameters:

* `$username`: `string` Username.  



### `getUri(): string`

Get database URI.



### `setUri(string $uri): static`

Set database URI.


Parameters:

* `$uri`: `string` Database URI.  



### `getKey(): string`

Get DB key.



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



### `setEnableFileReferenceDb(bool $enableFileReferenceDb): self`

Set whether to enable the file reference database. If disabled, will break file downloads.


Parameters:

* `$enableFileReferenceDb`: `bool` Whether to enable the file reference database. If disabled, will break file downloads.  



### `getEnableMinDb(): bool`

Get whether to enable the min database. If disabled, will break sendMessage (and other methods) in certain conditions.



### `setEnableMinDb(bool $enableMinDb): self`

Set whether to enable the min database. If disabled, will break sendMessage (and other methods) in certain conditions.


Parameters:

* `$enableMinDb`: `bool` Whether to enable the min database. If disabled, will break sendMessage (and other methods) in certain conditions.  



### `getEnableUsernameDb(): bool`

Get whether to enable the username database. If disabled, will break sendMessage (and other methods) with usernames.



### `setEnableUsernameDb(bool $enableUsernameDb): self`

Set whether to enable the username database. If disabled, will break sendMessage (and other methods) with usernames.


Parameters:

* `$enableUsernameDb`: `bool` Whether to enable the username database. If disabled, will break sendMessage (and other methods) with usernames.  



### `getEnableFullPeerDb(): bool`

Get whether to enable the full peer info database. If disabled, will break getFullInfo.



### `setEnableFullPeerDb(bool $enableFullPeerDb): self`

Set whether to enable the full peer info database. If disabled, will break getFullInfo.


Parameters:

* `$enableFullPeerDb`: `bool` Whether to enable the full peer info database. If disabled, will break getFullInfo.  



### `getEnablePeerInfoDb(): bool`

Get whether to enable the peer info database. If disabled, will break getInfo.



### `setEnablePeerInfoDb(bool $enablePeerInfoDb): self`

Set whether to enable the peer info database. If disabled, will break getInfo.


Parameters:

* `$enablePeerInfoDb`: `bool` Whether to enable the peer info database. If disabled, will break getInfo.  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
