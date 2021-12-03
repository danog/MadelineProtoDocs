---
title: Creating a client
description: To store information about an account session and avoid re-logging in, serialization must be done.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Creating a client

To store information about an account session and avoid re-logging in, serialization must be done.

To create the session and set the serialization destination file, do the following:
```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings); // The session will be serialized to session.madeline
```

Do the same to load a serialized session:
```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);  // The session will be loaded from session.madeline
```  


To change the session file after starting MadelineProto, do the following:
```php
$MadelineProto->session = 'newsession.madeline';
```

<a href="https://docs.madelineproto.xyz/docs/LOGIN.html">Next section</a>