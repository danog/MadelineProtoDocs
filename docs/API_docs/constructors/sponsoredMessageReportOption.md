---
title: "sponsoredMessageReportOption"
description: "A report option for a sponsored message »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sponsoredMessageReportOption  
[Back to constructors index](/API_docs/constructors/index.html)



A [report option for a sponsored message »](https://core.telegram.org/api/sponsored-messages#reporting-sponsored-messages).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Localized description of the option.|
|option|[bytes](/API_docs/types/bytes.html) | Yes|Option identifier to pass to [channels.reportSponsoredMessage](../methods/channels.reportSponsoredMessage.html).|



### Type: [SponsoredMessageReportOption](/API_docs/types/SponsoredMessageReportOption.html)


### Example:

```
$sponsoredMessageReportOption = ['_' => 'sponsoredMessageReportOption', 'text' => 'string', 'option' => 'bytes'];
```  
