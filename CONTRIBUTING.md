# Contributing to Prompt-to-JSON Enhancer

Thank you for your interest in contributing to the Prompt-to-JSON Enhancer project! We welcome contributions from the community and appreciate your help in making this project better.

## 🤝 How to Contribute

### Types of Contributions

We welcome several types of contributions:

- **Bug Reports**: Found a bug? Please report it!
- **Feature Requests**: Have an idea for a new feature?
- **Code Contributions**: Fix bugs, add features, improve documentation
- **Documentation**: Improve existing docs or add new ones
- **Testing**: Add test cases, improve test coverage
- **Examples**: Add more sample prompts and test cases

### Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/prompt-to-json-enhancer.git
   cd prompt-to-json-enhancer
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install in development mode
   ```

4. **Run Tests**
   ```bash
   # Run the Jupyter notebook tests
   jupyter notebook test_prompt_enhancer.ipynb
   
   # Or run pytest if available
   pytest tests/
   ```

## 🐛 Reporting Bugs

### Before Reporting

1. Check if the bug has already been reported in [Issues](https://github.com/username/prompt-to-json-enhancer/issues)
2. Try to reproduce the bug with the latest version
3. Check the logs in the `logs/` directory

### Bug Report Template

When reporting a bug, please include:

```markdown
**Bug Description**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment**
- OS: [e.g., Windows 10, macOS 12.0, Ubuntu 20.04]
- Python Version: [e.g., 3.8.5]
- Browser: [e.g., Chrome 96, Firefox 94] (for Chrome Extension)

**Logs**
Include relevant log entries from `logs/prompt_enhancer.log`

**Additional Context**
Any other context about the problem.
```

## 💡 Suggesting Features

### Feature Request Template

```markdown
**Feature Description**
A clear description of the feature you'd like to see.

**Use Case**
Describe the problem this feature would solve.

**Proposed Solution**
Describe your proposed solution.

**Alternatives**
Describe any alternative solutions you've considered.

**Additional Context**
Any other context or screenshots about the feature request.
```

## 🔧 Code Contributions

### Development Workflow

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/your-bug-fix
   ```

2. **Make Your Changes**
   - Follow the coding standards (see below)
   - Add tests for new functionality
   - Update documentation if needed

3. **Test Your Changes**
   ```bash
   # Run the test notebook
   jupyter notebook test_prompt_enhancer.ipynb
   
   # Check code style
   flake8 prompt_to_json_enhancer.py
   
   # Type checking (if mypy is installed)
   mypy prompt_to_json_enhancer.py
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

5. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Coding Standards

#### Python Code Style

- Follow **PEP 8** guidelines
- Use **type hints** for function parameters and return values
- Write **docstrings** for all functions and classes
- Keep functions small and focused
- Use meaningful variable and function names

#### Example Code Style

```python
def enhance_prompt(self, prompt: str) -> Dict[str, Any]:
    """
    Enhance a plain text prompt into structured JSON format.
    
    Args:
        prompt (str): The input prompt to enhance
        
    Returns:
        Dict[str, Any]: Enhanced prompt in JSON format
        
    Raises:
        ValueError: If prompt is empty or too long
        TypeError: If prompt is not a string
    """
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string")
    
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    # Implementation here...
    return enhanced_prompt
```

#### File Organization

- Keep related functionality together
- Use meaningful module names
- Separate configuration from logic
- Document all public APIs

#### Testing Requirements

- Add tests for all new functionality
- Test edge cases and error conditions
- Update existing tests if needed
- Ensure tests pass before submitting

### Pull Request Process

1. **Update Documentation**
   - Update README.md if needed
   - Add docstrings for new functions
   - Update configuration files if applicable

2. **Test Thoroughly**
   - Run the complete test suite
   - Test with different prompt types
   - Verify logging works correctly

3. **Submit Pull Request**
   - Use a descriptive title
   - Include a detailed description
   - Reference any related issues
   - Include screenshots if applicable

#### Pull Request Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Updated existing tests

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings or errors
```

## 📚 Documentation Contributions

### Types of Documentation

- **README updates**: Installation, usage, examples
- **Code comments**: Inline documentation
- **Docstrings**: Function and class documentation
- **Configuration docs**: Settings and options
- **Tutorials**: Step-by-step guides

### Documentation Standards

- Use clear, concise language
- Include code examples
- Keep formatting consistent
- Update related sections when making changes

## 🧪 Testing Contributions

### Adding Test Cases

1. **Create Test Data**
   - Add new prompts to `sample_data/sample_prompts.json`
   - Create edge cases in `sample_data/test_cases.json`

2. **Update Test Notebook**
   - Add new test cells to `test_prompt_enhancer.ipynb`
   - Include performance tests
   - Test error conditions

3. **Verify Results**
   - Check that tests pass
   - Verify output quality
   - Test with different configurations

## 🏷️ Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version number updated
- [ ] CHANGELOG.md updated
- [ ] Release notes prepared

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Email**: dev@promptenhancer.com

### Code Review Process

- All pull requests require review
- Maintainers will provide feedback
- Address feedback promptly
- Be open to suggestions

## 🙏 Recognition

Contributors will be:
- Listed in the README
- Mentioned in release notes
- Credited in the project documentation

## 📝 License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

Thank you for contributing to Prompt-to-JSON Enhancer! 🚀
