# Iteration: Research Brief Checker

## What Went Wrong
During my first demonstration, I used my research-brief-check skill to review a research brief about the volatility risk premium. The checker retrieved source abstracts through my AlphaSearch tool and identified several unsupported or overstated claims. The checker reviewed 12 claims, but Claim 12 received two different classifications: UNVERIFIABLE for the reported number of searches and OVERSTATED for the claim about unavailable research results. This made the final summary inconsistent.

## Why I Think It Happened
I think the problem came from my original SKILL.md instructions being too vague about how individual claims should be classified. It never explicitly said that each numbered claim could only receive one classification. It also didn't explain what to do when a sentence contained multiple claims that required different classifications. I also hadn't included a rule requiring the agent to verify that its category counts added up to the total number of claims reviewed.

## What I Changed
The main changes were:
- require exactly one classification per numbered claim.
- Split sentences containing multiple independently verifiable claims into separate numbered claims when necessary.
- Give every claim a unique number.
- Count each claim only once in the summary.

I kept the rest of the skill the same because its original research-checking behavior was generally working.

## Results After Retesting
Version 1 grouped the research brief into 12 claims and produced an ambiguous classification. Version 2 separated the brief into 20 individually classified claims, with each receiving exactly one status.

The checker also continued to identify meaningful research issues, including a missing paper on volatility risk premium strategies and conclusions that went beyond what the cited abstracts supported.

I consider the revision successful because it fixed the reporting inconsistency without removing the checker's ability to identify substantive problems.