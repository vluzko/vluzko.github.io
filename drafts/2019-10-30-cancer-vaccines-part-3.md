---
title: 'Cancer Vaccines Part 3 - Cancer Vaccines'
category: Biology
tags:
  - biology
  - immunology
  - vaccines
  - cancer
---

[Part 1]({%post_url 2019-10-30-cancer-vaccines-part-1 %}), [Part 2]({%post_url 2019-10-30-cancer-vaccines-part-2 %})

To recap: the immune system works by killing cells that produce non-self proteins, i.e. proteins that aren’t naturally produced by your cells.

Cancers produce lots of non-self proteins, but avoid the immune system by taking advantage of various mechanisms for blocking immune response.

Checkpoint inhibitor therapy is a set of therapies that block the cancer from blocking immune response, meaning the immune system can go about its merry business of killing tumors. They are very good.

To start we’re going to backtrack a little and talk about vaccines. Usually vaccines are preventative: you get a vaccine, and it keeps you from getting sick later on. There are many types of vaccine, but they all work in roughly the same way: they expose your immune system to a particular pathogen, the immune system memorizes this pathogen, and the next time it shows up it can react much faster.

Let’s say you want to build a vaccine to virus X. Well, the way a virus works is that it gets into your cells and hijacks it into producing some unusual proteins. Those proteins are of course not self, so the immune system notices this and kills the cells producing those weird proteins.

You can speed up this process by introducing the immune system to those proteins ahead of time. You can do this in a variety of ways, but once those proteins are in the body the immune system will notice them, respond to them, remember them (1), and next time it sees those proteins it will respond faster. In particular if you ever encounter the actual virus it will be ready, and the immune response to the virus will be much stronger and faster.

That’s all fine and dandy for things like smallpox that don’t change very much. If you build a vaccine to smallpox you can be confident that 10 years later smallpox won’t have mutated so much that the vaccine is no longer effective (2), (3). 

But cancer isn’t like that. Every cancer is unique. It has its own set of mutations, and a vaccine against one wouldn’t help with any of the others.

There are two responses to this:

    Figure out the most common cancer mutations, and vaccinate against those mutations. This is called a shared antigen vaccine.
    Wait until someone has cancer, then figure out what mutations they have and vaccinate against those. This is a therapeutic vaccine. (I’ll go more into how these are supposed to work in a bit)

To be clear: this is super obvious. Immunologists thought of doing this more-or-less as soon as it was possible to think of it.

But the vaccines they tried didn’t work! Totally ineffective! Why?

Because of immune escape (4). A vaccine can’t work if the immune system isn’t working. 

Enter checkpoint inhibitor therapy. Suddenly the immune system is working again, which reopens the possibility of a cancer vaccine.

Both types of vaccine are currently being tested, but I’ll focus on therapeutic vaccines because that’s what I worked on.

First thing: how does a therapeutic vaccine work? I said earlier that vaccines work by training your immune system to recognize particular proteins, but in the case of a therapeutic vaccine those proteins are already there, so why would a vaccine do anything?

The idea is that the immune system is, for whatever reason, having a hard time learning the proteins present in the cancer. Tumors are weird, they’re doing lots of things to inhibit immune system function (besides just using immune checkpoints), so maybe the immune system isn’t figuring out what proteins are present in the tumor.

So instead we put those same proteins somewhere else, away from the tumor where the immune system is still functioning. It builds up a response to those proteins, and then once it’s strong it goes and attacks the tumor. The vaccine is basically functioning as a miniboss to help the immune system level up before it faces the cancer.

How do we actually make a therapeutic vaccine? I’ll break it down:

Step 1: Figure out how the cancer is mutated

Remember: a vaccine works by putting non-self proteins into the body, so the immune system will build a response to those proteins and then be extra strong against anything else producing those proteins. The non-self proteins in a cancer are the ones that have been mutated. So we have to figure out what mutations are actually present.

To do this, you get a biopsy of the cancerous tissue and a biopsy of the person’s normal (non-cancerous) tissue. You sequence (5) both of them, i.e. you figure out the exome (6) for both. Then you look at the differences. Those are the mutations (7).

Step 2: Figure out which mutations are “good”

Whereby good I mean “likely to cause an immune response”.

Remember the pathway back in part 1? Protein -> epitope -> MHC -> T-cell? Getting the mutations only gets us the possible epitopes. It tells us that protein X has a subsequence Y that’s mutated, so if subsequence Y gets turned into an epitope and presented to the MHC, and it binds to the MHC, and that binds to the T-cell, then we could have an immune response.

So personalized cancer vaccine design is essentially a prediction problem: given these possible epitopes, which ones are likely to produce a strong immune response (8)?

Some things people have looked at in the literature (no comment on whether or not the group I was with made use of any of these):

    How significant is the mutation? How different is the resulting protein from the original?
    How much mutated protein is actually present? If the DNA is mutated but it never actually turns into protein, there’s nothing for the immune system to recognize (10)
    How well do we think the possible epitope will bind to the MHC molecules in the patient (11)? There are some existing algorithms for doing this (that aren’t very good), and some companies have built their own (that are better).
    Do we think this mutation is important to the cancer’s function? If it’s not then the cancer might just mutate again to lose the mutation, but if it is then maybe the cancer can’t lose the mutation.

Step 3: Manufacturing and delivery

I am going to be terrible and not talk about this. The manufacturing and delivery of vaccines is an entire field. How you make it and deliver it is a major component of how well the vaccine functions (not to mention that both present extremely difficult biochemical engineering problems). But! I know nothing about it except for what my company did, and I can’t tell you about that without getting the pants sued off me.

Step 4: Hope nothing goes wrong

Okay, you’ve got your vaccine. You administer checkpoint inhibitor therapy to get the immune system working, and then you administer your vaccine. 

You know what the cancer does? It mutates again to escape the immune system in some other way. Maybe it loses the genes for expressing class I MHC molecules, so the protein -> epitope -> MHC -> T-cell pathway is just completely broken. Maybe it takes advantage of a different immune checkpoint. Maybe it loses the mutations you targeted and gets new ones instead.

I don’t actually know how common this will be. I’m aware of research directions for preventing it / reacting to it, but I don’t know if they’ll work. And of course if they do the cancer might just come up with something else.

In conclusion: progress has been made, but cancer is an adaptable bitch and our superweapons still need work.

1. In particular: immune cells (including T-cells) that have responded to an infection enter a different state. They stick around and are on high alert for some long period of time. It’s not so much that the immune system “memorizes” the infection as it is that there are a bunch of veteran immune cells sitting around waiting for that bastard infection to come back.

2. Meaning it will still be producing the same proteins your immune system learned to recognize from the vaccine.

3. An obvious exception is the flu. The flu mutates so fast that you need a new vaccine every year. But you can still be confident that within a single year the flu will be stable enough that the vaccine will provide some protection. (I assume that there’s some protection from year to year too, but I don’t know how much).

4. And probably other stuff. Getting a vaccine to work is really hard even if the disease isn’t nullifying the entire immune system. We won’t know how hard the other stuff is until the vaccines we’re making now have actually been tested though.

5. Sequencing is a big complicated topic that I don’t want to get into. Pretend you have a magic box that will tell you what the DNA in a tissue is.

6. Reminder: the exome is all the DNA that will get turned into RNA and then turned into protein. It doesn’t fully define what proteins will get produced, because of [complicated biology], but it’s a pretty good estimate.

7. Don’t even get me started on how much of a simplification this is.

8. You might be wondering: why not just use all of them? For many groups this isn’t feasible due to constraints on the size of the vaccines they can manufacture. However some groups have tried putting everything in (for instance by taking a biopsy of the tumor, killing it, and then using the whole thing (or a sample of the whole, really) as the vaccine. This exposes your immune system to everything in the tumor.). My overall impression of these methods is that they don’t work very well, possibly because there’s too much noise for the immune system to sort through. (9)

9. That only kind of makes sense though, so let’s just leave it at “I don’t know why it doesn’t really work”.

10. This can happen in several ways. Some mutations work specifically by deactivating a protein (for instance by deactivating proteins that inhibit cell growth or reproduction). Other mutations aren’t actually part of the cancer’s function, and they just sort of show up because cancers are a mess.

11. Remember that every patient has their own set of MHC molecules. They’re not unique, but it would be unusual to find two people with the exact same MHC molecules.

