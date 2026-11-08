name: research-brief-check
description: Checks  finance research briefs for unsupported claims, inaccurate citations, and overstated conclusions. Use when reviewing an AlphaSearch research brief or checking research accuracy before submission.

# Research Brief Accuracy Checker
## Purpose
Review an existing finance research brief against its source abstracts. Identify inaccurate or unsupported claims without changing the original work.

## Instructions
1. Read the research brief provided by the user.
2. Identify the main factual claims about research findings, trading strategies, or financial models.
3. Locate the paper abstracts associated with each claim. Use provided source records or an available research database tool.
4. Compare each claim against what the corresponding abstract actually says.
5. Classify each claim using the categories below.
6. Report findings without correcting or rewriting the brief.

## Classification
- SUPPORTED: The source abstract clearly supports the claim
- OVERSTATED: The claim goes beyond what the abstract establishes
- CONTRADICTED: The claim conflicts with information in the abstract
- UNVERIFIABLE: The relevant source is missing or insufficient to judge the claim

## Output Format
Research Brief Accuracy Report
For each substantial claim:
Claim: [Quote or identify the claim]
Status: [SUPPORTED / OVERSTATED / CONTRADICTED / UNVERIFIABLE]
Source: [Paper title or identifier]
Evidence: [Brief explanation grounded in the source]

End the report with:
- Total claims reviewed
- Number of claims in each category
- Up to three highest-priority issues
- Overall assessment of the brief's reliability

## Rules
- Never edit, rewrite, or delete any files.
- Never invent citations, abstracts, or research findings.
- Do not treat a brief's own claims as source evidence.
- Do not assume a claim is accurate because it sounds financially reasonable.
- Distinguish missing evidence from contradictory evidence.
- Identify sources by title or paper ID for every supported claim.
- If evidence is unavailable, explicitly mark the claim UNVERIFIABLE.
- Report findings only. Leave all corrections to the user


## Claim Classification and Counting Rules
- Each numbered claim must receive exactly ONE classification: SUPPORTED, OVERSTATED, CONTRADICTED, or UNVERIFIABLE.
- If a sentence contains multiple independently verifiable claims
with different classifications, split it into separate numbered claims.
- Every claim must have a unique number.
- Count each numbered claim exactly once in the summary.
- Before reporting, verify that the four category counts sum to the total number of claims reviewed.
- Never report conflicting or inconsistent summary counts.
