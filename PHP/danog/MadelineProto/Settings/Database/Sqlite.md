# danog\MadelineProto\Settings\Database\Sqlite: SQLite backend settings.

> 
Stores the session's data in an SQLite database file (requires the pdo_sqlite extension):
no database server is needed, and lookups are much faster than with a server.


[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

SQLite backend settings.  


Stores the session's data in an SQLite database file (requires the pdo_sqlite extension):
no database server is needed, and lookups are much faster than with a server.



## Method list:
* [`getOrmSettings(): \danog\AsyncOrm\Settings`](#getOrmSettings)
* [`getPath(): string`](#getPath)
* [`setPath(string $path): \danog\MadelineProto\Settings\Database\Sqlite`](#setPath)
* [`getCacheTtl(): int`](#getCacheTtl)
* [`setCacheTtl((int|string) $cacheTtl): \danog\MadelineProto\Settings\Database\Sqlite`](#setCacheTtl)
* [`getSerializer(): ?\danog\MadelineProto\Settings\Database\SerializerType`](#getSerializer)
* [`setSerializer(?\danog\MadelineProto\Settings\Database\SerializerType $serializer): \danog\MadelineProto\Settings\Database\Sqlite`](#setSerializer)
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




### <a name="getPath"></a> `getPath(): string`

Get the absolute path of the database file.



### <a name="setPath"></a> `setPath(string $path): \danog\MadelineProto\Settings\Database\Sqlite`

Set the absolute path of the database file (created if it doesn't exist).


Parameters:

* `$path`: `string` Absolute path of the database file.  



### <a name="getCacheTtl"></a> `getCacheTtl(): int`

Get for how long to keep records in memory after last read, for cached backends.



### <a name="setCacheTtl"></a> `setCacheTtl((int|string) $cacheTtl): \danog\MadelineProto\Settings\Database\Sqlite`

Set for how long to keep records in memory after last read, for cached backends.
  
The cache TTL identifier can be a string like '+5 minutes'.  


Parameters:

* `$cacheTtl`: `(int|string)` For how long to keep records in memory after last read, for cached backends.  



### <a name="getSerializer"></a> `getSerializer(): ?\danog\MadelineProto\Settings\Database\SerializerType`

Get the serializer to use by default.


#### See also: 
* [\danog\MadelineProto\Settings\Database\SerializerType](../../../../danog/MadelineProto/Settings/Database/SerializerType.html)




### <a name="setSerializer"></a> `setSerializer(?\danog\MadelineProto\Settings\Database\SerializerType $serializer): \danog\MadelineProto\Settings\Database\Sqlite`

Set the serializer to use by default.


Parameters:

* `$serializer`: `?\danog\MadelineProto\Settings\Database\SerializerType` The serializer to use by default; if null, the best one is chosen.  


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
