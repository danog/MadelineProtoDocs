---
title: "Inline buttons"
description: "You can easily click inline buttons using MadelineProto, just access the correct button:"
nav_order: 21
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Inline buttons

You can easily click inline buttons using MadelineProto, just access the correct button:

```php
class MyEventHandler extends \danog\MadelineProto\EventHandler
{
    public function onUpdateNewChannelMessage($update)
    {
        $this->onUpdateNewMessage($update);
    }
    public function onUpdateNewMessage($update)
    {
        if (isset($update['message']['out']) && $update['message']['out']) {
            return;
        }
        
        if (isset($update['message']['reply_markup']['rows'])) {
            foreach ($update['message']['reply_markup']['rows'] as $row) {
                foreach ($row['buttons'] as $button) {
                    $button->click();
                }
            }
        }
        
    }
}


$settings = new \danog\MadelineProto\Settings;
MyEventHandler::startAndLoop('session.madeline', $settings);
```

This peice of code will automatically click all buttons in all keyboards sent in any chat.

You can then access properties of `$button` (they vary depending on the [type of button](https://docs.madelineproto.xyz/API_docs/types/KeyboardButton.html)):

```php
$text = $button['text'];
```

And click them:

```php
$button->click();
```

<a href="https://docs.madelineproto.xyz/docs/SECRET_CHATS.html">Next section</a>