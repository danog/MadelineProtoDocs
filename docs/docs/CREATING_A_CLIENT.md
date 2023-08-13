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

<a href="https://docs.madelineproto.xyz/docs/LOGIN.html">Next section</a>