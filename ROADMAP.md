# Orbit Roadmap

Orbit is my personal **Life OS**. It starts with solving the calendar/booking problem, then grows into an integrated system for tasks, notes, and intelligent assistance. This roadmap outlines the vision, scope, and progression from pre-alpha to v3.1.

---

## 🚧 Pre-Alpha (Proof of Concept)

**Vision:** Validate Orbit as a stand-alone master calendar.  
**Scope:**

- Basic Postgres schema (`users`, `calendars`, `events`, `bookings`).
- FastAPI backend with simple CRUD endpoints.
- Flutter frontend showing a unified calendar view.
- Manual event creation (no sync).
- Primitive booking page (public URL to pick slots).

---

## 🧪 Alpha

**Vision:** Orbit can act as _the_ master calendar across all sources.  
**Scope:**

- Read-only sync from external calendars (Google, Outlook, Zoho, Yahoo, etc.).
- Recurring events supported via `recurrence_rules`.
- 15-minute bookings validated against availability.
- Archival strategy: old events auto-deleted or moved to archive table.
- Public booking page styled minimally but functional.
- Deployment on Railway; CI/CD with GitHub.

---

## 🔬 Beta

**Vision:** External users can actually rely on Orbit, not just me.  
**Scope:**

- User authentication (multi-user).
- Stable sync adapters for major providers (Google + Outlook first).
- Invitations via email: external attendees can RSVP.
- Time-zone handling (storage in TIMESTAMP WITH TIME ZONE).
- Frontend polish (Flutter web + mobile both usable).
- Unit + integration tests for core booking logic.
- Begin collecting feedback from trusted testers.

---

## 🧭 Gamma

**Vision:** Orbit is usable day-to-day without hacks.  
**Scope:**

- Booking rules (working hours, buffer time, slot limits).
- Event categories/tags for better filtering.
- Small analytics: # events, booking stats, simple summaries.
- Notifications (email or app push when booking created).
- Better error handling and monitoring.
- Quality-of-life frontend UX polish.

---

## 🚀 Release Candidate (RC)

**Vision:** First stable baseline of Orbit calendar.  
**Scope:**

- Core features consolidated; bugs crushed.
- DB schema freeze for v1.0.
- Documentation for self-host deploys.
- Reliability hardening (rate limits, health checks).
- Final pre-launch usability pass.

---

## 🌍 Orbit v1.0 — Master Calendar with Booking

**Vision:** A one-stop **master calendar with personal booking page**:  
flexible, simple, under my control.  
**Scope:**

- Dependable event sync + recurring events.
- Lean booking page (public link).
- Read-only integration from all external calendars.
- Write-only for invitations (Orbit doesn’t push back to providers).
- Automated cleanup of expired events.
- Orbit is a trustworthy single source of truth for my time.

---

## 🗂 Orbit v2.0 — Calendar + Kanban

**Vision:** **Tasks + Calendar unified.** Orbit becomes my daily organizer.  
**Scope:**

- Task/board system (Trello-like Kanban).
- Link tasks to events (drag task into calendar slot).
- Task + calendar unified visualization.
- Task deadlines reflected in calendar automatically.
- Core productivity loop: schedule <-> execute <-> reflect.

---

## 📝 Orbit v2.1 — Notes + Kanban Integration

**Vision:** **Notion-lite experience inside Orbit.** Notes/tasks/calendar all talk to each other.  
**Scope:**

- Notes pages with text + task lists.
- Linking: meeting → notes, notes → calendar event, task → notes.
- Kanban cards evolve into richer documents.
- Knowledge vault integrated with time/task layer.
- Goal: eliminate context-switching across Notion, Trello, Calendar.

---

## 🤖 Orbit v3.0 — AI Copilot

**Vision:** Orbit transforms into my **AI-powered executive assistant.**  
**Scope:**

- AI agent monitors tasks, notes, calendar.
- Proactive suggestions:
  - Create work blocks automatically.
  - Detect overload, propose reschedules.
  - Prompt me about overdue tasks.
- Full LLM integration (latest available at the time).
- Personalized behavioral patterns learned from past.

---

## 🏗 Orbit v3.1 — Enterprise-Grade Life OS

**Vision:** Orbit runs my life **autonomously.** I don’t “use Orbit,” I _live inside Orbit._  
**Scope:**

- Enterprise-grade reliability and sync.
- API integrations into all major life/work tools.
- Auto-scheduling + auto-rescheduling.
- Habit tracking, time analytics, energy management.
- Stable daily driver: Orbit handles logistics; I focus on living.

---

# ✨ North Star

Orbit shouldn’t compete as a “shitty Outlook clone.”  
It’s not just a calendar, kanban, or notes app.  
Orbit is **the OS for me**:

- My data, my rules.
- Unified calendar + tasks + knowledge.
- Intelligent assistant that improves _my_ life, not ad revenue.
