# channels.sponsoredMessageReportResultChooseOption

> The user must choose a report option from the localized options available in options, and after selection, channels.reportSponsoredMessage must be invoked again, passing the option's option field to the option param of the method.

[Back to constructors index](/API_docs/constructors/index.html)



The user must choose a report option from the localized options available in `options`, and after selection, [channels.reportSponsoredMessage](../methods/channels.reportSponsoredMessage.html) must be invoked again, passing the option's `option` field to the `option` param of the method.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Title of the option selection popup.|
|options|Array of [SponsoredMessageReportOption](/API_docs/types/SponsoredMessageReportOption.html) | Yes|Localized list of options.|



### Type: [channels.SponsoredMessageReportResult](/API_docs/types/channels.SponsoredMessageReportResult.html)


### Example:

```
$channels_sponsoredMessageReportResultChooseOption = ['_' => 'channels.sponsoredMessageReportResultChooseOption', 'title' => 'string', 'options' => [SponsoredMessageReportOption, SponsoredMessageReportOption]];
```
