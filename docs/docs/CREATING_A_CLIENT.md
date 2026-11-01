---
title: "Creating a client"
description: "This page explains how to create a MadelineProto instance."
nav_order: 4
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Creating a client

This page explains how to create a MadelineProto instance.

To create the session and set the serialization destination file, do the following:

```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings); // The session will be serialized to session.madeline
```

Do the same to load a serialized session:

```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);  // The session will be loaded from session.madeline
```

MadelineProto can also be configured to run on ephemeral filesystems (i.e. docker containers with no volumes, storing all data on MySQL/Postgres/Redis) by setting a table prefix manually in the settings, as specified [here &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html).  

## Keep the instance in a variable

Temporary instances are not supported: create the instance once, store it in a variable (or a property of your service), and reuse it for as long as you need it.  

When the last reference to an `API` object goes away, its destructor shuts it down (it disconnects from the MadelineProto worker and saves the session), even if calls made through it are still running.  
For example, this doesn't work, because PHP destroys the temporary `API` returned by `api()` as soon as `->channels` is read, before `createChannel` returns:

```php
function api(): \danog\MadelineProto\API
{
    return new \danog\MadelineProto\API('session.madeline');
}

// Wrong: fails with "Disconnected from IPC server"
$result = api()->channels->createChannel(title: 'test', about: 'test', broadcast: true);
```

Do this instead (also much faster, since every new instance has to connect to the session again):

```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline');

$result = $MadelineProto->channels->createChannel(title: 'test', about: 'test', broadcast: true);
```

<a href="https://docs.madelineproto.xyz/docs/LOGIN.html">Next section</a>