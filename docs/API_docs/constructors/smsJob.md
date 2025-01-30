---
title: "smsJob"
description: "Info about an SMS job."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: smsJob  
[Back to constructors index](/API_docs/constructors/index.html)



Info about an SMS job.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|job\_id|[string](/API_docs/types/string.html) | Yes|Job ID|
|phone\_number|[string](/API_docs/types/string.html) | Yes|Destination phone number|
|text|[string](/API_docs/types/string.html) | Yes|Text|



### Type: [SmsJob](/API_docs/types/SmsJob.html)


### Example:

```
$smsJob = ['_' => 'smsJob', 'job_id' => 'string', 'phone_number' => 'string', 'text' => 'string'];
```  
