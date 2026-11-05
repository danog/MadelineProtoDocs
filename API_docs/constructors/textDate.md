# textDate

> textDate attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|relative|[Bool](/API_docs/types/Bool.html) | Optional|
|short\_time|[Bool](/API_docs/types/Bool.html) | Optional|
|long\_time|[Bool](/API_docs/types/Bool.html) | Optional|
|short\_date|[Bool](/API_docs/types/Bool.html) | Optional|
|long\_date|[Bool](/API_docs/types/Bool.html) | Optional|
|day\_of\_week|[Bool](/API_docs/types/Bool.html) | Optional|
|text|[RichText](/API_docs/types/RichText.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|



### Type: [RichText](/API_docs/types/RichText.html)


### Example:

```
$textDate = ['_' => 'textDate', 'relative' => Bool, 'short_time' => Bool, 'long_time' => Bool, 'short_date' => Bool, 'long_date' => Bool, 'day_of_week' => Bool, 'text' => RichText, 'date' => int];
```
