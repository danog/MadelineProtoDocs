---
title: "help.passportConfig"
description: "Telegram passport configuration"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_passportConfig.html
---
# Constructor: help.passportConfig  
[Back to constructors index](/API_docs/constructors/index.html)



Telegram [passport](https://core.telegram.org/passport) configuration

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](/API_docs/types/int.html) | Yes|
|countries\_langs|[DataJSON](/API_docs/types/DataJSON.html) | Yes|Localization|



### Type: [help.PassportConfig](/API_docs/types/help.PassportConfig.html)


### Example:

```
$help_passportConfig = ['_' => 'help.passportConfig', 'hash' => int, 'countries_langs' => DataJSON];
```  
