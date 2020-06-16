---
title: KeyboardButton
description: constructors and methods of type KeyboardButton
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: KeyboardButton
[Back to types index](index.md)

Clicking these buttons:

To click these buttons simply run the `click` method:  

```php
$result = $KeyboardButton->click();
```

`$result` can be one of the following:


* A string - If the button is a keyboardButtonUrl

* [Updates](Updates.md) - If the button is a keyboardButton, the message will be sent to the chat, in reply to the message with the keyboard

* [messages.BotCallbackAnswer](messages.BotCallbackAnswer.md) - If the button is a keyboardButtonCallback or a keyboardButtonGame the button will be pressed and the result will be returned

* `false` - If the button is an unsupported button, like keyboardButtonRequestPhone, keyboardButtonRequestGeoLocation, keyboardButtonSwitchInlinekeyboardButtonBuy; you will have to parse data from these buttons manually


You can also access the properties of the constructor as a normal array, for example `$button['name']`


### Possible values (constructors):

[keyboardButton](../constructors/keyboardButton.md)  

[keyboardButtonUrl](../constructors/keyboardButtonUrl.md)  

[keyboardButtonCallback](../constructors/keyboardButtonCallback.md)  

[keyboardButtonRequestPhone](../constructors/keyboardButtonRequestPhone.md)  

[keyboardButtonRequestGeoLocation](../constructors/keyboardButtonRequestGeoLocation.md)  

[keyboardButtonSwitchInline](../constructors/keyboardButtonSwitchInline.md)  

[keyboardButtonGame](../constructors/keyboardButtonGame.md)  

[keyboardButtonBuy](../constructors/keyboardButtonBuy.md)  

[keyboardButtonUrlAuth](../constructors/keyboardButtonUrlAuth.md)  

[inputKeyboardButtonUrlAuth](../constructors/inputKeyboardButtonUrlAuth.md)  



### Methods that return an object of this type (methods):



[keyboardButton](../constructors/keyboardButton.md)  

[keyboardButtonUrl](../constructors/keyboardButtonUrl.md)  

[keyboardButtonCallback](../constructors/keyboardButtonCallback.md)  

[keyboardButtonRequestPhone](../constructors/keyboardButtonRequestPhone.md)  

[keyboardButtonRequestGeoLocation](../constructors/keyboardButtonRequestGeoLocation.md)  

[keyboardButtonSwitchInline](../constructors/keyboardButtonSwitchInline.md)  

[keyboardButtonGame](../constructors/keyboardButtonGame.md)  

[keyboardButtonBuy](../constructors/keyboardButtonBuy.md)  

[keyboardButtonUrlAuth](../constructors/keyboardButtonUrlAuth.md)  

[inputKeyboardButtonUrlAuth](../constructors/inputKeyboardButtonUrlAuth.md)  

