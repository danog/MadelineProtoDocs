---
title: "reportResultChooseOption"
description: "The user must choose one of the following options, and then messages.report must be re-invoked, passing the option's option identifier to messages.report.option."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: reportResultChooseOption  
[Back to constructors index](/API_docs/constructors/index.html)



The user must choose one of the following options, and then [messages.report](../methods/messages.report.html) must be re-invoked, passing the option's `option` identifier to [messages.report](../methods/messages.report.html).`option`.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Title of the option popup|
|options|Array of [MessageReportOption](/API_docs/types/MessageReportOption.html) | Yes|Available options, rendered as menu entries.|



### Type: [ReportResult](/API_docs/types/ReportResult.html)


### Example:

```
$reportResultChooseOption = ['_' => 'reportResultChooseOption', 'title' => 'string', 'options' => [MessageReportOption, MessageReportOption]];
```  
