---
title: "updateDcOptions"
description: "Changes in the data center configuration options."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDcOptions  
[Back to constructors index](/API_docs/constructors/index.html)



Changes in the data center configuration options.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_options|Array of [DcOption](/API_docs/types/DcOption.html) | Yes|New connection options|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDcOptions = ['_' => 'updateDcOptions', 'dc_options' => [DcOption, DcOption]];
```  
