---
title: danog\MadelineProto\DataCenterConnection: Datacenter connection.
description: 

---
# `danog\MadelineProto\DataCenterConnection`
[Back to index](../../index.md)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Datacenter connection.  




## Constants
* `danog\MadelineProto\DataCenterConnection::READ_WEIGHT`: 

* `danog\MadelineProto\DataCenterConnection::READ_WEIGHT_MEDIA`: 

* `danog\MadelineProto\DataCenterConnection::WRITE_WEIGHT`: 


## Method list:
* `needReconnect(bool $needsReconnect): void`
* `shouldReconnect(): bool`
* `getAuthKey(bool $temp): \danog\MadelineProto\MTProto\AuthKey`
* `hasAuthKey(bool $temp): bool`
* `setAuthKey(\danog\MadelineProto\MTProto\AuthKey|null $key, bool $temp): void`
* `getTempAuthKey(): \danog\MadelineProto\MTProto\TempAuthKey`
* `getPermAuthKey(): \danog\MadelineProto\MTProto\PermAuthKey`
* `hasTempAuthKey(): bool`
* `hasPermAuthKey(): bool`
* `setTempAuthKey(\danog\MadelineProto\MTProto\TempAuthKey|null $key): void`
* `setPermAuthKey(\danog\MadelineProto\MTProto\PermAuthKey|null $key): void`
* `bind(bool $pfs): void`
* `isBound(): bool`
* `isAuthorized(): bool`
* `authorized(bool $authorized): void`
* `link(string $dc): void`
* `resetSession(): void`
* `createSession(): void`
* `flush(): void`
* `getCtx(): \danog\MadelineProto\Stream\ConnectionContext`
* `hasCtx(): bool`
* `connect(\danog\MadelineProto\Stream\ConnectionContext $ctx, int $id): \Generator`
* `signalDisconnect(int $id): void`
* `disconnect(): void`
* `reconnect(): \Generator`
* `restoreBackup(): void`
* `getAuthConnection(): \danog\MadelineProto\Connection`
* `hasConnection(int $id): bool|int`
* `waitGetConnection(): \Generator`
* `getConnection(int $id): \danog\MadelineProto\Connection`
* `even(): void`
* `reading(bool $reading, int $x): void`
* `writing(bool $writing, int $x): void`
* `setExtra(\danog\MadelineProto\MTProto $API): void`
* `getExtra(): \danog\MadelineProto\MTProto`
* `isHttp(): bool`
* `byIPAddress(): bool`
* `isMedia(): bool`
* `isCDN(): bool`
* `getSettings(): \danog\MadelineProto\Settings\Connection`
* `getGenericSettings(): \danog\MadelineProto\Settings`
* `jsonSerialize(): array`

## Methods:
### `needReconnect(bool $needsReconnect): void`

Indicate if this socket needs to be reconnected.


Parameters:
* `$needsReconnect`: `bool` Whether the socket has to be reconnected  



### `shouldReconnect(): bool`

Whether this sockets needs to be reconnected.



### `getAuthKey(bool $temp): \danog\MadelineProto\MTProto\AuthKey`

Get auth key.


Parameters:
* `$temp`: `bool` Whether to fetch the temporary auth key  


#### See also: 
* [`\danog\MadelineProto\MTProto\AuthKey`: MTProto auth key.](./MTProto/AuthKey.md)




### `hasAuthKey(bool $temp): bool`

Check if auth key is present.


Parameters:
* `$temp`: `bool`   



### `setAuthKey(\danog\MadelineProto\MTProto\AuthKey|null $key, bool $temp): void`

Set auth key.


Parameters:
* `$key`: `\danog\MadelineProto\MTProto\AuthKey|null` The auth key  
* `$temp`: `bool`   


#### See also: 
* [`\danog\MadelineProto\MTProto\AuthKey`: MTProto auth key.](./MTProto/AuthKey.md)




### `getTempAuthKey(): \danog\MadelineProto\MTProto\TempAuthKey`

Get temporary authorization key.


#### See also: 
* [`\danog\MadelineProto\MTProto\TempAuthKey`: MTProto temporary auth key.](./MTProto/TempAuthKey.md)




### `getPermAuthKey(): \danog\MadelineProto\MTProto\PermAuthKey`

Get permanent authorization key.


#### See also: 
* [`\danog\MadelineProto\MTProto\PermAuthKey`: MTProto permanent auth key.](./MTProto/PermAuthKey.md)




### `hasTempAuthKey(): bool`

Check if has temporary authorization key.



### `hasPermAuthKey(): bool`

Check if has permanent authorization key.



### `setTempAuthKey(\danog\MadelineProto\MTProto\TempAuthKey|null $key): void`

Set temporary authorization key.


Parameters:
* `$key`: `\danog\MadelineProto\MTProto\TempAuthKey|null` Auth key  


#### See also: 
* [`\danog\MadelineProto\MTProto\TempAuthKey`: MTProto temporary auth key.](./MTProto/TempAuthKey.md)




### `setPermAuthKey(\danog\MadelineProto\MTProto\PermAuthKey|null $key): void`

Set permanent authorization key.


Parameters:
* `$key`: `\danog\MadelineProto\MTProto\PermAuthKey|null` Auth key  


#### See also: 
* [`\danog\MadelineProto\MTProto\PermAuthKey`: MTProto permanent auth key.](./MTProto/PermAuthKey.md)




### `bind(bool $pfs): void`

Bind temporary and permanent auth keys.


Parameters:
* `$pfs`: `bool` Whether to bind using PFS  



### `isBound(): bool`

Check if auth keys are bound.



### `isAuthorized(): bool`

Check if we are logged in.



### `authorized(bool $authorized): void`

Set the authorized boolean.


Parameters:
* `$authorized`: `bool` Whether we are authorized  



### `link(string $dc): void`

Link permanent authorization info of main DC to media DC.


Parameters:
* `$dc`: `string` Main DC ID  



### `resetSession(): void`

Reset MTProto sessions.



### `createSession(): void`

Create MTProto sessions if needed.



### `flush(): void`

Flush all pending packets.



### `getCtx(): \danog\MadelineProto\Stream\ConnectionContext`

Get connection context.


#### See also: 
* [`\danog\MadelineProto\Stream\ConnectionContext`: Connection context class.](./Stream/ConnectionContext.md)




### `hasCtx(): bool`

Has connection context?



### `connect(\danog\MadelineProto\Stream\ConnectionContext $ctx, int $id): \Generator`

Connect function.


Parameters:
* `$ctx`: `\danog\MadelineProto\Stream\ConnectionContext` Connection context  
* `$id`: `int` Optional connection ID to reconnect  


#### See also: 
* [`\danog\MadelineProto\Stream\ConnectionContext`: Connection context class.](./Stream/ConnectionContext.md)
* `\Generator`




### `signalDisconnect(int $id): void`

Signal that a connection ID disconnected.


Parameters:
* `$id`: `int` Connection ID  



### `disconnect(): void`

Close all connections to DC.



### `reconnect(): \Generator`

Reconnect to DC.


#### See also: 
* `\Generator`




### `restoreBackup(): void`

Restore backed up messages.



### `getAuthConnection(): \danog\MadelineProto\Connection`

Get connection for authorization.


#### See also: 
* [`\danog\MadelineProto\Connection`: Connection class.](./Connection.md)




### `hasConnection(int $id): bool|int`

Check if any connection is available.


Parameters:
* `$id`: `int` Connection ID  



### `waitGetConnection(): \Generator`

Get best socket in round robin, asynchronously.


Fully typed return value:
```
\Generator<int, \Amp\Promise, mixed, \danog\MadelineProto\Connection>
```
#### See also: 
* `\Amp\Promise`
* [`\danog\MadelineProto\Connection`: Connection class.](./Connection.md)
* `\Generator`




### `getConnection(int $id): \danog\MadelineProto\Connection`

Get best socket in round robin.


Parameters:
* `$id`: `int` Connection ID, for manual fetching  


#### See also: 
* [`\danog\MadelineProto\Connection`: Connection class.](./Connection.md)




### `even(): void`

Even out round robin values.



### `reading(bool $reading, int $x): void`

Indicate that one of the sockets is busy reading.


Parameters:
* `$reading`: `bool` Whether we're busy reading  
* `$x`: `int` Connection ID  



### `writing(bool $writing, int $x): void`

Indicate that one of the sockets is busy writing.


Parameters:
* `$writing`: `bool` Whether we're busy writing  
* `$x`: `int` Connection ID  



### `setExtra(\danog\MadelineProto\MTProto $API): void`

Set main instance.


Parameters:
* `$API`: `\danog\MadelineProto\MTProto` Main instance  


#### See also: 
* `\danog\MadelineProto\MTProto`




### `getExtra(): \danog\MadelineProto\MTProto`

Get main instance.


#### See also: 
* `\danog\MadelineProto\MTProto`




### `isHttp(): bool`

Check if is an HTTP connection.



### `byIPAddress(): bool`

Check if is connected directly by IP address.



### `isMedia(): bool`

Check if is a media connection.



### `isCDN(): bool`

Check if is a CDN connection.



### `getSettings(): \danog\MadelineProto\Settings\Connection`

Get DC-specific settings.


#### See also: 
* [`\danog\MadelineProto\Settings\Connection`: Connection settings.](./Settings/Connection.md)




### `getGenericSettings(): \danog\MadelineProto\Settings`

Get global settings.


#### See also: 
* [`\danog\MadelineProto\Settings`: Settings class used for configuring MadelineProto.](./Settings.md)




### `jsonSerialize(): array`

JSON serialize function.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
