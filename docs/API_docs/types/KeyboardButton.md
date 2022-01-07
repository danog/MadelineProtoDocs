---
title: KeyboardButton
description: constructors and methods of type KeyboardButton
nav_exclude: true
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

[keyboardButton](/API_docs/constructors/keyboardButton.md)  

[keyboardButtonUrl](/API_docs/constructors/keyboardButtonUrl.md)  

[keyboardButtonCallback](/API_docs/constructors/keyboardButtonCallback.md)  

[keyboardButtonRequestPhone](/API_docs/constructors/keyboardButtonRequestPhone.md)  

[keyboardButtonRequestGeoLocation](/API_docs/constructors/keyboardButtonRequestGeoLocation.md)  

[keyboardButtonSwitchInline](/API_docs/constructors/keyboardButtonSwitchInline.md)  

[keyboardButtonGame](/API_docs/constructors/keyboardButtonGame.md)  

[keyboardButtonBuy](/API_docs/constructors/keyboardButtonBuy.md)  

[keyboardButtonUrlAuth](/API_docs/constructors/keyboardButtonUrlAuth.md)  

[inputKeyboardButtonUrlAuth](/API_docs/constructors/inputKeyboardButtonUrlAuth.md)  

[keyboardButtonRequestPoll](/API_docs/constructors/keyboardButtonRequestPoll.md)  

[inputKeyboardButtonUserProfile](/API_docs/constructors/inputKeyboardButtonUserProfile.md)  

[keyboardButtonUserProfile](/API_docs/constructors/keyboardButtonUserProfile.md)  



### Methods that return an object of this type (methods):



[keyboardButton](/API_docs/constructors/keyboardButton.md)  

[keyboardButtonUrl](/API_docs/constructors/keyboardButtonUrl.md)  

[keyboardButtonCallback](/API_docs/constructors/keyboardButtonCallback.md)  

[keyboardButtonRequestPhone](/API_docs/constructors/keyboardButtonRequestPhone.md)  

[keyboardButtonRequestGeoLocation](/API_docs/constructors/keyboardButtonRequestGeoLocation.md)  

[keyboardButtonSwitchInline](/API_docs/constructors/keyboardButtonSwitchInline.md)  

[keyboardButtonGame](/API_docs/constructors/keyboardButtonGame.md)  

[keyboardButtonBuy](/API_docs/constructors/keyboardButtonBuy.md)  

[keyboardButtonUrlAuth](/API_docs/constructors/keyboardButtonUrlAuth.md)  

[inputKeyboardButtonUrlAuth](/API_docs/constructors/inputKeyboardButtonUrlAuth.md)  

[keyboardButtonRequestPoll](/API_docs/constructors/keyboardButtonRequestPoll.md)  

[inputKeyboardButtonUserProfile](/API_docs/constructors/inputKeyboardButtonUserProfile.md)  

[keyboardButtonUserProfile](/API_docs/constructors/keyboardButtonUserProfile.md)  

