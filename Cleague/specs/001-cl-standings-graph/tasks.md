---
description: "Task list for セ・リーグ順位推移グラフ implementation"
---

# Tasks: セ・リーグ順位推移グラフ

**Input**: Design documents from `/specs/001-cl-standings-graph/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are NOT explicitly requested in the feature specification, so test tasks are not included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/` at repository root
- Frontend uses static HTML/CSS/JS (no build step)
- Backend uses Python Flask

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure (frontend/, backend/src/, backend/tests/)
- [x] T002 Initialize Python virtual environment and create backend/requirements.txt with Flask, Flask-CORS, BeautifulSoup4, Requests
- [x] T003 [P] Create frontend/index.html with basic HTML structure and Chart.js CDN link
- [x] T004 [P] Create frontend/css/styles.css with basic styling
- [x] T005 [P] Create .gitignore for Python (venv/, __pycache__/, *.pyc)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create backend/src/models.py with Team and StandingsData dataclasses
- [x] T007 [P] Define TEAMS constant in backend/src/models.py with 6 Central League teams (id, name, shortName, color)
- [x] T008 [P] Create backend/src/scraper.py with fetch_npb_standings() function skeleton
- [x] T009 [P] Create backend/src/parser.py with parse_standings_html() function skeleton
- [x] T010 Create backend/src/api.py with Flask app initialization and CORS configuration
- [x] T011 [P] Create frontend/js/utils.js with date calculation functions (getCurrentSeasonDates, parseUrlParams)
- [x] T012 [P] Create frontend/js/api.js with API_BASE_URL constant and fetchStandings() function
- [x] T013 [P] Create frontend/js/chart.js with initChart() and updateChart() function skeletons
- [x] T014 Create frontend/js/main.js as entry point with DOMContentLoaded event listener

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - デフォルト期間での順位推移表示 (Priority: P1) 🎯 MVP

**Goal**: パラメータ指定なしで現在シーズンの順位推移グラフを表示

**Independent Test**: ブラウザでindex.htmlを開き、パラメータなしで現在シーズンのグラフが表示されることを確認

### Implementation for User Story 1

- [x] T015 [P] [US1] Implement scraper.py: fetch_npb_standings() to scrape NPB website for current season data
- [x] T016 [P] [US1] Implement parser.py: parse_standings_html() to extract standings data from HTML table
- [x] T017 [US1] Implement api.py: GET /api/standings endpoint (no parameters = current season)
- [x] T018 [US1] Implement api.py: GET /api/teams endpoint to return TEAMS constant
- [x] T019 [US1] Implement api.py: GET /api/health endpoint for health check
- [x] T020 [US1] Implement utils.js: getCurrentSeasonDates() to calculate current season start/end dates
- [x] T021 [US1] Implement api.js: fetchStandings() to call /api/standings and handle response
- [x] T022 [US1] Implement api.js: fetchTeams() to call /api/teams
- [x] T023 [US1] Implement chart.js: createChartData() to transform API response to Chart.js format
- [x] T024 [US1] Implement chart.js: initChart() to create Chart.js instance with proper configuration (Y-axis reversed, team colors)
- [x] T025 [US1] Implement chart.js: setupLegendClickHandler() for legend click to toggle team visibility
- [x] T026 [US1] Implement chart.js: setupTooltipConfig() to show team name, date, rank, wins/losses on hover
- [x] T027 [US1] Implement main.js: loadDefaultGraph() to fetch data and render chart on page load
- [x] T028 [US1] Update index.html: Add canvas element for chart, loading indicator, error message container
- [x] T029 [US1] Update styles.css: Style chart container, loading indicator, error messages
- [x] T030 [US1] Add error handling in api.js for network failures and API errors
- [x] T031 [US1] Add error handling in api.py for scraping failures with appropriate error responses

**Checkpoint**: At this point, User Story 1 should be fully functional - opening index.html shows current season standings graph

---

## Phase 4: User Story 2 - 特定年度の全期間順位推移表示 (Priority: P2)

**Goal**: 年度パラメータを指定して過去シーズンのグラフを表示

**Independent Test**: URL に ?year=2025 を追加して、2025年シーズン全体のグラフが表示されることを確認

### Implementation for User Story 2

- [ ] T032 [P] [US2] Update scraper.py: Add year parameter support to fetch_npb_standings()
- [ ] T033 [P] [US2] Update parser.py: Handle different year data formats if needed
- [ ] T034 [US2] Update api.py: Add year query parameter handling to /api/standings endpoint
- [ ] T035 [US2] Update api.py: Add validation for year parameter (1950-current year)
- [ ] T036 [US2] Update api.py: Return 404 error for future years or years without data
- [ ] T037 [US2] Update utils.js: Add parseUrlParams() to extract year from URL query string
- [ ] T038 [US2] Update utils.js: Add getSeasonDates(year) to calculate season dates for specific year
- [ ] T039 [US2] Update main.js: Check for year parameter and call appropriate data fetch
- [ ] T040 [US2] Update index.html: Add year input field or display current year parameter
- [ ] T041 [US2] Update styles.css: Style year parameter display/input

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently - can view current or past seasons

---

## Phase 5: User Story 3 - 特定期間の順位推移表示 (Priority: P3)

**Goal**: 年度と開始月・終了月を指定して特定期間のグラフを表示

**Independent Test**: URL に ?year=2025&startMonth=7&endMonth=9 を追加して、2025年7-9月のグラフが表示されることを確認

### Implementation for User Story 3

- [ ] T042 [P] [US3] Update api.py: Add startMonth and endMonth query parameter handling
- [ ] T043 [P] [US3] Update api.py: Add validation for month parameters (1-12, startMonth <= endMonth)
- [ ] T044 [P] [US3] Update api.py: Add validation for season period (March-October)
- [ ] T045 [US3] Update api.py: Return 400 error for invalid month combinations with descriptive messages
- [ ] T046 [US3] Update scraper.py: Filter data by date range based on startMonth/endMonth
- [ ] T047 [US3] Update utils.js: Add getSeasonDates(year, startMonth, endMonth) overload
- [ ] T048 [US3] Update utils.js: Add month validation logic
- [ ] T049 [US3] Update main.js: Handle startMonth and endMonth parameters from URL
- [ ] T050 [US3] Update index.html: Add month range input fields (start month, end month)
- [ ] T051 [US3] Update index.html: Add form submission handler for parameter changes
- [ ] T052 [US3] Update styles.css: Style month input fields and form

**Checkpoint**: All user stories should now be independently functional - full parameter support

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T053 [P] Add comprehensive error messages for all edge cases in api.py
- [ ] T054 [P] Add loading state management in main.js (show/hide loading indicator)
- [ ] T055 [P] Add responsive design to styles.css for mobile devices
- [ ] T056 [P] Add chart title with current period information in chart.js
- [ ] T057 [P] Optimize Chart.js configuration for performance (animation: false for large datasets)
- [ ] T058 [P] Add LocalStorage caching in api.js to reduce redundant API calls
- [ ] T059 [P] Add rate limiting consideration in scraper.py (1 second delay between requests)
- [ ] T060 [P] Add User-Agent header in scraper.py for polite scraping
- [ ] T061 [P] Create README.md with setup instructions based on quickstart.md
- [ ] T062 [P] Add comments to complex logic in scraper.py and parser.py
- [ ] T063 Validate all acceptance scenarios from spec.md manually
- [ ] T064 Run quickstart.md validation (setup and run locally)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Extends US1 but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Extends US1/US2 but independently testable

### Within Each User Story

- Backend tasks (scraper, parser, API) can be done in parallel with frontend tasks (utils, api.js, chart.js)
- API endpoint must be complete before frontend can test integration
- Chart.js configuration depends on data structure from API
- Error handling should be added after core functionality works

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Within each user story, backend and frontend tasks marked [P] can run in parallel
- All Polish tasks marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Backend team can work on these in parallel:
T015: Implement scraper.py
T016: Implement parser.py
T017-T019: Implement API endpoints

# Frontend team can work on these in parallel:
T020: Implement utils.js date functions
T021-T022: Implement api.js fetch functions
T023-T026: Implement chart.js functions
T028-T029: Update HTML/CSS

# Integration point: T027 (main.js) requires both backend and frontend to be ready
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T005)
2. Complete Phase 2: Foundational (T006-T014) - CRITICAL
3. Complete Phase 3: User Story 1 (T015-T031)
4. **STOP and VALIDATE**: Test User Story 1 independently
   - Open index.html in browser
   - Verify current season graph displays
   - Test legend click functionality
   - Test hover tooltips
   - Test error handling (disconnect network)
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP! 🎯)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add Polish → Final release
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T014)
2. Once Foundational is done:
   - Developer A (Backend): T015-T019, T031 (US1 backend)
   - Developer B (Frontend): T020-T030 (US1 frontend)
3. After US1 complete:
   - Developer A: US2 backend (T032-T036)
   - Developer B: US2 frontend (T037-T041)
4. After US2 complete:
   - Developer A: US3 backend (T042-T046)
   - Developer B: US3 frontend (T047-T052)
5. Both: Polish tasks (T053-T064) in parallel

---

## Task Count Summary

- **Total Tasks**: 64
- **Phase 1 (Setup)**: 5 tasks
- **Phase 2 (Foundational)**: 9 tasks (BLOCKING)
- **Phase 3 (US1 - MVP)**: 17 tasks
- **Phase 4 (US2)**: 10 tasks
- **Phase 5 (US3)**: 11 tasks
- **Phase 6 (Polish)**: 12 tasks

**Parallel Opportunities**: 38 tasks marked [P] can run in parallel within their phase

**MVP Scope**: Phases 1-3 (31 tasks) deliver a working application

---

## Notes

- [P] tasks = different files, no dependencies within phase
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Backend uses Flask for simplicity (no async needed for this scale)
- Frontend uses Vanilla JS (no framework) per Constitution's Simplicity principle
- Chart.js handles all graph rendering and interactivity
- No database needed - data fetched in real-time via scraping