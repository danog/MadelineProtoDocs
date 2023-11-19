---
title: "Creating a client"
description: "To create the session and set the serialization destination file, do the following:"
nav_order: 4
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Creating a client

To create the session and set the serialization destination file, do the following:

```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings); // The session will be serialized to session.madeline
```

Do the same to load a serialized session:

```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);  // The session will be loaded from session.madeline
```

MadelineProto can also be configured to run on ephemeral filesystems (i.e. docker containers with no volumes, storing all data on MySQL/Postgres/Redis) by setting a table prefix manually in the settings, as specified [here &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html).  

<a href="https://docs.madelineproto.xyz/docs/LOGIN.html">Next section</a>