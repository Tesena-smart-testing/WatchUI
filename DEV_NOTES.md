# NOTES for DEV
Delete before PR - hopefully

## Design setup
- since library should work with more browser automation libraries, not with hardcoded selenium, REMOVE from setup `seleniumlibrary` and `selenium`. 
- user will have to choose, which supported browser auto. lib. wants to use and will take care of installing it (currently selenium or playwright)
- library code should stay as much as it is, just extract current selenium builtIns to new Selenium class, create PLaywright class. Each library has different keywords for the same action. Then use adapter/facade design pattern to call method via one class.

