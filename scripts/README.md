# Profile generators

`Update profile visuals` runs daily at 04:17 UTC (12:17 Asia/Shanghai), on relevant
script changes, and through the Actions **Run workflow** button. Scheduled runs
may be delayed by GitHub.

## Writing

`python3 scripts/update-writing.py` fetches the public Juejin profile, all article
pages, and all column pages. It updates only the `writing:start` / `writing:end`
region in the root README: article and view totals, three latest columns by
creation date, the top three articles by views, and three latest articles by
publication date. Popular and latest lists are ranked independently and can
overlap. Latest articles appear before popular articles. Each article shows views
and likes inline after its title as 👀 and 👍; publication dates are used for sorting only.
Compact lists keep metadata inline and put archive links beside group labels.
Newly created empty columns are included with zero articles and zero cumulative reads.
Column reads are the sum of current views of all unique member articles, shown
with 👀; this is not column-page traffic or unique visitors. Incomplete
membership aborts the update rather than publishing a partial total. The Vue
series retains its source link inline. Followers are not displayed.

No Juejin cookie or secret is needed. Requests retry three times. If the API fails
or returns incomplete data, the README is not written and the Writing job fails
visibly. The independent visual-generation job can still complete. A later run
retries the sync. Unchanged content produces no commit; README-only updates do
not match this workflow's push paths.

The job commits changes to `main`, rebasing on concurrent changes before pushing.
Conflicts fail safely without a force push. The existing workflow token needs
`contents: write`; branch protection must permit these bot commits.

Run updater checks with:

```sh
python3 -m unittest discover -s scripts -p 'test_update_writing.py'
```
