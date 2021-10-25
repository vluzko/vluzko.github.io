---
title: 'Cancer Vaccines Part 1 - Basic Immunology'
date: 2019-10-28
tags:
  - biology
  - immunology
  - vaccines
---
[Part 2]({%post_url 2019-10-30-cancer-vaccines-part-2 %}), [Part 3]({%post_url 2019-10-30-cancer-vaccines-part-3 %})

## Cancer Vaccines 1 - Immunology 001

For a few years, I worked at Moderna on their personalized cancer vaccine program. Of course I cannot talk about the specifics of Moderna's approach, but there are quite a few teams - industrial and academic - working on the problem, all with fairly similar approaches and I can talk about the overall methodology.

There are two parts of the human immune system: the innate immune system and the adaptive immune system. You can roughly think of these as "general" and "targeted". The adaptive immune system, as its name suggests, adapts to novel pathogens and responds

The rough process is this: every cell (pathogenic or otherwise) produces lots of proteins. Your cells only produce proteins from a very specific list of proteins. This list is determined by your DNA. That’s not all your DNA does, but part of it (the exome) determines what proteins your cells produce (1). So the adaptive immune system goes around looking for proteins that aren’t on the list, and then it murders everything making the forbidden proteins. We’ll refer to things on The List as “self”.

There are a few ways this can happen, but we’ll focus on one of them: deliberate presentation by your cells. Here’s how it works:

1. Your cells are full of proteins. If the cells are healthy all these proteins are on The List. If not (if it’s infected by a virus or cancerous, for instance), some of the proteins won’t be on The List (2) 
2. Some of those proteins get randomly selected (never mind how)
3. The selected proteins get randomly chopped up into short amino acid sequences called epitopes
4. Those epitopes are presented to MHC molecules on the surface of the cell.
5. If the epitope binds to the MHC (it has a little pocket the epitope tries to fit inside), the epitope + MHC complex sits on the surface of the cell, waiting.
6. A type of immune cell called a T-cell comes along and examines the epitope/MHC complex with a protein called a T-cell receptor. If the T-cell receptor doesn’t bind to the complex it does nothing. If it does bind it does a bunch of stuff to kill the cell and all the other cells producing epitopes like it. (3)

Since every epitope produced by a healthy cell should pass the T-cell test, they should be fine (4). Unhealthy cells produce at least some bad proteins though, so eventually one of those proteins should get presented to the T-cell and the unhealthy cell should die.

So really it’s a protein binding problem. Does the epitope bind to the MHC? And does the MHC/epitope complex bind to the T-cell?

Some likely questions:

* Do self proteins ever get chopped into epitopes that can bind an MHC?
    * Yes. That’s okay though, because there’s no immune response unless that binds to the T-cell receptor.
* Okay, so how do T-cells know not to bind the self-epitopes?
    * Good question. T-cells are grouped by their T-cell receptors. A T-cell receptor is just a big protein. It has specific chemical properties and will only bind specific epitope/MHCs. When T-cells are developed they get exposed to as much of of your self-proteins as possible. Any T-cell that binds a self-protein is killed off.
* Do all the bad epitopes bind to MHCs?
    * No. In fact most epitopes don’t bind to MHCs, regardless of source.
* How many bad epitopes will bind with the T-cell receptor?
    * I don’t know, and it’s sort of a numbers game. IIRC you have tens of thousands of different T-cell receptors, and it might bind one of them but not the others. If it does bind then the population of T-cells with that specific receptor expands and the problem gets a lot easier, but that first match still has to happen.

There’s actually multiple different types of MHC. There are two many classes, I and II, which activate different types of T-cells (CD8+ and CD4+ T-cells, respectively). CD8+ T-cells are the ones that do the actual killing (6), and CD4+ T-cells call in CD8+ T-cells to look at the problem.

You also have multiple MHCs of each type. Normally you’ll have six class I MHCs and some fairly large number of class II MHCs.

Which MHCs you have is determined genetically, so different populations have different distributions of particular types. For instance the MHC HLA-A*02:01 is present in something like 40% of the US population. This is very important from an epidemiology perspective, because different MHCs bind with different epitopes. A population that all has MHCs that bind to smallpox epitopes will be much more resistant than one with no smallpox-binding MHCs.

Protein in cells -> epitopes -> epitope/MHC complex -> T-cell -> immune response

That basic pathway is what a lot of vaccines build on, and it’s what all personalized cancer vaccines build on.

------------------------------
<!--
1. If you took high school biology you probably learned that DNA -> mRNA -> protein, and that each gene (a segment of DNA) turns into one protein. This is mostly right, but it is a simplification. The relationship between genes and proteins isn’t one-to-one, but many-to-many.

2. Well technically there might be cancers that only affect regulation but don’t change the actual proteins produced. I’m not aware of any though.

3. Never mind exactly what it does for now. Just know that it causes the immune system to focus specifically on cells producing that epitope.

4. If your cells are routinely failing you have an autoimmune disorder.

5. The actual process of T-cell maturation and selection is complicated (like everything else) and I know very little about it.

6. Probably. Maybe CD4+ T-cells do too, sometimes. It’s an area of active research. -->

