---
title: "channels.sponsoredMessageReportResultChooseOption"
description: "channels.sponsoredMessageReportResultChooseOption attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_sponsoredMessageReportResultChooseOption.html
---
# Constructor: channels.sponsoredMessageReportResultChooseOption  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](/API_docs/types/string.html) | Yes|
|options|Array of [SponsoredMessageReportOption](/API_docs/types/SponsoredMessageReportOption.html) | Yes|



### Type: [channels.SponsoredMessageReportResult](/API_docs/types/channels.SponsoredMessageReportResult.html)


### Example:

```
$channels_sponsoredMessageReportResultChooseOption = ['_' => 'channels.sponsoredMessageReportResultChooseOption', 'title' => 'string', 'options' => [SponsoredMessageReportOption, SponsoredMessageReportOption]];
```  
