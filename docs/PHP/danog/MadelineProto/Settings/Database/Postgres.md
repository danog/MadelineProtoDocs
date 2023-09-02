---
title: "danog\\MadelineProto\\Settings\\Database\\Postgres: Postgres backend settings."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Settings\Database\Postgres`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Postgres backend settings.  




## Method list:
* [`getDriverClass(): string`](#getdriverclass)
* [`getMaxConnections(): int`](#getmaxconnections)
* [`setMaxConnections(int $maxConnections): static`](#setmaxconnections)
* [`getIdleTimeout(): int`](#getidletimeout)
* [`setIdleTimeout(int $idleTimeout): static`](#setidletimeout)
* [`getDatabase(): string`](#getdatabase)
* [`setDatabase(string $database): static`](#setdatabase)
* [`getUsername(): string`](#getusername)
* [`setUsername(string $username): static`](#setusername)
* [`getUri(): string`](#geturi)
* [`setUri(string $uri): static`](#seturi)
* [`getKey(): string`](#getkey)
* [`getCacheTtl(): int`](#getcachettl)
* [`setCacheTtl(int|string $cacheTtl): static`](#setcachettl)
* [`getPassword(): string`](#getpassword)
* [`setPassword(string $password): static`](#setpassword)
* [`getSerializer(): ?\danog\MadelineProto\Settings\Database\SerializerType`](#getserializer)
* [`setSerializer(?\danog\MadelineProto\Settings\Database\SerializerType $serializer): static`](#setserializer)
* [`getEnableFileReferenceDb(): bool`](#getenablefilereferencedb)
* [`setEnableFileReferenceDb(bool $enableFileReferenceDb): self`](#setenablefilereferencedb)
* [`getEnableMinDb(): bool`](#getenablemindb)
* [`setEnableMinDb(bool $enableMinDb): self`](#setenablemindb)
* [`getEnableUsernameDb(): bool`](#getenableusernamedb)
* [`setEnableUsernameDb(bool $enableUsernameDb): self`](#setenableusernamedb)
* [`getEnableFullPeerDb(): bool`](#getenablefullpeerdb)
* [`setEnableFullPeerDb(bool $enableFullPeerDb): self`](#setenablefullpeerdb)
* [`getEnablePeerInfoDb(): bool`](#getenablepeerinfodb)
* [`setEnablePeerInfoDb(bool $enablePeerInfoDb): self`](#setenablepeerinfodb)

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
