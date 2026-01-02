# Todo App Constitution

<!--
Sync Impact Report:
Version Change: NONE → 1.0.0 (Initial constitution)
Modified Principles: N/A (Initial creation)
Added Sections: All sections (initial creation)
Removed Sections: None
Templates Requiring Updates:
  ✅ plan-template.md - Constitution Check section aligns with principles
  ✅ spec-template.md - Requirements and testing align with principles
  ✅ tasks-template.md - Task organization reflects TDD and simplicity principles
Follow-up TODOs: None
-->

## Core Principles

### I. Test-First Development (NON-NEGOTIABLE)

TDD is mandatory for this project:
- Tests MUST be written before implementation
- Red-Green-Refactor cycle MUST be strictly followed
- Tests MUST fail first, then implementation makes them pass
- No production code without corresponding tests

**Rationale**: Ensures code correctness, prevents regressions, and serves as living documentation.

### II. Simplicity and YAGNI

Every solution MUST be the simplest that works:
- No premature optimization or abstraction
- Implement only what is explicitly required
- No speculative features or "nice-to-haves"
- Prefer clear, straightforward code over clever solutions

**Rationale**: Reduces complexity, maintenance burden, and development time. Easier to understand and modify.

### III. In-Memory Storage First

For Phase I:
- All data MUST be stored in-memory (Python lists/dicts)
- No external databases or persistent storage
- Focus on core functionality and CLI interface
- Persistence can be added in future phases if needed

**Rationale**: Minimizes dependencies, accelerates development, and allows focus on business logic and user experience.

### IV. Python 3.13+ with UV

Technical stack requirements:
- Python 3.13 or higher MUST be used
- UV MUST be used for project initialization and dependency management
- Follow Python best practices and PEP standards
- Type hints SHOULD be used where they improve clarity

**Rationale**: Ensures modern Python features, fast dependency resolution, and maintainable code.

### V. CLI-First Interface

User interaction through command-line interface:
- Clear, numbered menu system for all operations
- Human-readable output with proper formatting
- Helpful messages for user actions
- Clean separation between UI and business logic

**Rationale**: Matches project requirements, simple to implement and test, no UI framework dependencies.

### VI. Explicit Task Requirements

Every task MUST be implemented exactly as specified:
- No deviation from task definitions
- All specified fields MUST be included
- All operations MUST be implemented as defined
- Edge cases MUST be handled per specification

**Rationale**: Ensures deliverables match expectations and prevents scope creep.

## Development Workflow

### Implementation Process

1. **Review Task**: Understand requirements and acceptance criteria
2. **Write Test**: Create test that validates the requirement (must fail)
3. **Implement**: Write minimal code to pass the test
4. **Refactor**: Clean up code while keeping tests green
5. **Validate**: Ensure all tests pass and requirement is met
6. **Commit**: Create atomic commit with clear message

### Code Organization

```text
src/
├── models/      # Data structures (Task model)
├── services/    # Business logic (add, update, delete, etc.)
└── cli/         # User interface (menu, display)

tests/
├── unit/        # Unit tests for individual functions
└── integration/ # Integration tests for complete workflows
```

### Quality Gates

Before any commit:
- All tests MUST pass
- Code MUST follow PEP 8 style guidelines
- No unused imports or dead code
- Clear, descriptive function and variable names

## Testing Requirements

### Test Coverage

- Every function MUST have corresponding unit tests
- Every user workflow MUST have integration tests
- Edge cases MUST be explicitly tested
- Error handling MUST be validated

### Test Structure

```python
# Given-When-Then pattern
def test_add_task_success():
    # Given: Initial state
    tasks = []

    # When: Action performed
    result = add_task(tasks, "Test task", "Description")

    # Then: Expected outcome
    assert len(tasks) == 1
    assert result["title"] == "Test task"
```

## Security and Validation

### Input Validation

- Task titles MUST NOT be empty
- Task IDs MUST be validated before operations
- Invalid inputs MUST produce clear error messages
- No silent failures

### Data Integrity

- Task IDs MUST be unique
- Task state MUST be consistent (completed: True/False only)
- No partial updates that leave data in inconsistent state

## Performance Standards

For Phase I (in-memory operations):
- All operations SHOULD complete in < 1ms
- No noticeable delay for user actions
- Efficient algorithms (avoid O(n²) where O(n) is possible)

**Note**: These are guidelines for this phase; different standards may apply for future phases with persistence.

## Governance

### Amendment Process

Constitution changes require:
1. Clear justification for the change
2. Impact analysis on existing code and templates
3. Update to all affected templates and documentation
4. Version increment following semantic versioning

### Compliance

- All pull requests MUST verify constitutional compliance
- Code reviews MUST check adherence to principles
- Violations MUST be justified in plan.md Complexity Tracking section
- No "temporary" violations - either follow principles or amend constitution

### Version Control

This constitution uses semantic versioning:
- **MAJOR**: Breaking changes to principles or governance
- **MINOR**: New principles or sections added
- **PATCH**: Clarifications or wording improvements

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
