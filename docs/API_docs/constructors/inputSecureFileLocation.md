---
title: "inputSecureFileLocation"
description: "Location of encrypted telegram passport file."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFileLocation  
[Back to constructors index](/API_docs/constructors/index.html)



Location of encrypted telegram [passport](https://core.telegram.org/passport) file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|File ID, **id** parameter value from [secureFile](../constructors/secureFile.html)|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Checksum, **access\_hash** parameter value from [secureFile](../constructors/secureFile.html)|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.html)


### Example:

```
$inputSecureFileLocation = ['_' => 'inputSecureFileLocation', 'id' => long, 'access_hash' => long];
```  
