
# Unit and Integration Testing in Python 3

This repository focuses on tasks aimed at learning how to write unit and integration tests in Python 3.

## Required Modules

- `parameterized`

## Tasks

---

### Task 0: Writing Parameterized Unit Tests

- Explore the `utils.access_nested_map` function to understand its functionality by experimenting in the Python console.
- Create a class `TestAccessNestedMap` that inherits from `unittest.TestCase`.
- Write a method `test_access_nested_map` inside the class to validate that the function produces the correct output.
- Use the `@parameterized.expand` decorator to test the function with the following inputs:
    - `nested_map={"a": 1}, path=("a",)`
    - `nested_map={"a": {"b": 2}}, path=("a",)`
    - `nested_map={"a": {"b": 2}}, path=("a", "b")`
- Use `assertEqual` to ensure the returned values match the expected output.
- Keep the method body concise (no longer than 2 lines).

---

### Task 1: Handling Exceptions in Unit Tests

- In `TestAccessNestedMap`, add a new method `test_access_nested_map_exception` to check if `KeyError` is raised in certain cases.
- Use `@parameterized.expand` to test the following scenarios:
    - `nested_map={}, path=("a",)`
    - `nested_map={"a": 1}, path=("a", "b")`
- Utilize the `assertRaises` context manager and verify that the exception message is as expected.

---

### Task 2: Mocking HTTP Requests

- Familiarize yourself with `utils.get_json`.
- Create a test class `TestGetJson` (inheriting from `unittest.TestCase`).
- Write the method `test_get_json` to validate that `utils.get_json` returns the expected result.
- Instead of making real HTTP requests, use `unittest.mock.patch` to mock `requests.get` and have it return a mock object with a `.json()` method that provides the specified `test_payload`.
- Test inputs:
    - `test_url="http://example.com", test_payload={"payload": True}`
    - `test_url="http://holberton.io", test_payload={"payload": False}`
- Ensure that `requests.get` is called exactly once per input with the correct URL, and the function output matches `test_payload`.

---

### Task 3: Memoization and Patching

- Read about memoization and explore the `utils.memoize` decorator.
- In a new class `TestMemoize` (inheriting from `unittest.TestCase`), write a method `test_memoize`.
- Define an inner class `TestClass` with two methods:
    ```python
    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()
    ```
- Use `unittest.mock.patch` to mock `a_method` and verify that calling `a_property` twice returns the correct result while ensuring `a_method` is only called once by using `assert_called_once`.

---

### Task 4: Testing with Patches and Parameterization

- Understand the `client.GithubOrgClient` class.
- In a new test class `TestGithubOrgClient` (inheriting from `unittest.TestCase`), write a method `test_org` to test `GithubOrgClient.org`.
- Use `@patch` as a decorator to mock `get_json` and ensure it’s called exactly once with the correct argument.
- Use `@parameterized.expand` to test with the following inputs:
    - `"google"`
    - `"abc"`
- Ensure no external HTTP calls are made during the test.

---

### Task 5: Mocking Properties

- Learn how to mock properties, particularly in the context of memoization.
- Write a test `test_public_repos_url` in `TestGithubOrgClient` to validate the `_public_repos_url` property.
- Use `patch` as a context manager to mock the `GithubOrgClient.org` method, ensuring it returns a pre-defined payload.
- Confirm that `_public_repos_url` returns the expected result based on the mocked data.

---

### Task 6: Testing Public Repos Method

- In `TestGithubOrgClient`, add a test `test_public_repos` to verify the behavior of `public_repos`.
- Use `@patch` to mock `get_json`, providing a custom payload.
- Use `patch` as a context manager to mock `_public_repos_url`.
- Check that the returned repository list matches your expected output and that both the mocked property and `get_json` are called exactly once.

---

### Task 7: Testing License Validation

- In `TestGithubOrgClient`, create a test `test_has_license` to validate the `has_license` method.
- Use `@parameterized.expand` to test the following cases:
    - `repo={"license": {"key": "bsd-3-clause"}}, license_key="bsd-3-clause"`
    - `repo={"license": {"key": "bsl-1.0"}}, license_key="bsd-3-clause"`
- Ensure the method’s output matches the expected return values.

---

### Task 8: Integration Test Setup with Fixtures

- For integration testing, create the class `TestIntegrationGithubOrgClient` (inheriting from `unittest.TestCase`).
- Use `@parameterized_class` to decorate the class, providing fixtures from `fixtures.py`, which contains:
    - `org_payload`, `repos_payload`, `expected_repos`, `apache2_repos`.
- In `setUpClass`, use `patch` to mock `requests.get`, and make sure it returns the correct payloads based on the anticipated URLs.
- In `tearDownClass`, stop the patcher.

---

### Task 9: Integration Test for Public Repos

- In `TestIntegrationGithubOrgClient`, write the method `test_public_repos` to test the `public_repos` method and verify it returns expected results based on the fixtures.
- Write `test_public_repos_with_license` to test `public_repos` with the argument `license="apache-2.0"`, and ensure the returned data aligns with the expected value in the fixtures.
