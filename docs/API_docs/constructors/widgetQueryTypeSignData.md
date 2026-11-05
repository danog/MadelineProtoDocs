---
title: "widgetQueryTypeSignData"
description: "widgetQueryTypeSignData attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: widgetQueryTypeSignData  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|wallet|[UserWallet](/API_docs/types/UserWallet.html) | Yes|
|sign\_data|[DataJSON](/API_docs/types/DataJSON.html) | Yes|



### Type: [WidgetQueryType](/API_docs/types/WidgetQueryType.html)


### Example:

```
$widgetQueryTypeSignData = ['_' => 'widgetQueryTypeSignData', 'wallet' => UserWallet, 'sign_data' => DataJSON];
```  
