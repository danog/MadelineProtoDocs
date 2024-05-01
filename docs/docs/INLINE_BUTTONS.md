---
title: "Inline buttons"
description: "You can easily click inline buttons using MadelineProto, just access the correct button:"
nav_order: 24
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Inline buttons

You can easily click inline buttons using MadelineProto, just access the correct button:

```php
use danog\MadelineProto\SimpleEventHandler;
use danog\MadelineProto\EventHandler\Attributes\Handler;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;

class MyEventHandler extends SimpleEventHandler
{
    #[Handler]
    public function clickButton(Incoming&Message $message): void
    {
        if ($message->keyboard) {
            // Press keyboard button by name
            $result = $message->keyboard->press("Button name", waitForResult: true);

            // Press keyboard button by coordinates
            $result = $message->keyboard->pressByCoordinates(
                row: 0,
                column: 2,
                waitForResult: true
            );

            // Or manually load button
            $button = $message->keyboard->buttons[0][2];

            $label = $button->label;
        }
    }
}


MyEventHandler::startAndLoop('session.madeline');
```

You can also access properties of `$button` (they vary depending on the [type of button](https://docs.madelineproto.xyz/API_docs/types/KeyboardButton.html)):

```php
$label = $button->label;
```

And click them:

```php
$button->click();
```

<a href="https://docs.madelineproto.xyz/docs/SECRET_CHATS.html">Next section</a>