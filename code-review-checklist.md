# Code Review Checklist

## Functionality ✓
- [ ] Code accomplishes the intended purpose
- [ ] Edge cases are handled appropriately
- [ ] Error handling is implemented where needed
- [ ] Input validation is present for user inputs

## Code Quality ✓
- [ ] Code is readable and well-structured
- [ ] Variable and function names are descriptive
- [ ] Functions are reasonably sized (< 50 lines ideally)
- [ ] No code duplication (DRY principle)
- [ ] Comments explain "why" not "what"

## Security ✓
- [ ] No hardcoded secrets, passwords, or API keys
- [ ] Input sanitization for user data
- [ ] Proper authentication/authorization checks
- [ ] SQL injection prevention (if applicable)
- [ ] XSS prevention (if applicable)

## Performance ✓
- [ ] No obvious performance bottlenecks
- [ ] Appropriate data structures used
- [ ] Database queries are optimized
- [ ] Memory usage is reasonable
- [ ] No infinite loops or excessive recursion

## Testing ✓
- [ ] Unit tests cover main functionality
- [ ] Edge cases are tested
- [ ] Tests are readable and maintainable
- [ ] No tests are commented out or skipped
- [ ] Test coverage is adequate

## Documentation ✓
- [ ] Public APIs are documented
- [ ] Complex algorithms are explained
- [ ] README updated if needed
- [ ] Breaking changes are documented

## Standards & Best Practices ✓
- [ ] Follows team coding standards
- [ ] Consistent formatting and style
- [ ] Proper use of language idioms
- [ ] Dependencies are justified and up-to-date
- [ ] No deprecated methods or libraries

## Git & Process ✓
- [ ] Commit messages are clear and descriptive
- [ ] PR description explains the changes
- [ ] Branch is up to date with main/master
- [ ] No merge conflicts
- [ ] Files are properly organized

## Final Checks ✓
- [ ] Code builds without warnings
- [ ] All tests pass
- [ ] Linting passes
- [ ] No debug code or console.logs left behind
- [ ] Ready for production deployment