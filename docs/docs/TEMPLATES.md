---
title: "Web templates for `$MadelineProto->start()`"
description: "The web template used for the $MadelineProto->start() and API ID web UIs can be changed."
nav_order: 29
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Web templates for `$MadelineProto->start()`

The web template used for the `$MadelineProto->start()` and API ID web UIs can be changed.

The change is made in the [settings &raquo;](https://docs.madelineproto.xyz/docs/SETTINGS.html), [`\danog\MadelineProto\Settings\Templates`](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Settings/Templates.html) class.  

By default, it is equal to:
```html
<!DOCTYPE html>
<html>
        <head>
        <title>MadelineProto</title>
        </head>
        <body>
        <h1>MadelineProto</h1>
        <form method="POST">
        %s
        <button type="submit"/>Go</button>
        </form>
        <p>%s</p>
        </body>
</html>
```

The new template must have a structure similar the the default template.

<a href="https://docs.madelineproto.xyz/#very-complex-and-complete-examples">Next section</a>