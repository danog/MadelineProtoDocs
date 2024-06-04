---
title: "factCheck"
description: "factCheck attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: factCheck  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|need\_check|[Bool](/API_docs/types/Bool.html) | Optional|
|country|[string](/API_docs/types/string.html) | Optional|
|text|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|
|hash|[long](/API_docs/types/long.html) | Yes|



### Type: [FactCheck](/API_docs/types/FactCheck.html)


### Example:

```
$factCheck = ['_' => 'factCheck', 'need_check' => Bool, 'country' => 'string', 'text' => TextWithEntities, 'hash' => long];
```  
