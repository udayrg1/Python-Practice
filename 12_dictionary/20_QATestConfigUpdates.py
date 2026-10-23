'''
Day 8 — Unique Challenge: QA Test Configuration Updates
Now let's use update() in a different scenario involving software testing configurations. This challenge is not just another product-price update.

A QA team maintains test execution settings:
test_configuration = {    "browser": "Chrome",    "environment": "QA",    "timeout": 30,    "retry_count": 2,    "screenshot": False}


The team receives a configuration update:
new_configuration = {    "timeout": 60,    "retry_count": 3,    "headless": True,    "screenshot": True}


Your requirements
1. Apply new_configuration to test_configuration using update().
2. Print the final configuration.
3. Identify how many configuration settings were changed or added:
   - Two existing settings are updated: timeout and retry_count.
   - One existing setting is updated: screenshot.
   - One new setting is added: headless.
4. Print the final number of configuration settings.
5. Print the value of browser to verify that an unrelated setting remains unchanged.
Rules:
- Use update() to apply the changes.
- Don't manually modify individual settings.
- Don't use if, else, or loops.
- Write the complete program yourself.
Important thinking point: The configuration dictionary should contain six settings after the update, not nine. Updating an existing key doesn't create a duplicate.

'''

test_configuration = {
    "browser": "Chrome",
    "environment": "QA",
    "timeout": 30,
    "retry_count": 2,
    "screenshot": False
}


test_configuration.update({
    "timeout": 60,
    "retry_count": 3,
    "headless": True,
    "screenshot": True
})

print(test_configuration)

print(len(test_configuration))

print(test_configuration["browser"])