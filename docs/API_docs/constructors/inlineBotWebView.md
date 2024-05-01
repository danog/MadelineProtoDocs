---
title: "inlineBotWebView"
description: "Specifies an inline mode mini app button, shown on top of the inline query results list."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inlineBotWebView  
[Back to constructors index](/API_docs/constructors/index.html)



Specifies an [inline mode mini app](https://core.telegram.org/api/bots/webapps#inline-mode-mini-apps) button, shown on top of the inline query results list.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Text of the button|
|url|[string](/API_docs/types/string.html) | Yes|Webapp URL|



### Type: [InlineBotWebView](/API_docs/types/InlineBotWebView.html)


### Example:

```
$inlineBotWebView = ['_' => 'inlineBotWebView', 'text' => 'string', 'url' => 'string'];
```  
