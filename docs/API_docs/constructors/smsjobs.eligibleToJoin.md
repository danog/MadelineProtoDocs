---
title: "smsjobs.eligibleToJoin"
description: "SMS jobs eligibility"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/smsjobs_eligibleToJoin.html
---
# Constructor: smsjobs.eligibleToJoin  
[Back to constructors index](/API_docs/constructors/index.html)



SMS jobs eligibility

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|terms\_url|[string](/API_docs/types/string.html) | Yes|Terms of service URL|
|monthly\_sent\_sms|[int](/API_docs/types/int.html) | Yes|Monthly sent SMSes|



### Type: [smsjobs.EligibilityToJoin](/API_docs/types/smsjobs.EligibilityToJoin.html)


### Example:

```
$smsjobs_eligibleToJoin = ['_' => 'smsjobs.eligibleToJoin', 'terms_url' => 'string', 'monthly_sent_sms' => int];
```  
