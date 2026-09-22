---
title: "danog\\MadelineProto\\Test\\CallRecorderCodecTest: End-to-end, offline: the video of a Matroska file is packetized into RTP payloads exactly as we"
description: "transmit it, depacketized and reassembled exactly as we receive it, recorded by the pure-PHP\nrecorder, and the resulting file demuxed again — for the codecs that carry their own framing\n(H.265 parameter sets, AV1 OBU size fields).\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Test\CallRecorderCodecTest`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

End-to-end, offline: the video of a Matroska file is packetized into RTP payloads exactly as we  

transmit it, depacketized and reassembled exactly as we receive it, recorded by the pure-PHP
recorder, and the resulting file demuxed again — for the codecs that carry their own framing
(H.265 parameter sets, AV1 OBU size fields).



## Method list:
* [`testHevcRecordsThroughRtp(): void`](#testHevcRecordsThroughRtp)
* [`testAv1RecordsThroughRtp(): void`](#testAv1RecordsThroughRtp)
* [`any(): \PHPUnit\Framework\MockObject\Rule\AnyInvokedCount`](#any)
* [`never(): \PHPUnit\Framework\MockObject\Rule\InvokedCount`](#never)
* [`atLeast(int $requiredInvocations): \PHPUnit\Framework\MockObject\Rule\InvokedAtLeastCount`](#atLeast)
* [`atLeastOnce(): \PHPUnit\Framework\MockObject\Rule\InvokedAtLeastOnce`](#atLeastOnce)
* [`once(): \PHPUnit\Framework\MockObject\Rule\InvokedCount`](#once)
* [`exactly(int $count): \PHPUnit\Framework\MockObject\Rule\InvokedCount`](#exactly)
* [`atMost(int $allowedInvocations): \PHPUnit\Framework\MockObject\Rule\InvokedAtMostCount`](#atMost)
* [`returnValue(mixed $value): \PHPUnit\Framework\MockObject\Stub\ReturnStub`](#returnValue)
* [`returnValueMap(array $valueMap): \PHPUnit\Framework\MockObject\Stub\ReturnValueMap`](#returnValueMap)
* [`returnArgument(int $argumentIndex): \PHPUnit\Framework\MockObject\Stub\ReturnArgument`](#returnArgument)
* [`returnCallback(mixed $callback): \PHPUnit\Framework\MockObject\Stub\ReturnCallback`](#returnCallback)
* [`returnSelf(): \PHPUnit\Framework\MockObject\Stub\ReturnSelf`](#returnSelf)
* [`throwException(Throwable $exception): \PHPUnit\Framework\MockObject\Stub\Exception`](#throwException)
* [`onConsecutiveCalls(mixed ...$args): \PHPUnit\Framework\MockObject\Stub\ConsecutiveCalls`](#onConsecutiveCalls)
* [`setUpBeforeClass(): void`](#setUpBeforeClass)
* [`tearDownAfterClass(): void`](#tearDownAfterClass)
* [`toString(): string`](#toString)
* [`count(): int`](#count)
* [`getActualOutputForAssertion(): string`](#getActualOutputForAssertion)
* [`expectOutputRegex(string $expectedRegex): void`](#expectOutputRegex)
* [`expectOutputString(string $expectedString): void`](#expectOutputString)
* [`expectException(class-string<Throwable> $exception): void`](#expectException)
* [`expectExceptionCode((int|string) $code): void`](#expectExceptionCode)
* [`expectExceptionMessage(string $message): void`](#expectExceptionMessage)
* [`expectExceptionMessageMatches(string $regularExpression): void`](#expectExceptionMessageMatches)
* [`expectExceptionObject(Exception $exception): void`](#expectExceptionObject)
* [`expectNotToPerformAssertions(): void`](#expectNotToPerformAssertions)
* [`getStatus(): int`](#getStatus)
* [`markAsRisky(): void`](#markAsRisky)
* [`getStatusMessage(): string`](#getStatusMessage)
* [`hasFailed(): bool`](#hasFailed)
* [`run(?\PHPUnit\Framework\TestResult $result = NULL): \PHPUnit\Framework\TestResult`](#run)
* [`getMockBuilder(class-string<RealInstanceType> $className): MockBuilder<RealInstanceType>`](#getMockBuilder)
* [`registerComparator(\SebastianBergmann\Comparator\Comparator $comparator): void`](#registerComparator)
* [`sortId(): string`](#sortId)
* [`provides(): list<ExecutionOrderDependency>`](#provides)
* [`requires(): list<ExecutionOrderDependency>`](#requires)
* [`assertArrayHasKey((int|string) $key, (array|ArrayAccess) $array, string $message = ''): void`](#assertArrayHasKey)
* [`assertArrayNotHasKey((int|string) $key, (array|ArrayAccess) $array, string $message = ''): void`](#assertArrayNotHasKey)
* [`assertContains(mixed $needle, iterable $haystack, string $message = ''): void`](#assertContains)
* [`assertContainsEquals(mixed $needle, iterable $haystack, string $message = ''): void`](#assertContainsEquals)
* [`assertNotContains(mixed $needle, iterable $haystack, string $message = ''): void`](#assertNotContains)
* [`assertNotContainsEquals(mixed $needle, iterable $haystack, string $message = ''): void`](#assertNotContainsEquals)
* [`assertContainsOnly(string $type, iterable $haystack, ?bool $isNativeType = NULL, string $message = ''): void`](#assertContainsOnly)
* [`assertContainsOnlyInstancesOf(string $className, iterable $haystack, string $message = ''): void`](#assertContainsOnlyInstancesOf)
* [`assertNotContainsOnly(string $type, iterable $haystack, ?bool $isNativeType = NULL, string $message = ''): void`](#assertNotContainsOnly)
* [`assertCount(int $expectedCount, (Countable|iterable) $haystack, string $message = ''): void`](#assertCount)
* [`assertNotCount(int $expectedCount, (Countable|iterable) $haystack, string $message = ''): void`](#assertNotCount)
* [`assertEquals(mixed $expected, mixed $actual, string $message = ''): void`](#assertEquals)
* [`assertEqualsCanonicalizing(mixed $expected, mixed $actual, string $message = ''): void`](#assertEqualsCanonicalizing)
* [`assertEqualsIgnoringCase(mixed $expected, mixed $actual, string $message = ''): void`](#assertEqualsIgnoringCase)
* [`assertEqualsWithDelta(mixed $expected, mixed $actual, float $delta, string $message = ''): void`](#assertEqualsWithDelta)
* [`assertNotEquals(mixed $expected, mixed $actual, string $message = ''): void`](#assertNotEquals)
* [`assertNotEqualsCanonicalizing(mixed $expected, mixed $actual, string $message = ''): void`](#assertNotEqualsCanonicalizing)
* [`assertNotEqualsIgnoringCase(mixed $expected, mixed $actual, string $message = ''): void`](#assertNotEqualsIgnoringCase)
* [`assertNotEqualsWithDelta(mixed $expected, mixed $actual, float $delta, string $message = ''): void`](#assertNotEqualsWithDelta)
* [`assertObjectEquals(object $expected, object $actual, string $method = 'equals', string $message = ''): void`](#assertObjectEquals)
* [`assertEmpty(mixed $actual, string $message = ''): void`](#assertEmpty)
* [`assertNotEmpty(mixed $actual, string $message = ''): void`](#assertNotEmpty)
* [`assertGreaterThan(mixed $expected, mixed $actual, string $message = ''): void`](#assertGreaterThan)
* [`assertGreaterThanOrEqual(mixed $expected, mixed $actual, string $message = ''): void`](#assertGreaterThanOrEqual)
* [`assertLessThan(mixed $expected, mixed $actual, string $message = ''): void`](#assertLessThan)
* [`assertLessThanOrEqual(mixed $expected, mixed $actual, string $message = ''): void`](#assertLessThanOrEqual)
* [`assertFileEquals(string $expected, string $actual, string $message = ''): void`](#assertFileEquals)
* [`assertFileEqualsCanonicalizing(string $expected, string $actual, string $message = ''): void`](#assertFileEqualsCanonicalizing)
* [`assertFileEqualsIgnoringCase(string $expected, string $actual, string $message = ''): void`](#assertFileEqualsIgnoringCase)
* [`assertFileNotEquals(string $expected, string $actual, string $message = ''): void`](#assertFileNotEquals)
* [`assertFileNotEqualsCanonicalizing(string $expected, string $actual, string $message = ''): void`](#assertFileNotEqualsCanonicalizing)
* [`assertFileNotEqualsIgnoringCase(string $expected, string $actual, string $message = ''): void`](#assertFileNotEqualsIgnoringCase)
* [`assertStringEqualsFile(string $expectedFile, string $actualString, string $message = ''): void`](#assertStringEqualsFile)
* [`assertStringEqualsFileCanonicalizing(string $expectedFile, string $actualString, string $message = ''): void`](#assertStringEqualsFileCanonicalizing)
* [`assertStringEqualsFileIgnoringCase(string $expectedFile, string $actualString, string $message = ''): void`](#assertStringEqualsFileIgnoringCase)
* [`assertStringNotEqualsFile(string $expectedFile, string $actualString, string $message = ''): void`](#assertStringNotEqualsFile)
* [`assertStringNotEqualsFileCanonicalizing(string $expectedFile, string $actualString, string $message = ''): void`](#assertStringNotEqualsFileCanonicalizing)
* [`assertStringNotEqualsFileIgnoringCase(string $expectedFile, string $actualString, string $message = ''): void`](#assertStringNotEqualsFileIgnoringCase)
* [`assertIsReadable(string $filename, string $message = ''): void`](#assertIsReadable)
* [`assertIsNotReadable(string $filename, string $message = ''): void`](#assertIsNotReadable)
* [`assertIsWritable(string $filename, string $message = ''): void`](#assertIsWritable)
* [`assertIsNotWritable(string $filename, string $message = ''): void`](#assertIsNotWritable)
* [`assertDirectoryExists(string $directory, string $message = ''): void`](#assertDirectoryExists)
* [`assertDirectoryDoesNotExist(string $directory, string $message = ''): void`](#assertDirectoryDoesNotExist)
* [`assertDirectoryIsReadable(string $directory, string $message = ''): void`](#assertDirectoryIsReadable)
* [`assertDirectoryIsNotReadable(string $directory, string $message = ''): void`](#assertDirectoryIsNotReadable)
* [`assertDirectoryIsWritable(string $directory, string $message = ''): void`](#assertDirectoryIsWritable)
* [`assertDirectoryIsNotWritable(string $directory, string $message = ''): void`](#assertDirectoryIsNotWritable)
* [`assertFileExists(string $filename, string $message = ''): void`](#assertFileExists)
* [`assertFileDoesNotExist(string $filename, string $message = ''): void`](#assertFileDoesNotExist)
* [`assertFileIsReadable(string $file, string $message = ''): void`](#assertFileIsReadable)
* [`assertFileIsNotReadable(string $file, string $message = ''): void`](#assertFileIsNotReadable)
* [`assertFileIsWritable(string $file, string $message = ''): void`](#assertFileIsWritable)
* [`assertFileIsNotWritable(string $file, string $message = ''): void`](#assertFileIsNotWritable)
* [`assertTrue(mixed $condition, string $message = ''): void`](#assertTrue)
* [`assertNotTrue(mixed $condition, string $message = ''): void`](#assertNotTrue)
* [`assertFalse(mixed $condition, string $message = ''): void`](#assertFalse)
* [`assertNotFalse(mixed $condition, string $message = ''): void`](#assertNotFalse)
* [`assertNull(mixed $actual, string $message = ''): void`](#assertNull)
* [`assertNotNull(mixed $actual, string $message = ''): void`](#assertNotNull)
* [`assertFinite(mixed $actual, string $message = ''): void`](#assertFinite)
* [`assertInfinite(mixed $actual, string $message = ''): void`](#assertInfinite)
* [`assertNan(mixed $actual, string $message = ''): void`](#assertNan)
* [`assertObjectHasProperty(string $propertyName, object $object, string $message = ''): void`](#assertObjectHasProperty)
* [`assertObjectNotHasProperty(string $propertyName, object $object, string $message = ''): void`](#assertObjectNotHasProperty)
* [`assertSame(ExpectedType $expected, mixed $actual, string $message = ''): void`](#assertSame)
* [`assertNotSame(mixed $expected, mixed $actual, string $message = ''): void`](#assertNotSame)
* [`assertInstanceOf(class-string<ExpectedType> $expected, mixed $actual, string $message = ''): void`](#assertInstanceOf)
* [`assertNotInstanceOf(class-string<ExpectedType> $expected, mixed $actual, string $message = ''): void`](#assertNotInstanceOf)
* [`assertIsArray(mixed $actual, string $message = ''): void`](#assertIsArray)
* [`assertIsBool(mixed $actual, string $message = ''): void`](#assertIsBool)
* [`assertIsFloat(mixed $actual, string $message = ''): void`](#assertIsFloat)
* [`assertIsInt(mixed $actual, string $message = ''): void`](#assertIsInt)
* [`assertIsNumeric(mixed $actual, string $message = ''): void`](#assertIsNumeric)
* [`assertIsObject(mixed $actual, string $message = ''): void`](#assertIsObject)
* [`assertIsResource(mixed $actual, string $message = ''): void`](#assertIsResource)
* [`assertIsClosedResource(mixed $actual, string $message = ''): void`](#assertIsClosedResource)
* [`assertIsString(mixed $actual, string $message = ''): void`](#assertIsString)
* [`assertIsScalar(mixed $actual, string $message = ''): void`](#assertIsScalar)
* [`assertIsCallable(mixed $actual, string $message = ''): void`](#assertIsCallable)
* [`assertIsIterable(mixed $actual, string $message = ''): void`](#assertIsIterable)
* [`assertIsNotArray(mixed $actual, string $message = ''): void`](#assertIsNotArray)
* [`assertIsNotBool(mixed $actual, string $message = ''): void`](#assertIsNotBool)
* [`assertIsNotFloat(mixed $actual, string $message = ''): void`](#assertIsNotFloat)
* [`assertIsNotInt(mixed $actual, string $message = ''): void`](#assertIsNotInt)
* [`assertIsNotNumeric(mixed $actual, string $message = ''): void`](#assertIsNotNumeric)
* [`assertIsNotObject(mixed $actual, string $message = ''): void`](#assertIsNotObject)
* [`assertIsNotResource(mixed $actual, string $message = ''): void`](#assertIsNotResource)
* [`assertIsNotClosedResource(mixed $actual, string $message = ''): void`](#assertIsNotClosedResource)
* [`assertIsNotString(mixed $actual, string $message = ''): void`](#assertIsNotString)
* [`assertIsNotScalar(mixed $actual, string $message = ''): void`](#assertIsNotScalar)
* [`assertIsNotCallable(mixed $actual, string $message = ''): void`](#assertIsNotCallable)
* [`assertIsNotIterable(mixed $actual, string $message = ''): void`](#assertIsNotIterable)
* [`assertMatchesRegularExpression(string $pattern, string $string, string $message = ''): void`](#assertMatchesRegularExpression)
* [`assertDoesNotMatchRegularExpression(string $pattern, string $string, string $message = ''): void`](#assertDoesNotMatchRegularExpression)
* [`assertSameSize((Countable|iterable) $expected, (Countable|iterable) $actual, string $message = ''): void`](#assertSameSize)
* [`assertNotSameSize((Countable|iterable) $expected, (Countable|iterable) $actual, string $message = ''): void`](#assertNotSameSize)
* [`assertStringMatchesFormat(string $format, string $string, string $message = ''): void`](#assertStringMatchesFormat)
* [`assertStringNotMatchesFormat(string $format, string $string, string $message = ''): void`](#assertStringNotMatchesFormat)
* [`assertStringMatchesFormatFile(string $formatFile, string $string, string $message = ''): void`](#assertStringMatchesFormatFile)
* [`assertStringNotMatchesFormatFile(string $formatFile, string $string, string $message = ''): void`](#assertStringNotMatchesFormatFile)
* [`assertStringStartsWith(string $prefix, string $string, string $message = ''): void`](#assertStringStartsWith)
* [`assertStringStartsNotWith(string $prefix, string $string, string $message = ''): void`](#assertStringStartsNotWith)
* [`assertStringContainsString(string $needle, string $haystack, string $message = ''): void`](#assertStringContainsString)
* [`assertStringContainsStringIgnoringCase(string $needle, string $haystack, string $message = ''): void`](#assertStringContainsStringIgnoringCase)
* [`assertStringNotContainsString(string $needle, string $haystack, string $message = ''): void`](#assertStringNotContainsString)
* [`assertStringNotContainsStringIgnoringCase(string $needle, string $haystack, string $message = ''): void`](#assertStringNotContainsStringIgnoringCase)
* [`assertStringEndsWith(string $suffix, string $string, string $message = ''): void`](#assertStringEndsWith)
* [`assertStringEndsNotWith(string $suffix, string $string, string $message = ''): void`](#assertStringEndsNotWith)
* [`assertXmlFileEqualsXmlFile(string $expectedFile, string $actualFile, string $message = ''): void`](#assertXmlFileEqualsXmlFile)
* [`assertXmlFileNotEqualsXmlFile(string $expectedFile, string $actualFile, string $message = ''): void`](#assertXmlFileNotEqualsXmlFile)
* [`assertXmlStringEqualsXmlFile(string $expectedFile, (DOMDocument|string) $actualXml, string $message = ''): void`](#assertXmlStringEqualsXmlFile)
* [`assertXmlStringNotEqualsXmlFile(string $expectedFile, (DOMDocument|string) $actualXml, string $message = ''): void`](#assertXmlStringNotEqualsXmlFile)
* [`assertXmlStringEqualsXmlString((DOMDocument|string) $expectedXml, (DOMDocument|string) $actualXml, string $message = ''): void`](#assertXmlStringEqualsXmlString)
* [`assertXmlStringNotEqualsXmlString((DOMDocument|string) $expectedXml, (DOMDocument|string) $actualXml, string $message = ''): void`](#assertXmlStringNotEqualsXmlString)
* [`assertThat(mixed $value, \PHPUnit\Framework\Constraint\Constraint $constraint, string $message = ''): void`](#assertThat)
* [`assertJson(string $actualJson, string $message = ''): void`](#assertJson)
* [`assertJsonStringEqualsJsonString(string $expectedJson, string $actualJson, string $message = ''): void`](#assertJsonStringEqualsJsonString)
* [`assertJsonStringNotEqualsJsonString(string $expectedJson, string $actualJson, string $message = ''): void`](#assertJsonStringNotEqualsJsonString)
* [`assertJsonStringEqualsJsonFile(string $expectedFile, string $actualJson, string $message = ''): void`](#assertJsonStringEqualsJsonFile)
* [`assertJsonStringNotEqualsJsonFile(string $expectedFile, string $actualJson, string $message = ''): void`](#assertJsonStringNotEqualsJsonFile)
* [`assertJsonFileEqualsJsonFile(string $expectedFile, string $actualFile, string $message = ''): void`](#assertJsonFileEqualsJsonFile)
* [`assertJsonFileNotEqualsJsonFile(string $expectedFile, string $actualFile, string $message = ''): void`](#assertJsonFileNotEqualsJsonFile)
* [`logicalAnd(): \PHPUnit\Framework\Constraint\LogicalAnd`](#logicalAnd)
* [`logicalOr(): \PHPUnit\Framework\Constraint\LogicalOr`](#logicalOr)
* [`logicalNot(\PHPUnit\Framework\Constraint\Constraint $constraint): \PHPUnit\Framework\Constraint\LogicalNot`](#logicalNot)
* [`logicalXor(): \PHPUnit\Framework\Constraint\LogicalXor`](#logicalXor)
* [`anything(): \PHPUnit\Framework\Constraint\IsAnything`](#anything)
* [`isTrue(): \PHPUnit\Framework\Constraint\IsTrue`](#isTrue)
* [`callback(callable(CallbackInput $callback): boo) $callback): Callback<CallbackInput>`](#callback)
* [`isFalse(): \PHPUnit\Framework\Constraint\IsFalse`](#isFalse)
* [`isJson(): \PHPUnit\Framework\Constraint\IsJson`](#isJson)
* [`isNull(): \PHPUnit\Framework\Constraint\IsNull`](#isNull)
* [`isFinite(): \PHPUnit\Framework\Constraint\IsFinite`](#isFinite)
* [`isInfinite(): \PHPUnit\Framework\Constraint\IsInfinite`](#isInfinite)
* [`isNan(): \PHPUnit\Framework\Constraint\IsNan`](#isNan)
* [`containsEqual(mixed $value): \PHPUnit\Framework\Constraint\TraversableContainsEqual`](#containsEqual)
* [`containsIdentical(mixed $value): \PHPUnit\Framework\Constraint\TraversableContainsIdentical`](#containsIdentical)
* [`containsOnly(string $type): \PHPUnit\Framework\Constraint\TraversableContainsOnly`](#containsOnly)
* [`containsOnlyInstancesOf(string $className): \PHPUnit\Framework\Constraint\TraversableContainsOnly`](#containsOnlyInstancesOf)
* [`arrayHasKey((int|string) $key): \PHPUnit\Framework\Constraint\ArrayHasKey`](#arrayHasKey)
* [`equalTo(mixed $value): \PHPUnit\Framework\Constraint\IsEqual`](#equalTo)
* [`equalToCanonicalizing(mixed $value): \PHPUnit\Framework\Constraint\IsEqualCanonicalizing`](#equalToCanonicalizing)
* [`equalToIgnoringCase(mixed $value): \PHPUnit\Framework\Constraint\IsEqualIgnoringCase`](#equalToIgnoringCase)
* [`equalToWithDelta(mixed $value, float $delta): \PHPUnit\Framework\Constraint\IsEqualWithDelta`](#equalToWithDelta)
* [`isEmpty(): \PHPUnit\Framework\Constraint\IsEmpty`](#isEmpty)
* [`isWritable(): \PHPUnit\Framework\Constraint\IsWritable`](#isWritable)
* [`isReadable(): \PHPUnit\Framework\Constraint\IsReadable`](#isReadable)
* [`directoryExists(): \PHPUnit\Framework\Constraint\DirectoryExists`](#directoryExists)
* [`fileExists(): \PHPUnit\Framework\Constraint\FileExists`](#fileExists)
* [`greaterThan(mixed $value): \PHPUnit\Framework\Constraint\GreaterThan`](#greaterThan)
* [`greaterThanOrEqual(mixed $value): \PHPUnit\Framework\Constraint\LogicalOr`](#greaterThanOrEqual)
* [`identicalTo(mixed $value): \PHPUnit\Framework\Constraint\IsIdentical`](#identicalTo)
* [`isInstanceOf(string $className): \PHPUnit\Framework\Constraint\IsInstanceOf`](#isInstanceOf)
* [`isType(string $type): \PHPUnit\Framework\Constraint\IsType`](#isType)
* [`lessThan(mixed $value): \PHPUnit\Framework\Constraint\LessThan`](#lessThan)
* [`lessThanOrEqual(mixed $value): \PHPUnit\Framework\Constraint\LogicalOr`](#lessThanOrEqual)
* [`matchesRegularExpression(string $pattern): \PHPUnit\Framework\Constraint\RegularExpression`](#matchesRegularExpression)
* [`matches(string $string): \PHPUnit\Framework\Constraint\StringMatchesFormatDescription`](#matches)
* [`stringStartsWith(mixed $prefix): \PHPUnit\Framework\Constraint\StringStartsWith`](#stringStartsWith)
* [`stringContains(string $string, bool $case = true): \PHPUnit\Framework\Constraint\StringContains`](#stringContains)
* [`stringEndsWith(string $suffix): \PHPUnit\Framework\Constraint\StringEndsWith`](#stringEndsWith)
* [`countOf(int $count): \PHPUnit\Framework\Constraint\Count`](#countOf)
* [`objectEquals(object $object, string $method = 'equals'): \PHPUnit\Framework\Constraint\ObjectEquals`](#objectEquals)
* [`fail(string $message = ''): never-return`](#fail)
* [`markTestIncomplete(string $message = ''): never-return`](#markTestIncomplete)
* [`markTestSkipped(string $message = ''): never-return`](#markTestSkipped)
* [`getCount(): int`](#getCount)
* [`resetCount(): void`](#resetCount)

## Methods:
### <a name="testHevcRecordsThroughRtp"></a> `testHevcRecordsThroughRtp(): void`





### <a name="testAv1RecordsThroughRtp"></a> `testAv1RecordsThroughRtp(): void`





### <a name="any"></a> `any(): \PHPUnit\Framework\MockObject\Rule\AnyInvokedCount`

Returns a matcher that matches when the method is executed
zero or more times.  


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\AnyInvokedCount`




### <a name="never"></a> `never(): \PHPUnit\Framework\MockObject\Rule\InvokedCount`

Returns a matcher that matches when the method is never executed.


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedCount`




### <a name="atLeast"></a> `atLeast(int $requiredInvocations): \PHPUnit\Framework\MockObject\Rule\InvokedAtLeastCount`

Returns a matcher that matches when the method is executed
at least N times.  


Parameters:

* `$requiredInvocations`: `int`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedAtLeastCount`




### <a name="atLeastOnce"></a> `atLeastOnce(): \PHPUnit\Framework\MockObject\Rule\InvokedAtLeastOnce`

Returns a matcher that matches when the method is executed at least once.


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedAtLeastOnce`




### <a name="once"></a> `once(): \PHPUnit\Framework\MockObject\Rule\InvokedCount`

Returns a matcher that matches when the method is executed exactly once.


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedCount`




### <a name="exactly"></a> `exactly(int $count): \PHPUnit\Framework\MockObject\Rule\InvokedCount`

Returns a matcher that matches when the method is executed
exactly $count times.  


Parameters:

* `$count`: `int`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedCount`




### <a name="atMost"></a> `atMost(int $allowedInvocations): \PHPUnit\Framework\MockObject\Rule\InvokedAtMostCount`

Returns a matcher that matches when the method is executed
at most N times.  


Parameters:

* `$allowedInvocations`: `int`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Rule\InvokedAtMostCount`




### <a name="returnValue"></a> `returnValue(mixed $value): \PHPUnit\Framework\MockObject\Stub\ReturnStub`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnStub`




### <a name="returnValueMap"></a> `returnValueMap(array $valueMap): \PHPUnit\Framework\MockObject\Stub\ReturnValueMap`




Parameters:

* `$valueMap`: `array`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnValueMap`




### <a name="returnArgument"></a> `returnArgument(int $argumentIndex): \PHPUnit\Framework\MockObject\Stub\ReturnArgument`




Parameters:

* `$argumentIndex`: `int`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnArgument`




### <a name="returnCallback"></a> `returnCallback(mixed $callback): \PHPUnit\Framework\MockObject\Stub\ReturnCallback`




Parameters:

* `$callback`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnCallback`




### <a name="returnSelf"></a> `returnSelf(): \PHPUnit\Framework\MockObject\Stub\ReturnSelf`

Returns the current object.
  
This method is useful when mocking a fluent interface.  


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ReturnSelf`




### <a name="throwException"></a> `throwException(Throwable $exception): \PHPUnit\Framework\MockObject\Stub\Exception`




Parameters:

* `$exception`: `Throwable`   


#### See also: 
* `Throwable`
* `\PHPUnit\Framework\MockObject\Stub\Exception`




### <a name="onConsecutiveCalls"></a> `onConsecutiveCalls(mixed ...$args): \PHPUnit\Framework\MockObject\Stub\ConsecutiveCalls`




Parameters:

* `...$args`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\MockObject\Stub\ConsecutiveCalls`




### <a name="setUpBeforeClass"></a> `setUpBeforeClass(): void`

This method is called before the first test of this test class is run.



### <a name="tearDownAfterClass"></a> `tearDownAfterClass(): void`

This method is called after the last test of this test class is run.



### <a name="toString"></a> `toString(): string`

Returns a string representation of the test case.



### <a name="count"></a> `count(): int`





### <a name="getActualOutputForAssertion"></a> `getActualOutputForAssertion(): string`





### <a name="expectOutputRegex"></a> `expectOutputRegex(string $expectedRegex): void`




Parameters:

* `$expectedRegex`: `string`   



### <a name="expectOutputString"></a> `expectOutputString(string $expectedString): void`




Parameters:

* `$expectedString`: `string`   



### <a name="expectException"></a> `expectException(class-string<Throwable> $exception): void`




Parameters:

* `$exception`: `class-string<Throwable>`   


#### See also: 
* `Throwable`




### <a name="expectExceptionCode"></a> `expectExceptionCode((int|string) $code): void`




Parameters:

* `$code`: `(int|string)`   



### <a name="expectExceptionMessage"></a> `expectExceptionMessage(string $message): void`




Parameters:

* `$message`: `string`   



### <a name="expectExceptionMessageMatches"></a> `expectExceptionMessageMatches(string $regularExpression): void`




Parameters:

* `$regularExpression`: `string`   



### <a name="expectExceptionObject"></a> `expectExceptionObject(Exception $exception): void`

Sets up an expectation for an exception to be raised by the code under test.
Information for expected exception class, expected exception message, and  
expected exception code are retrieved from a given Exception object.  


Parameters:

* `$exception`: `Exception`   


#### See also: 
* `Exception`




### <a name="expectNotToPerformAssertions"></a> `expectNotToPerformAssertions(): void`





### <a name="getStatus"></a> `getStatus(): int`





### <a name="markAsRisky"></a> `markAsRisky(): void`





### <a name="getStatusMessage"></a> `getStatusMessage(): string`





### <a name="hasFailed"></a> `hasFailed(): bool`





### <a name="run"></a> `run(?\PHPUnit\Framework\TestResult $result = NULL): \PHPUnit\Framework\TestResult`

Runs the test case and collects the results in a TestResult object.
If no TestResult object is passed a new one will be created.  


Parameters:

* `$result`: `?\PHPUnit\Framework\TestResult`   


#### See also: 
* `\PHPUnit\Framework\TestResult`




### <a name="getMockBuilder"></a> `getMockBuilder(class-string<RealInstanceType> $className): MockBuilder<RealInstanceType>`

Returns a builder object to create mock objects using a fluent interface.


Parameters:

* `$className`: `class-string<RealInstanceType>`   


#### See also: 
* `RealInstanceType`
* `MockBuilder`




### <a name="registerComparator"></a> `registerComparator(\SebastianBergmann\Comparator\Comparator $comparator): void`




Parameters:

* `$comparator`: `\SebastianBergmann\Comparator\Comparator`   


#### See also: 
* `\SebastianBergmann\Comparator\Comparator`




### <a name="sortId"></a> `sortId(): string`





### <a name="provides"></a> `provides(): list<ExecutionOrderDependency>`

Returns the normalized test name as class::method.


#### See also: 
* `ExecutionOrderDependency`




### <a name="requires"></a> `requires(): list<ExecutionOrderDependency>`

Returns a list of normalized dependency names, class::method.
  
This list can differ from the raw dependencies as the resolver has  
no need for the [!][shallow]clone prefix that is filtered out  
during normalization.  


#### See also: 
* `ExecutionOrderDependency`




### <a name="assertArrayHasKey"></a> `assertArrayHasKey((int|string) $key, (array|ArrayAccess) $array, string $message = ''): void`

Asserts that an array has a specified key.


Parameters:

* `$key`: `(int|string)`   
* `$array`: `(array|ArrayAccess)`   
* `$message`: `string`   


#### See also: 
* `ArrayAccess`




### <a name="assertArrayNotHasKey"></a> `assertArrayNotHasKey((int|string) $key, (array|ArrayAccess) $array, string $message = ''): void`

Asserts that an array does not have a specified key.


Parameters:

* `$key`: `(int|string)`   
* `$array`: `(array|ArrayAccess)`   
* `$message`: `string`   


#### See also: 
* `ArrayAccess`




### <a name="assertContains"></a> `assertContains(mixed $needle, iterable $haystack, string $message = ''): void`

Asserts that a haystack contains a needle.


Parameters:

* `$needle`: `mixed`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### <a name="assertContainsEquals"></a> `assertContainsEquals(mixed $needle, iterable $haystack, string $message = ''): void`




Parameters:

* `$needle`: `mixed`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### <a name="assertNotContains"></a> `assertNotContains(mixed $needle, iterable $haystack, string $message = ''): void`

Asserts that a haystack does not contain a needle.


Parameters:

* `$needle`: `mixed`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### <a name="assertNotContainsEquals"></a> `assertNotContainsEquals(mixed $needle, iterable $haystack, string $message = ''): void`




Parameters:

* `$needle`: `mixed`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### <a name="assertContainsOnly"></a> `assertContainsOnly(string $type, iterable $haystack, ?bool $isNativeType = NULL, string $message = ''): void`

Asserts that a haystack contains only values of a given type.


Parameters:

* `$type`: `string`   
* `$haystack`: `iterable`   
* `$isNativeType`: `?bool`   
* `$message`: `string`   



### <a name="assertContainsOnlyInstancesOf"></a> `assertContainsOnlyInstancesOf(string $className, iterable $haystack, string $message = ''): void`

Asserts that a haystack contains only instances of a given class name.


Parameters:

* `$className`: `string`   
* `$haystack`: `iterable`   
* `$message`: `string`   



### <a name="assertNotContainsOnly"></a> `assertNotContainsOnly(string $type, iterable $haystack, ?bool $isNativeType = NULL, string $message = ''): void`

Asserts that a haystack does not contain only values of a given type.


Parameters:

* `$type`: `string`   
* `$haystack`: `iterable`   
* `$isNativeType`: `?bool`   
* `$message`: `string`   



### <a name="assertCount"></a> `assertCount(int $expectedCount, (Countable|iterable) $haystack, string $message = ''): void`

Asserts the number of elements of an array, Countable or Traversable.


Parameters:

* `$expectedCount`: `int`   
* `$haystack`: `(Countable|iterable)`   
* `$message`: `string`   


#### See also: 
* `Countable`




### <a name="assertNotCount"></a> `assertNotCount(int $expectedCount, (Countable|iterable) $haystack, string $message = ''): void`

Asserts the number of elements of an array, Countable or Traversable.


Parameters:

* `$expectedCount`: `int`   
* `$haystack`: `(Countable|iterable)`   
* `$message`: `string`   


#### See also: 
* `Countable`




### <a name="assertEquals"></a> `assertEquals(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are equal.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertEqualsCanonicalizing"></a> `assertEqualsCanonicalizing(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are equal (canonicalizing).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertEqualsIgnoringCase"></a> `assertEqualsIgnoringCase(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are equal (ignoring case).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertEqualsWithDelta"></a> `assertEqualsWithDelta(mixed $expected, mixed $actual, float $delta, string $message = ''): void`

Asserts that two variables are equal (with delta).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$delta`: `float`   
* `$message`: `string`   



### <a name="assertNotEquals"></a> `assertNotEquals(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are not equal.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertNotEqualsCanonicalizing"></a> `assertNotEqualsCanonicalizing(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are not equal (canonicalizing).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertNotEqualsIgnoringCase"></a> `assertNotEqualsIgnoringCase(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables are not equal (ignoring case).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertNotEqualsWithDelta"></a> `assertNotEqualsWithDelta(mixed $expected, mixed $actual, float $delta, string $message = ''): void`

Asserts that two variables are not equal (with delta).


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$delta`: `float`   
* `$message`: `string`   



### <a name="assertObjectEquals"></a> `assertObjectEquals(object $expected, object $actual, string $method = 'equals', string $message = ''): void`




Parameters:

* `$expected`: `object`   
* `$actual`: `object`   
* `$method`: `string`   
* `$message`: `string`   



### <a name="assertEmpty"></a> `assertEmpty(mixed $actual, string $message = ''): void`

Asserts that a variable is empty.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertNotEmpty"></a> `assertNotEmpty(mixed $actual, string $message = ''): void`

Asserts that a variable is not empty.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertGreaterThan"></a> `assertGreaterThan(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that a value is greater than another value.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertGreaterThanOrEqual"></a> `assertGreaterThanOrEqual(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that a value is greater than or equal to another value.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertLessThan"></a> `assertLessThan(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that a value is smaller than another value.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertLessThanOrEqual"></a> `assertLessThanOrEqual(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that a value is smaller than or equal to another value.


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertFileEquals"></a> `assertFileEquals(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is equal to the contents of another
file.  


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### <a name="assertFileEqualsCanonicalizing"></a> `assertFileEqualsCanonicalizing(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is equal to the contents of another
file (canonicalizing).  


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### <a name="assertFileEqualsIgnoringCase"></a> `assertFileEqualsIgnoringCase(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is equal to the contents of another
file (ignoring case).  


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### <a name="assertFileNotEquals"></a> `assertFileNotEquals(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is not equal to the contents of
another file.  


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### <a name="assertFileNotEqualsCanonicalizing"></a> `assertFileNotEqualsCanonicalizing(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is not equal to the contents of another
file (canonicalizing).  


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### <a name="assertFileNotEqualsIgnoringCase"></a> `assertFileNotEqualsIgnoringCase(string $expected, string $actual, string $message = ''): void`

Asserts that the contents of one file is not equal to the contents of another
file (ignoring case).  


Parameters:

* `$expected`: `string`   
* `$actual`: `string`   
* `$message`: `string`   



### <a name="assertStringEqualsFile"></a> `assertStringEqualsFile(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is equal
to the contents of a file.  


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### <a name="assertStringEqualsFileCanonicalizing"></a> `assertStringEqualsFileCanonicalizing(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is equal
to the contents of a file (canonicalizing).  


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### <a name="assertStringEqualsFileIgnoringCase"></a> `assertStringEqualsFileIgnoringCase(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is equal
to the contents of a file (ignoring case).  


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### <a name="assertStringNotEqualsFile"></a> `assertStringNotEqualsFile(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is not equal
to the contents of a file.  


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### <a name="assertStringNotEqualsFileCanonicalizing"></a> `assertStringNotEqualsFileCanonicalizing(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is not equal
to the contents of a file (canonicalizing).  


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### <a name="assertStringNotEqualsFileIgnoringCase"></a> `assertStringNotEqualsFileIgnoringCase(string $expectedFile, string $actualString, string $message = ''): void`

Asserts that the contents of a string is not equal
to the contents of a file (ignoring case).  


Parameters:

* `$expectedFile`: `string`   
* `$actualString`: `string`   
* `$message`: `string`   



### <a name="assertIsReadable"></a> `assertIsReadable(string $filename, string $message = ''): void`

Asserts that a file/dir is readable.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### <a name="assertIsNotReadable"></a> `assertIsNotReadable(string $filename, string $message = ''): void`

Asserts that a file/dir exists and is not readable.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### <a name="assertIsWritable"></a> `assertIsWritable(string $filename, string $message = ''): void`

Asserts that a file/dir exists and is writable.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### <a name="assertIsNotWritable"></a> `assertIsNotWritable(string $filename, string $message = ''): void`

Asserts that a file/dir exists and is not writable.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### <a name="assertDirectoryExists"></a> `assertDirectoryExists(string $directory, string $message = ''): void`

Asserts that a directory exists.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### <a name="assertDirectoryDoesNotExist"></a> `assertDirectoryDoesNotExist(string $directory, string $message = ''): void`

Asserts that a directory does not exist.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### <a name="assertDirectoryIsReadable"></a> `assertDirectoryIsReadable(string $directory, string $message = ''): void`

Asserts that a directory exists and is readable.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### <a name="assertDirectoryIsNotReadable"></a> `assertDirectoryIsNotReadable(string $directory, string $message = ''): void`

Asserts that a directory exists and is not readable.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### <a name="assertDirectoryIsWritable"></a> `assertDirectoryIsWritable(string $directory, string $message = ''): void`

Asserts that a directory exists and is writable.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### <a name="assertDirectoryIsNotWritable"></a> `assertDirectoryIsNotWritable(string $directory, string $message = ''): void`

Asserts that a directory exists and is not writable.


Parameters:

* `$directory`: `string`   
* `$message`: `string`   



### <a name="assertFileExists"></a> `assertFileExists(string $filename, string $message = ''): void`

Asserts that a file exists.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### <a name="assertFileDoesNotExist"></a> `assertFileDoesNotExist(string $filename, string $message = ''): void`

Asserts that a file does not exist.


Parameters:

* `$filename`: `string`   
* `$message`: `string`   



### <a name="assertFileIsReadable"></a> `assertFileIsReadable(string $file, string $message = ''): void`

Asserts that a file exists and is readable.


Parameters:

* `$file`: `string`   
* `$message`: `string`   



### <a name="assertFileIsNotReadable"></a> `assertFileIsNotReadable(string $file, string $message = ''): void`

Asserts that a file exists and is not readable.


Parameters:

* `$file`: `string`   
* `$message`: `string`   



### <a name="assertFileIsWritable"></a> `assertFileIsWritable(string $file, string $message = ''): void`

Asserts that a file exists and is writable.


Parameters:

* `$file`: `string`   
* `$message`: `string`   



### <a name="assertFileIsNotWritable"></a> `assertFileIsNotWritable(string $file, string $message = ''): void`

Asserts that a file exists and is not writable.


Parameters:

* `$file`: `string`   
* `$message`: `string`   



### <a name="assertTrue"></a> `assertTrue(mixed $condition, string $message = ''): void`

Asserts that a condition is true.


Parameters:

* `$condition`: `mixed`   
* `$message`: `string`   



### <a name="assertNotTrue"></a> `assertNotTrue(mixed $condition, string $message = ''): void`

Asserts that a condition is not true.


Parameters:

* `$condition`: `mixed`   
* `$message`: `string`   



### <a name="assertFalse"></a> `assertFalse(mixed $condition, string $message = ''): void`

Asserts that a condition is false.


Parameters:

* `$condition`: `mixed`   
* `$message`: `string`   



### <a name="assertNotFalse"></a> `assertNotFalse(mixed $condition, string $message = ''): void`

Asserts that a condition is not false.


Parameters:

* `$condition`: `mixed`   
* `$message`: `string`   



### <a name="assertNull"></a> `assertNull(mixed $actual, string $message = ''): void`

Asserts that a variable is null.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertNotNull"></a> `assertNotNull(mixed $actual, string $message = ''): void`

Asserts that a variable is not null.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertFinite"></a> `assertFinite(mixed $actual, string $message = ''): void`

Asserts that a variable is finite.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertInfinite"></a> `assertInfinite(mixed $actual, string $message = ''): void`

Asserts that a variable is infinite.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertNan"></a> `assertNan(mixed $actual, string $message = ''): void`

Asserts that a variable is nan.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertObjectHasProperty"></a> `assertObjectHasProperty(string $propertyName, object $object, string $message = ''): void`

Asserts that an object has a specified property.


Parameters:

* `$propertyName`: `string`   
* `$object`: `object`   
* `$message`: `string`   



### <a name="assertObjectNotHasProperty"></a> `assertObjectNotHasProperty(string $propertyName, object $object, string $message = ''): void`

Asserts that an object does not have a specified property.


Parameters:

* `$propertyName`: `string`   
* `$object`: `object`   
* `$message`: `string`   



### <a name="assertSame"></a> `assertSame(ExpectedType $expected, mixed $actual, string $message = ''): void`

Asserts that two variables have the same type and value.
Used on objects, it asserts that two variables reference  
the same object.  


Parameters:

* `$expected`: `ExpectedType`   
* `$actual`: `mixed`   
* `$message`: `string`   


#### See also: 
* `ExpectedType`




### <a name="assertNotSame"></a> `assertNotSame(mixed $expected, mixed $actual, string $message = ''): void`

Asserts that two variables do not have the same type and value.
Used on objects, it asserts that two variables do not reference  
the same object.  


Parameters:

* `$expected`: `mixed`   
* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertInstanceOf"></a> `assertInstanceOf(class-string<ExpectedType> $expected, mixed $actual, string $message = ''): void`

Asserts that a variable is of a given type.


Parameters:

* `$expected`: `class-string<ExpectedType>`   
* `$actual`: `mixed`   
* `$message`: `string`   


#### See also: 
* `ExpectedType`




### <a name="assertNotInstanceOf"></a> `assertNotInstanceOf(class-string<ExpectedType> $expected, mixed $actual, string $message = ''): void`

Asserts that a variable is not of a given type.


Parameters:

* `$expected`: `class-string<ExpectedType>`   
* `$actual`: `mixed`   
* `$message`: `string`   


#### See also: 
* `ExpectedType`




### <a name="assertIsArray"></a> `assertIsArray(mixed $actual, string $message = ''): void`

Asserts that a variable is of type array.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsBool"></a> `assertIsBool(mixed $actual, string $message = ''): void`

Asserts that a variable is of type bool.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsFloat"></a> `assertIsFloat(mixed $actual, string $message = ''): void`

Asserts that a variable is of type float.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsInt"></a> `assertIsInt(mixed $actual, string $message = ''): void`

Asserts that a variable is of type int.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNumeric"></a> `assertIsNumeric(mixed $actual, string $message = ''): void`

Asserts that a variable is of type numeric.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsObject"></a> `assertIsObject(mixed $actual, string $message = ''): void`

Asserts that a variable is of type object.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsResource"></a> `assertIsResource(mixed $actual, string $message = ''): void`

Asserts that a variable is of type resource.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsClosedResource"></a> `assertIsClosedResource(mixed $actual, string $message = ''): void`

Asserts that a variable is of type resource and is closed.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsString"></a> `assertIsString(mixed $actual, string $message = ''): void`

Asserts that a variable is of type string.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsScalar"></a> `assertIsScalar(mixed $actual, string $message = ''): void`

Asserts that a variable is of type scalar.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsCallable"></a> `assertIsCallable(mixed $actual, string $message = ''): void`

Asserts that a variable is of type callable.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsIterable"></a> `assertIsIterable(mixed $actual, string $message = ''): void`

Asserts that a variable is of type iterable.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotArray"></a> `assertIsNotArray(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type array.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotBool"></a> `assertIsNotBool(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type bool.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotFloat"></a> `assertIsNotFloat(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type float.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotInt"></a> `assertIsNotInt(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type int.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotNumeric"></a> `assertIsNotNumeric(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type numeric.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotObject"></a> `assertIsNotObject(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type object.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotResource"></a> `assertIsNotResource(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type resource.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotClosedResource"></a> `assertIsNotClosedResource(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type resource.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotString"></a> `assertIsNotString(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type string.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotScalar"></a> `assertIsNotScalar(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type scalar.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotCallable"></a> `assertIsNotCallable(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type callable.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertIsNotIterable"></a> `assertIsNotIterable(mixed $actual, string $message = ''): void`

Asserts that a variable is not of type iterable.


Parameters:

* `$actual`: `mixed`   
* `$message`: `string`   



### <a name="assertMatchesRegularExpression"></a> `assertMatchesRegularExpression(string $pattern, string $string, string $message = ''): void`

Asserts that a string matches a given regular expression.


Parameters:

* `$pattern`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertDoesNotMatchRegularExpression"></a> `assertDoesNotMatchRegularExpression(string $pattern, string $string, string $message = ''): void`

Asserts that a string does not match a given regular expression.


Parameters:

* `$pattern`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertSameSize"></a> `assertSameSize((Countable|iterable) $expected, (Countable|iterable) $actual, string $message = ''): void`

Assert that the size of two arrays (or `Countable` or `Traversable` objects)
is the same.  


Parameters:

* `$expected`: `(Countable|iterable)`   
* `$actual`: `(Countable|iterable)`   
* `$message`: `string`   


#### See also: 
* `Countable`




### <a name="assertNotSameSize"></a> `assertNotSameSize((Countable|iterable) $expected, (Countable|iterable) $actual, string $message = ''): void`

Assert that the size of two arrays (or `Countable` or `Traversable` objects)
is not the same.  


Parameters:

* `$expected`: `(Countable|iterable)`   
* `$actual`: `(Countable|iterable)`   
* `$message`: `string`   


#### See also: 
* `Countable`




### <a name="assertStringMatchesFormat"></a> `assertStringMatchesFormat(string $format, string $string, string $message = ''): void`

Asserts that a string matches a given format string.


Parameters:

* `$format`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertStringNotMatchesFormat"></a> `assertStringNotMatchesFormat(string $format, string $string, string $message = ''): void`

Asserts that a string does not match a given format string.


Parameters:

* `$format`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertStringMatchesFormatFile"></a> `assertStringMatchesFormatFile(string $formatFile, string $string, string $message = ''): void`

Asserts that a string matches a given format file.


Parameters:

* `$formatFile`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertStringNotMatchesFormatFile"></a> `assertStringNotMatchesFormatFile(string $formatFile, string $string, string $message = ''): void`

Asserts that a string does not match a given format string.


Parameters:

* `$formatFile`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertStringStartsWith"></a> `assertStringStartsWith(string $prefix, string $string, string $message = ''): void`

Asserts that a string starts with a given prefix.


Parameters:

* `$prefix`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertStringStartsNotWith"></a> `assertStringStartsNotWith(string $prefix, string $string, string $message = ''): void`

Asserts that a string starts not with a given prefix.


Parameters:

* `$prefix`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertStringContainsString"></a> `assertStringContainsString(string $needle, string $haystack, string $message = ''): void`




Parameters:

* `$needle`: `string`   
* `$haystack`: `string`   
* `$message`: `string`   



### <a name="assertStringContainsStringIgnoringCase"></a> `assertStringContainsStringIgnoringCase(string $needle, string $haystack, string $message = ''): void`




Parameters:

* `$needle`: `string`   
* `$haystack`: `string`   
* `$message`: `string`   



### <a name="assertStringNotContainsString"></a> `assertStringNotContainsString(string $needle, string $haystack, string $message = ''): void`




Parameters:

* `$needle`: `string`   
* `$haystack`: `string`   
* `$message`: `string`   



### <a name="assertStringNotContainsStringIgnoringCase"></a> `assertStringNotContainsStringIgnoringCase(string $needle, string $haystack, string $message = ''): void`




Parameters:

* `$needle`: `string`   
* `$haystack`: `string`   
* `$message`: `string`   



### <a name="assertStringEndsWith"></a> `assertStringEndsWith(string $suffix, string $string, string $message = ''): void`

Asserts that a string ends with a given suffix.


Parameters:

* `$suffix`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertStringEndsNotWith"></a> `assertStringEndsNotWith(string $suffix, string $string, string $message = ''): void`

Asserts that a string ends not with a given suffix.


Parameters:

* `$suffix`: `string`   
* `$string`: `string`   
* `$message`: `string`   



### <a name="assertXmlFileEqualsXmlFile"></a> `assertXmlFileEqualsXmlFile(string $expectedFile, string $actualFile, string $message = ''): void`

Asserts that two XML files are equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualFile`: `string`   
* `$message`: `string`   



### <a name="assertXmlFileNotEqualsXmlFile"></a> `assertXmlFileNotEqualsXmlFile(string $expectedFile, string $actualFile, string $message = ''): void`

Asserts that two XML files are not equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualFile`: `string`   
* `$message`: `string`   



### <a name="assertXmlStringEqualsXmlFile"></a> `assertXmlStringEqualsXmlFile(string $expectedFile, (DOMDocument|string) $actualXml, string $message = ''): void`

Asserts that two XML documents are equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualXml`: `(DOMDocument|string)`   
* `$message`: `string`   


#### See also: 
* `DOMDocument`




### <a name="assertXmlStringNotEqualsXmlFile"></a> `assertXmlStringNotEqualsXmlFile(string $expectedFile, (DOMDocument|string) $actualXml, string $message = ''): void`

Asserts that two XML documents are not equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualXml`: `(DOMDocument|string)`   
* `$message`: `string`   


#### See also: 
* `DOMDocument`




### <a name="assertXmlStringEqualsXmlString"></a> `assertXmlStringEqualsXmlString((DOMDocument|string) $expectedXml, (DOMDocument|string) $actualXml, string $message = ''): void`

Asserts that two XML documents are equal.


Parameters:

* `$expectedXml`: `(DOMDocument|string)`   
* `$actualXml`: `(DOMDocument|string)`   
* `$message`: `string`   


#### See also: 
* `DOMDocument`




### <a name="assertXmlStringNotEqualsXmlString"></a> `assertXmlStringNotEqualsXmlString((DOMDocument|string) $expectedXml, (DOMDocument|string) $actualXml, string $message = ''): void`

Asserts that two XML documents are not equal.


Parameters:

* `$expectedXml`: `(DOMDocument|string)`   
* `$actualXml`: `(DOMDocument|string)`   
* `$message`: `string`   


#### See also: 
* `DOMDocument`




### <a name="assertThat"></a> `assertThat(mixed $value, \PHPUnit\Framework\Constraint\Constraint $constraint, string $message = ''): void`

Evaluates a PHPUnit\Framework\Constraint matcher object.


Parameters:

* `$value`: `mixed`   
* `$constraint`: `\PHPUnit\Framework\Constraint\Constraint`   
* `$message`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\Constraint`




### <a name="assertJson"></a> `assertJson(string $actualJson, string $message = ''): void`

Asserts that a string is a valid JSON string.


Parameters:

* `$actualJson`: `string`   
* `$message`: `string`   



### <a name="assertJsonStringEqualsJsonString"></a> `assertJsonStringEqualsJsonString(string $expectedJson, string $actualJson, string $message = ''): void`

Asserts that two given JSON encoded objects or arrays are equal.


Parameters:

* `$expectedJson`: `string`   
* `$actualJson`: `string`   
* `$message`: `string`   



### <a name="assertJsonStringNotEqualsJsonString"></a> `assertJsonStringNotEqualsJsonString(string $expectedJson, string $actualJson, string $message = ''): void`

Asserts that two given JSON encoded objects or arrays are not equal.


Parameters:

* `$expectedJson`: `string`   
* `$actualJson`: `string`   
* `$message`: `string`   



### <a name="assertJsonStringEqualsJsonFile"></a> `assertJsonStringEqualsJsonFile(string $expectedFile, string $actualJson, string $message = ''): void`

Asserts that the generated JSON encoded object and the content of the given file are equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualJson`: `string`   
* `$message`: `string`   



### <a name="assertJsonStringNotEqualsJsonFile"></a> `assertJsonStringNotEqualsJsonFile(string $expectedFile, string $actualJson, string $message = ''): void`

Asserts that the generated JSON encoded object and the content of the given file are not equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualJson`: `string`   
* `$message`: `string`   



### <a name="assertJsonFileEqualsJsonFile"></a> `assertJsonFileEqualsJsonFile(string $expectedFile, string $actualFile, string $message = ''): void`

Asserts that two JSON files are equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualFile`: `string`   
* `$message`: `string`   



### <a name="assertJsonFileNotEqualsJsonFile"></a> `assertJsonFileNotEqualsJsonFile(string $expectedFile, string $actualFile, string $message = ''): void`

Asserts that two JSON files are not equal.


Parameters:

* `$expectedFile`: `string`   
* `$actualFile`: `string`   
* `$message`: `string`   



### <a name="logicalAnd"></a> `logicalAnd(): \PHPUnit\Framework\Constraint\LogicalAnd`




#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalAnd`




### <a name="logicalOr"></a> `logicalOr(): \PHPUnit\Framework\Constraint\LogicalOr`




#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalOr`




### <a name="logicalNot"></a> `logicalNot(\PHPUnit\Framework\Constraint\Constraint $constraint): \PHPUnit\Framework\Constraint\LogicalNot`




Parameters:

* `$constraint`: `\PHPUnit\Framework\Constraint\Constraint`   


#### See also: 
* `\PHPUnit\Framework\Constraint\Constraint`
* `\PHPUnit\Framework\Constraint\LogicalNot`




### <a name="logicalXor"></a> `logicalXor(): \PHPUnit\Framework\Constraint\LogicalXor`




#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalXor`




### <a name="anything"></a> `anything(): \PHPUnit\Framework\Constraint\IsAnything`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsAnything`




### <a name="isTrue"></a> `isTrue(): \PHPUnit\Framework\Constraint\IsTrue`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsTrue`




### <a name="callback"></a> `callback(callable(CallbackInput $callback): boo) $callback): Callback<CallbackInput>`




Parameters:

* `$callback`: `callable(CallbackInput $callback): boo)`   


#### See also: 
* `CallbackInput`
* `Callback`




### <a name="isFalse"></a> `isFalse(): \PHPUnit\Framework\Constraint\IsFalse`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsFalse`




### <a name="isJson"></a> `isJson(): \PHPUnit\Framework\Constraint\IsJson`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsJson`




### <a name="isNull"></a> `isNull(): \PHPUnit\Framework\Constraint\IsNull`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsNull`




### <a name="isFinite"></a> `isFinite(): \PHPUnit\Framework\Constraint\IsFinite`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsFinite`




### <a name="isInfinite"></a> `isInfinite(): \PHPUnit\Framework\Constraint\IsInfinite`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsInfinite`




### <a name="isNan"></a> `isNan(): \PHPUnit\Framework\Constraint\IsNan`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsNan`




### <a name="containsEqual"></a> `containsEqual(mixed $value): \PHPUnit\Framework\Constraint\TraversableContainsEqual`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\TraversableContainsEqual`




### <a name="containsIdentical"></a> `containsIdentical(mixed $value): \PHPUnit\Framework\Constraint\TraversableContainsIdentical`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\TraversableContainsIdentical`




### <a name="containsOnly"></a> `containsOnly(string $type): \PHPUnit\Framework\Constraint\TraversableContainsOnly`




Parameters:

* `$type`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\TraversableContainsOnly`




### <a name="containsOnlyInstancesOf"></a> `containsOnlyInstancesOf(string $className): \PHPUnit\Framework\Constraint\TraversableContainsOnly`




Parameters:

* `$className`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\TraversableContainsOnly`




### <a name="arrayHasKey"></a> `arrayHasKey((int|string) $key): \PHPUnit\Framework\Constraint\ArrayHasKey`




Parameters:

* `$key`: `(int|string)`   


#### See also: 
* `\PHPUnit\Framework\Constraint\ArrayHasKey`




### <a name="equalTo"></a> `equalTo(mixed $value): \PHPUnit\Framework\Constraint\IsEqual`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsEqual`




### <a name="equalToCanonicalizing"></a> `equalToCanonicalizing(mixed $value): \PHPUnit\Framework\Constraint\IsEqualCanonicalizing`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsEqualCanonicalizing`




### <a name="equalToIgnoringCase"></a> `equalToIgnoringCase(mixed $value): \PHPUnit\Framework\Constraint\IsEqualIgnoringCase`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsEqualIgnoringCase`




### <a name="equalToWithDelta"></a> `equalToWithDelta(mixed $value, float $delta): \PHPUnit\Framework\Constraint\IsEqualWithDelta`




Parameters:

* `$value`: `mixed`   
* `$delta`: `float`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsEqualWithDelta`




### <a name="isEmpty"></a> `isEmpty(): \PHPUnit\Framework\Constraint\IsEmpty`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsEmpty`




### <a name="isWritable"></a> `isWritable(): \PHPUnit\Framework\Constraint\IsWritable`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsWritable`




### <a name="isReadable"></a> `isReadable(): \PHPUnit\Framework\Constraint\IsReadable`




#### See also: 
* `\PHPUnit\Framework\Constraint\IsReadable`




### <a name="directoryExists"></a> `directoryExists(): \PHPUnit\Framework\Constraint\DirectoryExists`




#### See also: 
* `\PHPUnit\Framework\Constraint\DirectoryExists`




### <a name="fileExists"></a> `fileExists(): \PHPUnit\Framework\Constraint\FileExists`




#### See also: 
* `\PHPUnit\Framework\Constraint\FileExists`




### <a name="greaterThan"></a> `greaterThan(mixed $value): \PHPUnit\Framework\Constraint\GreaterThan`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\GreaterThan`




### <a name="greaterThanOrEqual"></a> `greaterThanOrEqual(mixed $value): \PHPUnit\Framework\Constraint\LogicalOr`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalOr`




### <a name="identicalTo"></a> `identicalTo(mixed $value): \PHPUnit\Framework\Constraint\IsIdentical`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsIdentical`




### <a name="isInstanceOf"></a> `isInstanceOf(string $className): \PHPUnit\Framework\Constraint\IsInstanceOf`




Parameters:

* `$className`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsInstanceOf`




### <a name="isType"></a> `isType(string $type): \PHPUnit\Framework\Constraint\IsType`




Parameters:

* `$type`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\IsType`




### <a name="lessThan"></a> `lessThan(mixed $value): \PHPUnit\Framework\Constraint\LessThan`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\LessThan`




### <a name="lessThanOrEqual"></a> `lessThanOrEqual(mixed $value): \PHPUnit\Framework\Constraint\LogicalOr`




Parameters:

* `$value`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\LogicalOr`




### <a name="matchesRegularExpression"></a> `matchesRegularExpression(string $pattern): \PHPUnit\Framework\Constraint\RegularExpression`




Parameters:

* `$pattern`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\RegularExpression`




### <a name="matches"></a> `matches(string $string): \PHPUnit\Framework\Constraint\StringMatchesFormatDescription`




Parameters:

* `$string`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\StringMatchesFormatDescription`




### <a name="stringStartsWith"></a> `stringStartsWith(mixed $prefix): \PHPUnit\Framework\Constraint\StringStartsWith`




Parameters:

* `$prefix`: `mixed`   


#### See also: 
* `\PHPUnit\Framework\Constraint\StringStartsWith`




### <a name="stringContains"></a> `stringContains(string $string, bool $case = true): \PHPUnit\Framework\Constraint\StringContains`




Parameters:

* `$string`: `string`   
* `$case`: `bool`   


#### See also: 
* `\PHPUnit\Framework\Constraint\StringContains`




### <a name="stringEndsWith"></a> `stringEndsWith(string $suffix): \PHPUnit\Framework\Constraint\StringEndsWith`




Parameters:

* `$suffix`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\StringEndsWith`




### <a name="countOf"></a> `countOf(int $count): \PHPUnit\Framework\Constraint\Count`




Parameters:

* `$count`: `int`   


#### See also: 
* `\PHPUnit\Framework\Constraint\Count`




### <a name="objectEquals"></a> `objectEquals(object $object, string $method = 'equals'): \PHPUnit\Framework\Constraint\ObjectEquals`




Parameters:

* `$object`: `object`   
* `$method`: `string`   


#### See also: 
* `\PHPUnit\Framework\Constraint\ObjectEquals`




### <a name="fail"></a> `fail(string $message = ''): never-return`

Fails a test with the given message.


Parameters:

* `$message`: `string`   


#### See also: 
* `never-return`




### <a name="markTestIncomplete"></a> `markTestIncomplete(string $message = ''): never-return`

Mark the test as incomplete.


Parameters:

* `$message`: `string`   


#### See also: 
* `never-return`




### <a name="markTestSkipped"></a> `markTestSkipped(string $message = ''): never-return`

Mark the test as skipped.


Parameters:

* `$message`: `string`   


#### See also: 
* `never-return`




### <a name="getCount"></a> `getCount(): int`

Return the current assertion count.



### <a name="resetCount"></a> `resetCount(): void`

Reset the assertion counter.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
