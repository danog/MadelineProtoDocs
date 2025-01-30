---
title: "factCheck"
description: "Represents a fact-check » created by an independent fact-checker."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: factCheck  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [fact-check »](https://core.telegram.org/api/factcheck) created by an independent fact-checker.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|need\_check|[Bool](/API_docs/types/Bool.html) | Optional|If set, the `country`/`text` fields will **not** be set, and the fact check must be fetched manually by the client (if it isn't already cached with the key specified in `hash`) using bundled [messages.getFactCheck](../methods/messages.getFactCheck.html) requests, when the message with the factcheck scrolls into view.|
|country|[string](/API_docs/types/string.html) | Optional|A two-letter ISO 3166-1 alpha-2 country code of the country for which the fact-check should be shown.|
|text|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|The fact-check.|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|



### Type: [FactCheck](/API_docs/types/FactCheck.html)


### Example:

```
$factCheck = ['_' => 'factCheck', 'need_check' => Bool, 'country' => 'string', 'text' => TextWithEntities, 'hash' => long];
```  
