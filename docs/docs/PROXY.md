---
title: Using a proxy
description: You can use a proxy with MadelineProto.
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
Legacy proxy names are allowed (`\HttpProxy`, `\SocksProxy`), but not recommended.
The recommended way of getting proxy names to set in the settings is through the `getName` method of the new [proxy interface](#build-your-proxy).  

```php
use danog\MadelineProto\Stream\MTProtoTransport\ObfuscatedStream;
use danog\MadelineProto\Stream\Proxy\HttpProxy;
use danog\MadelineProto\Stream\Proxy\SocksProxy;
use my\Custom\Namespace\MyProxy;

$settings['connection_settings']['all']['proxy'] = ObfuscatedStream::getName();
// ...
$settings['connection_settings']['all']['proxy'] = HttpProxy::getName();
// ...
$settings['connection_settings']['all']['proxy'] = SocksProxy::getName();
// ...
$settings['connection_settings']['all']['proxy'] = MyProxy::getName();
```

You can also set multiple proxies:

## Multiple proxies with automatic switch

To set multiple proxies, and let MadelineProto choose the best one, simply assign arrays of proxy and proxy extras to the appropriate settings.  
You can also use [iterable objects](https://www.php.net/manual/en/class.iterator.php) instead of arrays of proxy settings to dynamically change the proxies used without reloading the settings.  

```php
use danog\MadelineProto\Stream\MTProtoTransport\ObfuscatedStream;
use danog\MadelineProto\Stream\Proxy\HttpProxy;
use danog\MadelineProto\Stream\Proxy\SocksProxy;
use my\Custom\Namespace\MyProxy;

$settings['connection_settings']['all']['proxy'] = [
    ObfuscatedStream::getName(),
    ObfuscatedStream::getName(),
    HttpProxy::getName(),
    SocksProxy::getName(),
    MyProxy::getName()
];
$settings['connection_settings']['all']['proxy_extra'] = [
    [
        'address' => 'magtg.com',
        'port'    =>  443,
        'secret'  => 'dd.....'
    ],
    [
        'address' => '1.2.3.4',
        'port'    =>  443,
        'secret'  => 'dd.....'
    ],
    [
        'address'  => '0.0.0.0',
        'port'     =>  80,
        'username' => 'user',
        'password' => 'pass'
    ],
    [
        'address' => '0.0.0.0',
        'port'    =>  242,
        'username' => 'user',
        'password' => 'pass'
    ],
    [
        'address' => '0.0.0.0',
        'port'    =>  242,
        'custom' => 'args',
    ],
];
```

## MTProxy

```php
use danog\MadelineProto\Stream\MTProtoTransport\ObfuscatedStream;

$settings['connection_settings']['all']['proxy'] = ObfuscatedStream::getName();
$settings['connection_settings']['all']['proxy_extra'] = [
    'address' => '0.0.0.0',
    'port'    =>  443,
    'secret'  => 'dd.....'
];

$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
```

Both normal and `dd` secrets are supported, the transport is changed automatically by MadelineProto.

## Socks5 proxy

No password:

```php
use danog\MadelineProto\Stream\Proxy\SocksProxy;

$settings['connection_settings']['all']['proxy'] = SocksProxy::getName();
$settings['connection_settings']['all']['proxy_extra'] = [
    'address'  => '0.0.0.0',
    'port'     =>  2343,
];

$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
```


With password:

```php
use danog\MadelineProto\Stream\Proxy\SocksProxy;

$settings['connection_settings']['all']['proxy'] = SocksProxy::getName();
$settings['connection_settings']['all']['proxy_extra'] = [
    'address'  => '0.0.0.0',
    'port'     =>  2343,
    'username' => 'username',
    'password' => 'password',
];

$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
```

## HTTP proxy

No password:

```php
use danog\MadelineProto\Stream\Proxy\HttpProxy;

$settings['connection_settings']['all']['proxy'] = HttpProxy::getName();
$settings['connection_settings']['all']['proxy_extra'] = [
    'address'  => '0.0.0.0',
    'port'     =>  2343,
];

$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
```


With password:

```php
use danog\MadelineProto\Stream\Proxy\HttpProxy;

$settings['connection_settings']['all']['proxy'] = HttpProxy::getName();
$settings['connection_settings']['all']['proxy_extra'] = [
    'address'  => '0.0.0.0',
    'port'     =>  2343,
    'username' => 'username',
    'password' => 'password',
];

$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
```


## Build your proxy

In order to build your proxy, you have to use the new MadelineProto stream API to create your own proxy class.  
Feel free to study [existing proxies](https://github.com/danog/MadelineProto/tree/master/src/danog/MadelineProto/Stream/Proxy) and the [stream API](https://github.com/danog/MadelineProto/tree/master/src/danog/MadelineProto/Stream): it's well structured and well documented, so feel free to read the code.  
Don't forget to add support for [TLS connections](https://github.com/danog/MadelineProto/blob/master/src/danog/MadelineProto/Stream/Proxy/SocksProxy.php#L141) as well!  


<a href="https://docs.madelineproto.xyz/docs/USING_METHODS.html">Next section</a>