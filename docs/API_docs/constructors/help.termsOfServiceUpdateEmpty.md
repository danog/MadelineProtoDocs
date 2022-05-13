---
title: "help.termsOfServiceUpdateEmpty"
description: "No changes were made to telegram's terms of service"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_termsOfServiceUpdateEmpty.html
---
# Constructor: help.termsOfServiceUpdateEmpty  
[Back to constructors index](/API_docs/constructors/index.html)



No changes were made to telegram's terms of service

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](/API_docs/types/int.html) | Yes|New TOS updates will have to be queried using [help.getTermsOfServiceUpdate](../methods/help.getTermsOfServiceUpdate.html) in `expires` seconds|



### Type: [help.TermsOfServiceUpdate](/API_docs/types/help.TermsOfServiceUpdate.html)


### Example:

```
$help_termsOfServiceUpdateEmpty = ['_' => 'help.termsOfServiceUpdateEmpty', 'expires' => int];
```  
