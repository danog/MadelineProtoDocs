# smsjobs.eligibleToJoin

> SMS jobs eligibility

[Back to constructors index](/API_docs/constructors/index.html)



SMS jobs eligibility

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|terms\_url|[string](/API_docs/types/string.html) | Yes|Terms of service URL|
|monthly\_sent\_sms|[int](/API_docs/types/int.html) | Yes|Monthly sent SMSes|



### Type: [smsjobs.EligibilityToJoin](/API_docs/types/smsjobs.EligibilityToJoin.html)


### Example:

```
$smsjobs_eligibleToJoin = ['_' => 'smsjobs.eligibleToJoin', 'terms_url' => 'string', 'monthly_sent_sms' => int];
```
