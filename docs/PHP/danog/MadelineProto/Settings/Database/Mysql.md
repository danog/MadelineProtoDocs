---
title: "danog\\MadelineProto\\Settings\\Database\\Mysql: MySQL backend settings."
description: "MariaDb 10.2+ or Mysql 5.6+ required."

image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# `danog\MadelineProto\Settings\Database\Mysql`
[Back to index](../../../../index.md)

> Author: Daniil Gentili <daniil@daniil.it>  
  

MySQL backend settings.  

MariaDb 10.2+ or Mysql 5.6+ required.


## Method list:
* `getMaxConnections(): int`
* `setMaxConnections(int $maxConnections): self`
* `getIdleTimeout(): int`
* `setIdleTimeout(int $idleTimeout): self`
* `getDatabase(): string`
* `setDatabase(string $database): self`
* `getUsername(): string`
* `setUsername(string $username): self`
* `getUri(): string`
* `setUri(string $uri): self`
* `getKey(): string`
* `getCacheTtl(): int`
* `setCacheTtl(int|string $cacheTtl): self`
* `getPassword(): string`
* `setPassword(string $password): self`
* `getEnableFileReferenceDb(): bool`
* `setEnableFileReferenceDb(bool $enableFileReferenceDb): self`
* `getEnableMinDb(): bool`
* `setEnableMinDb(bool $enableMinDb): self`
* `getEnableUsernameDb(): bool`
* `setEnableUsernameDb(bool $enableUsernameDb): self`
* `getEnableFullPeerDb(): bool`
* `setEnableFullPeerDb(bool $enableFullPeerDb): self`
* `getEnablePeerInfoDb(): bool`
* `setEnablePeerInfoDb(bool $enablePeerInfoDb): self`

## Methods:
### `getMaxConnections(): int`

Get maximum connection limit.



### `setMaxConnections(int $maxConnections): self`

Set maximum connection limit.


Parameters:
* `$maxConnections`: `int` Maximum connection limit.  



### `getIdleTimeout(): int`

Get idle timeout.



### `setIdleTimeout(int $idleTimeout): self`

Set idle timeout.


Parameters:
* `$idleTimeout`: `int` Idle timeout.  



### `getDatabase(): string`

Get database name.



### `setDatabase(string $database): self`

Set database name.


Parameters:
* `$database`: `string` Database name.  



### `getUsername(): string`

Get username.



### `setUsername(string $username): self`

Set username.


Parameters:
* `$username`: `string` Username.  



### `getUri(): string`

Get database URI.



### `setUri(string $uri): self`

Set database URI.


Parameters:
* `$uri`: `string` Database URI.  



### `getKey(): string`

Get DB key.



### `getCacheTtl(): int`

Get for how long to keep records in memory after last read, for cached backends.



### `setCacheTtl(int|string $cacheTtl): self`

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



### `setPassword(string $password): self`

Set password.


Parameters:
* `$password`: `string` Password.  



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
