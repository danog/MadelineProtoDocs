---
title: "keyboardButtonWebView"
description: "Button to open a bot mini app using messages.requestWebView, sending over user information after user confirmation."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonWebView  
[Back to constructors index](/API_docs/constructors/index.html)



Button to open a [bot mini app](https://core.telegram.org/api/bots/webapps) using [messages.requestWebView](../methods/messages.requestWebView.html), sending over user information after user confirmation.

Can only be sent or received as part of an inline keyboard, use [keyboardButtonSimpleWebView](../constructors/keyboardButtonSimpleWebView.html) for reply keyboards.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|style|[KeyboardButtonStyle](/API_docs/types/KeyboardButtonStyle.html) | Optional|
|text|[string](/API_docs/types/string.html) | Yes|Button text|
|url|[string](/API_docs/types/string.html) | Yes|[Web app url](https://core.telegram.org/api/bots/webapps)|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$keyboardButtonWebView = ['_' => 'keyboardButtonWebView', 'style' => KeyboardButtonStyle, 'text' => 'string', 'url' => 'string'];
```  
