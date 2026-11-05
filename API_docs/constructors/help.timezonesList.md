# help.timezonesList

> Timezone information that may be used elsewhere in the API, such as to set Telegram Business opening hours ».

[Back to constructors index](/API_docs/constructors/index.html)



Timezone information that may be used elsewhere in the API, such as to set [Telegram Business opening hours »](https://core.telegram.org/api/business#opening-hours).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|timezones|Array of [Timezone](/API_docs/types/Timezone.html) | Yes|Timezones|
|hash|[int](/API_docs/types/int.html) | Yes|



### Type: [help.TimezonesList](/API_docs/types/help.TimezonesList.html)


### Example:

```
$help_timezonesList = ['_' => 'help.timezonesList', 'timezones' => [Timezone, Timezone], 'hash' => int];
```
