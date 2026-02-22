# PLATFORM-2898: Investigate stale data in distributed cache

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 26 · **Story Points:** 8
**Reporter:** Priya Menon (Backend Lead) · **Assignee:** You (Intern)
**Labels:** `backend`, `python`, `caching`, `investigation`
**Task Type:** Code Debugging

---

## Description

Users are seeing stale data after cache invalidation. When an item is updated in the database, the cache invalidation fires but some nodes in the cluster continue serving old data for 10-15 seconds.

**DEBUGGING task — no hint comments in the code.**

## Symptoms

- UPDATE to product price reflects in DB immediately but cache returns old price
- Invalidation log shows message sent but peer nodes don't seem to process it
- Problem gets worse under high concurrency (10+ simultaneous invalidations)
- Cache stats show items are being re-added to cache immediately after invalidation

## Acceptance Criteria

- [ ] Root cause found and fixed
- [ ] All unit tests pass
