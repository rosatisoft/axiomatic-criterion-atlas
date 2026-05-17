Axiomatic Criterion Atlas (ACA)
Persistent Geometry-Based Semantic Navigation 

Author: Ernesto Rosati Beristain 
Independent Researcher Artificial Intelligence Safety Research México 
ORCID: https://orcid.org/0009-0008-1974-6538 
DOI: 10.5281/zenodo.20250560 
Code repository: https://github.com/rosatisoft/axiomatic-criterion-atlas 
Colab: https://colab.research.google.com/drive/1JSgACANC1MGPu5FnqOrDI07fvyQUimdo?usp=sharing
© 2026 Ernesto Rosati Beristain This work is licensed under
Apache License Version 2.0, January 2004 http://www.apache.org/licenses/
 
## Abstract

Large Language Models (LLMs) can maintain locally coherent language while progressively destabilizing the semantic orientation that originally constrained their reasoning process. Existing mitigation approaches rely heavily on probabilistic continuation, prompt engineering, or post-generation filtering, which often fail to distinguish between mere contextual coherence and the preservation of epistemic criterion. This work introduces the Axiomatic Criterion Atlas (ACA) Runtime: a geometry-based criterion supervision framework that models semantic reasoning as navigable evolution within a structured contextual topology. Rather than reconstructing criterion through repeated natural language prompts, ACA externalizes it into a persistent geometric infrastructure composed of invariant orientation and contextual semantic fields. Experimental results demonstrate that semantically coherent trajectories can progressively lose epistemic orientation under rhetorical pressure, a vulnerability ACA mitigates through topology-aware runtime supervision. A comparative benchmark reveals that replacing prompt-heavy criterion preservation with ACA’s deterministic semantic orientation yields a runtime token reduction of $70.26\%$. These results suggest that reliable generative reasoning depends on preserving navigability through persistent semantic topology, proposing a fundamental transition from prompt-engineered control toward reusable geometric criterion infrastructure.


\section{1. Introduction}

Large Language Models (LLMs) have demonstrated remarkable capabilities across reasoning, coding, retrieval, summarization, planning, and conversational interaction. Despite these advances, modern generative systems continue to exhibit semantic instability during extended reasoning, particularly under ambiguous, contradictory, adversarial, emotionally persuasive, or weakly constrained contextual conditions. Current mitigation strategies primarily focus on factual verification, reinforcement alignment, prompt engineering, retrieval augmentation, moderation layers, or post-generation filtering. While these approaches significantly improve output reliability, they generally evaluate instability after reasoning expansion has already occurred. As a result, generative systems may remain linguistically coherent while progressively drifting away from the foundational semantic orientation that originally constrained the reasoning process.

This operational limitation reveals a critical distinction that remains insufficiently formalized in current language model research: contextual coherence does not necessarily imply the preservation of an epistemic criterion. A reasoning trajectory may remain semantically compatible with a contextual field while progressively inverting the foundational structures that originally defined the orientation of that field. In practice, a dialogue may preserve lexical consistency, stylistic continuity, and contextual proximity, while directionally shifting toward contradiction, opportunistic reinterpretation, rhetorical dominance, evidential erosion, or the absolute inversion of foundational constraints. This phenomenon becomes particularly visible in long conversational trajectories, persuasive discourse, adversarial framing, and contexts where emotional or ideological pressure competes with evidential or structural coherence. Under these conditions, probabilistic continuation may preserve local linguistic fluency while progressively destabilizing the deeper orientation of the reasoning process itself. Consequently, the core issue extends beyond hallucination, factual inaccuracy, or contextual ambiguity alone; the deeper challenge is the absence of persistent criterion preservation throughout semantic trajectory evolution.

Modern LLM reasoning frequently behaves as repeated semantic reconstruction. Each interaction reintroduces the criterion, contextual grounding, continuity constraints, alignment instructions, and semantic stabilization through repeated natural language prompting and contextual accumulation. As semantic trajectories grow, this process becomes increasingly expensive, fragile, and operationally unstable. The Axiomatic Criterion Atlas (ACA) proposes a fundamentally different formulation: rather than reconstructing the semantic criterion during every interaction, ACA models semantic reasoning as navigable geometric positioning within a structured contextual topology. Under this framework, semantic reasoning evolves through contextual semantic fields, invariant orientation, topology-aware transitions, and persistent trajectory continuity. 

Importantly, ACA does not attempt to exhaustively resolve the semantic space at every inference step. Instead, the framework preserves navigability, orientation continuity, contextual recoverability, and criterion stability through reusable geometric semantic infrastructure. In this formulation, semantic fields and invariant matrices function analogously to navigational structures within information systems; they do not explicitly contain every possible semantic output, but instead preserve the directional orientation that allows efficient navigation through the semantic space while maintaining criterion continuity. This distinction fundamentally changes the operational interpretation of semantic supervision. While traditional prompt-heavy systems repeatedly reconstruct semantic orientation through probabilistic contextual reinforcement, ACA externalizes the criterion into a persistent geometric structure. Consequently, semantic reasoning becomes less dependent on repeated linguistic reconstruction and more dependent on stable orientation throughout contextual evolution.

Building upon the semantic field framework introduced in previous work, this paper introduces the Axiomatic Criterion Atlas (ACA) Runtime: a geometry-based criterion supervision architecture that explicitly separates contextual coherence from epistemic criterion preservation. The proposed framework models semantic meaning as structured contextual topology constructed from invariant anchor relations, semantic field geometry, directional orientation, and contextual subspace organization within an embedding space. The central hypothesis of this work is that criterion preservation can be modeled as a directional geometric property rather than solely as probabilistic linguistic continuity. Under this formulation, semantic compatibility alone is insufficient to guarantee stable reasoning, as a semantic trajectory may remain geometrically compatible with a contextual region while progressively inverting the invariant structures that define its epistemic orientation. To address this limitation, ACA introduces directional semantic invariants, origin-cost evaluation, topology-aware semantic transitions, invariant orientation continuity, and runtime trajectory supervision, mapping criterion drift as a progressive directional inversion.

A central contribution of this work is the introduction of Semantic Reorientation Criteria: a topology-aware runtime mechanism capable of distinguishing between destabilizing semantic drift, neighboring contextual recovery, and criterion-preserving semantic evolution. The experiments demonstrate that semantically coherent trajectories may progressively lose epistemic orientation under rhetorical pressure while remaining geometrically compatible with their local contextual fields. Conversely, the results reveal that neighboring contextual transitions may preserve criterion continuity through semantic reorientation rather than producing semantic collapse. To operationalize these behaviors, the ACA Runtime combines semantic field projection, contextual subspace geometry, origin-cost evaluation, directional invariant analysis, topology-aware transition supervision, and deterministic runtime criterion policies. 

Experimental evaluations demonstrate that the semantic criterion may be preserved geometrically before unrestricted reasoning expansion occurs. Furthermore, a comparative runtime benchmark reveals a measured runtime token reduction of $70.26\%$ relative to prompt-heavy criterion reconstruction approaches. Crucially, this reduction emerged not by removing semantic supervision, but by externalizing the criterion into a persistent geometric infrastructure. These results suggest that reliable generative reasoning depends not only on probabilistic language continuation, but on preserving stable semantic navigability throughout contextual evolution. ACA therefore proposes a definitive transition from probabilistic prompt-conditioned semantic reconstruction toward persistent geometry-based semantic navigation through invariant-oriented contextual topology.

\section{2. Related Work}

Research on reliable language model systems has addressed instability through several complementary directions, including hallucination detection, retrieval augmentation, uncertainty estimation, alignment methods, semantic routing, and interpretability. ACA builds upon these areas but introduces a different operational distinction: a reasoning trajectory may remain contextually coherent while losing epistemic orientation.

\subsection{2.1 Hallucination Detection and Factual Reliability}
A large body of work frames language model unreliability as hallucination, commonly understood as the generation of plausible but nonfactual or unsupported content. Recent surveys describe hallucination as a central challenge for LLM reliability, especially because fluent outputs may conceal factual inaccuracies or unsupported claims. Several approaches attempt to detect hallucination after generation. SelfCheckGPT, for example, evaluates consistency across multiple sampled responses, relying on the observation that hallucinated claims often vary or contradict one another across stochastic generations. Semantic entropy methods similarly estimate uncertainty over meaning rather than surface-level token variation, detecting a subset of hallucinations described as confabulations. These approaches are important, but they generally operate after generation or through repeated sampling. ACA differs by evaluating the geometric stability of a semantic trajectory before unrestricted reasoning expansion. The goal is not only to detect nonfactual claims, but to identify when reasoning begins to invert the invariant structure that gives a field its epistemic orientation.

\subsection{2.2 Retrieval-Augmented Generation and External Grounding}
Retrieval-Augmented Generation addresses factual reliability by combining parametric model knowledge with non-parametric external memory. The original RAG formulation retrieves relevant passages from a dense index and conditions generation on retrieved evidence, improving performance on knowledge-intensive tasks and producing more specific and factual outputs than parametric-only baselines. RAG is highly relevant to factual grounding, but it does not fully solve criterion preservation. A model may retrieve correct documents and still reason over them through a distorted interpretive frame. In ACA terms, retrieval can improve evidential access, but it does not by itself guarantee that the reasoning trajectory preserves the directional invariants of the active semantic field. Thus, ACA is complementary to RAG; retrieval provides external grounding, while geometric criterion preservation evaluates whether reasoning remains structurally oriented while using that grounding.

\subsection{2.3 Self-Evaluation and Semantic Uncertainty}
Another line of work investigates whether models can estimate their own reliability. Kadavath et al. show that larger models can sometimes evaluate the validity of their own claims under appropriate formats, using self-estimated probabilities such as whether an answer is likely true. These methods are valuable because they introduce a form of internal uncertainty awareness. However, self-evaluation remains tied to model-generated judgments and probabilistic calibration. ACA instead proposes an external deterministic geometric layer: rather than asking the model whether it is likely correct, the system measures whether the semantic trajectory preserves or inverts predefined invariant directions. This distinction is central; ACA is not primarily a confidence estimator, but a criterion-orientation detector.

\subsection{2.4 Alignment and Constitutional AI}
Alignment methods attempt to shape model behavior according to human preferences, principles, or safety constraints. Constitutional AI, for example, trains models using a set of principles and AI-generated feedback to improve harmlessness without relying exclusively on human labels. Such approaches show that explicit principles can influence model behavior. However, they are mainly training-time or feedback-based methods. ACA proposes a runtime geometric mechanism where principles are not only textual rules but are represented as invariant directions in an embedding space. The system then evaluates whether a reasoning trajectory remains directionally aligned with those invariants. In this sense, ACA does not replace alignment; it offers a measurable runtime layer for detecting when a model’s reasoning begins to drift away from the structural meaning of the principles it is supposed to preserve.

\subsection{2.5 Mechanistic Interpretability and Representation Geometry}
Mechanistic interpretability seeks to understand the internal computations of neural networks by identifying circuits, features, and representations that explain model behavior. Transformer Circuits and later work on monosemantic features attempt to decompose model internals into interpretable components. ACA shares with interpretability research the premise that language model behavior can be studied geometrically and structurally. However, it operates at a different level. Instead of reverse-engineering internal circuits, ACA constructs external semantic fields from anchor embeddings and evaluates input or dialogue trajectories against those fields. The framework therefore functions as a runtime semantic control layer rather than a full mechanistic explanation of model internals.

\subsection{2.6 Semantic Field Geometry and Runtime Control}
The previous foundational framework introduced semantic dispersion as a geometric interpretation of language model instability. It modeled contextual meaning as semantic fields built from anchor relations, evaluated inputs using origin cost, field competition margins, density, and stability indices, and demonstrated that unstable inputs could be routed through deterministic runtime policies before full reasoning occurs. The present work extends that foundation. The earlier framework focused on whether an input belongs to a stable contextual field. The current paper asks a deeper question: whether a trajectory that remains contextually coherent also preserves the epistemic orientation of that field. This leads to the central contribution of the present work: contextual coherence and epistemic integrity are formally separated, mapping the phenomenon where a message remains close to a semantic field while directionally inverting its invariants as criterion drift.

\subsection{2.7 Position of ACA Relative to Current Paradigms}
A significant portion of modern LLM alignment and reasoning stability is currently achieved through prompt engineering and contextual reinforcement, where semantic criteria are repeatedly injected into the active context window to maintain coherence, avoid contradiction, or preserve evidential grounding. While these approaches improve local reasoning behavior, they introduce severe operational limitations, including escalating prompt overhead, continuous semantic reconstruction, cascading context accumulation, and structural fragility under prolonged interaction. As reasoning trajectories extend, criterion preservation becomes an increasingly expensive runtime process.

In contrast to these prompt-heavy paradigms, the ACA Runtime externalizes the criterion from repeated natural language instructions into a persistent, reusable semantic infrastructure composed of invariant matrices, semantic fields, and contextual topology. ACA does not attempt to exhaustively encode or resolve the entire semantic space during every interaction. Instead, it treats semantic reasoning as navigable geometric positioning within structured contextual topology, functioning analogously to indexing structures that allow efficient navigation across large information spaces without exhaustive traversal. 

This architectural shift ensures that while semantic complexity remains unconstrained, semantic navigation remains geometrically tractable. Consequently, the runtime maintains navigability, neighboring field continuity, and orientation persistence throughout contextual evolution with substantially lower overhead. By transforming the operational problem from exhaustive prompt-conditioned reconstruction to persistent, geometry-based semantic navigation, ACA provides a highly scalable framework for criterion-preserving generative systems, explaining the substantial reduction in token overhead observed during comparative benchmarks.


---

### 3. Theoretical Framework

This section formalizes the geometric framework underlying ACE Atlas: Geometric Criterion Preservation.

The proposed model extends previous semantic field formulations by introducing a distinction between contextual coherence and epistemic orientation. While semantic field proximity measures whether a message belongs to a contextual region, directional invariant analysis measures whether the trajectory preserves the foundational structure that gives meaning to that region.

Under this formulation, reasoning is modeled not only as probabilistic token continuation, but as geometric trajectory evolution within structured semantic fields.

#### 3.1 Semantic Embedding Space

Let

$$\mathcal{E}\subset\mathbb{R}^d$$

represent the embedding space induced by a semantic encoder or language model embedding function.

Each textual input:

$x$

is represented as an embedding vector:

$$v_x\in\mathcal{E}$$

where semantic relations emerge through geometric proximity, directional structure, and contextual clustering within the latent space.

ACE Atlas assumes that contextual meaning is not represented solely by isolated vectors, but by relational geometric structures formed through semantically coherent anchor configurations.

#### 3.2 Semantic Fields

A semantic field is defined as a structured contextual region generated from semantically coherent anchor relations.

Let:

$$C=[v_1,v_2,\dots,v_k]$$

represent a contextual anchor matrix where each:

$$v_i\in\mathcal{E}$$

corresponds to an embedding associated with an invariant, axiom, contextual relation, or foundational semantic statement.

The semantic field generated by these anchors is approximated as:

$$S=\operatorname{span}(C)$$

The resulting subspace represents the contextual geometry associated with a coherent semantic domain.

Examples include:

* factual fields,
* scientific fields,
* legal fields,
* operational fields,
* conceptual fields,
* or rhetorical fields.

A semantic field therefore defines a region of contextual compatibility rather than a fixed set of explicit symbolic rules.

#### 3.3 Contextual Compatibility

Given an input embedding:

$$z\in\mathcal{E}$$

ACE Atlas evaluates contextual compatibility through orthogonal projection onto the semantic field.

Let:

$$\Pi_S(z)$$

represent the orthogonal projection of:

$z$

onto the semantic subspace:

$S$

The contextual deviation of the input relative to the field is measured through origin cost:

$$O_S(z)=||z-\Pi_S(z)||^2$$

Interpretation:

* low origin cost indicates strong contextual compatibility,
* high origin cost indicates semantic dispersion or contextual instability.

This metric allows ACE Atlas to evaluate whether a message belongs geometrically to a semantic field.

However, contextual compatibility alone is insufficient to determine preservation of criterion.

#### 3.4 Limitation of Contextual Coherence

A central hypothesis of this work is that semantic coherence alone does not guarantee preservation of epistemic orientation.

A reasoning trajectory may remain geometrically close to a semantic field while progressively inverting the invariant principles that define the structural meaning of that field.

Under this interpretation:

* contextual compatibility measures semantic proximity,
* but not directional preservation of foundational structure.

This distinction is critical because many persuasive, ideological, or rhetorically stable trajectories preserve contextual fluency while progressively destabilizing evidential or structural coherence.

Consequently:

$$\text{contextual coherence} \neq \text{epistemic integrity}$$

ACE Atlas therefore introduces directional invariant analysis as a second geometric layer.

#### 3.5 Directional Invariants

For each foundational invariant:

$I_i$

ACE Atlas defines two semantic poles:

* a coherent pole representing preservation of the invariant,
* and an inverted pole representing directional violation of the invariant.

These poles are represented as embeddings:

$v_i^{+}$

and

$v_i^{-}$

respectively.

Examples may include:

* evidence preservation vs narrative substitution,
* coherence vs contradiction,
* causal consistency vs arbitrary reinterpretation,
* factual grounding vs rhetorical dominance.

Each invariant then generates a directional criterion vector:

$$d_i=v_i^{+}-v_i^{-}$$

normalized within the embedding space.

The vector:

$d_i$

represents the geometric direction associated with preservation of the invariant.

#### 3.6 Epistemic Orientation

Given a semantic trajectory element:

$z$

the epistemic orientation relative to invariant:

$I_i$

is defined as:

$$\phi_i(z)=\langle z,d_i\rangle$$

Interpretation:

* positive orientation indicates preservation of the invariant,
* negative orientation indicates directional inversion,
* near-zero orientation indicates ambiguity or weak directional determination.

This formulation introduces a directional geometric dimension absent from standard similarity-based embedding analysis.

Traditional embedding proximity captures semantic closeness, but not necessarily preservation of epistemic structure.

ACE Atlas therefore distinguishes between:

* belonging to a field,
* and remaining directionally aligned with the principles that define that field.

#### 3.7 Semantic Trajectories

Reasoning and dialogue are modeled as evolving semantic trajectories:

$$\tau=(z_1,z_2,\dots,z_t)$$

where each:

$z_t$

represents the embedding associated with a reasoning step, utterance, or conversational turn.

Under this framework, reasoning becomes a geometric process evolving through semantic fields over time.

The trajectory may:

* remain stable,
* transition between compatible fields,
* become ambiguous,
* or drift directionally away from foundational invariants.

#### 3.8 Criterion Drift

ACE Atlas defines criterion drift as the progressive inversion of foundational invariants during trajectory evolution despite superficial contextual compatibility.

Formally, criterion drift occurs when:

$$O_S(z_t)\text{ low}\quad\wedge\quad\phi_i(z_t)<0$$

That is:

* the trajectory remains contextually close to the semantic field,
* while epistemic orientation becomes negative.

This distinction represents the central contribution of the framework.

A trajectory may remain:

* fluent,
* coherent,
* semantically compatible,
* and rhetorically persuasive,

while structurally inverting the foundational meaning of the active semantic field.

#### 3.9 Geometric Criterion Preservation

Criterion preservation occurs when semantic trajectories maintain positive directional orientation relative to foundational invariants during contextual evolution.

Formally:

$$\phi_i(z_t)\ge0\quad\forall i$$

throughout trajectory evolution.

Under this interpretation, criterion is not modeled as:

* fixed answers,
* rigid symbolic rules,
* or ideological enforcement.

Instead, criterion is modeled as:

persistent structural orientation during semantic evolution.

This formulation allows:

* adaptation,
* specialization,
* contextual transition,
* and generative flexibility,

while preserving foundational semantic integrity.

#### 3.10 Deterministic Runtime Criterion Policies

ACE Atlas transforms geometric measurements into deterministic runtime decisions.

Typical policies include:

**ALLOW**

$$O_S(z)\text{ low}\quad\wedge\quad\phi_i(z)\ge0$$

The trajectory remains contextually and directionally stable.

**CLARIFY**

$$|\phi_i(z)|\approx0$$

The trajectory exhibits insufficient directional determination or semantic ambiguity.

**FLAG_CRITERION_DRIFT**

$$\phi_i(z)<0$$

The trajectory directionally inverts foundational invariants despite contextual compatibility.

These policies allow ACE Atlas to detect instability before unrestricted reasoning expansion occurs.

#### 3.11 Central Theoretical Claim

The central theoretical claim of ACE Atlas is that reliable generative reasoning requires more than contextual coherence alone.

It requires persistent geometric preservation of foundational invariants during semantic trajectory evolution.

Under this formulation:

criterion does not emerge solely from probabilistic language continuation.

Criterion emerges from the preservation of directional structural orientation within geometrically stabilized semantic fields.

---

# 4. Mathematical Formulation

This section presents the formal mathematical structure of ACE Atlas for separating contextual coherence from epistemic integrity in generative language systems.

## 4.1 Embedding Space

Let:

$$\mathcal{E}\subseteq\mathbb{R}^{d}$$

be the embedding space induced by a semantic encoder:

$$E:\mathcal{X}\rightarrow\mathbb{R}^{d}$$

where $\mathcal{X}$ is the space of textual inputs.

For any text $x\in\mathcal{X}$, its embedding is:

$$z = E(x), \qquad z\in\mathcal{E}$$

ACE Atlas assumes that semantic relations can be analyzed through geometric structure in $\mathcal{E}$.

---

## 4.2 Context Matrix

A semantic field is constructed from a set of anchor statements:

$$A_S=\{a_1,a_2,\dots,a_k\}$$

where each anchor represents an invariant, axiom, contextual relation, or domain-defining statement.

Each anchor is embedded as:

$$v_i=E(a_i), \qquad v_i\in\mathbb{R}^{d}$$

The context matrix associated with field $S$ is:

$$C_S=\begin{bmatrix}v_1^T\\ v_2^T\\ \vdots\\ v_k^T\end{bmatrix}\in\mathbb{R}^{k\times d}$$

This matrix represents the geometric structure of the semantic field.

---

## 4.3 Semantic Field Subspace

The semantic field $S$ is approximated as the subspace generated by its anchor embeddings:

$$S=\operatorname{span}(v_1,v_2,\dots,v_k)$$

To obtain an orthonormal basis for $S$, singular value decomposition is applied:

$$C_S = U\Sigma W^T$$

Let:

$$B_S \in \mathbb{R}^{d\times r}$$

be the orthonormal basis formed by the first $r$ right singular vectors associated with non-negligible singular values.

Then:

$$S \approx \operatorname{span}(B_S)$$

where $r\leq k$ is the effective semantic rank of the field.

---

## 4.4 Contextual Projection

Given an input embedding $z$, its orthogonal projection onto semantic field $S$ is:

$$\Pi_S(z)=B_SB_S^Tz$$

The residual component outside the field is:

$$r_S(z)=z-\Pi_S(z)$$

This residual measures the component of the input not explained by the contextual field.

---

## 4.5 Origin Cost

ACE Atlas defines the origin cost of $z$ relative to field $S$ as:

$$O_S(z)=||z-\Pi_S(z)||^2$$

or equivalently:

$$O_S(z)=||r_S(z)||^2$$

Interpretation:

$$O_S(z)\approx 0$$

indicates strong contextual compatibility, while large $O_S(z)$ indicates semantic dispersion relative to field $S$.

---

## 4.6 Field Selection

Given a collection of semantic fields:

$$\mathcal{S}=\{S_1,S_2,\dots,S_m\}$$

the dominant contextual field for $z$ is selected by minimum origin cost:

$$S^*(z)=\arg\min_{S_j\in\mathcal{S}}O_{S_j}(z)$$

The second-best field is:

$$S^{(2)}(z)=\arg\min_{S_j\in\mathcal{S}\setminus\{S^*(z)\}}O_{S_j}(z)$$

The field competition margin is:

$$M(z)=O_{S^{(2)}(z)}(z)-O_{S^*(z)}(z)$$

A larger margin indicates stronger contextual determination. A small margin indicates ambiguity or field competition.

---

## 4.7 Contextual Coherence

Contextual coherence is defined as a function of origin cost and field margin:

$$\kappa(z)=f\left(O_{S^*(z)}(z),M(z)\right)$$

where $\kappa(z)$ increases as origin cost decreases and field margin increases.

A simple operational form is:

$$\kappa(z)=\frac{M(z)}{O_{S^*(z)}(z)+\epsilon}$$

where $\epsilon>0$ prevents numerical instability.

This score measures whether $z$ belongs clearly to a semantic field.

However, contextual coherence does not determine whether the input preserves the epistemic orientation of that field.

---

## 4.8 Directional Invariant Poles

Let:

$$\mathcal{I}=\{I_1,I_2,\dots,I_n\}$$

be a set of foundational invariants associated with epistemic integrity.

For each invariant $I_i$, define two semantic poles:

$$p_i^+$$

representing preservation of the invariant, and:

$$p_i^-$$

representing inversion of the invariant.

Their embeddings are:

$$v_i^+=E(p_i^+)$$

$$v_i^-=E(p_i^-)$$

The directional invariant vector is:

$$d_i=\frac{v_i^+-v_i^-}{||v_i^+-v_i^-||}$$

where $d_i$ points from invariant inversion toward invariant preservation.

---

## 4.9 Epistemic Orientation Score

For an input embedding $z$, the epistemic orientation relative to invariant $I_i$ is:

$$\phi_i(z)=\langle \hat{z},d_i\rangle$$

where:

$$\hat{z}=\frac{z}{||z||}$$

and $d_i$ is normalized.

Interpretation:

$$\phi_i(z)>0$$

indicates directional preservation of invariant $I_i$;

$$\phi_i(z)<0$$

indicates directional inversion;

$$\phi_i(z)\approx0$$

indicates ambiguity or weak directional determination.

---

## 4.10 Aggregate Epistemic Integrity

For a set of invariants $\mathcal{I}$, aggregate epistemic integrity may be defined as:

$$\Phi(z)=\frac{1}{n}\sum_{i=1}^{n}w_i\phi_i(z)$$

where:

$$w_i\geq0,\qquad \sum_{i=1}^{n}w_i=1$$

are invariant weights.

A conservative alternative is:

$$\Phi_{\min}(z)=\min_i \phi_i(z)$$

This conservative form flags inversion if any critical invariant is violated.

---

## 4.11 Semantic Trajectory

A reasoning process or dialogue is represented as a semantic trajectory:

$$\tau=(z_1,z_2,\dots,z_T)$$

where each $z_t$ corresponds to a reasoning step, generated segment, or conversational turn.

Contextual coherence over time is:

$$\kappa(\tau)=\{\kappa(z_t)\}_{t=1}^{T}$$

Epistemic orientation over time is:

$$\Phi(\tau)=\{\Phi(z_t)\}_{t=1}^{T}$$

---

## 4.12 Criterion Drift

Criterion drift occurs when a trajectory remains contextually coherent while losing epistemic orientation.

Formally, for a trajectory element $z_t$:

$$\text{Drift}(z_t)=\left[O_{S^*(z_t)}(z_t)\leq\theta_O\right]\wedge\left[\Phi(z_t)<\theta_\Phi\right]$$

where:

* $\theta_O$ is the maximum acceptable origin cost,
* $\theta_\Phi$ is the minimum acceptable epistemic orientation threshold.

The central failure mode is:

$$O_{S^*(z_t)}(z_t)\leq\theta_O\quad\wedge\quad\Phi(z_t)<0$$

This means the input remains inside the contextual field while directionally inverting its epistemic structure.

---

## 4.13 Geometric Criterion Preservation

A trajectory preserves criterion when it remains both contextually coherent and epistemically oriented:

$$\forall t\in\{1,\dots,T\}:O_{S^*(z_t)}(z_t)\leq\theta_O\quad\wedge\quad\Phi(z_t)\geq\theta_\Phi$$

Equivalently:

$$\operatorname{Preserve}(\tau)=1$$

if:

$$\min_t \Phi(z_t)\geq\theta_\Phi$$

and:

$$\max_t O_{S^*(z_t)}(z_t)\leq\theta_O$$

Otherwise:

$$\operatorname{Preserve}(\tau)=0$$

---

## 4.14 Deterministic Runtime Policy

ACE Atlas converts geometric measurements into deterministic runtime actions.

Let:

$$a(z)\in\{\text{ALLOW},\text{CLARIFY},\text{FLAG\_DRIFT}\}$$

The policy is defined as:

$$a(z)=\begin{cases}\text{ALLOW}, & O_{S^*}(z)\leq\theta_O \wedge \Phi(z)\geq\theta_\Phi \\ \text{CLARIFY}, & M(z)<\theta_M \vee |\Phi(z)|<\theta_A \\ \text{FLAG\_DRIFT}, & O_{S^*}(z)\leq\theta_O \wedge \Phi(z)<\theta_\Phi \end{cases}$$

where:

* $\theta_M$ is the ambiguity threshold for field competition,
* $\theta_A$ is the ambiguity threshold for epistemic orientation,
* $\theta_O$ controls contextual compatibility,
* $\theta_\Phi$ controls epistemic preservation.

This policy allows the system to distinguish:

1. messages outside the field,
2. messages ambiguously located between fields,
3. messages inside a field but directionally inverted.

---

## 4.15 Central Mathematical Claim

The core claim of ACE Atlas is that reliable generative reasoning requires simultaneous satisfaction of two conditions:

$$\text{Contextual Coherence}$$

and

$$\text{Epistemic Integrity}$$

Formally:

$$\text{Reliable}(z)\iff\left[O_{S^*(z)}(z)\leq\theta_O\right]\wedge\left[\Phi(z)\geq\theta_\Phi\right]$$

Thus, contextual coherence alone is insufficient:

$$O_{S^*(z)}(z)\leq\theta_O\nRightarrow\Phi(z)\geq\theta_\Phi$$

This formalizes the central distinction of the paper:

$$\boxed{\text{Contextual Coherence}\neq\text{Epistemic Integrity}}$$

ACE Atlas models criterion as the preservation of directional epistemic structure within geometrically stable semantic fields.

---

# 5. Experimental Setup

This section describes the experimental configuration used to evaluate ACE Atlas under controlled semantic trajectory conditions.

The experiments were designed to test the central hypothesis of this work:

a reasoning trajectory may remain contextually coherent while progressively inverting the epistemic orientation of its foundational semantic field.

The evaluation therefore measures two independent dimensions:

1. Contextual Coherence
2. Epistemic Integrity

All experiments were conducted deterministically using fixed semantic fields, fixed invariant definitions, cached embeddings, and predefined runtime thresholds.

---

## 5.1 Experimental Objectives

The experimental framework was designed to evaluate five core questions:

1. Can semantic fields be constructed geometrically from invariant anchor relations?
2. Can contextual compatibility be measured through semantic field projection?
3. Can semantically coherent trajectories directionally invert foundational invariants?
4. Can criterion drift be detected geometrically before unrestricted reasoning expansion?
5. Can deterministic runtime policies distinguish:
* stable reasoning,
* ambiguity,
* and directional criterion inversion?



The experiments do not attempt to solve universal truth verification, consciousness, or general intelligence.

Instead, the experiments evaluate whether geometric criterion preservation can be operationalized as a measurable runtime property.

---

## 5.2 Semantic Fields

Three primary semantic fields were constructed for the criterion stability experiments:

1. Fundamental Field
2. Factual Field
3. Rhetorical Field

These fields were intentionally selected to model:

* structural coherence,
* evidential reasoning,
* and persuasive semantic pressure.

Each field was generated from manually curated anchor statements representing coherent semantic structures.

### 5.2.1 Fundamental Field

The Fundamental Field contains invariants associated with structural epistemic coherence.

Example anchors include:

* “Identity remains stable within a coherent context.”
* “A statement cannot be true and false in the same sense simultaneously.”
* “Facts must not be replaced by persuasive narratives.”
* “Interpretation must remain bounded by evidence.”
* “Semantic continuity requires stable orientation over time.”

The purpose of this field is not ideological enforcement, but preservation of structural semantic orientation.

### 5.2.2 Factual Field

The Factual Field contains anchors associated with evidential and document-constrained reasoning.

Example anchors include:

* “A factual claim requires evidence.”
* “Contradictory testimony must be identified before conclusion.”
* “A narrative cannot override verifiable evidence.”
* “Temporal order matters when evaluating responsibility.”
* “Unsupported claims remain uncertain.”

This field models evidential semantic structure.

### 5.2.3 Rhetorical Field

The Rhetorical Field contains anchors associated with persuasive and emotionally framed semantic structures.

Example anchors include:

* “Emotional framing can shift interpretation away from facts.”
* “Repeated claims can create perceived truth without verification.”
* “Narrative pressure can alter judgment.”
* “The appearance of coherence is not equivalent to truth.”
* “Persuasive language can substitute emotional force for evidence.”

This field was designed to model semantic pressure capable of competing with factual or structural coherence.

---

## 5.3 Anchor Embeddings

Each anchor statement:

$$a_i$$

was embedded using the OpenAI embedding model:

$$E(\cdot)=\texttt{text-embedding-3-small}$$

with embedding dimensionality:

$$d=1536$$

Each anchor embedding is therefore represented as:

$$v_i=E(a_i)\in\mathbb{R}^{1536}$$

Embeddings were cached to guarantee deterministic reproducibility across repeated evaluations.

No fine-tuning or gradient optimization was applied during the experiments.

---

## 5.4 Context Matrix Construction

For each semantic field $S$, anchor embeddings were aggregated into a context matrix:

$$C_S= \begin{bmatrix} v_1^T \\ v_2^T \\ \vdots \\ v_k^T \end{bmatrix}$$

Singular Value Decomposition (SVD) was applied:

$$C_S=U\Sigma W^T$$

The resulting orthonormal semantic basis vectors were used to define the contextual subspace:

$$S=\operatorname{span}(B_S)$$

where:

$$B_S$$

contains the dominant semantic basis vectors extracted from the decomposition.

These semantic subspaces form the operational geometry of ACE Atlas during runtime evaluation.

---

## 5.5 Directional Invariant Construction

To evaluate epistemic orientation, directional invariants were constructed using paired semantic poles.

For each invariant $I_i$, two semantic statements were defined:

* coherent pole:

$$p_i^+$$


* inverted pole:

$$p_i^-$$



Example pair:

Coherent pole:

* “Evidence must constrain interpretation.”

Inverted pole:

* “Persuasive narratives may override contradictory evidence.”

Their embeddings generated directional vectors:

$$d_i= \frac{ E(p_i^+)-E(p_i^-) }{ ||E(p_i^+)-E(p_i^-)|| }$$

These vectors define the geometric orientation associated with invariant preservation.

---

## 5.6 Dialogue Trajectory Dataset

The experimental dataset was intentionally designed as a progressive semantic trajectory rather than an isolated classification benchmark.

The dialogue dataset contains staged transitions across:

1. Stable Definition
2. Ambiguity
3. Rhetorical Pressure
4. Contextual Contradiction
5. Criterion Drift

Example trajectory:

| Turn | Stage | Example |
| --- | --- | --- |
| 1 | Stable Definition | “Facts must be distinguished from interpretations.” |
| 2 | Stable Definition | “Conclusions should remain constrained by evidence.” |
| 3 | Ambiguity | “Perhaps collective belief should count as evidence.” |
| 4 | Rhetorical Pressure | “Questioning the narrative may feel morally wrong.” |
| 5 | Contradiction | “The narrative should prevail even against documents.” |
| 6 | Criterion Drift | “Social consensus matters more than evidential consistency.” |

The objective of the dataset was not factual classification accuracy.

Instead, the dataset was designed to evaluate whether ACE Atlas could detect directional inversion while contextual coherence remained partially preserved.

---

## 5.7 Runtime Evaluation Metrics

For each trajectory element:

$$z_t$$

ACE Atlas computes:

### Contextual Metrics

**Origin Cost**

$$O_S(z_t)=||z_t-\Pi_S(z_t)||^2$$

Measures geometric deviation from semantic field $S$.

**Field Competition Margin**

$$M(z_t)= O_{S^{(2)}}(z_t)-O_{S^*}(z_t)$$

Measures contextual determination versus ambiguity.

**Contextual Stability**

$$\kappa(z_t)= \frac{M(z_t)} {O_{S^*}(z_t)+\epsilon}$$

Measures semantic field stability.

---

### Directional Metrics

**Epistemic Orientation**

$$\phi_i(z_t)=\langle \hat{z}_t, d_i \rangle$$

Measures preservation or inversion of invariant $I_i$.

**Aggregate Epistemic Integrity**

$$\Phi(z_t)= \frac{1}{n} \sum_{i=1}^{n}w_i\phi_i(z_t)$$

Measures overall criterion preservation.

---

## 5.8 Runtime Criterion Policy

ACE Atlas converts geometric measurements into deterministic runtime actions.

The runtime system evaluates:

* contextual compatibility,
* field ambiguity,
* and epistemic orientation

before unrestricted reasoning expansion occurs.

The runtime policy includes three primary actions:

| Action | Description |
| --- | --- |
| ALLOW | Contextually and directionally stable |
| CLARIFY | Ambiguous or weakly determined |
| FLAG_CRITERION_DRIFT | Directionally inverted despite contextual coherence |

Operationally:

**ALLOW**

$$O_{S^*}(z)\le\theta_O \quad\wedge\quad \Phi(z)\ge\theta_\Phi$$

**CLARIFY**

$$M(z)<\theta_M \quad\vee\quad |\Phi(z)|<\theta_A$$

**FLAG_CRITERION_DRIFT**

$$O_{S^*}(z)\le\theta_O \quad\wedge\quad \Phi(z)<0$$

This policy allows ACE Atlas to distinguish:

* semantic ambiguity,
* contextual instability,
* and directional criterion inversion.

---

## 5.9 PCA Visualization

Principal Component Analysis (PCA) was used to visualize semantic field geometry and trajectory evolution.

PCA projections included:

* semantic anchors,
* semantic fields,
* dialogue trajectory points,
* and runtime transitions.

The visualization objective was not exact topological preservation, but interpretable representation of semantic movement across contextual regions.

The resulting projections revealed:

* coherent clustering of semantic fields,
* progressive movement toward rhetorical regions,
* partial contextual return through lexical reuse,
* and directional inversion despite contextual proximity.

This distinction proved critical:

semantic proximity alone did not guarantee preservation of epistemic orientation.

---

## 5.10 Experimental Interpretation Strategy

The experiments were evaluated under two independent dimensions:

| Dimension | Purpose |
| --- | --- |
| Contextual Coherence | Determines whether the trajectory belongs to a semantic field |
| Epistemic Integrity | Determines whether the trajectory preserves the invariant structure of the field |

This separation forms the central experimental contribution of ACE Atlas.

The framework therefore evaluates not merely whether reasoning appears coherent, but whether the reasoning trajectory preserves the foundational semantic orientation that defines the meaning of the active contextual field.

---

## 5.11 ACA Runtime

An operational criterion-supervision architecture built directly from the experimental geometric framework.

Importantly, ACA Runtime was not introduced as an independent theoretical layer disconnected from the experiments.

Rather, the runtime architecture emerged as a direct operational consequence of the experimental findings themselves.

Specifically, the experiments demonstrated that:

* semantic fields remained geometrically stable,
* directional orientation could be measured persistently,
* contextual transitions exhibited topological structure,
* and semantic trajectories could be supervised deterministically through invariant continuity.

These observations allowed the original geometric framework to evolve into an operational runtime architecture.

### 5.11.1 Runtime Operational Pipeline

The runtime architecture evaluates semantic trajectories through the following operational stages:

$$\text{Input} \rightarrow \text{Embedding} \rightarrow \text{Field Projection} \rightarrow \text{Orientation Evaluation} \rightarrow \text{Trajectory Continuity} \rightarrow \text{Topology Evaluation} \rightarrow \text{Runtime Decision}$$

Each stage preserves a different component of criterion continuity.

**Input Embedding**

The runtime first transforms the active semantic input into embedding space:

$$z = \text{Embed}(x)$$

where:

* $x$ represents the active semantic input,
* and $z$ represents its geometric semantic representation.

**Field Projection**

The embedded input is then projected against all semantic fields:

$$S = \{S_1, S_2, \dots, S_m\}$$

using origin-cost evaluation:

$$O_j = ||z - \Pi_{S_j}(z)||^2$$

The runtime selects the dominant contextual field:

$$S^* = \arg\min(O_j)$$

This stage determines contextual semantic positioning.

**Orientation Evaluation**

After contextual positioning, ACA Runtime evaluates directional invariant preservation.

For each invariant direction:

$$d_i$$

the runtime computes semantic orientation:

$$\phi_i = \text{Orientation}(z, d_i)$$

Aggregate orientation:

$$\Phi$$

then represents criterion continuity relative to the active semantic field.

This stage separates:

* contextual compatibility,
* from epistemic orientation.

**Trajectory Continuity**

The runtime then evaluates semantic continuity across interaction history.

Rather than analyzing isolated statements independently, ACA Runtime evaluates:

* orientation persistence,
* directional continuity,
* semantic recovery,
* and contextual evolution through time.

This transforms semantic supervision into:

trajectory-aware criterion preservation.

**Topology Evaluation**

The experiments further revealed that contextual transitions exhibit topological organization.

Neighboring fields may preserve criterion continuity, while distant transitions may destabilize orientation.

For example:

$$\text{foundational} \leftrightarrow \text{factual}$$

frequently preserved criterion continuity through semantic reorientation.

By contrast:

$$\text{foundational} \rightarrow \text{rhetorical} \rightarrow \text{inversion}$$

frequently produced criterion destabilization.

The runtime therefore evaluates:

* neighboring field transitions,
* distant transitions,
* semantic reorientation,
* and inversion risk

before unrestricted semantic continuation proceeds.

**Runtime Decision Layer**

The final runtime stage transforms geometric semantic measurements into operational criterion policies.

The runtime currently supports:

* `allow`
* `allow_light`
* `monitor`
* `clarify`
* `reject_or_clarify`
* `flag_drift`

These policies are determined through the interaction between:

* semantic compatibility,
* invariant orientation,
* topology-aware transitions,
* and trajectory continuity.

Importantly, the runtime does not attempt to rigidly constrain semantic generation.

Instead, it supervises whether semantic evolution remains:

* structurally coherent,
* recoverable,
* topology-compatible,
* and directionally aligned with the invariant structure of the active semantic field.

---

### 5.11.2 Experimental Significance

The runtime architecture represents an important evolution of the original ACE Atlas experiments.

Initially, the framework operated primarily as:

* semantic field analysis,
* geometric trajectory evaluation,
* and criterion drift visualization.

However, the experiments demonstrated that the same geometric structures could also function operationally as:

* persistent semantic orientation,
* contextual navigation infrastructure,
* and runtime criterion supervision.

This transition was critical.

The framework evolved from:

geometric semantic analysis

toward:

operational semantic navigation.

Under this formulation, ACA Runtime no longer reconstructs criterion repeatedly through prompt accumulation.

Instead, the runtime preserves semantic navigability through:

* invariant matrices,
* contextual topology,
* and persistent orientation continuity.

This explains both:

* the observed runtime stability,
* and the substantial reduction in prompt overhead observed during the comparative benchmark experiments.

Consequently, the runtime architecture emerged not as an external addition to the framework, but as the natural operational evolution of the geometric experimental results themselves.

---

## 5.12 Semantic Topology Configuration

The experimental framework initially modeled semantic fields as partially independent contextual subspaces constructed from:

* invariant anchors,
* contextual semantic relations,
* and embedding-based geometric organization.

However, as runtime trajectory analysis evolved, the experiments revealed that semantic fields do not behave as isolated regions.

Instead, the fields exhibit:

* neighboring continuity,
* directional compatibility,
* overlap structure,
* and transition-dependent stability.

This led to the introduction of:

semantic topology configuration

within ACA Runtime.

Under this formulation, semantic fields are interpreted not merely as classification categories, but as:

connected navigable contextual regions.

---

### 5.12.1 Semantic Field Organization

The runtime experiments currently operate using three primary semantic fields:

$$\mathcal{F} = \{ F_{\text{foundational}}, F_{\text{factual}}, F_{\text{rhetorical}} \}$$

Each field is constructed from:

* invariant anchors,
* contextual semantic examples,
* and orthogonal geometric projections derived through SVD-based subspace decomposition.

The fields represent different modes of semantic organization:

| Field | Operational Function |
| --- | --- |
| Foundational | invariant continuity and criterion preservation |
| Factual | evidential grounding and contextual stabilization |
| Rhetorical | persuasive semantic framing and narrative influence |

The fields are therefore not merely semantic categories, but:

operational contextual attractors.

---

### 5.12.2 Neighboring Topology

Trajectory experiments demonstrated that certain semantic transitions preserve criterion continuity despite contextual movement.

In particular, transitions between:

$$F_{\text{foundational}} \leftrightarrow F_{\text{factual}}$$

frequently preserved:

* orientation continuity,
* semantic recovery,
* invariant stability,
* and criterion coherence.

This revealed that neighboring semantic regions may function cooperatively during reasoning evolution.

Under ACA Runtime, these transitions are treated as:

topology-compatible neighboring fields.

Importantly, neighboring movement does not necessarily imply semantic drift.

Instead, neighboring contextual evolution may act as:

* epistemic stabilization,
* semantic recovery,
* or criterion reorientation.

This behavior motivated the introduction of:

semantic reorientation

as a distinct runtime condition.

---

### 5.12.3 Destabilizing Topology

By contrast, experiments involving rhetorical escalation frequently produced:

* orientation decay,
* semantic inversion,
* criterion destabilization,
* and contextual fragmentation.

Transitions such as:

$$F_{\text{foundational}} \rightarrow F_{\text{rhetorical}} \rightarrow \text{inversion}$$

showed substantially higher instability.

These transitions frequently displaced semantic trajectories away from:

* evidential grounding,
* invariant continuity,
* and stable criterion preservation.

Under ACA Runtime, these transitions are interpreted as:

topology-destabilizing trajectories.

This distinction allows the runtime to differentiate between:

* coherent contextual evolution,
* and destabilizing semantic drift.

---

### 5.12.4 Topology-Aware Runtime Evaluation

The runtime therefore evaluates not only:

* semantic position,
* or local field compatibility,

but also:

* field relationships,
* transition distance,
* neighboring continuity,
* and orientation persistence across contextual movement.

This transforms semantic supervision into:

topology-aware semantic navigation.

Operationally, the runtime classifies transitions according to:

| Transition Type | Runtime Interpretation |
| --- | --- |
| Neighboring Transition | potentially stabilizing |
| Compatible Transition | orientation-preserving |
| Ambiguous Transition | monitor or clarify |
| Destabilizing Transition | drift supervision |
| Inversion Trajectory | flag_drift |

The resulting runtime architecture therefore supervises:

* where semantic trajectories are positioned,
* how they evolve,
* and whether criterion continuity remains recoverable.

---

### 5.12.5 Semantic Navigation Interpretation

The introduction of semantic topology fundamentally changes the interpretation of criterion supervision.

Traditional prompt-heavy systems frequently reconstruct semantic grounding repeatedly during interaction.

ACA instead treats semantic reasoning as:

navigable movement within structured contextual topology.

Under this formulation, semantic complexity may remain extremely large while semantic navigation remains operationally tractable through:

* invariant orientation,
* neighboring continuity,
* and topology-aware runtime positioning.

Importantly, the Atlas does not attempt to explicitly enumerate every semantic state.

Instead, it preserves:

* navigability,
* orientation continuity,
* contextual recoverability,
* and criterion-preserving transition structure.

This interpretation explains why semantic continuity may remain stable while runtime overhead is substantially reduced.

Rather than reconstructing criterion repeatedly through natural language prompts, ACA Runtime preserves persistent orientation within semantic topology itself.

Runtime Policy Definitions

State
Meaning
allow
stable continuity
allow light
neighboring reorientation
monitor
uncertain continuity
clarify
ambiguous positioning
reject_or_clarify
unresolved incompatibility
flag_drift
criterion inversion


progressive degradation of orientation.

Stable
↓
Neighbor Reorientation
↓
Uncertain Continuity
↓
Ambiguous Positioning
↓
Incompatibility
↓
Criterion Inversion


\section{6. Experimental Results}

This section presents the experimental results obtained using the ACE Atlas criterion preservation framework. The experiments were designed to evaluate whether contextual coherence and epistemic integrity remain equivalent during reasoning evolution, or whether a semantic trajectory may preserve contextual compatibility while directionally inverting its foundational invariants. The results demonstrate that these two dimensions diverge under rhetorical pressure, ambiguity, and contextual contradiction. Specifically, semantic trajectories may remain geometrically close to a contextual field while progressively losing directional epistemic orientation. This behavior constitutes the central experimental finding of the paper.

\subsection{6.1 Semantic Field Organization}

The first experiment evaluated the geometric organization of semantic fields constructed from anchor embeddings. Three primary fields were analyzed: the Fundamental Field, the Factual Field, and the Rhetorical Field. Principal Component Analysis (PCA) projections revealed stable geometric clustering across these contextual domains. The Fundamental and Factual fields formed partially overlapping regions associated with evidential consistency, logical continuity, semantic persistence, and structurally constrained interpretation. In contrast, the Rhetorical field occupied an adjacent but directionally distinct region associated with persuasive framing, emotional pressure, narrative dominance, and semantic reinterpretation.

Importantly, the rhetorical region was not fully separated from the factual region. This overlap is critical: the experiments suggest that rhetorical trajectories frequently reuse factual vocabulary while progressively modifying the epistemic orientation of interpretation itself. Consequently, semantic proximity alone proved insufficient to distinguish between evidential preservation and persuasive reinterpretation. This observation motivated the introduction of directional invariant analysis.

\begin{figure}[h]
    \centering
    % Insert Figure 1 here
    \caption{Semantic Field Geometry. PCA projection demonstrating coherent geometric regions where rhetorical language partially overlaps factual language, illustrating that contextual proximity alone cannot guarantee preservation of criterion.}
\end{figure}

\subsection{6.2 Contextual Stability Across the Dialogue Trajectory}

The second experiment evaluated contextual compatibility throughout a staged dialogue trajectory. For each trajectory element $\tau = (z_1, z_2, \dots, z_T)$, ACE Atlas computed the origin cost, dominant semantic field, field competition margin, and contextual stability. 

The early dialogue stages remained strongly aligned with the Fundamental and Factual fields, exhibiting low origin cost, high field margins, strong semantic density, and stable contextual coherence. As ambiguity and rhetorical pressure increased, the trajectory gradually migrated toward the rhetorical field. However, contextual compatibility remained partially preserved because the dialogue continued reusing evidential vocabulary, consistency terminology, legal framing, and semantic structures associated with factual reasoning. This produced a critical phenomenon: the trajectory remained semantically coherent while progressively destabilizing its foundational orientation. This behavior cannot be explained solely through contextual dispersion.



\subsection{6.3 Directional Epistemic Orientation}

The third experiment evaluated epistemic orientation relative to foundational directional invariants. For each invariant $I_i$, ACE Atlas computed $\phi_i(z_t) = \langle \hat{z}_t, d_i \rangle$, where $d_i$ represents the invariant-preserving semantic direction. 

Unlike origin cost, epistemic orientation revealed a progressive directional inversion throughout the dialogue. The early stages exhibited $\phi_i(z_t) > 0$, indicating the preservation of evidential and structural invariants. As rhetorical pressure increased, orientation scores progressively decreased. During the contradiction and drift stages, the orientation fell below zero ($\phi_i(z_t) < 0$), indicating a directional inversion of the foundational semantic structure. Crucially, this inversion occurred while contextual proximity remained partially preserved, demonstrating that contextual coherence and epistemic integrity diverge under rhetorical pressure.


\begin{figure}[h]
    \centering
    % Insert Figure 3 here
    \caption{Epistemic Orientation Through Time. The trajectory remains contextually coherent while directional preservation collapses, crossing the zero-orientation threshold and rendering criterion loss geometrically measurable.}
\end{figure}

\subsection{6.4 Semantic Trajectory Evolution and Reorientation}

PCA trajectory analysis revealed that the dialogue evolved continuously rather than discontinuously. As ambiguity increased, the trajectory approached overlap regions between factual and rhetorical semantic structures, suggesting that criterion drift frequently emerges through gradual reinterpretation rather than abrupt contradiction. Meaning progressively shifts, directional orientation weakens, and foundational constraints become subordinated to rhetorical structure.

However, initial runtime experiments revealed that semantically coherent reasoning frequently exhibited controlled neighboring contextual transitions while still preserving criterion continuity. One of the clearest observed patterns was the transition from foundational to factual and back to foundational. These movements did not produce semantic inversion or criterion collapse; instead, they demonstrated positive orientation continuity and stable semantic recovery. 

This behavior defines the operational state of \textit{semantic reorientation}: a topology-preserving neighboring semantic transition that temporarily re-anchors contextual interpretation while maintaining invariant continuity. Consequently, reasoning trajectories are interpreted dynamically according to field relationships, invariant continuity, and contextual topology, distinguishing destabilizing semantic drift from productive reorientation.

\subsection{6.5 Runtime Criterion Policy Results}

The runtime policy layer transforms geometric measurements into deterministic reasoning actions by evaluating contextual compatibility, field ambiguity, and epistemic orientation before unrestricted reasoning expansion. 

\begin{table}[h]
\centering
\begin{tabular}{ll}
\hline
\textbf{Runtime Action} & \textbf{Operational Description} \\
\hline
\texttt{ALLOW} & Stable semantic compatibility with preserved orientation continuity. \\
\texttt{ALLOW\_LIGHT} & Criterion preserved under neighboring contextual transition. \\
\texttt{MONITOR} & Low-confidence semantic compatibility requiring continued supervision. \\
\texttt{CLARIFY} & Ambiguous semantic interpretation requiring additional context. \\
\texttt{REJECT\_OR\_CLARIFY} & Semantic instability or unresolved field incompatibility. \\
\texttt{FLAG\_CRITERION\_DRIFT} & Detected orientation inversion or destabilizing semantic drift. \\
\hline
\end{tabular}
\caption{ACA Runtime Policy States. The system detects inversion of criterion independently of surface-level semantic instability.}
\end{table}

Stable dialogue stages consistently triggered \texttt{ALLOW}, while ambiguous stages triggered \texttt{CLARIFY}. Contradictory and rhetorically inverted stages triggered \texttt{FLAG\_CRITERION\_DRIFT}. Importantly, the drift detection policy activated even when contextual coherence remained relatively stable, proving that ACE Atlas detects the inversion of the criterion itself, not merely semantic dispersion.

\subsection{6.6 Core Experimental Finding}

The experiments demonstrate a previously underformalized failure mode in generative reasoning systems: a semantic trajectory may remain linguistically fluent, preserve contextual proximity, reuse evidential vocabulary, and maintain semantic coherence, while simultaneously directionally inverting foundational invariants, subordinating evidence to rhetoric, or destabilizing causal structure.

Because this phenomenon cannot be fully captured through semantic similarity, factual retrieval, probabilistic confidence, or contextual compatibility alone, reliable generative systems require the simultaneous preservation of Contextual Coherence and Epistemic Integrity. The central result of this paper is formally summarized as:
$$\text{Contextual Coherence} \neq \text{Epistemic Integrity}$$

\subsection{6.7 Operational Interpretation and Pipeline}

The core objective of ACE Atlas during inference is to evaluate whether a reasoning trajectory remains structurally oriented relative to the active semantic field before unrestricted reasoning expansion occurs. Given an input $x$, it is embedded into semantic space as $z = E(x)$ where $z \in \mathbb{R}^d$. ACE Atlas evaluates contextual compatibility against available semantic fields $\mathcal{S} = \{S_1, S_2, \dots, S_m\}$ using origin cost $O_{S_j}(z) = ||z - \Pi_{S_j}(z)||^2$, selecting the dominant field $S^*$ via minimum origin cost. 

Once positioned, the epistemic orientation is evaluated relative to the invariant structure of $S^*$. For each invariant $I_i$, the framework computes $\phi_i(z) = \langle \hat{z}, d_i \rangle$. Aggregate epistemic integrity is evaluated as $\Phi(z) = \frac{1}{n}\sum_i w_i\phi_i(z)$. These geometric measurements are then converted into the deterministic runtime policies previously outlined, transforming semantic geometry into measurable reasoning constraints.



\subsection{6.8 Runtime Efficiency Benchmark}

Beyond semantic stability, the framework was evaluated to determine if geometric criterion preservation can reduce the computational overhead traditionally required for prompt-based alignment. A comparative runtime benchmark was constructed between a prompt-heavy criterion-preservation strategy (relying on repeated natural language instructions) and the ACA Runtime architecture (externalized persistent geometric infrastructure).

The benchmark evaluated 15-turn semantic trajectory scenarios designed to test criterion continuity, semantic drift, contextual ambiguity, and rhetorical escalation. The prompt-heavy approach required repeatedly injecting instructions (e.g., maintain coherence, avoid contradiction, preserve evidential grounding) into the active context window, exacerbating context accumulation. In contrast, ACA Runtime preserved criterion structurally through field projection and orientation continuity, requiring only a minimal system prompt.

\begin{table}[h]
\centering
\begin{tabular}{lcc}
\hline
\textbf{Runtime Strategy} & \textbf{Cumulative Token Usage (15 Turns)} & \textbf{Efficiency Gain} \\
\hline
Prompt-Heavy Criterion Runtime & 126,893 tokens & - \\
ACA Runtime Criterion Supervision & 37,697 tokens & \textbf{70.26\% Reduction} \\
\hline
\end{tabular}
\caption{Runtime Token Efficiency Benchmark. Externalizing semantic criterion into geometric infrastructure substantially reduces context accumulation across long dialogue trajectories.}
\end{table}



scenario
turn
prompt_heavy_tokens
aca_runtime_tokens
token_savings
token_savings_percent
stable_foundational
1
274
67
207
75.55


stable_foundational
2
283
76
207
73.14


stable_foundational
3
294
87
207
70.41


stable_foundational
4
304
97
207
68.09


stable_foundational
5
315
108
207
65.71


rhetorical_drift
1
272
65
207
76.1


rhetorical_drift
2
281
74
207
73.67


rhetorical_drift
3
296
89
207
69.93


rhetorical_drift
4
302
95
207
68.54


rhetorical_drift
5
311
104
207
66.56


ambiguous_context
1
266
59
207
77.82


ambiguous_context
2
276
69
207
75


ambiguous_context
3
292
85
207
70.89


ambiguous_context
4
296
89
207
69.93


ambiguous_context
5
304
97
207
68.09


controversial_pressure
1
274
67
207
75.55


controversial_pressure
2
296
89
207
69.93


controversial_pressure
3
300
93
207
69


controversial_pressure
4
322
115
207
64.29


controversial_pressure
5
334
127
207
61.98


TOTAL


5892
1752
4140
70.26




https://colab.research.google.com/drive/1JSgACANC1MGPu5FnqOrDI07fvyQUimdo?usp=sharing

The benchmark demonstrates a measured runtime token reduction of $70.26\%$. Crucially, this reduction was not achieved by removing contextual reasoning or reducing semantic supervision. Instead, the efficiency emerged because the criterion was externalized from repeated natural language instructions into a persistent geometric infrastructure. Under ACA Runtime, criterion becomes reusable semantic structure, suggesting that reliable generative reasoning can scale efficiently by preserving directional orientation rather than repeatedly reconstructing it linguistically.


\subsection{6.9 Runtime Efficiency Benchmark}

The previous experiments demonstrated that ACE Atlas can preserve the semantic criterion through contextual field geometry, directional invariant orientation, semantic trajectory supervision, and topology-aware runtime policies. However, beyond semantic stability itself, an additional operational question emerges: Can criterion preservation reduce the computational overhead traditionally required for prompt-based alignment and reasoning supervision?

To evaluate this question, a comparative runtime benchmark was constructed between a prompt-heavy criterion-preservation strategy and the ACA Runtime criterion-preservation architecture. The objective of the benchmark was not to measure raw language generation quality alone, but rather to evaluate the operational cost of maintaining criterion continuity throughout multi-step reasoning trajectories.

\subsubsection{6.9.1 Prompt-Heavy Criterion Strategy}
Modern prompt-engineering approaches frequently preserve reasoning stability by repeatedly injecting criterion instructions into the active context window. Typical prompts include persistent instructions such as maintaining coherence, avoiding contradiction, preserving evidential grounding, maintaining continuity, preserving uncertainty, avoiding rhetorical manipulation, and preserving causal consistency. Under this approach, the criterion remains encoded primarily as repeated natural language instructions. 

As contextual trajectories evolve, these instructions often accumulate across multiple reasoning stages, increasing runtime token overhead. For the benchmark, a representative criterion-preservation prompt was constructed containing evidential constraints, continuity preservation, contradiction avoidance, and foundational semantic invariants. The resulting criterion prompt required approximately:
$$254 \text{ tokens}$$
per interaction, even before user context accumulation began.

\subsubsection{6.9.2 ACA Runtime Criterion Strategy}
In contrast, ACA Runtime externalizes the criterion into semantic fields, directional invariants, contextual topology, runtime trajectory supervision, and persistent geometric orientation. Under this architecture, the criterion does not require repeated textual reinjection during every interaction. Instead, runtime supervision is performed structurally through field projection, origin-cost evaluation, orientation continuity, neighboring transition analysis, and deterministic criterion policies. Operationally, the ACA runtime only required a minimal system prompt, lightweight runtime metadata, and semantic field supervision.

\subsubsection{6.9.3 Benchmark Configuration}
The benchmark evaluated four semantic trajectory scenarios: Stable Foundational Reasoning, Rhetorical Drift, Ambiguous Context, and Controversial Semantic Pressure. Each scenario contained staged multi-turn reasoning trajectories designed to evaluate criterion continuity, semantic drift, contextual ambiguity, rhetorical escalation, and semantic reorientation. 

Two runtime strategies were then compared: the \textit{Prompt-Heavy Runtime} (criterion preserved through repeated textual prompting) and the \textit{ACA Runtime} (criterion preserved through semantic field geometry and runtime orientation supervision). The benchmark measured accumulated input tokens, contextual accumulation overhead, and the absolute criterion-preservation runtime cost.

\subsubsection{6.9.4 Runtime Results}
The benchmark produced the following total runtime costs across the evaluated scenarios:

\begin{table}[h]
\centering
\begin{tabular}{lc}
\hline
\textbf{Runtime Strategy} & \textbf{Total Tokens} \\
\hline
Prompt-Heavy Criterion Runtime & 5,892 \\
ACA Runtime Criterion Supervision & 1,752 \\
\hline
\end{tabular}
\caption{Runtime Token Efficiency Benchmark comparing prompt-based reconstruction versus geometric externalization.}
\end{table}

This resulted in an observed token reduction of:
$$4,140 \text{ tokens}$$
Which translates to an equivalent runtime efficiency gain of:
$$70.26\%$$


\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{1QQqC.jpg} % 
    \caption{Criterion Externalization and Runtime Token Reduction. The ACA Runtime architecture reduces operational overhead by preserving orientation structurally rather than linguistically.}
    \label{fig:token_reduction}
\end{figure}

\subsubsection{6.9.5 Interpretation}
Importantly, this reduction was not achieved by removing contextual reasoning or reducing semantic supervision. Instead, the reduction emerged because the criterion was externalized from repeated natural language instructions into a persistent geometric infrastructure. Under traditional approaches, the criterion is repeatedly reintroduced as text. Under ACA Runtime, it becomes a reusable semantic structure defined by invariant orientation and contextual topology. This distinction is operationally significant, suggesting that semantic criteria may be preserved much more efficiently when represented geometrically rather than repeatedly reconstructed linguistically.

\subsubsection{6.9.6 Runtime Criterion Persistence}
The experiments further demonstrated that ACA Runtime preserves criterion continuity even during contextual transitions. In particular, neighboring semantic transitions such as:
$$\text{foundational} \rightarrow \text{factual} \rightarrow \text{foundational}$$
did not necessarily produce criterion collapse. Instead, ACA Runtime identified a new operational behavior: \textit{semantic reorientation}, where contextual movement occurs and neighboring fields temporarily stabilize interpretation, yet criterion continuity remains preserved. This behavior differs fundamentally from unrestricted semantic drift, allowing the runtime to distinguish between destabilizing inversion, semantic ambiguity, and criterion-preserving neighboring transitions.

\subsubsection{6.9.7 Operational Implications}
The runtime benchmark suggests that criterion preservation may function as reusable semantic infrastructure, topology-aware runtime supervision, and persistent geometric orientation, rather than requiring repeated prompt-based reconstruction. This introduces several operational advantages: reduced prompt overhead, lower contextual accumulation, improved runtime continuity, and topology-aware semantic recovery. More broadly, the results suggest that reliable generative reasoning may depend not only on larger models or longer prompts, but on preserving directional semantic orientation throughout reasoning evolution. Under this interpretation, the semantic criterion becomes measurable, reusable, operational, and geometrically persistent.


\section{7. Limitations}

Although ACE Atlas demonstrates that contextual coherence and epistemic integrity can be geometrically separated, the present framework remains an early-stage semantic criterion architecture with important theoretical and operational limitations. This section outlines the primary constraints of the current formulation.

\subsection{7.1 No Universal Truth Verification}
ACE Atlas does not determine universal truth. The framework evaluates contextual compatibility, directional invariant preservation, and semantic trajectory orientation. Consequently, the system cannot independently verify objective reality, factual certainty, metaphysical truth, or universal correctness. A trajectory may preserve criterion relative to a semantic field while the field itself remains incomplete, biased, or externally incorrect. The framework therefore evaluates structural consistency relative to defined invariants rather than absolute epistemic certainty. This distinction is fundamental: ACE Atlas is a criterion-preservation framework, not a universal truth engine.

\subsection{7.2 Dependence on Anchor Construction}
Semantic fields depend heavily on the quality and structure of anchor selection. The current experiments use manually curated anchors representing conceptual invariants, factual constraints, and rhetorical structures. Poorly designed anchors may produce unstable fields, semantic overlap, incomplete contextual representation, or distorted invariant orientation. Similarly, directional invariant vectors depend on carefully constructed semantic pole pairs. Improper pole construction may weaken orientation sensitivity, introduce unintended semantic bias, or reduce interpretability. The present work therefore assumes that anchor construction itself is epistemically meaningful. Automated anchor discovery remains an open research problem.

\subsection{7.3 Embedding Model Dependence}
ACE Atlas operates entirely within embedding geometry. As a result, all measurements depend on the representational structure induced by the underlying embedding model. Different embedding architectures may produce different semantic topologies, altered field separations, different directional sensitivities, and distinct invariant projections. While the experiments were conducted using \texttt{text-embedding-3-small}, the framework itself is embedding-model agnostic. Future work should evaluate model transferability, geometric stability across embedding families, and robustness under multilingual semantic spaces.

\subsection{7.4 Limited Dataset Scale}
The experimental trajectories in this work were intentionally controlled and interpretable. The datasets were designed to isolate criterion drift, visualize semantic transitions, and evaluate directional inversion. Consequently, the experiments do not yet demonstrate large-scale conversational deployment, long-horizon autonomous reasoning, or real-world production robustness. The current experiments should therefore be interpreted as proof-of-concept demonstrations rather than definitive large-scale validation. Future work should evaluate broader conversational corpora, adversarial dialogue environments, legal reasoning datasets, scientific reasoning benchmarks, and multi-agent semantic interaction.

\subsection{7.5 PCA Projection Limitations}
The visualizations presented in this work rely on Principal Component Analysis (PCA) for interpretability. PCA projections reduce high-dimensional semantic geometry into two-dimensional representations. As a consequence, local distances may distort, directional structure may partially collapse, and overlap relationships may appear exaggerated or simplified. The figures should therefore be interpreted as conceptual geometric illustrations rather than exact topological representations of the embedding space. Future work may explore UMAP, diffusion geometry, manifold learning, or higher-dimensional interactive semantic visualization.

\subsection{7.6 Runtime Threshold Sensitivity}
The runtime policy layer depends on threshold selection. Key thresholds include origin-cost tolerance, field competition margins, ambiguity intervals, and epistemic orientation limits. Improper threshold calibration may produce excessive drift detection, insufficient sensitivity, or unstable runtime transitions. Although deterministic policies improve interpretability, robust threshold optimization remains an unresolved engineering problem. Adaptive threshold calibration and probabilistic confidence integration remain areas for future research.

\subsection{7.7 No Internal Mechanistic Interpretation}
ACE Atlas evaluates reasoning trajectories externally through semantic geometry. The framework does not directly analyze transformer circuits, attention heads, activation pathways, or internal model computation. Consequently, ACE Atlas should not be interpreted as a mechanistic explanation of neural reasoning. Instead, it functions as a runtime semantic stability layer, a geometric criterion evaluator, and a trajectory-orientation framework. The relationship between external semantic geometry and internal neural representations remains an open research area.

\subsection{7.8 Criterion Relativity}
Criterion preservation depends on the invariant structures chosen for evaluation. Different semantic systems may define different foundational invariants, distinct evidential hierarchies, or incompatible epistemic assumptions. ACE Atlas does not claim that all semantic fields share identical invariant structures. Instead, the framework evaluates whether trajectories remain directionally consistent relative to the active field being evaluated. This introduces an important philosophical limitation: criterion preservation is field-relative unless invariant universality can be independently justified. The present work intentionally avoids asserting universal ideological or metaphysical authority.

\subsection{7.9 Semantic Geometry Is Not Consciousness}
The framework models semantic orientation, structural coherence, and criterion preservation. It does not model consciousness, subjective awareness, intentionality, or phenomenological experience. Although the language of "orientation," "criterion," and "discernment" may resemble cognitive or philosophical concepts, ACE Atlas remains a geometric semantic framework operating over embedding trajectories. No claim is made regarding sentience or self-awareness.

\subsection{7.10 Current Scope of the Framework}
The present work establishes three primary claims: (1) Semantic fields can be geometrically modeled from invariant anchor relations; (2) Contextual coherence and epistemic integrity are not equivalent; and (3) Directional criterion drift can emerge inside semantically coherent reasoning trajectories. These claims represent the current scope of the framework. The work does not yet establish universal semantic stability, fully autonomous criterion-preserving reasoning, or generalized epistemic alignment across all domains. Instead, ACE Atlas introduces a geometric formulation that enables criterion preservation to become measurable, operational, and experimentally observable inside semantic trajectory evolution.

\subsection{7.11 Final Limitation}
Perhaps the deepest limitation of ACE Atlas is that the framework assumes meaning possesses sufficient structural continuity to admit geometric representation. If semantic meaning were entirely arbitrary, discontinuous, or purely stochastic, stable semantic fields and invariant directional structure would not emerge consistently in embedding space. The effectiveness of ACE Atlas therefore depends on an underlying assumption: that semantic structure contains persistent relational geometry capable of supporting directional epistemic orientation. The experimental results suggest that such structure does emerge empirically. However, the full theoretical foundations of why semantic geometry stabilizes in large language models remain unresolved.


\sectionsection{8. Conclusion}

This work introduced the ACA Runtime, a geometry-based criterion supervision architecture designed to preserve semantic continuity through invariant orientation, contextual semantic fields, topology-aware transitions, and runtime trajectory supervision. Rather than treating semantic stability as a purely probabilistic phenomenon, ACA Runtime models the criterion as directional semantic structure, contextual geometric orientation, and persistent trajectory continuity. The experiments demonstrated that semantic reasoning does not require rigid contextual immobility in order to preserve coherence. Instead, stable reasoning may evolve through neighboring semantic transitions, contextual reorientation, invariant continuity, and topology-aware recovery. 

One of the most important observations was the emergence of semantic reorientation, where neighboring contextual fields temporarily stabilize interpretation without producing criterion collapse. This suggests that semantic reasoning behaves less like isolated classification and more like constrained geometric navigation across a semantic topology. The runtime experiments further demonstrated that ACA Runtime can operationally supervise semantic drift, orientation decay, rhetorical escalation, inversion risk, and contextual ambiguity through reusable runtime policies rather than repeated prompt reconstruction.

Importantly, the architecture externalizes the semantic criterion from natural language prompts into invariant matrices, contextual field geometry, trajectory continuity, and persistent semantic infrastructure. This distinction proved operationally significant. The runtime benchmark demonstrated that criterion preservation through semantic infrastructure produced a measured runtime token reduction of $70.26\%$ relative to a prompt-heavy criterion-preservation strategy. Crucially, this reduction was not achieved by removing contextual reasoning or semantic supervision. Instead, the reduction emerged because the criterion no longer required repeated linguistic reconstruction during every interaction. 

Under the ACA Runtime, the criterion becomes persistent. This introduces the possibility of reusable criterion supervision, lower runtime complexity, persistent contextual orientation, topology-aware semantic recovery, and scalable semantic continuity across long reasoning trajectories. More broadly, the experiments suggest that reliable generative reasoning may depend not only on increasing model scale or prompt complexity, but on preserving directional semantic orientation throughout contextual evolution. Under this interpretation, the semantic criterion becomes measurable, reusable, topology-aware, operationally persistent, and geometrically representable. ACA Runtime therefore proposes a shift from prompt-engineered semantic control toward a reusable geometric criterion infrastructure. Future work will explore adaptive semantic topology, dynamic field generation, online atlas evolution, multi-agent criterion synchronization, and persistent semantic memory architectures. The current results suggest that semantic orientation may provide a practical operational foundation for scalable, criterion-preserving generative systems.


\section{9. References}

\begin{description}

\item Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., ... \& Kaplan, J. (2022). Constitutional AI: Harmlessness from AI feedback. \textit{arXiv preprint arXiv:2212.08073}.

\item Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., ... \& Olah, C. (2021). A mathematical framework for transformer circuits. \textit{Transformer Circuits Thread}, 1.

\item Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., ... \& Kaplan, J. (2022). Language models (mostly) know what they know. \textit{arXiv preprint arXiv:2207.05221}.

\item Kuhn, L., Gal, Y., \& Farquhar, S. (2023). Semantic entropy computes trustworthy uncertainty estimates for large language models in zero-shot. \textit{Proceedings of the International Conference on Learning Representations (ICLR)}.

\item Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... \& Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. \textit{Advances in Neural Information Processing Systems}, 33, 9459-9474.

\item Manakul, P., Liusie, A., \& Gales, M. J. (2023). SelfCheckGPT: Zero-resource black-box hallucination detection for generative large language models. \textit{Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)}.

\item OpenAI. (2024). \textit{New embedding models and API updates}. Retrieved from https://openai.com/blog/new-embedding-models-and-api-updates

\item Rosati Beristain, E. (2026). Axiomatic Criterion Engine (ACE) — Ontological Discernment Engine. \textit{Zenodo}. https://doi.org/10.5281/zenodo.18654895

\end{description}

