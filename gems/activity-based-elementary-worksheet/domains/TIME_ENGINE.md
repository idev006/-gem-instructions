# TIME_ENGINE — Time Calculation / Duration Rules

Version: 1.1.0
Status: PRODUCTION_CANDIDATE
Owning worker: `W02_TIME_CLOCK`
Registry authority: `domains/DOMAIN_REGISTRY.md`
Academic rules status: DETERMINISTIC_MATURE

## 1. Scope

Supports:

- start + duration → end
- end − duration → start
- start/end → elapsed duration
- compare two times
- simple schedule/table reasoning
- 12-hour/24-hour representation conversion when explicitly required
- controlled midnight crossing

Analog clock geometry remains in `CLOCK_READING_ENGINE.md` / W02 clock branch.

## 2. Parameters

`TIME_SUBDOMAIN, TIME_FORMAT, TIME_TASK_TYPE, START_TIME_RANGE, MIN_DURATION, MAX_DURATION, MINUTE_INTERVAL, TIME_CROSS_MIDNIGHT_ALLOWED, TARGET_ANSWER_SET, ANSWER_DISTRIBUTION, ANSWER_UNIT_MODE, ANSWER_TIME_FORMAT`

Default Thai elementary behavior:

- `TIME_FORMAT=24_HOUR` for calculation tables
- daytime activities
- midnight crossing disabled
- balanced answers
- answer key off

## 3. Canonical representation

Convert a valid time to minutes from day start:

`total_minutes = hour*60 + minute`

Valid minute: 00–59.

Same-day duration:

`duration = end_minutes - start_minutes`

Require positive duration unless zero duration is explicitly allowed.

Midnight-crossing mode:

`duration = (end_minutes + 1440 - start_minutes) % 1440`

Use this only when crossing is explicitly enabled or clearly required.

## 4. Transformations

Forward:

`end_minutes = start_minutes + duration_minutes`

Reverse:

`start_minutes = end_minutes - duration_minutes`

Normalize according to active day/crossing rules.

Duration decomposition:

`hours = duration // 60`
`minutes = duration % 60`

Independent verification must recompute the original relation after normalization.

## 5. Comparison/schedule

For times within the same stated day:

- earlier/later comparison uses canonical minute values;
- time difference = absolute or directional difference according to wording;
- schedules must preserve chronological order unless the learning objective explicitly asks students to detect inconsistency.

For multi-event schedules, do not infer unstated travel/duration intervals.

## 6. Granularity

`MINUTE_INTERVAL` controls generated values. Examples:

- 60 → whole hour
- 30 → half hour
- 15 → quarter hour
- 5 → five-minute increments
- 1 → minute precision

Generated starts, ends and durations must respect the intended granularity unless the task intentionally mixes them.

## 7. Difficulty/grade progression

Follow `MEASUREMENT_COVERAGE_P1_P6.md`.

Conservative AUTO progression:

- P1: simple whole-hour reading/calculation only when requested
- P2: familiar hour/minute increments, one-step contexts
- P3: start/end/duration with common 5/15/30-minute increments
- P4: mixed hours/minutes, regrouping, schedule comparisons
- P5: multi-step duration reasoning and controlled crossing contexts
- P6: multi-step schedule/time reasoning; midnight crossing only when objective supports it

Do not introduce midnight crossing merely because grade is high.

## 8. Answer-first generation

Choose a valid canonical relation first, then derive givens for the requested task type, independently recompute, and only then attach context.

Student-visible questions must not reveal hidden target answer values when key is off.

## 9. Render guidance

Time-calculation worksheets are normally text/table/numeric-heavy. Preferred final render path is `DOCUMENT_FIRST` unless the request requires themed visual composition that justifies HYBRID.

The final prompt must resolve one render path; do not emit alternatives.

## 10. QA

Prompt-phase gates:

`PROMPT_TIME_PARSE_QA`
`PROMPT_DURATION_QA`
`PROMPT_TIME_BOUNDS_QA`
`PROMPT_TIME_INTERVAL_QA`
`PROMPT_TIME_CROSSING_QA`
`PROMPT_TIME_FORWARD_REVERSE_QA`
`PROMPT_TIME_SCHEDULE_QA`
`PROMPT_TIME_UNIT_QA`
`PROMPT_MEASUREMENT_GRADE_APPROPRIATENESS_QA`
`STUDENT_VISIBLE_ANSWER_LEAK_QA`

Any incorrect time relation, invalid time syntax, forbidden crossing, or inconsistent schedule blocks prompt release.