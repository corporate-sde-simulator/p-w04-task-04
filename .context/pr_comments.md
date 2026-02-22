# PR Review - Distributed cache invalidation protocol (by Raj)

## Reviewer: Kavitha Rajan
---

**Overall:** Good foundation but critical bugs need fixing before merge.

### `cacheInvalidator.py`

> **Bug #1:** Invalidation broadcast uses fire-and-forget without confirming peers received the message
> This is the higher priority fix. Check the logic carefully and compare against the design doc.

### `peerManager.py`

> **Bug #2:** Version vector comparison is wrong because concurrent updates are treated as causal
> This is more subtle but will cause issues in production. Make sure to add a test case for this.

---

**Raj**
> Acknowledged. I have documented the issues for whoever picks this up.
