---

description: "Task list for Todo CLI App implementation"
---

# Tasks: Todo CLI App

**Input**: Design documents from `specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md (required)

**Tests**: INCLUDED - TDD is mandatory per project constitution (Test-First Development NON-NEGOTIABLE)

**Organization**: Tasks follow TDD workflow - tests written FIRST, implementation SECOND, organized by functional area.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: User Story label (US1 = User Story 1 - Manage Task Lifecycle)
- Include exact file paths in descriptions

## Path Conventions

Single project structure:
- `src/models/` - Data models
- `src/services/` - Business logic
- `src/cli/` - User interface
- `tests/unit/` - Unit tests
- `tests/integration/` - Integration tests

---

## Phase 1: Setup

**Purpose**: Project initialization and structure

- [ ] T001 Initialize Python project with UV ensuring Python 3.13+ compatibility
- [ ] T002 [P] Configure pyproject.toml with Python >=3.13 requirement
- [ ] T003 [P] Add pytest as development dependency via UV
- [ ] T004 [P] Create project directory structure: src/models/, src/services/, src/cli/, tests/unit/, tests/integration/
- [ ] T005 [P] Create empty __init__.py files in src/, src/models/, src/services/, src/cli/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before implementation

**⚠️ CRITICAL**: No feature implementation can begin until this phase is complete

- [ ] T006 [US1] Write unit test for Task model creation with valid data in tests/unit/test_task_model.py
- [ ] T007 [P] [US1] Write unit test for Task model with empty title validation (must fail) in tests/unit/test_task_model.py
- [ ] T008 [P] [US1] Write unit test for Task model with only title (description=None) in tests/unit/test_task_model.py
- [ ] T009 [P] [US1] Write unit test for Task model default completed=False in tests/unit/test_task_model.py
- [ ] T010 [US1] Implement Task dataclass in src/models/task.py with id, title, description, completed fields
- [ ] T011 [US1] Implement in-memory storage structure (tasks list and next_id counter) in src/services/task_service.py

**Checkpoint**: Foundation ready - TDD tests exist and implementation tasks can proceed

---

## Phase 3: User Story 1 - Manage Task Lifecycle (Priority: P1) 🎯 MVP

**Goal**: Complete CRUD operations + status toggle for task management through CLI

**Independent Test**: Run CLI, add tasks, view them, update, delete, and toggle completion status. Verify all operations work correctly.

### Add Task Functionality (FR-001, FR-002, FR-003, FR-008)

**TDD Workflow**: Write tests FIRST → Verify they FAIL → Implement → Verify tests PASS

- [ ] T012 [P] [US1] Write unit test for add_task with valid title and description in tests/unit/test_task_service.py
- [ ] T013 [P] [US1] Write unit test for add_task with title only (no description) in tests/unit/test_task_service.py
- [ ] T014 [P] [US1] Write unit test for add_task with empty title (must return error) in tests/unit/test_task_service.py
- [ ] T015 [P] [US1] Write unit test for add_task ID auto-increment behavior in tests/unit/test_task_service.py
- [ ] T016 [P] [US1] Write unit test for add_task default status=Pending in tests/unit/test_task_service.py
- [ ] T017 [US1] Implement add_task function in src/services/task_service.py with title validation and ID generation
- [ ] T018 [US1] Verify all add_task tests pass - run pytest tests/unit/test_task_service.py::test_add*

### View Tasks Functionality (FR-004)

- [ ] T019 [P] [US1] Write unit test for get_all_tasks with existing tasks in tests/unit/test_task_service.py
- [ ] T020 [P] [US1] Write unit test for get_all_tasks with empty task list in tests/unit/test_task_service.py
- [ ] T021 [US1] Implement get_all_tasks function in src/services/task_service.py
- [ ] T022 [US1] Verify all get_all_tasks tests pass - run pytest tests/unit/test_task_service.py::test_get*

### Update Task Functionality (FR-005, FR-009)

- [ ] T023 [P] [US1] Write unit test for update_task with valid ID and new title in tests/unit/test_task_service.py
- [ ] T024 [P] [US1] Write unit test for update_task with valid ID and new description in tests/unit/test_task_service.py
- [ ] T025 [P] [US1] Write unit test for update_task with both title and description in tests/unit/test_task_service.py
- [ ] T026 [P] [US1] Write unit test for update_task with invalid ID (must return error) in tests/unit/test_task_service.py
- [ ] T027 [P] [US1] Write unit test for update_task with no fields provided (must return error) in tests/unit/test_task_service.py
- [ ] T028 [US1] Implement update_task function in src/services/task_service.py with ID validation
- [ ] T029 [US1] Verify all update_task tests pass - run pytest tests/unit/test_task_service.py::test_update*

### Delete Task Functionality (FR-006, FR-009)

- [ ] T030 [P] [US1] Write unit test for delete_task with valid ID in tests/unit/test_task_service.py
- [ ] T031 [P] [US1] Write unit test for delete_task with invalid ID (must return error) in tests/unit/test_task_service.py
- [ ] T032 [P] [US1] Write unit test for delete_task verifying ID not reused in tests/unit/test_task_service.py
- [ ] T033 [US1] Implement delete_task function in src/services/task_service.py with ID validation
- [ ] T034 [US1] Verify all delete_task tests pass - run pytest tests/unit/test_task_service.py::test_delete*

### Toggle Completion Functionality (FR-007, FR-009)

- [ ] T035 [P] [US1] Write unit test for toggle_complete with valid ID (Pending → Completed) in tests/unit/test_task_service.py
- [ ] T036 [P] [US1] Write unit test for toggle_complete with valid ID (Completed → Pending) in tests/unit/test_task_service.py
- [ ] T037 [P] [US1] Write unit test for toggle_complete with invalid ID (must return error) in tests/unit/test_task_service.py
- [ ] T038 [US1] Implement toggle_complete function in src/services/task_service.py with ID validation
- [ ] T039 [US1] Verify all toggle_complete tests pass - run pytest tests/unit/test_task_service.py::test_toggle*

### CLI Display Module (NFR-005, FR-010)

- [ ] T040 [P] [US1] Write unit test for display_tasks with multiple tasks in tests/unit/test_cli_display.py
- [ ] T041 [P] [US1] Write unit test for display_tasks with empty list in tests/unit/test_cli_display.py
- [ ] T042 [P] [US1] Write unit test for display_error_message in tests/unit/test_cli_display.py
- [ ] T043 [P] [US1] Write unit test for display_success_message in tests/unit/test_cli_display.py
- [ ] T044 [US1] Implement display_tasks function in src/cli/display.py with formatted output
- [ ] T045 [US1] Implement display_error_message and display_success_message functions in src/cli/display.py
- [ ] T046 [US1] Verify all display tests pass - run pytest tests/unit/test_cli_display.py

### CLI Menu Integration (NFR-001, NFR-002)

- [ ] T047 [US1] Implement display_menu function in src/cli/menu.py showing numbered options (1-5, 0=Exit)
- [ ] T048 [US1] Implement get_user_input function in src/cli/menu.py for menu selection
- [ ] T049 [US1] Implement handle_add_task function in src/cli/menu.py calling task_service.add_task
- [ ] T050 [US1] Implement handle_view_tasks function in src/cli/menu.py calling task_service.get_all_tasks
- [ ] T051 [US1] Implement handle_update_task function in src/cli/menu.py calling task_service.update_task
- [ ] T052 [US1] Implement handle_delete_task function in src/cli/menu.py calling task_service.delete_task
- [ ] T053 [US1] Implement handle_toggle_complete function in src/cli/menu.py calling task_service.toggle_complete
- [ ] T054 [US1] Implement main_loop function in src/cli/menu.py with menu display and option routing
- [ ] T055 [US1] Add error handling for invalid menu selections in src/cli/menu.py

### Integration Testing (Complete Workflow)

- [ ] T056 [US1] Write integration test for complete workflow: add → view → update → delete in tests/integration/test_full_workflow.py
- [ ] T057 [US1] Write integration test for toggle completion workflow in tests/integration/test_full_workflow.py
- [ ] T058 [US1] Write integration test for error handling: empty title, invalid ID in tests/integration/test_full_workflow.py
- [ ] T059 [US1] Write integration test for ID non-reuse after deletion in tests/integration/test_full_workflow.py
- [ ] T060 [US1] Write integration test for handling 1000+ tasks (performance validation) in tests/integration/test_full_workflow.py
- [ ] T061 [US1] Run all integration tests - verify pytest tests/integration/ passes

**Checkpoint**: User Story 1 complete - all CRUD + toggle operations functional and tested

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Final touches and documentation

- [ ] T062 [P] Create README.md with installation instructions, usage guide, and examples
- [ ] T063 [P] Add user-friendly welcome message and exit message in src/cli/menu.py
- [ ] T064 [P] Add input prompts with clear instructions for each operation in src/cli/menu.py
- [ ] T065 [P] Format task display with visual indicators (✓ for completed, ⏳ for pending) in src/cli/display.py
- [ ] T066 [P] Add confirmation prompt for delete operation in src/cli/menu.py
- [ ] T067 Run complete test suite - verify pytest runs all tests successfully
- [ ] T068 Run PEP 8 style check - ensure code follows Python style guidelines
- [ ] T069 Verify all 10 functional requirements (FR-001 to FR-010) are implemented
- [ ] T070 Verify all 6 success criteria (SC-001 to SC-006) are met

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all feature implementation
- **User Story 1 (Phase 3)**: Depends on Foundational phase completion
  - Tests MUST be written before implementation within each functional area
  - Within each functional area: Tests → Verify FAIL → Implement → Verify PASS
- **Polish (Phase 4)**: Depends on User Story 1 completion

### TDD Workflow Within Each Functional Area

**CRITICAL**: Follow strict TDD Red-Green-Refactor cycle

1. **Red Phase**: Write tests FIRST (T012-T016 for add_task)
2. **Verify Red**: Run tests, confirm they FAIL (no implementation yet)
3. **Green Phase**: Implement feature (T017 for add_task)
4. **Verify Green**: Run tests (T018), confirm they PASS
5. **Refactor**: Clean up code while keeping tests green
6. **Move to next functional area**: Repeat Red-Green-Refactor

### Task Dependencies Within User Story 1

**Test Dependencies** (must write tests before implementation):
- T012-T016 (add_task tests) → T017 (add_task implementation)
- T019-T020 (get_all tests) → T021 (get_all implementation)
- T023-T027 (update tests) → T028 (update implementation)
- T030-T032 (delete tests) → T033 (delete implementation)
- T035-T037 (toggle tests) → T038 (toggle implementation)
- T040-T043 (display tests) → T044-T045 (display implementation)

**Implementation Dependencies** (must complete prerequisite implementations):
- T010-T011 (Task model + storage) → T017 (add_task implementation)
- T017 (add_task) → T021 (get_all) - needs tasks to retrieve
- T017, T021 (add + get_all) → T028 (update) - needs task retrieval
- T017, T021 (add + get_all) → T033 (delete) - needs task retrieval
- T017, T021 (add + get_all) → T038 (toggle) - needs task retrieval
- T017, T021, T028, T033, T038 (all service functions) → T047-T055 (CLI integration)
- T044-T045 (display functions) → T047-T055 (CLI integration)
- All unit tests + implementations → T056-T061 (integration tests)

### Parallel Opportunities

**Setup Phase** (all can run in parallel):
- T002, T003, T004, T005 can run simultaneously

**Test Writing** (parallel within each functional area):
- Add task tests: T012, T013, T014, T015, T016 (all parallel)
- View task tests: T019, T020 (parallel)
- Update task tests: T023, T024, T025, T026, T027 (all parallel)
- Delete task tests: T030, T031, T032 (all parallel)
- Toggle task tests: T035, T036, T037 (all parallel)
- Display tests: T040, T041, T042, T043 (all parallel)

**Polish Phase** (most can run in parallel):
- T062, T063, T064, T065, T066 can run simultaneously

---

## Parallel Example: Add Task TDD Cycle

```bash
# Red Phase: Write all tests in parallel
Task T012: "Write unit test for add_task with valid title and description"
Task T013: "Write unit test for add_task with title only"
Task T014: "Write unit test for add_task with empty title (must fail)"
Task T015: "Write unit test for add_task ID auto-increment"
Task T016: "Write unit test for add_task default status=Pending"

# Verify Red: Run tests (should ALL FAIL - no implementation yet)
pytest tests/unit/test_task_service.py::test_add* --verbose

# Green Phase: Implement feature (sequential - single file)
Task T017: "Implement add_task function in src/services/task_service.py"

# Verify Green: Run tests (should ALL PASS now)
Task T018: "Verify all add_task tests pass"
pytest tests/unit/test_task_service.py::test_add* --verbose
```

---

## Implementation Strategy

### MVP First (Strict TDD Approach)

1. **Complete Phase 1**: Setup (T001-T005)
2. **Complete Phase 2**: Foundational (T006-T011)
   - Write Task model tests FIRST
   - Verify tests FAIL
   - Implement Task model
   - Verify tests PASS
3. **Complete Phase 3 using TDD cycle for each functional area**:
   - **Add Task**: T012-T016 (tests) → verify FAIL → T017-T018 (implement + verify PASS)
   - **View Tasks**: T019-T020 (tests) → verify FAIL → T021-T022 (implement + verify PASS)
   - **Update Task**: T023-T027 (tests) → verify FAIL → T028-T029 (implement + verify PASS)
   - **Delete Task**: T030-T032 (tests) → verify FAIL → T033-T034 (implement + verify PASS)
   - **Toggle Complete**: T035-T037 (tests) → verify FAIL → T038-T039 (implement + verify PASS)
   - **CLI Display**: T040-T043 (tests) → verify FAIL → T044-T046 (implement + verify PASS)
   - **CLI Menu**: T047-T055 (implementation - menu integration)
   - **Integration Tests**: T056-T061 (end-to-end validation)
4. **Complete Phase 4**: Polish (T062-T070)
5. **STOP and VALIDATE**: Run full test suite, verify all requirements met

### Constitution Compliance Checkpoints

**After each TDD cycle, verify**:
- ✅ Tests written BEFORE implementation (Test-First Development)
- ✅ Tests failed first (Red phase confirmed)
- ✅ Implementation made tests pass (Green phase confirmed)
- ✅ Code is simplest solution (YAGNI principle)
- ✅ No premature abstractions or optimizations

---

## Notes

- **[P]** tasks = different files, no dependencies, can run in parallel
- **[US1]** label = User Story 1 (Manage Task Lifecycle)
- **TDD CRITICAL**: Tests MUST be written before implementation - violations break constitution
- **Red-Green-Refactor**: Verify tests FAIL before implementing, then verify PASS after
- Each functional area follows complete TDD cycle before moving to next
- Integration tests come AFTER all unit tests and implementations complete
- Commit after each TDD cycle (Red → Green → Refactor)
- Stop at any checkpoint to validate independently
- All tasks map to specific FR (Functional Requirements) from spec.md

---

## Task Count Summary

- **Phase 1 (Setup)**: 5 tasks
- **Phase 2 (Foundational)**: 6 tasks
- **Phase 3 (User Story 1)**: 50 tasks
  - Add Task: 7 tasks (5 tests + 1 impl + 1 verify)
  - View Tasks: 4 tasks (2 tests + 1 impl + 1 verify)
  - Update Task: 7 tasks (5 tests + 1 impl + 1 verify)
  - Delete Task: 5 tasks (3 tests + 1 impl + 1 verify)
  - Toggle Complete: 5 tasks (3 tests + 1 impl + 1 verify)
  - CLI Display: 7 tasks (4 tests + 2 impl + 1 verify)
  - CLI Menu: 9 tasks (implementation + error handling)
  - Integration: 6 tasks (5 tests + 1 verify)
- **Phase 4 (Polish)**: 9 tasks
- **Total**: 70 tasks

**Parallel Opportunities**: 35+ tasks can run in parallel (marked with [P])

**TDD Cycles**: 6 major cycles (Task model, Add, View, Update, Delete, Toggle, Display)
