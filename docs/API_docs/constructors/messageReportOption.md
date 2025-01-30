---
title: "messageReportOption"
description: "Report menu option"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReportOption  
[Back to constructors index](/API_docs/constructors/index.html)



Report menu option

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Option title|
|option|[bytes](/API_docs/types/bytes.html) | Yes|Option identifier: if the user selects this option, re-invoke [messages.report](../methods/messages.report.html), passing this option to `option`|



### Type: [MessageReportOption](/API_docs/types/MessageReportOption.html)


### Example:

```
$messageReportOption = ['_' => 'messageReportOption', 'text' => 'string', 'option' => 'bytes'];
```  
