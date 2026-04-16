# Repository Maintenance Workflow

This document records the minimum recurring maintenance workflow for `the-0.5-chronicles` now that the project has a stable site structure, GitHub Pages deployment, release history, and issue tracker setup.

## 1. Working Rule

Treat this repository as the canonical source for:

- the public site structure
- current chapter routing
- content-state behavior (`public`, `unlisted`, `draft`)
- GitHub-side project metadata and maintenance records

Do not rely on memory for structural decisions. If a routing, archive, or publishing rule becomes important enough to repeat, write it down here or in the README.

## 2. When To Cut A Release

Do not cut a release for every content edit. Cut a release when a batch of changes materially affects the public project shape or repository operation.

Typical release triggers:

- a new formal volume page, open-volume page, or Now Records entry point becomes part of the public structure
- a namespace migration, redirect layer, archive cleanup, or routing fix changes how readers reach material
- issue templates, workflows, labels, milestones, or repo metadata are materially updated
- a stable batch of chapter promotions or structural editorial work has landed and the public framing is coherent

Recommended release rule:

1. Land and verify the batch on `main`.
2. Confirm the GitHub Pages deployment is green.
3. Check the live site for the affected public routes.
4. Cut a tagged release with concise notes describing the structural or editorial milestone.

Use lightweight semantic versioning (`v0.x.y`) until the project reaches a more fixed publication model.

## 3. Minimum Verification Before Push Or Merge To `main`

Every change set that touches site behavior, content state, routing, or documentation should pass this minimum checklist.

Required:

1. Run `npm ci` if dependencies changed or the workspace is not known-good.
2. Run `npm run build`.
3. Review affected routes locally or by inspecting generated route output during build.
4. Check whether any edited content entry has the correct state:
   - `public`: listed normally
   - `unlisted`: routable but omitted from archive/index/RSS
   - `draft`: excluded from site build

Required when relevant:

1. If a volume page changes, confirm its chapter links point to the intended canonical routes.
2. If archive or migration namespaces change, verify compatibility redirects still resolve.
3. If `unlisted` or `draft` entries are moved, verify they do not accidentally leak into:
   - `/blog/`
   - `/rss.xml`
   - any curated public landing page that should not expose them
4. If GitHub workflow files change, inspect the workflow YAML and confirm the expected trigger still matches repo behavior.

Do not treat a green build alone as sufficient when the change is primarily editorial or navigational. Link behavior and content-state behavior matter separately.

## 4. Editorial And Content-State Handling

Use this repo’s three-state model consistently:

- `public`: ready to appear in archive, feeds, and ordinary navigation
- `unlisted`: readable and linkable, but intentionally outside archive/feed surfaces
- `draft`: still excluded from publication

Practical rule:

1. Write in `manuscripts/` when the material is still raw.
2. Move into `src/content/blog/` when the entry is part of the site-managed editorial flow.
3. Mark it `unlisted` if it should be readable in sequence before public promotion.
4. Promote to public only when the framing, route, and landing-page links are ready.

For archive namespaces:

- `vol-0-early-archive` is preserved as legacy draft/archive material and should stay intentionally unlisted unless there is a deliberate decision to make a piece public
- `vol-open-2026-2029` is the forward working line for 2026+ chapter-shaped material and should remain more cautious than formal volumes
- `Now Records` is for present-tense witness material, not the same thing as the open-volume chapter line

## 5. Issue, Label, Milestone, And Template Usage

Use GitHub issues to hold follow-up work that should survive across sessions.

Templates:

- `Bug Report`: for routing failures, build problems, broken pages, or incorrect content-state behavior
- `Editorial or Content Task`: for chapter work, structure cleanup, archive decisions, navigation updates, and documentation

Primary labels currently in use:

- `editorial`
- `volume`
- `open-volume`
- `archive`
- `now-records`
- `infrastructure`
- `priority-high`
- `priority-medium`
- `priority-low`
- `ready`

Usage rule:

1. Apply one scope label (`volume`, `open-volume`, `archive`, `now-records`, or `infrastructure`) where possible.
2. Apply a priority label for triage.
3. Add `editorial` when the work is fundamentally about content, framing, or chapter organization.
4. Add `ready` only when the issue is well-scoped enough to execute without rediscovery.

Milestones should reflect delivery tranches rather than individual commits. Current milestone groups are:

- `Repository and Infrastructure`
- `Formal Volumes I-IV`
- `Open Volume and Now Records`
- `Legacy Archive and Migration`

Close issues only after:

- the repo change is merged or pushed
- the relevant build verification is complete
- any needed GitHub-side follow-up is also done

## 6. GitHub-Side Checks To Review Periodically

Check these whenever a structural change lands, a release is cut, or deployment behavior changes:

1. Repository About section:
   - description
   - homepage URL
   - topics
2. GitHub Pages:
   - source remains GitHub Actions
   - custom domain and HTTPS stay healthy
3. Actions:
   - latest deploy run on `main` is green
   - artifact/deploy steps still complete successfully
4. Issue tracker hygiene:
   - templates still match actual repo workflows
   - labels and milestones still reflect current structure
5. Release hygiene:
   - latest tag matches a real structural milestone
   - release notes describe what changed in public-facing or repo-operational terms
6. README and badges:
   - site URL is current
   - deploy badge still resolves
   - canonical repo name and links remain correct

## 7. Practical Maintenance Rhythm

Use this as the default sequence for non-trivial repo work:

1. Open or update an issue if the work should be tracked.
2. Make the repo/content/routing changes.
3. Run `npm run build`.
4. Review routes, content-state behavior, and any touched public entry pages.
5. Push to `main`.
6. Watch the GitHub Pages deployment.
7. Verify the live site for the affected URLs if the change is public-facing.
8. Comment on and close the related issue.
9. Cut a release if the batch changed the public project shape or repo operating model.

## 8. Related Files

- `README.md`
- `STRUCTURE_MIGRATION_2026-04.md`
- `.github/workflows/deploy.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/editorial_task.yml`
- `.github/pull_request_template.md`
