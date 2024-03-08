---
title: "keyboardButtonSimpleWebView"
description: "Button to open a bot mini app using messages.requestSimpleWebView, without sending user information to the web app."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonSimpleWebView  
[Back to constructors index](/API_docs/constructors/index.html)



Button to open a [bot mini app](https://core.telegram.org/api/bots/webapps) using [messages.requestSimpleWebView](../methods/messages.requestSimpleWebView.html), without sending user information to the web app.

Can only be sent or received as part of a reply keyboard, use [keyboardButtonWebView](../constructors/keyboardButtonWebView.html) for inline keyboards.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Button text|
|url|[string](/API_docs/types/string.html) | Yes|[Web app URL](https://core.telegram.org/api/bots/webapps)|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$keyboardButtonSimpleWebView = ['_' => 'keyboardButtonSimpleWebView', 'text' => 'string', 'url' => 'string'];
```  
