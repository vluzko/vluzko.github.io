---
title: "Concrete AI Timelines"
date: 2022-04-09
tags:
    - ml
    - forecasting
---
## Concrete AI Timelines
I'm generally interested in timelines for AI progress, but frequently disappointed by the most discussion. The questions asked about AI progress tend to be some mix of long term, poorly specified, and very high-level (e.g. some variant of "When will we have AGI?"). These questions are *interesting*, but they're too nebulous to be useful for building a real timeline.

I want a much broader set of questions:
* Covers a wide range of expected time to resolution. There should be questions about expected progress from three months to ten years. (Longer than ten years is probably infeasible for prediction)
* Covers many different subfields of AI.
* Uses concrete metrics, ideally based on existing benchmarks.
* Has well-defined resolution dates.

The first point in particular is very important, both because it gives us established track records for predictors that (hopefully) generalize to longer term questions, *and* because it lets us build more detailed timelines for when particular milestones will be reached.

For now I am posting the questions on [Manifold](https://manifold.markets/group/technical-ai-timelines). Prediction markets aren't a great fit for this style of question (I would prefer to collect distributions over timelines from experts), but it's so much more easily usable than its competitors that I think it's worth it.

Some questions that I think are representative:

* When will I be able to run a model that is at least as good as GPT-3 on all benchmarks (from original paper) on a single consumer (<1.5k USD) GPU? (Hardware / efficiency progress, medium term)
* When will a single trained model reach superhuman performance on all Atari environments? (Multi-task RL progress, medium term)
* Once any model achieves superhuman performance on a competition coding benchmark (natural language description of problem + test cases -> code that passes tests), how long will it be until any company is using a model to write "entry level" code (roughly: a fully automated system that is assigned issues, fixes the bug/implements the feature, and submits PRs)? (Code synthesis progress, long term)
* When will a single model first achieve 10@k solve rate >= X% on the CodeContests dataset? (Code synthesis progress, medium term)
* When will SOTA for Atari 100k pass human median and mean performance across all games? (RL efficiency progress, short-medium term)
* When will SOTA on all MMLU questions pass X%? (NLP progress, short-medium term)

