---
title: "messageEntityTextUrl"
description: "Message entity representing a text url: for in-text urls like https://google.com use messageEntityUrl."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityTextUrl  
[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing a [text url](https://google.com): for in-text urls like <https://google.com> use [messageEntityUrl](../constructors/messageEntityUrl.html).

Note that an additional confirmation popup with the full URL must be displayed to the user before opening this link, unless the domain satisfies the conditions specified in the [domain whitelist documentation »](https://core.telegram.org/api/config#whitelisted-domains).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length))|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length))|
|url|[string](/API_docs/types/string.html) | Yes|The actual URL|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityTextUrl = ['_' => 'messageEntityTextUrl', 'offset' => int, 'length' => int, 'url' => 'string'];
```  
