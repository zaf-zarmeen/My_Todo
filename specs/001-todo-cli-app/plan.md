# Implementation Plan: Todo CLI App

**Branch**: `001-todo-cli-app` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/001-todo-cli-app/spec.md`

## Summary

Build a Python CLI application for managing todo tasks in memory. The application provides complete CRUD operations (Create, Read, Update, Delete) plus status toggling through a numbered menu interface. All data stored in-memory using Python lists with no external dependencies beyond Python 3.13+ and UV.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (Python standard library only)
**Storage**: In-memory (Python list)
**Testing**: pytest
**Target Platform**: Cross-platform (Windows, Linux, macOS) command-line terminals
**Project Type**: Single project (standalone CLI application)
**Performance Goals**: < 1ms per operation for in-memory CRUD operations
**Constraints**: No persistence, < 100ms user-perceived response time, single-user local execution
**Scale/Scope**: Handle 1000+ tasks efficiently, ~300 LOC for core functionality

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### ✅ I. Test-First Development (NON-NEGOTIABLE)
- **Status**: COMPLIANT
- **Implementation**: pytest will be used, tests written before implementation
- **Verification**: Red-Green-Refactor cycle enforced in tasks.md workflow

### ✅ II. Simplicity and YAGNI
- **Status**: COMPLIANT
- **Implementation**: No premature abstractions, using Python list (not database), no external libraries beyond pytest
- **Verification**: Only implementing 5 core operations from spec, no extras

### ✅ III. In-Memory Storage First
- **Status**: COMPLIANT
- **Implementation**: Tasks stored in Python list, IDs tracked with counter variable
- **Verification**: No file I/O or database code

### ✅ IV. Python 3.13+ with UV
- **Status**: COMPLIANT
- **Implementation**: Project initialized with UV, Python 3.13+ required
- **Verification**: pyproject.toml specifies Python >=3.13

### ✅ V. CLI-First Interface
- **Status**: COMPLIANT
- **Implementation**: Numbered menu (1-5, 0=Exit), clear text prompts and output
- **Verification**: Clean separation: cli/ for UI, services/ for logic

### ✅ VI. Explicit Task Requirements
- **Status**: COMPLIANT
- **Implementation**: All 10 functional requirements (FR-001 to FR-010) will be implemented exactly as specified
- **Verification**: Each task in tasks.md maps to specific FR

**Gate Result**: ✅ PASS - No constitutional violations. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-cli-app/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification
├── research.md          # Phase 0 output (no research needed - straightforward implementation)
├── data-model.md        # Phase 1 output (Task entity definition)
├── quickstart.md        # Phase 1 output (how to run the app)
├── contracts/           # Phase 1 output (not applicable - no API contracts for CLI)
└── checklists/          # Quality validation checklists
    └── requirements.md  # Spec validation checklist
```

### Source Code (repository root)

```text
src/
├── models/
│   └── task.py          # Task dataclass with id, title, description, completed
├── services/
│   └── task_service.py  # CRUD operations: add, get_all, update, delete, toggle_complete
└── cli/
    ├── menu.py          # Display menu, get user input, main loop
    └── display.py       # Format and display tasks, messages

tests/
├── unit/
│   ├── test_task_model.py      # Task creation, validation
│   ├── test_task_service.py    # Each CRUD operation, edge cases
│   └── test_cli_display.py     # Display formatting
└── integration/
    └── test_full_workflow.py   # Complete user journey: add→view→update→delete→toggle

pyproject.toml           # UV project config, Python 3.13+ requirement
README.md                # Project overview, installation, usage
```

**Structure Decision**: Single project structure selected because:
- Simple standalone CLI application
- No frontend/backend separation needed
- No API or web components
- Minimal complexity aligns with YAGNI principle

## Complexity Tracking

> **No violations detected** - Constitution Check passed all gates.

No complexity tracking required.

## Phase 0: Research

**Status**: Not required for this feature

**Rationale**:
- Python standard library usage is well-documented
- In-memory storage with Python list is straightforward
- CLI input/output using built-in `input()` and `print()`
- pytest is standard Python testing framework
- No architectural decisions or technology choices requiring research

All technical context is complete and unambiguous. Proceeding directly to Phase 1.

## Phase 1: Design & Contracts

### Data Model

See [data-model.md](./data-model.md) for complete entity definitions.

**Summary**:
- **Task** entity with 4 fields: id (int), title (str), description (str|None), completed (bool)
- Validation: title required (non-empty), description optional
- State transitions: completed can toggle between True/False
- ID generation: Auto-increment counter starting at 1

### Contracts

**Not applicable** - CLI application has no API contracts. User interactions are terminal-based menu selections and text input.

The "contract" is the menu interface:
- Input: User selects number (0-5) or enters text when prompted
- Output: Formatted text display or error messages

See [quickstart.md](./quickstart.md) for user interaction patterns.

### Architecture Decisions

**Storage Architecture**:
- **Decision**: Single global list + counter variable
- **Rationale**: Simplest solution for in-memory storage, meets all requirements
- **Alternatives considered**: Dictionary (unnecessarily complex), class-based store (premature abstraction)

**Module Organization**:
- **Decision**: Three modules (models, services, cli) with clear separation
- **Rationale**: Clean architecture, testable, follows constitution's code organization
- **Alternatives considered**: Single file (unmaintainable), more modules (over-engineering)

**Error Handling**:
- **Decision**: Return error messages as strings, display in CLI layer
- **Rationale**: Simple, testable, no exception overhead for expected errors
- **Alternatives considered**: Exceptions (overkill for validation), error codes (less clear)

**ID Generation**:
- **Decision**: Global counter variable, never decrement on delete
- **Rationale**: Meets "IDs never reused" requirement, simplest implementation
- **Alternatives considered**: UUID (unnecessarily complex), reusing IDs (violates spec)

## Phase 2: Task Planning

**Scope**: Task breakdown will be created using `/sp.tasks` command after this plan is approved.

**Approach**:
- Follow TDD strictly: tests first, then implementation
- Organize tasks by User Story 1 phases (Setup, Foundation, Implementation)
- Leverage parallel opportunities: models and tests can run concurrently
- Each task maps to specific functional requirements (FR-001 to FR-010)

See `tasks.md` (generated by `/sp.tasks` command) for complete task breakdown.

## Implementation Notes

### Testing Strategy

1. **Unit Tests** (test individual functions):
   - Task model validation
   - Each service operation (add, update, delete, toggle, get_all)
   - Display formatting functions
   - Edge cases: empty title, invalid ID, no tasks

2. **Integration Tests** (test complete workflows):
   - Full user journey: add multiple tasks → view → update one → delete one → toggle status
   - Error handling flows: attempt invalid operations, verify error messages

### Development Sequence

1. **Phase 1: Setup** (T-001)
   - Initialize with UV: `uv init`
   - Configure pyproject.toml with Python >=3.13
   - Add pytest dependency

2. **Phase 2: Foundation** (T-002 to T-004)
   - Create Task model (T-002)
   - Implement in-memory storage structure (T-003)
   - Set up test framework (T-004)

3. **Phase 3: Core Operations** (T-005 to T-009)
   - Add task (T-005): Write tests → Fail → Implement → Pass
   - View tasks (T-006): Write tests → Fail → Implement → Pass
   - Update task (T-007): Write tests → Fail → Implement → Pass
   - Delete task (T-008): Write tests → Fail → Implement → Pass
   - Toggle completion (T-009): Write tests → Fail → Implement → Pass

4. **Phase 4: CLI Integration** (T-010)
   - Build menu system, integrate with services
   - Add error handling and user messages

### Quality Assurance

- All tests must pass before any commit
- Code follows PEP 8 style guidelines
- Type hints used for function signatures
- Clear variable names (no abbreviations)
- No dead code or unused imports

### Success Validation

Before marking complete, verify:
- ✅ All 10 functional requirements (FR-001 to FR-010) implemented
- ✅ All 6 success criteria (SC-001 to SC-006) met
- ✅ All edge cases handled per specification
- ✅ Test coverage: every function has unit tests, workflows have integration tests
- ✅ Constitution compliance: TDD followed, simplicity maintained, CLI-first

## Dependencies

**External**:
- Python 3.13+ (user must install)
- UV (user must install)

**Development**:
- pytest (managed by UV)

**Internal**: None

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| ID collision after many delete operations | Low | Medium | Use counter that never decrements; test with 1000+ tasks |
| Performance degradation with large task lists | Low | Low | Use efficient O(n) algorithms; test with 1000+ tasks per SC-005 |
| Input validation gaps | Medium | Medium | Comprehensive edge case testing in unit tests |
| Menu navigation confusion | Low | Low | Clear numbered menu, helpful messages per NFR-005 |

## Next Steps

1. ✅ Approve this plan
2. Generate detailed task breakdown: `/sp.tasks`
3. Review and approve tasks.md
4. Begin implementation following TDD workflow
5. After completion: `/sp.git.commit_pr` to create PR
