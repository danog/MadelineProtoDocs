---
title: KeyboardButton
description: constructors and methods of type KeyboardButton
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Type: KeyboardButton
[Back to types index](index.html)

Clicking these buttons:

To click these buttons simply run the `click` method:  

```php
$result = $KeyboardButton->click();
```

`$result` can be one of the following:


* A string - If the button is a keyboardButtonUrl

* [Updates](Updates.html) - If the button is a keyboardButton, the message will be sent to the chat, in reply to the message with the keyboard

* [messages.BotCallbackAnswer](messages.BotCallbackAnswer.html) - If the button is a keyboardButtonCallback or a keyboardButtonGame the button will be pressed and the result will be returned

* `false` - If the button is an unsupported button, like keyboardButtonRequestPhone, keyboardButtonRequestGeoLocation, keyboardButtonSwitchInlinekeyboardButtonBuy; you will have to parse data from these buttons manually


You can also access the properties of the constructor as a normal array, for example `$button['name']`


### Possible values (constructors):

[keyboardButton](/API_docs/constructors/keyboardButton.html)  

[keyboardButtonUrl](/API_docs/constructors/keyboardButtonUrl.html)  

[keyboardButtonCallback](/API_docs/constructors/keyboardButtonCallback.html)  

[keyboardButtonRequestPhone](/API_docs/constructors/keyboardButtonRequestPhone.html)  

[keyboardButtonRequestGeoLocation](/API_docs/constructors/keyboardButtonRequestGeoLocation.html)  

[keyboardButtonSwitchInline](/API_docs/constructors/keyboardButtonSwitchInline.html)  

[keyboardButtonGame](/API_docs/constructors/keyboardButtonGame.html)  

[keyboardButtonBuy](/API_docs/constructors/keyboardButtonBuy.html)  

[keyboardButtonUrlAuth](/API_docs/constructors/keyboardButtonUrlAuth.html)  

[inputKeyboardButtonUrlAuth](/API_docs/constructors/inputKeyboardButtonUrlAuth.html)  

[keyboardButtonRequestPoll](/API_docs/constructors/keyboardButtonRequestPoll.html)  

[inputKeyboardButtonUserProfile](/API_docs/constructors/inputKeyboardButtonUserProfile.html)  

[keyboardButtonUserProfile](/API_docs/constructors/keyboardButtonUserProfile.html)  

[keyboardButtonWebView](/API_docs/constructors/keyboardButtonWebView.html)  

[keyboardButtonSimpleWebView](/API_docs/constructors/keyboardButtonSimpleWebView.html)  

[keyboardButtonRequestPeer](/API_docs/constructors/keyboardButtonRequestPeer.html)  



### Methods that return an object of this type (methods):



