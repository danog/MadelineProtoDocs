---
title: "help.appConfig"
description: "Contains various client configuration parameters"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_appConfig.html
---
# Constructor: help.appConfig  
[Back to constructors index](/API_docs/constructors/index.html)



Contains various [client configuration parameters](https://core.telegram.org/api/config#client-configuration)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](/API_docs/types/int.html) | Yes|
|config|[JSONValue](/API_docs/types/JSONValue.html) | Yes|[Client configuration parameters](https://core.telegram.org/api/config#client-configuration)|



### Type: [help.AppConfig](/API_docs/types/help.AppConfig.html)


### Example:

```
$help_appConfig = ['_' => 'help.appConfig', 'hash' => int, 'config' => JSONValue];
```  
