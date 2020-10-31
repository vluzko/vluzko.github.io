---
title: 'Cancer Vaccines Part 2 - Cancer Immunology'
date: 2019-10-30
permalink: /posts/2019/10/cancer-vaccines-2/
category: Biology
tags:
  - biology
  - immunology
  - vaccines
  - cancer
---

[Part 1]({%post_url 2019-10-30-cancer-vaccines-part-1 %}), [Part 3]({%post_url 2019-10-30-cancer-vaccines-part-3 %})

To recap: the adaptive immune system goes around looking for cells producing proteins that aren’t in your natural proteome, i.e. the set of proteins your DNA encodes. When it finds those cells, it kills them.


In case you don’t know, cancer is just your cells but mutated. Specifically they’ve mutated in ways that cause them to grow and reproduce unchecked, eventually taking over your body and killing you.

A mutation is just a change to your DNA.(1) If the change is to a part of your DNA that encodes a protein, and it changes the codon (2) then it changes the resulting protein. (A protein-changing mutation is a non-synonymous mutation).

But wait! That’s a new protein! It isn’t on The List of acceptable proteins to be in your body! So the immune system should, in theory, kill this mutated cell!

Except… cancers are just a bunch of mutations. And empirically cancer isn’t all getting killed by the immune system. What gives?

You might think that maybe all the mutations in cancer don’t change the proteins, and cancer works some other way. Fortunately for us, this isn’t the case (3). All or almost all cancers have at least a few mutations that change its proteome.

This is weird though. The cancer is producing bad proteins! Why doesn’t the immune system kill it?

Well, it does. Most of the time. I’m not sure how often this happens, but it’s probably relatively common for a cell to mutate in a way that would make it cancerous, except your immune system immediately kills it.

Here are ways this goes wrong:

    Your immune system is weak. 
        You might be old (old people have weaker immune systems),
        You might be on immuno-suppressants (drugs that make your immune system weaker, often given to transplant patients to help prevent rejection).
        You might have AIDS. (Cancer is one of the most common causes of death among people with AIDS)
    The cancer undergoes immune escape, i.e. it mutates in a way that makes it invisible/untargetable by the immune system.
    The mutations just aren’t very immunogenic (they don’t cause a strong immune response). Remember, every mutated protein has to go through the epitope -> MHC -> T-cell pathway. If by sheer chance the mutated proteins just don’t bind, there won’t be an immune response or it will be very weak.
    The cancer gets very strong mutations and grows so fast that the immune system can’t keep up.
        In practice if this happens the cancer will probably undergo immune escape at some point anyway. Cancers are constantly mutating and it’s only a matter of time before it escapes the immune system.

We’re going to focus on immune escape, specifically on immune checkpoints.

An immune checkpoint is a protein receptor sitting on the surface of an immune cell. If a protein binds to that receptor, the immune response is in some way inhibited (4). Cancers very often learns to produce the protein that binds those receptors, meaning that even though the immune system views them as non-self/not on The List, it won’t kill them (5).

This brings us to cancer immunotherapy, i.e. using the immune system to kill cancer. The field has a long history that I won’t go into, but recently there’s been a major advance called checkpoint inhibitor therapy. This is any therapy based around preventing the cancer from using checkpoint inhibitors to escape the immune system.

Let’s say your cancer is producing protein A that binds to immune checkpoint receptor B. This is saving it from the immune system. The patient receives a drug anti-A, that in some way prevents A from working. Maybe it binds to A so that A can’t bind to the checkpoint receptor. Maybe it blocks B in some way. Maybe it does some other weird thing. The point is that B isn’t getting activated anymore, the immune response isn’t suppressed, and it’s free to murder tumor cells to its heart’s content.

Checkpoint inhibitor therapy has been very successful. It turns out that immune checkpoints are one of the key ways that cancer escapes the immune system, and blocking it does a damn good job of killing cancer. In some cases they double long term survival rates (6) (we don’t know what they do past 5-10 years because they haven’t been around long enough).

The interactions between the immune system and cancer are of course much more complicated than this. Cancer often escapes the immune system in more than one way, or it will mutate to escape in a new way after the checkpoint inhibitor therapy has been administrated. It’s a constant back and forth, and we don’t have the ability to shut all of the mechanisms down. Yet. (7)

1. “Just a change to your DNA”, they say. Ha. As someone who has spent a lot of time on understanding and writing code to handle all the ways things can mutate: this is an absurd understatement. Your DNA can change in ridiculously complicated ways.

2. The codon is the set of three nucleotides (three “molecules” of DNA) that gets translated to a single amino acid. A single amino acid is usually coded for by more than one codon, so it’s possible to change a codon without changing the resulting protein. If this doesn’t make sense don’t worry about it: the point is that not all mutations actually change a protein, but some do.

3. I guess it’s theoretically possible that there exists a cancer that with no protein-changing mutations. There are other ways for mutations to affect cell function without changing an actual protein, and that type of mutation does occur in cancer, but I’m not aware of any cancer that only has them.

4. There are a variety of different checkpoints that inhibit immune response in a variety of ways. There are also checkpoints that, when activated, increase immune response.

5. The obvious question is “why do checkpoints exist at all”. To prevent auto immunity. Yes, I know I said that autoimmunity is prevented by killing all the T-cells that react to self. I lied.

Another obvious question is “why don’t all cells overproduce the checkpoint inhibitors? Isn’t there immense evolutionary pressure on them to do so?” I don’t know, I’m afraid. For whatever reason it looks like cells don’t learn to do this very often.

Another obvious question is “why don’t viruses do this”. I also don’t know that. Maybe that would make the virus too big?

6. “Long term survival” = still alive 5 years of cancer.

7. It’s possible that even when we do we won’t be able to use it, because the side effects will be too bad. (The side effects of immunotherapy are generally autoimmune problems).
