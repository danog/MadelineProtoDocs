---
title: "keyboardButtonRequestPoll"
description: "A button that allows the user to create and send a poll when pressed; available only in private"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonRequestPoll  
[Back to constructors index](index.md)



A button that allows the user to create and send a poll when pressed; available only in private

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|quiz|[Bool](../types/Bool.md) | Optional|If set, only quiz polls can be sent|
|text|[string](../types/string.md) | Yes|Button text|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButtonRequestPoll = ['_' => 'keyboardButtonRequestPoll', 'quiz' => Bool, 'text' => 'string'];
```  
