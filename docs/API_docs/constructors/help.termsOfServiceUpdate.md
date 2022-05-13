---
title: "help.termsOfServiceUpdate"
description: "Info about an update of telegram's terms of service. If the terms of service are declined, then the account.deleteAccount method should be called with the reason 'Decline ToS update'"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_termsOfServiceUpdate.html
---
# Constructor: help.termsOfServiceUpdate  
[Back to constructors index](/API_docs/constructors/index.html)



Info about an update of telegram's terms of service. If the terms of service are declined, then the [account.deleteAccount](../methods/account.deleteAccount.html) method should be called with the reason "Decline ToS update"

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](/API_docs/types/int.html) | Yes|New TOS updates will have to be queried using [help.getTermsOfServiceUpdate](../methods/help.getTermsOfServiceUpdate.html) in `expires` seconds|
|terms\_of\_service|[help.TermsOfService](/API_docs/constructors/help.TermsOfService.html) | Yes|New terms of service|



### Type: [help.TermsOfServiceUpdate](/API_docs/types/help.TermsOfServiceUpdate.html)


### Example:

```
$help_termsOfServiceUpdate = ['_' => 'help.termsOfServiceUpdate', 'expires' => int, 'terms_of_service' => help.TermsOfService];
```  
