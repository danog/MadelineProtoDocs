---
title: "danog\\MadelineProto\\Test\\EntitiesTest: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Test\EntitiesTest`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Method list:
* [`testMb(): void`](#testmb-void)
* [`testEntities(string $mode, string $html, string $bare, array $entities, ?string $htmlReverse = NULL): void`](#testentities-string-mode-string-html-string-bare-array-entities-string-htmlreverse-null-void)
* [`provideEntities(): array`](#provideentities-array)
* [`setUpBeforeClass(): void`](#setupbeforeclass-void)
* [`tearDownAfterClass(): void`](#teardownafterclass-void)
* [`any(): \PHPUnit\Framework\MockObject\Rule\AnyInvokedCount`](#any-phpunit-framework-mockobject-rule-anyinvokedcount)
* [`never(): \PHPUnit\Framework\MockObject\Rule\InvokedCount`](#never-phpunit-framework-mockobject-rule-invokedcount)
* [`atLeast(int $requiredInvocations): \PHPUnit\Framework\MockObject\Rule\InvokedAtLeastCount`](#atleast-int-requiredinvocations-phpunit-framework-mockobject-rule-invokedatleastcount)
* [`atLeastOnce(): \PHPUnit\Framework\MockObject\Rule\InvokedAtLeastOnce`](#atleastonce-phpunit-framework-mockobject-rule-invokedatleastonce)
* [`once(): \PHPUnit\Framework\MockObject\Rule\InvokedCount`](#once-phpunit-framework-mockobject-rule-invokedcount)
* [`exactly(int $count): \PHPUnit\Framework\MockObject\Rule\InvokedCount`](#exactly-int-count-phpunit-framework-mockobject-rule-invokedcount)
* [`atMost(int $allowedInvocations): \PHPUnit\Framework\MockObject\Rule\InvokedAtMostCount`](#atmost-int-allowedinvocations-phpunit-framework-mockobject-rule-invokedatmostcount)
* [`returnValue(mixed $value): \PHPUnit\Framework\MockObject\Stub\ReturnStub`](#returnvalue-mixed-value-phpunit-framework-mockobject-stub-returnstub)
* [`returnValueMap(array $valueMap): \PHPUnit\Framework\MockObject\Stub\ReturnValueMap`](#returnvaluemap-array-valuemap-phpunit-framework-mockobject-stub-returnvaluemap)
* [`returnArgument(int $argumentIndex): \PHPUnit\Framework\MockObject\Stub\ReturnArgument`](#returnargument-int-argumentindex-phpunit-framework-mockobject-stub-returnargument)
* [`returnCallback(mixed $callback): \PHPUnit\Framework\MockObject\Stub\ReturnCallback`](#returncallback-mixed-callback-phpunit-framework-mockobject-stub-returncallback)
* [`returnSelf(): \PHPUnit\Framework\MockObject\Stub\ReturnSelf`](#returnself-phpunit-framework-mockobject-stub-returnself)
* [`throwException(\Throwable $exception): \PHPUnit\Framework\MockObject\Stub\Exception`](#throwexception-throwable-exception-phpunit-framework-mockobject-stub-exception)
* [`onConsecutiveCalls(mixed ...$args): \PHPUnit\Framework\MockObject\Stub\ConsecutiveCalls`](#onconsecutivecalls-mixed-args-phpunit-framework-mockobject-stub-consecutivecalls)
* [`toString(): string`](#tostring-string)
* [`count(): int`](#count-int)
* [`getActualOutputForAssertion(): string`](#getactualoutputforassertion-string)
* [`expectOutputRegex(string $expectedRegex): void`](#expectoutputregex-string-expectedregex-void)
* [`expectOutputString(string $expectedString): void`](#expectoutputstring-string-expectedstring-void)
* [`expectException(string $exception): void`](#expectexception-string-exception-void)
* [`expectExceptionCode(int|string $code): void`](#expectexceptioncode-int-string-code-void)
* [`expectExceptionMessage(string $message): void`](#expectexceptionmessage-string-message-void)
* [`expectExceptionMessageMatches(string $regularExpression): void`](#expectexceptionmessagematches-string-regularexpression-void)
* [`expectExceptionObject(\Exception $exception): void`](#expectexceptionobject-exception-exception-void)
* [`expectNotToPerformAssertions(): void`](#expectnottoperformassertions-void)
* [`getStatus(): int`](#getstatus-int)
* [`markAsRisky(): void`](#markasrisky-void)
* [`getStatusMessage(): string`](#getstatusmessage-string)
* [`hasFailed(): bool`](#hasfailed-bool)
* [`run(?\PHPUnit\Framework\TestResult $result = NULL): \PHPUnit\Framework\TestResult`](#run-phpunit-framework-testresult-result-null-phpunit-framework-testresult)
* [`getMockBuilder(string $className): \PHPUnit\Framework\MockObject\MockBuilder`](#getmockbuilder-string-classname-phpunit-framework-mockobject-mockbuilder)
* [`registerComparator(\SebastianBergmann\Comparator\Comparator $comparator): void`](#registercomparator-sebastianbergmann-comparator-comparator-comparator-void)
* [`sortId(): string`](#sortid-string)
* [`provides(): list<\ExecutionOrderDependency>`](#provides-list-executionorderdependency)
* [`requires(): list<\ExecutionOrderDependency>`](#requires-list-executionorderdependency)
* [`assertArrayHasKey(int|string $key, array|\ArrayAccess $array, string $message = ''): void`](#assertarrayhaskey-int-string-key-array-arrayaccess-array-string-message-void)
* [`assertArrayNotHasKey(int|string $key, array|\ArrayAccess $array, string $message = ''): void`](#assertarraynothaskey-int-string-key-array-arrayaccess-array-string-message-void)
* [`assertContains(mixed $needle, iterable $haystack, string $message = ''): void`](#assertcontains-mixed-needle-iterable-haystack-string-message-void)
* [`assertContainsEquals(mixed $needle, iterable $haystack, string $message = ''): void`](#assertcontainsequals-mixed-needle-iterable-haystack-string-message-void)
* [`assertNotContains(mixed $needle, iterable $haystack, string $message = ''): void`](#assertnotcontains-mixed-needle-iterable-haystack-string-message-void)
* [`assertNotContainsEquals(mixed $needle, iterable $haystack, string $message = ''): void`](#assertnotcontainsequals-mixed-needle-iterable-haystack-string-message-void)
* [`assertContainsOnly(string $type, iterable $haystack, ?bool $isNativeType = NULL, string $message = ''): void`](#assertcontainsonly-string-type-iterable-haystack-bool-isnativetype-null-string-message-void)
* [`assertContainsOnlyInstancesOf(string $className, iterable $haystack, string $message = ''): void`](#assertcontainsonlyinstancesof-string-classname-iterable-haystack-string-message-void)
* [`assertNotContainsOnly(string $type, iterable $haystack, ?bool $isNativeType = NULL, string $message = ''): void`](#assertnotcontainsonly-string-type-iterable-haystack-bool-isnativetype-null-string-message-void)
* [`assertCount(int $expectedCount, \Countable|iterable $haystack, string $message = ''): void`](#assertcount-int-expectedcount-countable-iterable-haystack-string-message-void)
* [`assertNotCount(int $expectedCount, \Countable|iterable $haystack, string $message = ''): void`](#assertnotcount-int-expectedcount-countable-iterable-haystack-string-message-void)
* [`assertEquals(mixed $expected, mixed $actual, string $message = ''): void`](#assertequals-mixed-expected-mixed-actual-string-message-void)
* [`assertEqualsCanonicalizing(mixed $expected, mixed $actual, string $message = ''): void`](#assertequalscanonicalizing-mixed-expected-mixed-actual-string-message-void)
* [`assertEqualsIgnoringCase(mixed $expected, mixed $actual, string $message = ''): void`](#assertequalsignoringcase-mixed-expected-mixed-actual-string-message-void)
* [`assertEqualsWithDelta(mixed $expected, mixed $actual, float $delta, string $message = ''): void`](#assertequalswithdelta-mixed-expected-mixed-actual-float-delta-string-message-void)
* [`assertNotEquals(mixed $expected, mixed $actual, string $message = ''): void`](#assertnotequals-mixed-expected-mixed-actual-string-message-void)
* [`assertNotEqualsCanonicalizing(mixed $expected, mixed $actual, string $message = ''): void`](#assertnotequalscanonicalizing-mixed-expected-mixed-actual-string-message-void)
* [`assertNotEqualsIgnoringCase(mixed $expected, mixed $actual, string $message = ''): void`](#assertnotequalsignoringcase-mixed-expected-mixed-actual-string-message-void)
* [`assertNotEqualsWithDelta(mixed $expected, mixed $actual, float $delta, string $message = ''): void`](#assertnotequalswithdelta-mixed-expected-mixed-actual-float-delta-string-message-void)
* [`assertObjectEquals(object $expected, object $actual, string $method = 'equals', string $message = ''): void`](#assertobjectequals-object-expected-object-actual-string-method-equals-string-message-void)
* [`assertEmpty(mixed $actual, string $message = ''): void`](#assertempty-mixed-actual-string-message-void)
* [`assertNotEmpty(mixed $actual, string $message = ''): void`](#assertnotempty-mixed-actual-string-message-void)
* [`assertGreaterThan(mixed $expected, mixed $actual, string $message = ''): void`](#assertgreaterthan-mixed-expected-mixed-actual-string-message-void)
* [`assertGreaterThanOrEqual(mixed $expected, mixed $actual, string $message = ''): void`](#assertgreaterthanorequal-mixed-expected-mixed-actual-string-message-void)
* [`assertLessThan(mixed $expected, mixed $actual, string $message = ''): void`](#assertlessthan-mixed-expected-mixed-actual-string-message-void)
* [`assertLessThanOrEqual(mixed $expected, mixed $actual, string $message = ''): void`](#assertlessthanorequal-mixed-expected-mixed-actual-string-message-void)
* [`assertFileEquals(string $expected, string $actual, string $message = ''): void`](#assertfileequals-string-expected-string-actual-string-message-void)
* [`assertFileEqualsCanonicalizing(string $expected, string $actual, string $message = ''): void`](#assertfileequalscanonicalizing-string-expected-string-actual-string-message-void)
* [`assertFileEqualsIgnoringCase(string $expected, string $actual, string $message = ''): void`](#assertfileequalsignoringcase-string-expected-string-actual-string-message-void)
* [`assertFileNotEquals(string $expected, string $actual, string $message = ''): void`](#assertfilenotequals-string-expected-string-actual-string-message-void)
* [`assertFileNotEqualsCanonicalizing(string $expected, string $actual, string $message = ''): void`](#assertfilenotequalscanonicalizing-string-expected-string-actual-string-message-void)
* [`assertFileNotEqualsIgnoringCase(string $expected, string $actual, string $message = ''): void`](#assertfilenotequalsignoringcase-string-expected-string-actual-string-message-void)
* [`assertStringEqualsFile(string $expectedFile, string $actualString, string $message = ''): void`](#assertstringequalsfile-string-expectedfile-string-actualstring-string-message-void)
* [`assertStringEqualsFileCanonicalizing(string $expectedFile, string $actualString, string $message = ''): void`](#assertstringequalsfilecanonicalizing-string-expectedfile-string-actualstring-string-message-void)
* [`assertStringEqualsFileIgnoringCase(string $expectedFile, string $actualString, string $message = ''): void`](#assertstringequalsfileignoringcase-string-expectedfile-string-actualstring-string-message-void)
* [`assertStringNotEqualsFile(string $expectedFile, string $actualString, string $message = ''): void`](#assertstringnotequalsfile-string-expectedfile-string-actualstring-string-message-void)
* [`assertStringNotEqualsFileCanonicalizing(string $expectedFile, string $actualString, string $message = ''): void`](#assertstringnotequalsfilecanonicalizing-string-expectedfile-string-actualstring-string-message-void)
* [`assertStringNotEqualsFileIgnoringCase(string $expectedFile, string $actualString, string $message = ''): void`](#assertstringnotequalsfileignoringcase-string-expectedfile-string-actualstring-string-message-void)
* [`assertIsReadable(string $filename, string $message = ''): void`](#assertisreadable-string-filename-string-message-void)
* [`assertIsNotReadable(string $filename, string $message = ''): void`](#assertisnotreadable-string-filename-string-message-void)
* [`assertIsWritable(string $filename, string $message = ''): void`](#assertiswritable-string-filename-string-message-void)
* [`assertIsNotWritable(string $filename, string $message = ''): void`](#assertisnotwritable-string-filename-string-message-void)
* [`assertDirectoryExists(string $directory, string $message = ''): void`](#assertdirectoryexists-string-directory-string-message-void)
* [`assertDirectoryDoesNotExist(string $directory, string $message = ''): void`](#assertdirectorydoesnotexist-string-directory-string-message-void)
* [`assertDirectoryIsReadable(string $directory, string $message = ''): void`](#assertdirectoryisreadable-string-directory-string-message-void)
* [`assertDirectoryIsNotReadable(string $directory, string $message = ''): void`](#assertdirectoryisnotreadable-string-directory-string-message-void)
* [`assertDirectoryIsWritable(string $directory, string $message = ''): void`](#assertdirectoryiswritable-string-directory-string-message-void)
* [`assertDirectoryIsNotWritable(string $directory, string $message = ''): void`](#assertdirectoryisnotwritable-string-directory-string-message-void)
* [`assertFileExists(string $filename, string $message = ''): void`](#assertfileexists-string-filename-string-message-void)
* [`assertFileDoesNotExist(string $filename, string $message = ''): void`](#assertfiledoesnotexist-string-filename-string-message-void)
* [`assertFileIsReadable(string $file, string $message = ''): void`](#assertfileisreadable-string-file-string-message-void)
* [`assertFileIsNotReadable(string $file, string $message = ''): void`](#assertfileisnotreadable-string-file-string-message-void)
* [`assertFileIsWritable(string $file, string $message = ''): void`](#assertfileiswritable-string-file-string-message-void)
* [`assertFileIsNotWritable(string $file, string $message = ''): void`](#assertfileisnotwritable-string-file-string-message-void)
* [`assertTrue(mixed $condition, string $message = ''): void`](#asserttrue-mixed-condition-string-message-void)
* [`assertNotTrue(mixed $condition, string $message = ''): void`](#assertnottrue-mixed-condition-string-message-void)
* [`assertFalse(mixed $condition, string $message = ''): void`](#assertfalse-mixed-condition-string-message-void)
* [`assertNotFalse(mixed $condition, string $message = ''): void`](#assertnotfalse-mixed-condition-string-message-void)
* [`assertNull(mixed $actual, string $message = ''): void`](#assertnull-mixed-actual-string-message-void)
* [`assertNotNull(mixed $actual, string $message = ''): void`](#assertnotnull-mixed-actual-string-message-void)
* [`assertFinite(mixed $actual, string $message = ''): void`](#assertfinite-mixed-actual-string-message-void)
* [`assertInfinite(mixed $actual, string $message = ''): void`](#assertinfinite-mixed-actual-string-message-void)
* [`assertNan(mixed $actual, string $message = ''): void`](#assertnan-mixed-actual-string-message-void)
* [`assertSame(mixed $expected, mixed $actual, string $message = ''): void`](#assertsame-mixed-expected-mixed-actual-string-message-void)
* [`assertNotSame(mixed $expected, mixed $actual, string $message = ''): void`](#assertnotsame-mixed-expected-mixed-actual-string-message-void)
* [`assertInstanceOf(string $expected, mixed $actual, string $message = ''): void`](#assertinstanceof-string-expected-mixed-actual-string-message-void)
* [`assertNotInstanceOf(string $expected, mixed $actual, string $message = ''): void`](#assertnotinstanceof-string-expected-mixed-actual-string-message-void)
* [`assertIsArray(mixed $actual, string $message = ''): void`](#assertisarray-mixed-actual-string-message-void)
* [`assertIsBool(mixed $actual, string $message = ''): void`](#assertisbool-mixed-actual-string-message-void)
* [`assertIsFloat(mixed $actual, string $message = ''): void`](#assertisfloat-mixed-actual-string-message-void)
* [`assertIsInt(mixed $actual, string $message = ''): void`](#assertisint-mixed-actual-string-message-void)
* [`assertIsNumeric(mixed $actual, string $message = ''): void`](#assertisnumeric-mixed-actual-string-message-void)
* [`assertIsObject(mixed $actual, string $message = ''): void`](#assertisobject-mixed-actual-string-message-void)
* [`assertIsResource(mixed $actual, string $message = ''): void`](#assertisresource-mixed-actual-string-message-void)
* [`assertIsClosedResource(mixed $actual, string $message = ''): void`](#assertisclosedresource-mixed-actual-string-message-void)
* [`assertIsString(mixed $actual, string $message = ''): void`](#assertisstring-mixed-actual-string-message-void)
* [`assertIsScalar(mixed $actual, string $message = ''): void`](#assertisscalar-mixed-actual-string-message-void)
* [`assertIsCallable(mixed $actual, string $message = ''): void`](#assertiscallable-mixed-actual-string-message-void)
* [`assertIsIterable(mixed $actual, string $message = ''): void`](#assertisiterable-mixed-actual-string-message-void)
* [`assertIsNotArray(mixed $actual, string $message = ''): void`](#assertisnotarray-mixed-actual-string-message-void)
* [`assertIsNotBool(mixed $actual, string $message = ''): void`](#assertisnotbool-mixed-actual-string-message-void)
* [`assertIsNotFloat(mixed $actual, string $message = ''): void`](#assertisnotfloat-mixed-actual-string-message-void)
* [`assertIsNotInt(mixed $actual, string $message = ''): void`](#assertisnotint-mixed-actual-string-message-void)
* [`assertIsNotNumeric(mixed $actual, string $message = ''): void`](#assertisnotnumeric-mixed-actual-string-message-void)
* [`assertIsNotObject(mixed $actual, string $message = ''): void`](#assertisnotobject-mixed-actual-string-message-void)
* [`assertIsNotResource(mixed $actual, string $message = ''): void`](#assertisnotresource-mixed-actual-string-message-void)
* [`assertIsNotClosedResource(mixed $actual, string $message = ''): void`](#assertisnotclosedresource-mixed-actual-string-message-void)
* [`assertIsNotString(mixed $actual, string $message = ''): void`](#assertisnotstring-mixed-actual-string-message-void)
* [`assertIsNotScalar(mixed $actual, string $message = ''): void`](#assertisnotscalar-mixed-actual-string-message-void)
* [`assertIsNotCallable(mixed $actual, string $message = ''): void`](#assertisnotcallable-mixed-actual-string-message-void)
* [`assertIsNotIterable(mixed $actual, string $message = ''): void`](#assertisnotiterable-mixed-actual-string-message-void)
* [`assertMatchesRegularExpression(string $pattern, string $string, string $message = ''): void`](#assertmatchesregularexpression-string-pattern-string-string-string-message-void)
* [`assertDoesNotMatchRegularExpression(string $pattern, string $string, string $message = ''): void`](#assertdoesnotmatchregularexpression-string-pattern-string-string-string-message-void)
* [`assertSameSize(\Countable|iterable $expected, \Countable|iterable $actual, string $message = ''): void`](#assertsamesize-countable-iterable-expected-countable-iterable-actual-string-message-void)
* [`assertNotSameSize(\Countable|iterable $expected, \Countable|iterable $actual, string $message = ''): void`](#assertnotsamesize-countable-iterable-expected-countable-iterable-actual-string-message-void)
* [`assertStringMatchesFormat(string $format, string $string, string $message = ''): void`](#assertstringmatchesformat-string-format-string-string-string-message-void)
* [`assertStringNotMatchesFormat(string $format, string $string, string $message = ''): void`](#assertstringnotmatchesformat-string-format-string-string-string-message-void)
* [`assertStringMatchesFormatFile(string $formatFile, string $string, string $message = ''): void`](#assertstringmatchesformatfile-string-formatfile-string-string-string-message-void)
* [`assertStringNotMatchesFormatFile(string $formatFile, string $string, string $message = ''): void`](#assertstringnotmatchesformatfile-string-formatfile-string-string-string-message-void)
* [`assertStringStartsWith(string $prefix, string $string, string $message = ''): void`](#assertstringstartswith-string-prefix-string-string-string-message-void)
* [`assertStringStartsNotWith(string $prefix, string $string, string $message = ''): void`](#assertstringstartsnotwith-string-prefix-string-string-string-message-void)
* [`assertStringContainsString(string $needle, string $haystack, string $message = ''): void`](#assertstringcontainsstring-string-needle-string-haystack-string-message-void)
* [`assertStringContainsStringIgnoringCase(string $needle, string $haystack, string $message = ''): void`](#assertstringcontainsstringignoringcase-string-needle-string-haystack-string-message-void)
* [`assertStringNotContainsString(string $needle, string $haystack, string $message = ''): void`](#assertstringnotcontainsstring-string-needle-string-haystack-string-message-void)
* [`assertStringNotContainsStringIgnoringCase(string $needle, string $haystack, string $message = ''): void`](#assertstringnotcontainsstringignoringcase-string-needle-string-haystack-string-message-void)
* [`assertStringEndsWith(string $suffix, string $string, string $message = ''): void`](#assertstringendswith-string-suffix-string-string-string-message-void)
* [`assertStringEndsNotWith(string $suffix, string $string, string $message = ''): void`](#assertstringendsnotwith-string-suffix-string-string-string-message-void)
* [`assertXmlFileEqualsXmlFile(string $expectedFile, string $actualFile, string $message = ''): void`](#assertxmlfileequalsxmlfile-string-expectedfile-string-actualfile-string-message-void)
* [`assertXmlFileNotEqualsXmlFile(string $expectedFile, string $actualFile, string $message = ''): void`](#assertxmlfilenotequalsxmlfile-string-expectedfile-string-actualfile-string-message-void)
* [`assertXmlStringEqualsXmlFile(string $expectedFile, \DOMDocument|string $actualXml, string $message = ''): void`](#assertxmlstringequalsxmlfile-string-expectedfile-domdocument-string-actualxml-string-message-void)
* [`assertXmlStringNotEqualsXmlFile(string $expectedFile, \DOMDocument|string $actualXml, string $message = ''): void`](#assertxmlstringnotequalsxmlfile-string-expectedfile-domdocument-string-actualxml-string-message-void)
* [`assertXmlStringEqualsXmlString(\DOMDocument|string $expectedXml, \DOMDocument|string $actualXml, string $message = ''): void`](#assertxmlstringequalsxmlstring-domdocument-string-expectedxml-domdocument-string-actualxml-string-message-void)
* [`assertXmlStringNotEqualsXmlString(\DOMDocument|string $expectedXml, \DOMDocument|string $actualXml, string $message = ''): void`](#assertxmlstringnotequalsxmlstring-domdocument-string-expectedxml-domdocument-string-actualxml-string-message-void)
* [`assertThat(mixed $value, \PHPUnit\Framework\Constraint\Constraint $constraint, string $message = ''): void`](#assertthat-mixed-value-phpunit-framework-constraint-constraint-constraint-string-message-void)
* [`assertJson(string $actualJson, string $message = ''): void`](#assertjson-string-actualjson-string-message-void)
* [`assertJsonStringEqualsJsonString(string $expectedJson, string $actualJson, string $message = ''): void`](#assertjsonstringequalsjsonstring-string-expectedjson-string-actualjson-string-message-void)
* [`assertJsonStringNotEqualsJsonString(string $expectedJson, string $actualJson, string $message = ''): void`](#assertjsonstringnotequalsjsonstring-string-expectedjson-string-actualjson-string-message-void)
* [`assertJsonStringEqualsJsonFile(string $expectedFile, string $actualJson, string $message = ''): void`](#assertjsonstringequalsjsonfile-string-expectedfile-string-actualjson-string-message-void)
* [`assertJsonStringNotEqualsJsonFile(string $expectedFile, string $actualJson, string $message = ''): void`](#assertjsonstringnotequalsjsonfile-string-expectedfile-string-actualjson-string-message-void)
* [`assertJsonFileEqualsJsonFile(string $expectedFile, string $actualFile, string $message = ''): void`](#assertjsonfileequalsjsonfile-string-expectedfile-string-actualfile-string-message-void)
* [`assertJsonFileNotEqualsJsonFile(string $expectedFile, string $actualFile, string $message = ''): void`](#assertjsonfilenotequalsjsonfile-string-expectedfile-string-actualfile-string-message-void)
* [`logicalAnd(): \PHPUnit\Framework\Constraint\LogicalAnd`](#logicaland-phpunit-framework-constraint-logicaland)
* [`logicalOr(): \PHPUnit\Framework\Constraint\LogicalOr`](#logicalor-phpunit-framework-constraint-logicalor)
* [`logicalNot(\PHPUnit\Framework\Constraint\Constraint $constraint): \PHPUnit\Framework\Constraint\LogicalNot`](#logicalnot-phpunit-framework-constraint-constraint-constraint-phpunit-framework-constraint-logicalnot)
* [`logicalXor(): \PHPUnit\Framework\Constraint\LogicalXor`](#logicalxor-phpunit-framework-constraint-logicalxor)
* [`anything(): \PHPUnit\Framework\Constraint\IsAnything`](#anything-phpunit-framework-constraint-isanything)
* [`isTrue(): \PHPUnit\Framework\Constraint\IsTrue`](#istrue-phpunit-framework-constraint-istrue)
* [`callback(callable $callback): \PHPUnit\Framework\Constraint\Callback`](#callback-callable-callback-phpunit-framework-constraint-callback)
* [`isFalse(): \PHPUnit\Framework\Constraint\IsFalse`](#isfalse-phpunit-framework-constraint-isfalse)
* [`isJson(): \PHPUnit\Framework\Constraint\IsJson`](#isjson-phpunit-framework-constraint-isjson)
* [`isNull(): \PHPUnit\Framework\Constraint\IsNull`](#isnull-phpunit-framework-constraint-isnull)
* [`isFinite(): \PHPUnit\Framework\Constraint\IsFinite`](#isfinite-phpunit-framework-constraint-isfinite)
* [`isInfinite(): \PHPUnit\Framework\Constraint\IsInfinite`](#isinfinite-phpunit-framework-constraint-isinfinite)
* [`isNan(): \PHPUnit\Framework\Constraint\IsNan`](#isnan-phpunit-framework-constraint-isnan)
* [`containsEqual(mixed $value): \PHPUnit\Framework\Constraint\TraversableContainsEqual`](#containsequal-mixed-value-phpunit-framework-constraint-traversablecontainsequal)
* [`containsIdentical(mixed $value): \PHPUnit\Framework\Constraint\TraversableContainsIdentical`](#containsidentical-mixed-value-phpunit-framework-constraint-traversablecontainsidentical)
* [`containsOnly(string $type): \PHPUnit\Framework\Constraint\TraversableContainsOnly`](#containsonly-string-type-phpunit-framework-constraint-traversablecontainsonly)
* [`containsOnlyInstancesOf(string $className): \PHPUnit\Framework\Constraint\TraversableContainsOnly`](#containsonlyinstancesof-string-classname-phpunit-framework-constraint-traversablecontainsonly)
* [`arrayHasKey(int|string $key): \PHPUnit\Framework\Constraint\ArrayHasKey`](#arrayhaskey-int-string-key-phpunit-framework-constraint-arrayhaskey)
* [`equalTo(mixed $value): \PHPUnit\Framework\Constraint\IsEqual`](#equalto-mixed-value-phpunit-framework-constraint-isequal)
* [`equalToCanonicalizing(mixed $value): \PHPUnit\Framework\Constraint\IsEqualCanonicalizing`](#equaltocanonicalizing-mixed-value-phpunit-framework-constraint-isequalcanonicalizing)
* [`equalToIgnoringCase(mixed $value): \PHPUnit\Framework\Constraint\IsEqualIgnoringCase`](#equaltoignoringcase-mixed-value-phpunit-framework-constraint-isequalignoringcase)
* [`equalToWithDelta(mixed $value, float $delta): \PHPUnit\Framework\Constraint\IsEqualWithDelta`](#equaltowithdelta-mixed-value-float-delta-phpunit-framework-constraint-isequalwithdelta)
* [`isEmpty(): \PHPUnit\Framework\Constraint\IsEmpty`](#isempty-phpunit-framework-constraint-isempty)
* [`isWritable(): \PHPUnit\Framework\Constraint\IsWritable`](#iswritable-phpunit-framework-constraint-iswritable)
* [`isReadable(): \PHPUnit\Framework\Constraint\IsReadable`](#isreadable-phpunit-framework-constraint-isreadable)
* [`directoryExists(): \PHPUnit\Framework\Constraint\DirectoryExists`](#directoryexists-phpunit-framework-constraint-directoryexists)
* [`fileExists(): \PHPUnit\Framework\Constraint\FileExists`](#fileexists-phpunit-framework-constraint-fileexists)
* [`greaterThan(mixed $value): \PHPUnit\Framework\Constraint\GreaterThan`](#greaterthan-mixed-value-phpunit-framework-constraint-greaterthan)
* [`greaterThanOrEqual(mixed $value): \PHPUnit\Framework\Constraint\LogicalOr`](#greaterthanorequal-mixed-value-phpunit-framework-constraint-logicalor)
* [`identicalTo(mixed $value): \PHPUnit\Framework\Constraint\IsIdentical`](#identicalto-mixed-value-phpunit-framework-constraint-isidentical)
* [`isInstanceOf(string $className): \PHPUnit\Framework\Constraint\IsInstanceOf`](#isinstanceof-string-classname-phpunit-framework-constraint-isinstanceof)
* [`isType(string $type): \PHPUnit\Framework\Constraint\IsType`](#istype-string-type-phpunit-framework-constraint-istype)
* [`lessThan(mixed $value): \PHPUnit\Framework\Constraint\LessThan`](#lessthan-mixed-value-phpunit-framework-constraint-lessthan)
* [`lessThanOrEqual(mixed $value): \PHPUnit\Framework\Constraint\LogicalOr`](#lessthanorequal-mixed-value-phpunit-framework-constraint-logicalor)
* [`matchesRegularExpression(string $pattern): \PHPUnit\Framework\Constraint\RegularExpression`](#matchesregularexpression-string-pattern-phpunit-framework-constraint-regularexpression)
* [`matches(string $string): \PHPUnit\Framework\Constraint\StringMatchesFormatDescription`](#matches-string-string-phpunit-framework-constraint-stringmatchesformatdescription)
* [`stringStartsWith(mixed $prefix): \PHPUnit\Framework\Constraint\StringStartsWith`](#stringstartswith-mixed-prefix-phpunit-framework-constraint-stringstartswith)
* [`stringContains(string $string, bool $case = true): \PHPUnit\Framework\Constraint\StringContains`](#stringcontains-string-string-bool-case-true-phpunit-framework-constraint-stringcontains)
* [`stringEndsWith(string $suffix): \PHPUnit\Framework\Constraint\StringEndsWith`](#stringendswith-string-suffix-phpunit-framework-constraint-stringendswith)
* [`countOf(int $count): \PHPUnit\Framework\Constraint\Count`](#countof-int-count-phpunit-framework-constraint-count)
* [`objectEquals(object $object, string $method = 'equals'): \PHPUnit\Framework\Constraint\ObjectEquals`](#objectequals-object-object-string-method-equals-phpunit-framework-constraint-objectequals)
* [`fail(string $message = ''): void`](#fail-string-message-void)
* [`markTestIncomplete(string $message = ''): void`](#marktestincomplete-string-message-void)
* [`markTestSkipped(string $message = ''): void`](#marktestskipped-string-message-void)
* [`getCount(): int`](#getcount-int)
* [`resetCount(): void`](#resetcount-void)

## Methods:
### `testMb(): void`





### `testEntities(string $mode, string $html, string $bare, array $entities, ?string $htmlReverse = NULL): void`




Parameters:

* `$mode`: `string`   
* `$html`: `string`   
* `$bare`: `string`   
* `$entities`: `array`   
* `$htmlReverse`: `?string`   



### `provideEntities(): array`





### `setUpBeforeClass(): void`

Setup MadelineProto instance.



### `tearDownAfterClass(): void`

Teardown.



### `any(): \PHPUnit\Framework\MockObject\Rule\AnyInvokedCount`

Returns a matcher that matches when the method is executed
zero or more times.


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\AnyInvokedCount`




### `never(): \PHPUnit\Framework\MockObject\Rule\InvokedCount`

Returns a matcher that matches when the method is never executed.


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedCount`




### `atLeast(int $requiredInvocations): \PHPUnit\Framework\MockObject\Rule\InvokedAtLeastCount`

Returns a matcher that matches when the method is executed
at least N times.


Parameters:

* `$requiredInvocations`: `int`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedAtLeastCount`




### `atLeastOnce(): \PHPUnit\Framework\MockObject\Rule\InvokedAtLeastOnce`

Returns a matcher that matches when the method is executed at least once.


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedAtLeastOnce`




### `once(): \PHPUnit\Framework\MockObject\Rule\InvokedCount`

Returns a matcher that matches when the method is executed exactly once.


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedCount`




### `exactly(int $count): \PHPUnit\Framework\MockObject\Rule\InvokedCount`

Returns a matcher that matches when the method is executed
exactly $count times.


Parameters:

* `$count`: `int`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedCount`




### `atMost(int $allowedInvocations): \PHPUnit\Framework\MockObject\Rule\InvokedAtMostCount`

Returns a matcher that matches when the method is executed
at most N times.


Parameters:

* `$allowedInvocations`: `int`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedAtMostCount`




### `returnValue(mixed $value): \PHPUnit\Framework\MockObject\Stub\ReturnStub`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnStub`




### `returnValueMap(array $valueMap): \PHPUnit\Framework\MockObject\Stub\ReturnValueMap`




Parameters:

* `$valueMap`: `array`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnValueMap`




### `returnArgument(int $argumentIndex): \PHPUnit\Framework\MockObject\Stub\ReturnArgument`




Parameters:

* `$argumentIndex`: `int`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnArgument`




### `returnCallback(mixed $callback): \PHPUnit\Framework\MockObject\Stub\ReturnCallback`




Parameters:

* `$callback`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnCallback`




### `returnSelf(): \PHPUnit\Framework\MockObject\Stub\ReturnSelf`

Returns the current object.
This method is useful when mocking a fluent interface.

#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnSelf`




### `throwException(\Throwable $exception): \PHPUnit\Framework\MockObject\Stub\Exception`




Parameters:

* `$exception`: `\Throwable`   


#### See also: 
* `\Throwable`
* `\PHPUnit\Framework\MockObject\Stub\Exception`




### `onConsecutiveCalls(mixed ...$args): \PHPUnit\Framework\MockObject\Stub\ConsecutiveCalls`




Parameters:

* `...$args`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ConsecutiveCalls`




### `toString(): string`

Returns a string representation of the test case.



### `count(): int`





### `getActualOutputForAssertion(): string`





### `expectOutputRegex(string $expectedRegex): void`




Parameters:

* `$expectedRegex`: `string`   



### `expectOutputString(string $expectedString): void`




Parameters:

* `$expectedString`: `string`   



### `expectException(string $exception): void`




Parameters:

* `$exception`: `string`   
  Full type:
  ```
  class-string<\Throwable>
  ```


#### See also: 
* `\Throwable`




### `expectExceptionCode(int|string $code): void`




Parameters:

* `$code`: `int|string`   



### `expectExceptionMessage(string $message): void`




Parameters:

* `$message`: `string`   



### `expectExceptionMessageMatches(string $regularExpression): void`




Parameters:

* `$regularExpression`: `string`   



### `expectExceptionObject(\Exception $exception): void`

Sets up an expectation for an exception to be raised by the code under test.
Information for expected exception class, expected exception message, and  
expected exception code are retrieved from a given Exception object.

Parameters:

* `$exception`: `\Exception`   


#### See also: 
* `\Exception`




### `expectNotToPerformAssertions(): void`





### `getStatus(): int`





### `markAsRisky(): void`





### `getStatusMessage(): string`





### `hasFailed(): bool`





### `run(?\PHPUnit\Framework\TestResult $result = NULL): \PHPUnit\Framework\TestResult`

Runs the test case and collects the results in a TestResult object.
If no TestResult object is passed a new one will be created.

Parameters:

* `$result`: `?\PHPUnit\Framework\TestResult`   


#### See also: 
* `\PHPUnit\Framework\TestResult`




### `getMockBuilder(string $className): \PHPUnit\Framework\MockObject\MockBuilder`

Returns a builder object to create mock objects using a fluent interface.


Parameters:

* `$className`: `string`   
  Full type:
  ```
  class-string<\RealInstanceType>
  ```


Fully typed return value:
```
\MockBuilder<\RealInstanceType>
```
#### See also: 
* `\RealInstanceType`
* `\MockBuilder`
* `\PHPUnit\Framework\MockObject\MockBuilder`




### `registerComparator(\SebastianBergmann\Comparator\Comparator $comparator): void`




Parameters:

* `$comparator`: `\SebastianBergmann\Comparator\Comparator`   


#### See also: 
* `\SebastianBergmann\Comparator\Comparator`




### `sortId(): string`





### `provides(): list<\ExecutionOrderDependency>`

Returns the normalized test name as class::method.


#### See also: 
* `\ExecutionOrderDependency`




### `requires(): list<\ExecutionOrderDependency>`

Returns a list of normalized dependency names, class::method.
This list can differ from the raw dependencies as the resolver has  
no need for the [!][shallow]clone prefix that is filtered out  
during normalization.

#### See also: 
* `\ExecutionOrderDependency`




### `assertArrayHasKey(int|string $key, array|\ArrayAccess $array, string $message = ''): void`

Asserts that an array has a specified key.


Parameters:

* `$key`: `int|string`   
* `$array`: `array|\ArrayAccess`   
* `$message`: `string`   


#### See also: 
* `\ArrayAccess`




### `assertArrayNotHasKey(int|string $key, array|\ArrayAccess $array, string $message = ''): void`

Asserts that an array does not have a specified key.


Parameters:

* `$key`: `int|string`   
* `$array`: `array|\ArrayAccess`   
* `$message`: `string`   


#### See also: 
* `\ArrayAccess`




### `assertContains(mixed $needle, iterable $haystack, string $message = ''): void`

Asserts that a haystack contains a needle.


Parameters:

* `$needle`: `mixed`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### `assertContainsEquals(mixed $needle, iterable $haystack, string $message = ''): void`




Parameters:

* `$needle`: `mixed`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### `assertNotContains(mixed $needle, iterable $haystack, string $message = ''): void`

Asserts that a haystack does not contain a needle.


Parameters:

* `$needle`: `mixed`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### `assertNotContainsEquals(mixed $needle, iterable $haystack, string $message = ''): void`




Parameters:

* `$needle`: `mixed`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### `assertContainsOnly(string $type, iterable $haystack, ?bool $isNativeType = NULL, string $message = ''): void`

Asserts that a haystack contains only values of a given type.


Parameters:

* `$type`: `string`   
* `$haystack`: `iterable`   
* `$isNativeType`: `?bool`   
* `$message`: `string`   



### `assertContainsOnlyInstancesOf(string $className, iterable $haystack, string $message = ''): void`

Asserts that a haystack contains only instances of a given class name.


Parameters:

* `$className`: `string`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### `assertNotContainsOnly(string $type, iterable $haystack, ?bool $isNativeType = NULL, string $message = ''): void`

Asserts that a haystack does not contain only values of a given type.


Parameters:

* `$type`: `string`   
* `$haystack`: `iterable`   
* `$isNativeType`: `?bool`   
* `$message`: `string`   



### `assertCount(int $expectedCount, \Countable|iterable $haystack, string $message = ''): void`

Asserts the number of elements of an array, Countable or Traversable.


Parameters:

* `$expectedCount`: `int`   
* `$haystack`: `\Countable|iterable`   
* `$message`: `string`   


#### See also: 
* `\Countable`




### `assertNotCount(int $expectedCount, \Countable|iterable $haystack, string $message = ''): void`

Asserts the number of elements of an array, Countable or Traversable.


Parameters:

* `$expectedCount`: `int`   
* `$haystack`: `\Countable|iterable`   
* `$message`: `string`   


#### See also: 
* `\Countable`




### `assertEquals(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are equal.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertEqualsCanonicalizing(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are equal (canonicalizing).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertEqualsIgnoringCase(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are equal (ignoring case).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertEqualsWithDelta(mixed $expected, mixed $actual, float $delta, string $message = ''): void`

Asserts that two variables are equal (with delta).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$delta`: `float`   
* `$message`: `string`   



### `assertNotEquals(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are not equal.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertNotEqualsCanonicalizing(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are not equal (canonicalizing).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertNotEqualsIgnoringCase(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are not equal (ignoring case).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertNotEqualsWithDelta(mixed $expected, mixed $actual, float $delta, string $message = ''): void`

Asserts that two variables are not equal (with delta).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$delta`: `float`   
* `$message`: `string`   



### `assertObjectEquals(object $expected, object $actual, string $method = 'equals', string $message = ''): void`




Parameters:

* `$expected`: `object`   
* `$actual`: `object`   
* `$method`: `string`   
* `$message`: `string`   



### `assertEmpty(mixed $actual, string $message = ''): void`

Asserts that a variable is empty.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertNotEmpty(mixed $actual, string $message = ''): void`

Asserts that a variable is not empty.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertGreaterThan(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that a value is greater than another value.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertGreaterThanOrEqual(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that a value is greater than or equal to another value.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertLessThan(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that a value is smaller than another value.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertLessThanOrEqual(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that a value is smaller than or equal to another value.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertFileEquals(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is equal to the contents of another
file.


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### `assertFileEqualsCanonicalizing(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is equal to the contents of another
file (canonicalizing).


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### `assertFileEqualsIgnoringCase(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is equal to the contents of another
file (ignoring case).


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### `assertFileNotEquals(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is not equal to the contents of
another file.


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### `assertFileNotEqualsCanonicalizing(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is not equal to the contents of another
file (canonicalizing).


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### `assertFileNotEqualsIgnoringCase(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is not equal to the contents of another
file (ignoring case).


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### `assertStringEqualsFile(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is equal
to the contents of a file.


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### `assertStringEqualsFileCanonicalizing(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is equal
to the contents of a file (canonicalizing).


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### `assertStringEqualsFileIgnoringCase(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is equal
to the contents of a file (ignoring case).


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### `assertStringNotEqualsFile(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is not equal
to the contents of a file.


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### `assertStringNotEqualsFileCanonicalizing(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is not equal
to the contents of a file (canonicalizing).


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### `assertStringNotEqualsFileIgnoringCase(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is not equal
to the contents of a file (ignoring case).


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### `assertIsReadable(string $filename, string $message = ''): void`

Asserts that a file/dir is readable.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### `assertIsNotReadable(string $filename, string $message = ''): void`

Asserts that a file/dir exists and is not readable.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### `assertIsWritable(string $filename, string $message = ''): void`

Asserts that a file/dir exists and is writable.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### `assertIsNotWritable(string $filename, string $message = ''): void`

Asserts that a file/dir exists and is not writable.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### `assertDirectoryExists(string $directory, string $message = ''): void`

Asserts that a directory exists.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### `assertDirectoryDoesNotExist(string $directory, string $message = ''): void`

Asserts that a directory does not exist.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### `assertDirectoryIsReadable(string $directory, string $message = ''): void`

Asserts that a directory exists and is readable.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### `assertDirectoryIsNotReadable(string $directory, string $message = ''): void`

Asserts that a directory exists and is not readable.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### `assertDirectoryIsWritable(string $directory, string $message = ''): void`

Asserts that a directory exists and is writable.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### `assertDirectoryIsNotWritable(string $directory, string $message = ''): void`

Asserts that a directory exists and is not writable.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### `assertFileExists(string $filename, string $message = ''): void`

Asserts that a file exists.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### `assertFileDoesNotExist(string $filename, string $message = ''): void`

Asserts that a file does not exist.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### `assertFileIsReadable(string $file, string $message = ''): void`

Asserts that a file exists and is readable.


Parameters:

* `$file`: `string`   
* `$message`: `string`   



### `assertFileIsNotReadable(string $file, string $message = ''): void`

Asserts that a file exists and is not readable.


Parameters:

* `$file`: `string`   
* `$message`: `string`   



### `assertFileIsWritable(string $file, string $message = ''): void`

Asserts that a file exists and is writable.


Parameters:

* `$file`: `string`   
* `$message`: `string`   



### `assertFileIsNotWritable(string $file, string $message = ''): void`

Asserts that a file exists and is not writable.


Parameters:

* `$file`: `string`   
* `$message`: `string`   



### `assertTrue(mixed $condition, string $message = ''): void`

Asserts that a condition is true.


Parameters:

* `$condition`: `mixed`   
* `$message`: `string`   



### `assertNotTrue(mixed $condition, string $message = ''): void`

Asserts that a condition is not true.


Parameters:

* `$condition`: `mixed`   
* `$message`: `string`   



### `assertFalse(mixed $condition, string $message = ''): void`

Asserts that a condition is false.


Parameters:

* `$condition`: `mixed`   
* `$message`: `string`   



### `assertNotFalse(mixed $condition, string $message = ''): void`

Asserts that a condition is not false.


Parameters:

* `$condition`: `mixed`   
* `$message`: `string`   



### `assertNull(mixed $actual, string $message = ''): void`

Asserts that a variable is null.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertNotNull(mixed $actual, string $message = ''): void`

Asserts that a variable is not null.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertFinite(mixed $actual, string $message = ''): void`

Asserts that a variable is finite.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertInfinite(mixed $actual, string $message = ''): void`

Asserts that a variable is infinite.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertNan(mixed $actual, string $message = ''): void`

Asserts that a variable is nan.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertSame(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables have the same type and value.
Used on objects, it asserts that two variables reference  
the same object.

Parameters:

* `$expected`: `mixed`   
  Full type:
  ```
  \ExpectedType
  ```
* `$actual`: `mixed`   
* `$message`: `string`   


#### See also: 
* `\ExpectedType`




### `assertNotSame(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables do not have the same type and value.
Used on objects, it asserts that two variables do not reference  
the same object.

Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### `assertInstanceOf(string $expected, mixed $actual, string $message = ''): void`

Asserts that a variable is of a given type.


Parameters:

* `$expected`: `string`   
  Full type:
  ```
  class-string<\ExpectedType>
  ```
* `$actual`: `mixed`   
* `$message`: `string`   


#### See also: 
* `\ExpectedType`




### `assertNotInstanceOf(string $expected, mixed $actual, string $message = ''): void`

Asserts that a variable is not of a given type.


Parameters:

* `$expected`: `string`   
  Full type:
  ```
  class-string<\ExpectedType>
  ```
* `$actual`: `mixed`   
* `$message`: `string`   


#### See also: 
* `\ExpectedType`




### `assertIsArray(mixed $actual, string $message = ''): void`

Asserts that a variable is of type array.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsBool(mixed $actual, string $message = ''): void`

Asserts that a variable is of type bool.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsFloat(mixed $actual, string $message = ''): void`

Asserts that a variable is of type float.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsInt(mixed $actual, string $message = ''): void`

Asserts that a variable is of type int.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNumeric(mixed $actual, string $message = ''): void`

Asserts that a variable is of type numeric.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsObject(mixed $actual, string $message = ''): void`

Asserts that a variable is of type object.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsResource(mixed $actual, string $message = ''): void`

Asserts that a variable is of type resource.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsClosedResource(mixed $actual, string $message = ''): void`

Asserts that a variable is of type resource and is closed.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsString(mixed $actual, string $message = ''): void`

Asserts that a variable is of type string.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsScalar(mixed $actual, string $message = ''): void`

Asserts that a variable is of type scalar.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsCallable(mixed $actual, string $message = ''): void`

Asserts that a variable is of type callable.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsIterable(mixed $actual, string $message = ''): void`

Asserts that a variable is of type iterable.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotArray(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type array.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotBool(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type bool.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotFloat(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type float.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotInt(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type int.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotNumeric(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type numeric.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotObject(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type object.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotResource(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type resource.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotClosedResource(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type resource.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotString(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type string.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotScalar(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type scalar.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotCallable(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type callable.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertIsNotIterable(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type iterable.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### `assertMatchesRegularExpression(string $pattern, string $string, string $message = ''): void`

Asserts that a string matches a given regular expression.


Parameters:

* `$pattern`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertDoesNotMatchRegularExpression(string $pattern, string $string, string $message = ''): void`

Asserts that a string does not match a given regular expression.


Parameters:

* `$pattern`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertSameSize(\Countable|iterable $expected, \Countable|iterable $actual, string $message = ''): void`

Assert that the size of two arrays (or `Countable` or `Traversable` objects)
is the same.


Parameters:

* `$expected`: `\Countable|iterable`   
* `$actual`: `\Countable|iterable`   
* `$message`: `string`   


#### See also: 
* `\Countable`




### `assertNotSameSize(\Countable|iterable $expected, \Countable|iterable $actual, string $message = ''): void`

Assert that the size of two arrays (or `Countable` or `Traversable` objects)
is not the same.


Parameters:

* `$expected`: `\Countable|iterable`   
* `$actual`: `\Countable|iterable`   
* `$message`: `string`   


#### See also: 
* `\Countable`




### `assertStringMatchesFormat(string $format, string $string, string $message = ''): void`

Asserts that a string matches a given format string.


Parameters:

* `$format`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertStringNotMatchesFormat(string $format, string $string, string $message = ''): void`

Asserts that a string does not match a given format string.


Parameters:

* `$format`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertStringMatchesFormatFile(string $formatFile, string $string, string $message = ''): void`

Asserts that a string matches a given format file.


Parameters:

* `$formatFile`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertStringNotMatchesFormatFile(string $formatFile, string $string, string $message = ''): void`

Asserts that a string does not match a given format string.


Parameters:

* `$formatFile`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertStringStartsWith(string $prefix, string $string, string $message = ''): void`

Asserts that a string starts with a given prefix.


Parameters:

* `$prefix`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertStringStartsNotWith(string $prefix, string $string, string $message = ''): void`

Asserts that a string starts not with a given prefix.


Parameters:

* `$prefix`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertStringContainsString(string $needle, string $haystack, string $message = ''): void`




Parameters:

* `$needle`: `string`   
* `$haystack`: `string`   
* `$message`: `string`   



### `assertStringContainsStringIgnoringCase(string $needle, string $haystack, string $message = ''): void`




Parameters:

* `$needle`: `string`   
* `$haystack`: `string`   
* `$message`: `string`   



### `assertStringNotContainsString(string $needle, string $haystack, string $message = ''): void`




Parameters:

* `$needle`: `string`   
* `$haystack`: `string`   
* `$message`: `string`   



### `assertStringNotContainsStringIgnoringCase(string $needle, string $haystack, string $message = ''): void`




Parameters:

* `$needle`: `string`   
* `$haystack`: `string`   
* `$message`: `string`   



### `assertStringEndsWith(string $suffix, string $string, string $message = ''): void`

Asserts that a string ends with a given suffix.


Parameters:

* `$suffix`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertStringEndsNotWith(string $suffix, string $string, string $message = ''): void`

Asserts that a string ends not with a given suffix.


Parameters:

* `$suffix`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### `assertXmlFileEqualsXmlFile(string $expectedFile, string $actualFile, string $message = ''): void`

Asserts that two XML files are equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualFile`: `string`   
* `$message`: `string`   



### `assertXmlFileNotEqualsXmlFile(string $expectedFile, string $actualFile, string $message = ''): void`

Asserts that two XML files are not equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualFile`: `string`   
* `$message`: `string`   



### `assertXmlStringEqualsXmlFile(string $expectedFile, \DOMDocument|string $actualXml, string $message = ''): void`

Asserts that two XML documents are equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualXml`: `\DOMDocument|string`   
* `$message`: `string`   


#### See also: 
* `\DOMDocument`




### `assertXmlStringNotEqualsXmlFile(string $expectedFile, \DOMDocument|string $actualXml, string $message = ''): void`

Asserts that two XML documents are not equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualXml`: `\DOMDocument|string`   
* `$message`: `string`   


#### See also: 
* `\DOMDocument`




### `assertXmlStringEqualsXmlString(\DOMDocument|string $expectedXml, \DOMDocument|string $actualXml, string $message = ''): void`

Asserts that two XML documents are equal.


Parameters:

* `$expectedXml`: `\DOMDocument|string`   
* `$actualXml`: `\DOMDocument|string`   
* `$message`: `string`   


#### See also: 
* `\DOMDocument`




### `assertXmlStringNotEqualsXmlString(\DOMDocument|string $expectedXml, \DOMDocument|string $actualXml, string $message = ''): void`

Asserts that two XML documents are not equal.


Parameters:

* `$expectedXml`: `\DOMDocument|string`   
* `$actualXml`: `\DOMDocument|string`   
* `$message`: `string`   


#### See also: 
* `\DOMDocument`




### `assertThat(mixed $value, \PHPUnit\Framework\Constraint\Constraint $constraint, string $message = ''): void`

Evaluates a PHPUnit\Framework\Constraint matcher object.


Parameters:

* `$value`: `mixed`   
* `$constraint`: `\PHPUnit\Framework\Constraint\Constraint`   
* `$message`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\Constraint`




### `assertJson(string $actualJson, string $message = ''): void`

Asserts that a string is a valid JSON string.


Parameters:

* `$actualJson`: `string`   
* `$message`: `string`   



### `assertJsonStringEqualsJsonString(string $expectedJson, string $actualJson, string $message = ''): void`

Asserts that two given JSON encoded objects or arrays are equal.


Parameters:

* `$expectedJson`: `string`   
* `$actualJson`: `string`   
* `$message`: `string`   



### `assertJsonStringNotEqualsJsonString(string $expectedJson, string $actualJson, string $message = ''): void`

Asserts that two given JSON encoded objects or arrays are not equal.


Parameters:

* `$expectedJson`: `string`   
* `$actualJson`: `string`   
* `$message`: `string`   



### `assertJsonStringEqualsJsonFile(string $expectedFile, string $actualJson, string $message = ''): void`

Asserts that the generated JSON encoded object and the content of the given file are equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualJson`: `string`   
* `$message`: `string`   



### `assertJsonStringNotEqualsJsonFile(string $expectedFile, string $actualJson, string $message = ''): void`

Asserts that the generated JSON encoded object and the content of the given file are not equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualJson`: `string`   
* `$message`: `string`   



### `assertJsonFileEqualsJsonFile(string $expectedFile, string $actualFile, string $message = ''): void`

Asserts that two JSON files are equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualFile`: `string`   
* `$message`: `string`   



### `assertJsonFileNotEqualsJsonFile(string $expectedFile, string $actualFile, string $message = ''): void`

Asserts that two JSON files are not equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualFile`: `string`   
* `$message`: `string`   



### `logicalAnd(): \PHPUnit\Framework\Constraint\LogicalAnd`




#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalAnd`




### `logicalOr(): \PHPUnit\Framework\Constraint\LogicalOr`




#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalOr`




### `logicalNot(\PHPUnit\Framework\Constraint\Constraint $constraint): \PHPUnit\Framework\Constraint\LogicalNot`




Parameters:

* `$constraint`: `\PHPUnit\Framework\Constraint\Constraint`   


#### See also: 
* `\PHPUnit\Framework\Constraint\Constraint`
* `\PHPUnit\Framework\Constraint\LogicalNot`




### `logicalXor(): \PHPUnit\Framework\Constraint\LogicalXor`




#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalXor`




### `anything(): \PHPUnit\Framework\Constraint\IsAnything`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsAnything`




### `isTrue(): \PHPUnit\Framework\Constraint\IsTrue`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsTrue`




### `callback(callable $callback): \PHPUnit\Framework\Constraint\Callback`




Parameters:

* `$callback`: `callable`   
  Full type:
  ```
  callable(\CallbackInput $callback): boo)
  ```


Fully typed return value:
```
\Callback<\CallbackInput>
```
#### See also: 
* `\CallbackInput`
* `\Callback`
* `\PHPUnit\Framework\Constraint\Callback`




### `isFalse(): \PHPUnit\Framework\Constraint\IsFalse`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsFalse`




### `isJson(): \PHPUnit\Framework\Constraint\IsJson`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsJson`




### `isNull(): \PHPUnit\Framework\Constraint\IsNull`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsNull`




### `isFinite(): \PHPUnit\Framework\Constraint\IsFinite`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsFinite`




### `isInfinite(): \PHPUnit\Framework\Constraint\IsInfinite`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsInfinite`




### `isNan(): \PHPUnit\Framework\Constraint\IsNan`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsNan`




### `containsEqual(mixed $value): \PHPUnit\Framework\Constraint\TraversableContainsEqual`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\TraversableContainsEqual`




### `containsIdentical(mixed $value): \PHPUnit\Framework\Constraint\TraversableContainsIdentical`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\TraversableContainsIdentical`




### `containsOnly(string $type): \PHPUnit\Framework\Constraint\TraversableContainsOnly`




Parameters:

* `$type`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\TraversableContainsOnly`




### `containsOnlyInstancesOf(string $className): \PHPUnit\Framework\Constraint\TraversableContainsOnly`




Parameters:

* `$className`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\TraversableContainsOnly`




### `arrayHasKey(int|string $key): \PHPUnit\Framework\Constraint\ArrayHasKey`




Parameters:

* `$key`: `int|string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\ArrayHasKey`




### `equalTo(mixed $value): \PHPUnit\Framework\Constraint\IsEqual`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsEqual`




### `equalToCanonicalizing(mixed $value): \PHPUnit\Framework\Constraint\IsEqualCanonicalizing`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsEqualCanonicalizing`




### `equalToIgnoringCase(mixed $value): \PHPUnit\Framework\Constraint\IsEqualIgnoringCase`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsEqualIgnoringCase`




### `equalToWithDelta(mixed $value, float $delta): \PHPUnit\Framework\Constraint\IsEqualWithDelta`




Parameters:

* `$value`: `mixed`   
* `$delta`: `float`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsEqualWithDelta`




### `isEmpty(): \PHPUnit\Framework\Constraint\IsEmpty`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsEmpty`




### `isWritable(): \PHPUnit\Framework\Constraint\IsWritable`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsWritable`




### `isReadable(): \PHPUnit\Framework\Constraint\IsReadable`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsReadable`




### `directoryExists(): \PHPUnit\Framework\Constraint\DirectoryExists`




#### See also: 
* `\PHPUnit\Framework\Constraint\DirectoryExists`




### `fileExists(): \PHPUnit\Framework\Constraint\FileExists`




#### See also: 
* `\PHPUnit\Framework\Constraint\FileExists`




### `greaterThan(mixed $value): \PHPUnit\Framework\Constraint\GreaterThan`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\GreaterThan`




### `greaterThanOrEqual(mixed $value): \PHPUnit\Framework\Constraint\LogicalOr`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalOr`




### `identicalTo(mixed $value): \PHPUnit\Framework\Constraint\IsIdentical`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsIdentical`




### `isInstanceOf(string $className): \PHPUnit\Framework\Constraint\IsInstanceOf`




Parameters:

* `$className`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsInstanceOf`




### `isType(string $type): \PHPUnit\Framework\Constraint\IsType`




Parameters:

* `$type`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsType`




### `lessThan(mixed $value): \PHPUnit\Framework\Constraint\LessThan`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\LessThan`




### `lessThanOrEqual(mixed $value): \PHPUnit\Framework\Constraint\LogicalOr`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalOr`




### `matchesRegularExpression(string $pattern): \PHPUnit\Framework\Constraint\RegularExpression`




Parameters:

* `$pattern`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\RegularExpression`




### `matches(string $string): \PHPUnit\Framework\Constraint\StringMatchesFormatDescription`




Parameters:

* `$string`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\StringMatchesFormatDescription`




### `stringStartsWith(mixed $prefix): \PHPUnit\Framework\Constraint\StringStartsWith`




Parameters:

* `$prefix`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\StringStartsWith`




### `stringContains(string $string, bool $case = true): \PHPUnit\Framework\Constraint\StringContains`




Parameters:

* `$string`: `string`   
* `$case`: `bool`   


#### See also: 
* `\PHPUnit\Framework\Constraint\StringContains`




### `stringEndsWith(string $suffix): \PHPUnit\Framework\Constraint\StringEndsWith`




Parameters:

* `$suffix`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\StringEndsWith`




### `countOf(int $count): \PHPUnit\Framework\Constraint\Count`




Parameters:

* `$count`: `int`   


#### See also: 
* `\PHPUnit\Framework\Constraint\Count`




### `objectEquals(object $object, string $method = 'equals'): \PHPUnit\Framework\Constraint\ObjectEquals`




Parameters:

* `$object`: `object`   
* `$method`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\ObjectEquals`




### `fail(string $message = ''): void`

Fails a test with the given message.


Parameters:

* `$message`: `string`   


Fully typed return value:
```
\never-return
```

### `markTestIncomplete(string $message = ''): void`

Mark the test as incomplete.


Parameters:

* `$message`: `string`   


Fully typed return value:
```
\never-return
```

### `markTestSkipped(string $message = ''): void`

Mark the test as skipped.


Parameters:

* `$message`: `string`   


Fully typed return value:
```
\never-return
```

### `getCount(): int`

Return the current assertion count.



### `resetCount(): void`

Reset the assertion counter.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
