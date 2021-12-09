---
title: 'Cancer Vaccines Part 3 - Cancer Vaccines'
date: 2019-10-30
tags:
  - biology
  - immunology
  - vaccines
  - cancer
---

## Cancer Vaccines 3 - Personalized Cancer Vaccines
[Part 1](/posts/personalized-cancer-vaccines-1.html), [Part 2](/posts/personalized-cancer-vaccines-1.html)

To recap: the immune system works by killing cells that produce non-self proteins, i.e. proteins that aren’t naturally produced by your cells.

Cancers produce lots of non-self proteins, but avoid the immune system by taking advantage of various mechanisms for blocking immune response.

Checkpoint inhibitor therapy is a set of therapies that block the cancer from blocking immune response, meaning the immune system can go about its merry business of killing tumors.

### Vaccines
Let's backtrack a little and talk about vaccines. Usually vaccines are preventative (prophylactic): you get a vaccine, and it keeps you from getting sick later on. There are many types of vaccine, but they all work in roughly the same way: they expose your immune system to a particular pathogen, the immune system memorizes this pathogen, and the next time it shows up it can react faster, stronger, or both.

Let’s say you want to build a vaccine to virus X. Viruses work by entering your cells and hijacking them into producing some unusual proteins. Those proteins are of course not self, so the immune system notices this and kills the cells producing the weird proteins.

This process can be sped up by introducing the immune system to these proteins ahead of time. That's a vaccine. This is a simplification, but the key takeaway is that if you introduce the proteins a pathogen produces to the immune system, you prime the immune system to attack that pathogen.

But cancer isn’t like a virus. Every cancer is unique. It has its own set of mutations, and a vaccine against one wouldn’t help with any of the others.

There are two possible responses to this:

* Figure out the most common cancer mutations, and vaccinate against those mutations. This is called a shared antigen vaccine.
* Wait until someone has cancer, then figure out what mutations they have and vaccinate against those. This is a therapeutic vaccine.

But the various cancer vaccines of the past didn't really work. Why? Because the cancer is shutting down the immune system.

Enter checkpoint inhibitor therapy. Suddenly the immune system is working again (or at least working *better*), which reopens the possibility of a cancer vaccine. I'll focus on therapeutic vaccines, since that's what I worked on.

How do we actually make a therapeutic vaccine? I’ll break it down:

### Step 1: Mutation Detection

Remember: a vaccine works by putting non-self proteins into the body, so the immune system will build a response to those proteins and then be extra strong against anything else producing those proteins. The non-self proteins in a cancer are the ones that have been mutated. So we have to figure out what mutations are actually present.

To do this, you get a biopsy of the cancerous tissue and a biopsy of the person’s normal (non-cancerous) tissue. You sequence (5) both of them, i.e. you figure out the exome (6) for both. Then you look at the differences. Those are the mutations (7).

### Step 2: Mutation Ranking
A cancer may contain many hundreds of mutations, and vaccinating against all of them is difficult (and maybe undesirable). We need to decide which mutations are the most likely to cause an immune response.

Remember the T-cell activation pathway from part 1: protein -> epitope -> MHC -> T-cell? Getting the mutations gets us the possible epitopes. It tells us that protein X has a subsequence Y that’s mutated, so if subsequence Y gets turned into an epitope and presented to the MHC, and it binds to the MHC, and that binds to the T-cell, then we could have an immune response.

So personalized cancer vaccine design is essentially a prediction problem: given these possible epitopes, which ones are likely to produce a strong immune response?

Some things people have looked at in the literature (no comment on whether or not the group I was with made use of any of these):

* How "significant" is the mutation (i.e. how physically different is the resulting protein)? How different is the resulting protein from the original?
* How much mutated protein is actually present? If the DNA is mutated but it never actually turns into protein, there’s nothing for the immune system to recognize
* How well do we think the possible epitope will bind to the MHC molecules in the patient? There are some existing algorithms for doing this, and some companies have built their own (that are better).
    * There are some open source algorithms for this (Mhcflurry), some closed source but for sale algorithms (NetMHC), and some in-house predictors built by various companies.
* Whether the mutation is important to the cancer’s function. If it’s not then the cancer might just mutate again to lose the mutation, but if it is then maybe the cancer can’t lose the mutation.

### Step 3: Hope
Okay, you’ve got your vaccine. You administer checkpoint inhibitor therapy to get the immune system working, and then you administer your vaccine.

You know what the cancer does? It mutates again to escape the immune system in some other way. Maybe it loses the genes for expressing class I MHC molecules, so the T-cell activation pathway is just completely broken. Maybe it takes advantage of a different immune checkpoint. Maybe it loses the mutations you targeted and gets new ones instead.

<!-- 1. In particular: immune cells (including T-cells) that have responded to an infection enter a different state. They stick around and are on high alert for some long period of time. It’s not so much that the immune system “memorizes” the infection as it is that there are a bunch of veteran immune cells sitting around waiting for that bastard infection to come back.
2. Meaning it will still be producing the same proteins your immune system learned to recognize from the vaccine.

3. An obvious exception is the flu. The flu mutates so fast that you need a new vaccine every year. But you can still be confident that within a single year the flu will be stable enough that the vaccine will provide some protection. (I assume that there’s some protection from year to year too, but I don’t know how much).

4. And probably other stuff. Getting a vaccine to work is really hard even if the disease isn’t nullifying the entire immune system. We won’t know how hard the other stuff is until the vaccines we’re making now have actually been tested though.

5. Sequencing is a big complicated topic that I don’t want to get into. Pretend you have a magic box that will tell you what the DNA in a tissue is.

6. Reminder: the exome is all the DNA that will get turned into RNA and then turned into protein. It doesn’t fully define what proteins will get produced, because of [complicated biology], but it’s a pretty good estimate.

7. Don’t even get me started on how much of a simplification this is.

8. You might be wondering: why not just use all of them? For many groups this isn’t feasible due to constraints on the size of the vaccines they can manufacture. However some groups have tried putting everything in (for instance by taking a biopsy of the tumor, killing it, and then using the whole thing (or a sample of the whole, really) as the vaccine. This exposes your immune system to everything in the tumor.). My overall impression of these methods is that they don’t work very well, possibly because there’s too much noise for the immune system to sort through. (9)

9. That only kind of makes sense though, so let’s just leave it at “I don’t know why it doesn’t really work”.

10. This can happen in several ways. Some mutations work specifically by deactivating a protein (for instance by deactivating proteins that inhibit cell growth or reproduction). Other mutations aren’t actually part of the cancer’s function, and they just sort of show up because cancers are a mess.

11. Remember that every patient has their own set of MHC molecules. They’re not unique, but it would be unusual to find two people with the exact same MHC molecules. -->

