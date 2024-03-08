---
title: "help.timezonesList"
description: "help.timezonesList attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_timezonesList.html
---
# Constructor: help.timezonesList  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|timezones|Array of [Timezone](/API_docs/types/Timezone.html) | Yes|
|hash|[int](/API_docs/types/int.html) | Yes|



### Type: [help.TimezonesList](/API_docs/types/help.TimezonesList.html)


### Example:

```
$help_timezonesList = ['_' => 'help.timezonesList', 'timezones' => [Timezone, Timezone], 'hash' => int];
```  
