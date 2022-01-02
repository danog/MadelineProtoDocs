---
title: "Using a proxy"
description: "You can use a proxy with MadelineProto."
nav_order: 23
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Using a proxy

You can use a proxy with MadelineProto.

* [How to set a proxy](#how-to-set-a-proxy)
* [Multiple proxies with automatic switch](#multiple-proxies-with-automatic-switch)
* [Use pre-built MTProxy](#mtproxy)
* [Use pre-built Socks5 proxy](#socks5-proxy)
* [Use pre-built HTTP proxy](#http-proxy)
* [Build your own proxy](#build-your-proxy)


## How to set a proxy

In order to set a proxy for MadelineProto, you have to modify the [settings](SETTINGS.html).  
You can set multiple proxies, and let MadelineProto choose the best one.  


```php
use danog\MadelineProto\Stream\MTProtoTransport\ObfuscatedStream;
use danog\MadelineProto\Stream\Proxy\HttpProxy;
use danog\MadelineProto\Stream\Proxy\SocksProxy;
use danog\MadelineProto\Settings\Connection;
use my\Custom\Namespace\MyProxy;

$settings = new Connection;
$settings->addProxy(
    ObfuscatedStream::class, 
    [
        'address' => 'magtg.com',
        'port'    =>  443,
        'secret'  => 'dd.....'
    ]
);
$settings->addProxy(
    ObfuscatedStream::class, 
    [
        'address' => 'magtg2.com',
        'port'    =>  443,
        'secret'  => 'dd.....'
    ]
);
$settings->addProxy(
    HttpProxy::class,
    [
        'address'  => '0.0.0.0',
        'port'     =>  80,
        'username' => 'user',
        'password' => 'pass'
    ],
);
$settings->addProxy(
    SocksProxy::class,
    [
        'address'  => '0.0.0.0',
        'port'     =>  80,
        'username' => 'user',
        'password' => 'pass'
    ],
);
$settings->addProxy(
    MyProxy::class,
    [
        'custom' => 'data'
    ],
);

$MadelineProto->updateSettings($settings);
```

## MTProxy

```php
use danog\MadelineProto\Settings\Connection;
use danog\MadelineProto\Stream\MTProtoTransport\ObfuscatedStream;

$settings = new Connection;
$settings->addProxy(
    ObfuscatedStream::class, 
    [
        'address' => 'magtg.com',
        'port'    =>  443,
        'secret'  => 'dd.....'
    ]
);

$MadelineProto->updateSettings($settings);
```

Both normal and `dd` secrets are supported, the transport is changed automatically by MadelineProto.

## Socks5 proxy

No password:

```php
use danog\MadelineProto\Stream\Proxy\SocksProxy;

$settings = new Connection;
$settings->addProxy(
    SocksProxy::class, 
    [
        'address'  => '0.0.0.0',
        'port'     =>  2343,
    ]
);

$MadelineProto->updateSettings($settings);
```


With password:

```php
use danog\MadelineProto\Stream\Proxy\SocksProxy;

$settings = new Connection;
$settings->addProxy(
    SocksProxy::class, 
    [
        'address'  => '0.0.0.0',
        'port'     =>  2343,
        'username' => 'username',
        'password' => 'password',
    ]
);

$MadelineProto->updateSettings($settings);
```
## HTTP proxy

No password:

```php
use danog\MadelineProto\Stream\Proxy\HttpProxy;

$settings = new Connection;
$settings->addProxy(
    HttpProxy::class, 
    [
        'address'  => '0.0.0.0',
        'port'     =>  2343,
    ]
);

$MadelineProto->updateSettings($settings);
```


With password:

```php
use danog\MadelineProto\Stream\Proxy\HttpProxy;

$settings = new Connection;
$settings->addProxy(
    HttpProxy::class, 
    [
        'address'  => '0.0.0.0',
        'port'     =>  2343,
        'username' => 'username',
        'password' => 'password',
    ]
);

$MadelineProto->updateSettings($settings);
```

## Build your proxy

In order to build your proxy, you have to use the new MadelineProto stream API to create your own proxy class.  
Feel free to study [existing proxies](https://github.com/danog/MadelineProto/tree/master/src/danog/MadelineProto/Stream/Proxy) and the [stream API](https://github.com/danog/MadelineProto/tree/master/src/danog/MadelineProto/Stream): it's well structured and well documented, so feel free to read the code.  
Don't forget to add support for [TLS connections](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Stream/Proxy/SocksProxy.php#L141) as well!  

<a href="https://docs.madelineproto.xyz/docs/ASYNC.html">Next section</a>