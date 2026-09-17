---
title: "ephemeral.welcomeMessages"
description: "ephemeral.welcomeMessages attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/ephemeral_welcomeMessages.html
---
# Constructor: ephemeral.welcomeMessages  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Yes|
|messages|Array of [EphemeralMessage](/API_docs/types/EphemeralMessage.html) | Yes|



### Type: [ephemeral.WelcomeMessages](/API_docs/types/ephemeral.WelcomeMessages.html)


### Example:

```
$ephemeral_welcomeMessages = ['_' => 'ephemeral.welcomeMessages', 'hash' => long, 'messages' => [EphemeralMessage, EphemeralMessage]];
```  
