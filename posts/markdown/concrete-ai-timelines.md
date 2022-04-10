---
title: "Concrete AI Timelines"
date: 2022-04-09
tags:
    - ml
    - forecasting
---
## Concrete AI Timelines
I'm generally interested in timelines for AI progress, but in practice the questions asked about them tend to be some mix of long term, poorly specified, and very high-level (e.g. some variant of "When will we have AGI?").

So I'm building a list of concrete, fairly near term questions related to AI progress. I've posted some of them on [Manifold](https://manifold.markets/fold/technical-ai-timelines/markets), and will post them on [Metaculus](https://www.metaculus.com/questions/) when I have time. If any [GJOpen](https://www.gjopen.com/) style forecasting tournament ever opens to user-submitted questions I'll post them there too.

Many questions are of the form "When will SOTA on $BENCHMARK pass X?", which is two-dimensional: for every X a forecaster has a distribution over all possible times (including never). Posting these questions on prediction markets requires picking a single value for X, but here I'm going to post the general form.

Once I've had time to rewrite my site generator I will make a separate "Timelines" section that goes into more detail on each question.

### Current Questions

* When will I be able to run a model that is at least as good as GPT-3 on all benchmarks (from original paper) on a single consumer (<1.5k USD) GPU
* When will a single trained model reach superhuman performance on all Atari environments
* When will a single trained model reach superhuman performance on all OpenAI Gym environments
* Once any model achieves superhuman performance on a competition coding benchmark (natural language description of problem + test cases -> code that passes tests), how long will it be until any company is using a model to write "entry level" code (roughly: a fully automated system that is assigned issues, fixes the bug/implements the feature, and submits PRs)?
* When will there be realistic AI generated video from natural language descriptions?
* When will it cost less than 100k USD to train and run a language model that outperforms GPT-3 175B on all benchmarks?
* When will a single model first achieve 10@k solve rate >= X% on the CodeContests dataset?
* When will a single model achieve superhuman performance on QuALITY? (https://arxiv.org/pdf/2112.08608.pdf)
* When will SOTA for Atari 100k pass human median and mean performance across all games?
* When will SOTA on MMLU STEM questions pass X%?
* When will SOTA on all MMLU questions pass X%?
* When will no-calculator SOTA on the MATH dataset pass X% (https://arxiv.org/abs/2103.03874)
* When will top-1 SOTA on the APPS dataset pass X%? (https://arxiv.org/abs/2105.09938)
* When will a single model be capable of winning a gold medal on the IMO Grand Challenge?
* When will a single model achieve results within 10% of SOTA on benchmarks in different domains (e.g. Pong and ImageNet)?
* When will a language model with a context window >10k tokens achieve SOTA?
    * Models with no architectural limit on how far back they can remember (e.g. LSTMS) count.

