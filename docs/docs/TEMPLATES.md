---
title: "Web templates for `$MadelineProto->start()`"
description: "You get the web template used for the $MadelineProto->start() web UI thusly:"
nav_order: 26
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Web templates for `$MadelineProto->start()`

You get the web template used for the `$MadelineProto->start()` web UI thusly:

```php
$template = yield $MadelineProto->getWebTemplate();
```

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

To modify the web template, use:
```php
yield $MadelineProto->setWebTemplate($new_template);
```

The new template must have a structure similar the the default template.

<a href="https://docs.madelineproto.xyz/#very-complex-and-complete-examples">Next section</a>