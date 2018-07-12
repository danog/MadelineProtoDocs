---
title: inputPaymentCredentials
description: inputPaymentCredentials attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPaymentCredentials  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|save|[Bool](../types/Bool.md) | Optional|
|data|[DataJSON](../types/DataJSON.md) | Yes|



### Type: [InputPaymentCredentials](../types/InputPaymentCredentials.md)


### Example:

```
$inputPaymentCredentials = ['_' => 'inputPaymentCredentials', 'save' => Bool, 'data' => DataJSON];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPaymentCredentials", "save": Bool, "data": DataJSON}
```


Or, if you're into Lua:  


```
inputPaymentCredentials={_='inputPaymentCredentials', save=Bool, data=DataJSON}

```


