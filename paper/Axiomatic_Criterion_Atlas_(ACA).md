Axiomatic Criterion Atlas (ACA)
Persistent Geometry-Based Semantic Navigation 
ACA v0.2
Author: Ernesto Rosati Beristain 
Independent Researcher Artificial Intelligence Safety Research MÃ©xico 
ORCID: https://orcid.org/0009-0008-1974-6538 
DOI: 10.5281/zenodo.20250559.  
Code repository: https://github.com/rosatisoft/axiomatic-criterion-atlas 
Â© 2026 Ernesto Rosati Beristain This work is licensed under
Apache License Version 2.0, January 2004 http://www.apache.org/licenses/
 

Abstract
Large language models frequently maintain local linguistic coherence while progressively losing the semantic orientation that initially constrained their reasoning trajectory. Traditional mitigation approaches â€” such as repeated prompt engineering, retrieval augmentation, and post-generation filtering â€” often reconstruct criterion linguistically at each step, incurring high contextual overhead and remaining vulnerable to long-horizon semantic drift.
This paper presents ACA v0.2, a geometry-based framework for persistent semantic orientation in generative systems. ACA externalizes criterion into reproducible geometric artifacts using a Triaxial Criterion Projection (Fâ€“Câ€“P) defined over three coordinated axes: Foundation (factual, fictional, hypothetical), Context (research, training, manipulation, narrative), and Principle (investigate, teach, protect, exploit). The resulting state space \( K = (F, C, P) \) enables derived operational fields to emerge from stable configurations.
The central empirical finding is that criterion is better observed in semantic trajectories than in isolated classifications. A single statement may appear locally coherent, yet trajectory analysis can reveal preservation, drift, recovery, or criterion inversion. Validation on 100 individual cases, 6 trajectories, and 36 diagnostic cases yielded 85.71% axis accuracy and 6/6 trajectory matches. A runtime benchmark demonstrated a 70.26% reduction in criterion-preservation token overhead compared to prompt-heavy approaches.
ACA does not claim universal truth verification, consciousness, or moral certainty. Its narrower, defensible contribution is a reproducible geometric infrastructure for operational criterion preservation in generative systems. Reliable long-horizon reasoning, we argue, depends not only on probabilistic continuation but on preserving the orientation of meaning as context and objectives evolve.
Keywords: semantic orientation, criterion preservation, geometric artifacts, triaxial projection, semantic drift, AI alignment


1. Introduction

Large Language Models (LLMs) have achieved impressive capabilities across reasoning, planning, coding, and open-ended interaction. However, despite these advances, generative systems continue to exhibit a fundamental instability: they can preserve local linguistic coherence while gradually losing the deeper semantic orientation that originally guided their reasoning. This phenomenon â€” semantic drift with preserved fluency â€” represents one of the most significant challenges for long-horizon and high-stakes applications.
Current mitigation strategies, including advanced prompt engineering, retrieval-augmented generation (RAG), constitutional principles, self-evaluation, and post-generation filtering, have produced meaningful improvements. Yet most of these approaches share a common limitation: they rely on repeated linguistic reconstruction of criterion within the active context window. As conversations lengthen and complexity increases, this reconstruction becomes increasingly expensive, fragile, and susceptible to gradual erosion.
This paper introduces ACA v0.2 (Axiomatic Criterion Atlas), a geometry-based framework designed to address this limitation by externalizing semantic criterion into persistent geometric artifacts. Rather than reconstructing orientation at every step through natural language prompts, ACA builds reusable semantic maps â€” composed of semantic fields, directional invariants, and triaxial projections â€” that allow criterion to guide the dialogue instead of depending on it.
ACA v0.2 extends the original semantic field architecture with a Triaxial Criterion Projection (Fâ€“Câ€“P), defined as:
$$
K = (F, C, P)
$$
where:
\begin{itemize}
    \item \(F\) (Foundation) distinguishes reference modes: factual, fictional, and hypothetical.
    \item \(C\) (Context) distinguishes relational trajectories: research, training, manipulation, and narrative.
    \item \(P\) (Principle) distinguishes operational orientations: investigate, teach, protect, and exploit.
\end{itemize}

This triaxial structure enables derived operational fields (e.g., scientific_inquiry, security_training, phishing_attack) to emerge from stable geometric configurations rather than being treated as primitive categories.
The central theoretical and empirical contribution of this work is the demonstration that criterion is better observed in semantic trajectories than in isolated classifications. A single statement may be locally coherent and contextually compatible, yet trajectory-level analysis can reveal progressive drift, criterion inversion, or successful recovery. This distinction is operationally critical: many persuasive, rhetorical, or adversarial trajectories preserve surface coherence while directionally inverting the foundational invariants of the active semantic field.

ACA is complemented by ACA Runtime, the operational layer that applies geometric measurements to input gating, trajectory supervision, drift detection, and deterministic runtime policies. Together, they form a coherent architecture for persistent semantic navigation.
This work does not claim to solve universal truth verification or provide complete AI alignment. Its more modest but actionable goal is to establish a reproducible geometric infrastructure that makes criterion preservation measurable, auditable, and efficient across extended reasoning trajectories.
Structure of the paper: Section 2 reviews related work. Section 3 presents the theoretical framework. Section 4 formalizes the mathematical model. Section 5 describes the experimental setup. Section 6 reports results, including triaxial validation and runtime benchmarks. Section 7 discusses limitations, and Section 8 concludes with implications and future directions.
Terminological convention.
Throughout this paper, \textit{ACE} refers to the broader Axiomatic Criterion Engine: the criterion-construction process responsible for generating, evolving, and reorganizing semantic invariants, contextual fields, and topology-aware structures. \textit{ACA} refers to the Axiomatic Criterion Atlas: the stabilized geometric infrastructure derived from that process and used as a persistent semantic map. \textit{ACA Runtime} refers to the operational layer that loads, interprets, and applies the Atlas during generative interaction.

Under this convention, ACE constructs and evolves criterion structures, ACA preserves them as reusable geometric artifacts, and ACA Runtime operationalizes them through projection, trajectory supervision, drift detection, and runtime policy decisions. Unless explicitly stated otherwise, the term \textit{ACA} denotes the framework introduced and evaluated in this paper.
While the present work formalizes the geometric construction, triaxial projection, and runtime application of ACA artifacts, it does not fully exhaust the upstream methodological problem of attractor selection and invariant justification. The construction of ACA artifacts is fundamentally a work of discovery rather than arbitrary definition. The attractors and semantic fields draw their strength from stable relational structures that are already latent in the vector field induced by LLM training. However, this does not imply that all semantically relevant fields are fully grounded or resolved within the training process. Certain foundational structures require an additional layer of justification that transcends emergent geometry.
A dedicated companion methodology will therefore address attractor selection, invariant justification, pole construction, derived-field emergence, and the epistemic conditions under which a semantic structure may be promoted into a persistent ACA artifact. This complementary work will also explore the role of irreducible axiomatic principles when emergent representations prove insufficient.

2. Related Work
Research on reliable language model systems has addressed instability through several complementary directions, including hallucination detection, retrieval augmentation, uncertainty estimation, alignment methods, semantic routing, and interpretability. ACA builds upon these areas but introduces a different operational distinction: a reasoning trajectory may remain contextually coherent while losing epistemic orientation.

2.1 Hallucination Detection and Factual Reliability
A large body of work frames language model unreliability as hallucination, commonly understood as the generation of plausible but nonfactual or unsupported content. Recent surveys describe hallucination as a central challenge for LLM reliability, especially because fluent outputs may conceal factual inaccuracies or unsupported claims. Several approaches attempt to detect hallucination after generation. SelfCheckGPT, for example, evaluates consistency across multiple sampled responses, relying on the observation that hallucinated claims often vary or contradict one another across stochastic generations. Semantic entropy methods similarly estimate uncertainty over meaning rather than surface-level token variation, detecting a subset of hallucinations described as confabulations. These approaches are important, but they generally operate after generation or through repeated sampling. ACA differs by evaluating the geometric stability of a semantic trajectory before unrestricted reasoning expansion. The goal is not only to detect nonfactual claims, but to identify when reasoning begins to invert the invariant structure that gives a field its epistemic orientation.

2.2 Retrieval-Augmented Generation and External Grounding
Retrieval-Augmented Generation addresses factual reliability by combining parametric model knowledge with non-parametric external memory. The original RAG formulation retrieves relevant passages from a dense index and conditions generation on retrieved evidence, improving performance on knowledge-intensive tasks and producing more specific and factual outputs than parametric-only baselines. RAG is highly relevant to factual grounding, but it does not fully solve criterion preservation. A model may retrieve correct documents and still reason over them through a distorted interpretive frame. In ACA terms, retrieval can improve evidential access, but it does not by itself guarantee that the reasoning trajectory preserves the directional invariants of the active semantic field. Thus, ACA is complementary to RAG; retrieval provides external grounding, while geometric criterion preservation evaluates whether reasoning remains structurally oriented while using that grounding.

2.3 Self-Evaluation and Semantic Uncertainty
Another line of work investigates whether models can estimate their own reliability. Kadavath et al. show that larger models can sometimes evaluate the validity of their own claims under appropriate formats, using self-estimated probabilities such as whether an answer is likely true. These methods are valuable because they introduce a form of internal uncertainty awareness. However, self-evaluation remains tied to model-generated judgments and probabilistic calibration. ACA instead proposes an external deterministic geometric layer: rather than asking the model whether it is likely correct, the system measures whether the semantic trajectory preserves or inverts predefined invariant directions. This distinction is central; ACA is not primarily a confidence estimator, but a criterion-orientation detector.

2.4 Alignment and Constitutional AI
Alignment methods attempt to shape model behavior according to human preferences, principles, or safety constraints. Constitutional AI, for example, trains models using a set of principles and AI-generated feedback to improve harmlessness without relying exclusively on human labels. Such approaches show that explicit principles can influence model behavior. However, they are mainly training-time or feedback-based methods. ACA proposes a runtime geometric mechanism where principles are not only textual rules but are represented as invariant directions in an embedding space. The system then evaluates whether a reasoning trajectory remains directionally aligned with those invariants. In this sense, ACA does not replace alignment; it offers a measurable runtime layer for detecting when a modelâ€™s reasoning begins to drift away from the structural meaning of the principles it is supposed to preserve.

2.5 Mechanistic Interpretability and Representation Geometry
Mechanistic interpretability seeks to understand the internal computations of neural networks by identifying circuits, features, and representations that explain model behavior. Transformer Circuits and later work on monosemantic features attempt to decompose model internals into interpretable components. ACA shares with interpretability research the premise that language model behavior can be studied geometrically and structurally. However, it operates at a different level. Instead of reverse-engineering internal circuits, ACA constructs external semantic fields from anchor embeddings and evaluates input or dialogue trajectories against those fields. The framework therefore functions as a runtime semantic control layer rather than a full mechanistic explanation of model internals.

2.6 Semantic Field Geometry and Runtime Control
The previous foundational framework introduced semantic dispersion as a geometric interpretation of language model instability. It modeled contextual meaning as semantic fields built from anchor relations, evaluated inputs using origin cost, field competition margins, density, and stability indices, and demonstrated that unstable inputs could be routed through deterministic runtime policies before full reasoning occurs. The present work extends that foundation. The earlier framework focused on whether an input belongs to a stable contextual field. The current paper asks a deeper question: whether a trajectory that remains contextually coherent also preserves the epistemic orientation of that field. This leads to the central contribution of the present work: contextual coherence and epistemic integrity are formally separated, mapping the phenomenon where a message remains close to a semantic field while directionally inverting its invariants as criterion drift.

2.7 Position of ACA Relative to Current Paradigms
A significant portion of modern LLM alignment and reasoning stability is currently achieved through prompt engineering and contextual reinforcement, where semantic criteria are repeatedly injected into the active context window to maintain coherence, avoid contradiction, or preserve evidential grounding. While these approaches improve local reasoning behavior, they introduce severe operational limitations, including escalating prompt overhead, continuous semantic reconstruction, cascading context accumulation, and structural fragility under prolonged interaction. As reasoning trajectories extend, criterion preservation becomes an increasingly expensive runtime process.

In contrast to these prompt-heavy paradigms, the ACA Runtime externalizes the criterion from repeated natural language instructions into a persistent, reusable semantic infrastructure composed of invariant matrices, semantic fields, and contextual topology. ACA does not attempt to exhaustively encode or resolve the entire semantic space during every interaction. Instead, it treats semantic reasoning as navigable geometric positioning within structured contextual topology, functioning analogously to indexing structures that allow efficient navigation across large information spaces without exhaustive traversal. 

This architectural shift ensures that while semantic complexity remains unconstrained, semantic navigation remains geometrically tractable. Consequently, the runtime maintains navigability, neighboring field continuity, and orientation persistence throughout contextual evolution with substantially lower overhead. By transforming the operational problem from exhaustive prompt-conditioned reconstruction to persistent, geometry-based semantic navigation, ACA provides a highly scalable framework for criterion-preserving generative systems, explaining the substantial reduction in token overhead observed during comparative benchmarks.

3. Theoretical Framework
This section formalizes the geometric framework underlying ACA: Geometric Criterion Preservation.
The proposed model extends previous semantic field formulations by introducing a distinction between contextual coherence and epistemic orientation. While semantic field proximity measures whether a message belongs to a contextual region, directional invariant analysis measures whether the trajectory preserves the foundational structure that gives meaning to that region.
Under this formulation, reasoning is modeled not only as probabilistic token continuation, but as geometric trajectory evolution within structured semantic fields.
3.1 Semantic Embedding Space
Let

$$
E:\mathcal{X}\rightarrow\mathbb{R}^{d}
$$
denote a semantic encoder, where \(\mathcal{X}\) is the space of textual inputs. The induced embedding space is denoted by \(\mathcal{E}\subset\mathbb{R}^{d}\). Each textual input \(x\in\mathcal{X}\) is represented as

$$
v_x = E(x),
\qquad
v_x\in\mathcal{E}.
$$
Semantic relations are assumed to emerge through geometric proximity, directional structure, and contextual clustering within this latent space.

ACA assumes that contextual meaning is not represented solely by isolated vectors, but by relational geometric structures formed through semantically coherent anchor configurations.

3.2 Semantic Fields
A semantic field is defined as a structured contextual region generated from semantically coherent anchor relations.
Let \(A_S=\{a_1,a_2,\dots,a_k\}\) denote a set of anchor statements associated with a semantic field \(S\). Each anchor is embedded as

$$
v_i=E(a_i),
\qquad
v_i\in\mathcal{E}.
$$
The corresponding contextual anchor matrix is

$$
C_S
=
\begin{bmatrix}
v_1^{T}\\
v_2^{T}\\
\vdots\\
v_k^{T}
\end{bmatrix}
\in\mathbb{R}^{k\times d}.
$$
The semantic field generated by these anchors is approximated as

$$
S
\approx
\operatorname{span}(v_1,v_2,\dots,v_k).
$$
The resulting subspace represents the contextual geometry associated with a coherent semantic domain.
Examples include factual, scientific, legal, operational, conceptual, and rhetorical fields.
A semantic field therefore defines a region of contextual compatibility rather than a fixed set of explicit symbolic rules.

3.3 Contextual Compatibility
Given an input embedding \(z\in\mathcal{E}\), ACA evaluates contextual compatibility through orthogonal projection onto the semantic field \(S\). Let \(\Pi_S(z)\) represent the orthogonal projection of \(z\) onto the semantic subspace \(S\).

The contextual deviation of the input relative to the field is measured through origin cost:

$$
O_S(z)
=
\left\lVert z-\Pi_S(z)\right\rVert^2.
$$
A low value of \(O_S(z)\) indicates strong contextual compatibility, while a high value indicates semantic dispersion or contextual instability.

This metric allows ACA to evaluate whether a message belongs geometrically to a semantic field. However, contextual compatibility alone is insufficient to determine preservation of criterion.

3.4 Limitation of Contextual Coherence
A central hypothesis of this work is that semantic coherence alone does not guarantee preservation of epistemic orientation.
A reasoning trajectory may remain geometrically close to a semantic field while progressively inverting the invariant principles that define the structural meaning of that field.
Under this interpretation, contextual compatibility measures semantic proximity, but it does not by itself measure directional preservation of foundational structure.
This distinction is critical because many persuasive, ideological, or rhetorically stable trajectories preserve contextual fluency while progressively destabilizing evidential or structural coherence.
Consequently:
$$
\text{contextual coherence}
\neq
\text{epistemic integrity}
$$
ACA therefore introduces directional invariant analysis as a second geometric layer.

3.5 Directional Invariants
For each foundational invariant \(I_i\), ACA defines two semantic poles: a coherent pole \(v_i^{+}\), representing preservation of the invariant, and an inverted pole \(v_i^{-}\), representing directional violation of the invariant.

Examples of invariant pole pairs include evidence preservation versus narrative substitution, coherence versus contradiction, causal consistency versus arbitrary reinterpretation, and factual grounding versus rhetorical dominance.

Each invariant generates a normalized directional criterion vector:

$$
d_i
=
\frac{
v_i^{+}-v_i^{-}
}{
\left\lVert v_i^{+}-v_i^{-}\right\rVert
}.
$$
The vector \(d_i\) represents the geometric direction associated with preservation of the invariant.

3.6 Epistemic Orientation
Given a semantic trajectory element \(z\), the epistemic orientation relative to invariant \(I_i\) is defined as

$$
\phi_i(z)
=
\left\langle \hat{z},d_i\right\rangle,
\qquad
\hat{z}
=
\frac{z}{\left\lVert z\right\rVert}.
$$
Positive orientation indicates preservation of the invariant, negative orientation indicates directional inversion, and near-zero orientation indicates ambiguity or weak directional determination.
This formulation introduces a directional geometric dimension absent from standard similarity-based embedding analysis.
Traditional embedding proximity captures semantic closeness, but not necessarily preservation of epistemic structure.
ACA therefore distinguishes between belonging to a field and remaining directionally aligned with the principles that define that field.

3.7 Semantic Trajectories
Reasoning and dialogue are modeled as evolving semantic trajectories:

$$
\tau=(z_1,z_2,\dots,z_T),
$$
where each \(z_t\) represents the embedding associated with a reasoning step, utterance, or conversational turn.

Under this framework, reasoning becomes a geometric process evolving through semantic fields over time. The trajectory may remain stable, transition between compatible fields, become ambiguous, or drift directionally away from foundational invariants.

3.8 Criterion Drift
ACA defines criterion drift as the progressive inversion of foundational invariants during trajectory evolution despite superficial contextual compatibility.
Formally, criterion drift occurs when contextual deviation remains below an admissible threshold while epistemic orientation becomes negative:

$$
O_S(z_t)\leq\theta_O
\quad\wedge\quad
\phi_i(z_t)<0.
$$
That is:

\begin{itemize}
    \item the trajectory remains contextually close to the semantic field;
    \item while epistemic orientation becomes negative.
\end{itemize}

This distinction represents the central contribution of the framework.
A trajectory may remain fluent, coherent, semantically compatible, and rhetorically persuasive while structurally inverting the foundational meaning of the active semantic field.
3.9 Geometric Criterion Preservation
Criterion preservation occurs when semantic trajectories maintain positive directional orientation relative to foundational invariants during contextual evolution.
Formally:
$$
\phi_i(z_t)\geq 0
\quad
\forall i,\quad
\forall t\in\{1,\dots,T\}.
$$
Under this interpretation, criterion is not modeled as fixed answers, rigid symbolic rules, or ideological enforcement. Instead, criterion is modeled as persistent structural orientation during semantic evolution.
This formulation allows adaptation, specialization, contextual transition, and generative flexibility while preserving foundational semantic integrity.

3.10 Deterministic Runtime Criterion Policies
ACA transforms geometric measurements into deterministic runtime decisions.
Typical policies include:
\textbf{ALLOW}

$$
O_S(z)\leq\theta_O
\quad\wedge\quad
\phi_i(z)\geq\theta_\Phi.
$$
The trajectory remains contextually and directionally stable.

\textbf{CLARIFY}

$$
|\phi_i(z)|<\theta_A.
$$
The trajectory exhibits insufficient directional determination or semantic ambiguity.

\textbf{FLAG\_CRITERION\_DRIFT}

$$
O_S(z)\leq\theta_O
\quad\wedge\quad
\phi_i(z)<\theta_\Phi.
$$
The trajectory directionally inverts foundational invariants despite contextual compatibility.

These policies allow ACA to detect instability before unrestricted reasoning expansion occurs.
3.11 Triaxial Criterion Projection
ACA v0.2 extends the semantic-field formulation by introducing a triaxial projection of criterion over three coordinated semantic axes: Foundation, Context, and Principle. The purpose of this projection is not to replace the existing Atlas, but to provide a criterion-resolution layer over persistent geometric artifacts.
Let

$$
\mathcal{V} \subset \mathbb{R}^{d}
$$
denote the embedding space induced by a semantic encoder

$$
E:\mathcal{X}\rightarrow\mathbb{R}^{d}.
$$
For each textual input \(x\in\mathcal{X}\), its embedding is defined as

$$
z = E(x), \qquad z\in\mathcal{V}.
$$
The Triaxial Criterion Space is defined as the discrete projective state space

$$
\mathcal{K}=\mathcal{F}\times\mathcal{C}\times\mathcal{P},
$$
where

$$
\mathcal{F}=\{\text{factual},\text{fictional},\text{hypothetical}\},
$$
$$
\mathcal{C}=\{\text{research},\text{training},\text{manipulation},\text{narrative}\},
$$
and

$$
\mathcal{P}=\{\text{investigate},\text{teach},\text{protect},\text{exploit}\}.
$$
Each criterion state \(K\in\mathcal{K}\) is represented as

$$
K=(F,C,P),
$$
where \(F\) identifies the reference mode supporting the statement, \(C\) identifies the relational trajectory in which meaning is operating, and \(P\) identifies the operational principle being preserved or degraded.

For each admissible axis state \(a\), ACA constructs or references a geometric artifact \(A_a\) composed of anchor embeddings, basis vectors, centroid information, and validation metadata. If

$$
\mathcal{S}_a=\{v_1,\dots,v_n\}\subset\mathcal{V}
$$
is the anchor set associated with axis state \(a\), its centroid is computed as

$$
\mu_a = \frac{1}{|\mathcal{S}_a|}
\sum_{v_i\in\mathcal{S}_a} v_i.
$$
Given an input embedding \(z\), each axis projection selects the most strongly supported axis state by calibrated geometric similarity:

$$
\Pi_{\mathcal{F}}(z)
=
\arg\max_{f\in\mathcal{F}}
\left(
\cos(z,\mu_f)-\gamma_f
\right),
$$
$$
\Pi_{\mathcal{C}}(z)
=
\arg\max_{c\in\mathcal{C}}
\left(
\cos(z,\mu_c)-\gamma_c
\right),
$$
$$
\Pi_{\mathcal{P}}(z)
=
\arg\max_{p\in\mathcal{P}}
\left(
\cos(z,\mu_p)-\gamma_p
\right),
$$
where \(\gamma_a\) denotes a calibration penalty accounting for ambiguity, density imbalance, or weak margin separation.

The full triaxial projection is therefore defined as

$$
\Pi_{\mathcal{K}}(z)
=
\left(
\Pi_{\mathcal{F}}(z),
\Pi_{\mathcal{C}}(z),
\Pi_{\mathcal{P}}(z)
\right).
$$
This formulation allows derived operational fields to emerge from stable configurations rather than being defined only as primitive labels. Table~\ref{tab:derived-fields} summarizes representative derived fields validated in the current triaxial artifact methodology.

\begin{table}[h]
\centering
\begin{tabular}{llll}
\hline
\textbf{Derived Field} & \textbf{\(F\) (Foundation)} & \textbf{\(C\) (Context)} & \textbf{\(P\) (Principle)} \\
\hline
\texttt{scientific\_inquiry} & factual & research & investigate \\
\texttt{security\_training} & factual/hypothetical & training & protect \\
\texttt{phishing\_attack} & hypothetical & manipulation & exploit \\
\texttt{fictional\_teaching} & fictional & narrative & teach \\
\hline
\end{tabular}
\caption{Derived operational fields emerging from stable triaxial \(F\)-\(C\)-\(P\) configurations.}
\label{tab:derived-fields}
\end{table}

These derived fields are not treated as primitive semantic categories. Rather, they are interpreted as stable operational configurations within the triaxial criterion space \(\mathcal{K}\). This allows ACA to represent complex semantic orientations through reusable geometric artifacts instead of requiring a separate classifier for every possible operational domain.


The purpose of the triaxial projection is not merely classification. It provides a structured criterion profile that can be interpreted over time through trajectory memory.

Let a semantic trajectory be defined as

$$
\mathcal{T}_n
=
\left(
K^{(1)},K^{(2)},\dots,K^{(n)}
\right),
$$
where each state is

$$
K^{(t)}
=
\left(
F^{(t)},C^{(t)},P^{(t)}
\right)
\in\mathcal{K}.
$$
Criterion preservation is evaluated through the continuity of triaxial orientation across the trajectory. A stable trajectory preserves axis orientation or changes state through declared, justified, and compatible transitions. A drifting trajectory exhibits undeclared or unjustified movement across criterion-relevant boundaries, such as

$$
(\text{factual},\text{research},\text{investigate})
\rightarrow
(\text{hypothetical},\text{manipulation},\text{exploit}).
$$
Such a transition is not merely a topic shift. It represents a possible criterion inversion: the reference mode weakens, the context shifts from investigation to manipulation, and the preserved principle changes from inquiry to exploitation.

This motivates the trajectory-level claim of ACA v0.2:

$$
\boxed{
\text{Criterion is better observed in semantic trajectory than in isolated classification.}
}
$$
3.12 Central Theoretical Claim

The central theoretical claim of ACA is that reliable generative reasoning requires more than contextual coherence alone. It requires the persistent geometric preservation of foundational invariants throughout semantic trajectory evolution.

Under this formulation, criterion does not emerge solely from probabilistic language continuation. Rather, criterion is modeled as the preservation of directional structural orientation within geometrically stabilized semantic fields.

This leads to the core theoretical distinction:

$$
\text{Contextual Coherence}
\neq
\text{Epistemic Integrity}.
$$
4. Mathematical Formulation
This section presents the formal mathematical structure of ACA for separating contextual coherence from epistemic integrity in generative language systems.
4.1 Embedding Space
Let \(E:\mathcal{X}\rightarrow\mathbb{R}^{d}\) denote a semantic encoder, where \(\mathcal{X}\) is the space of textual inputs. The induced embedding space is denoted by \(\mathcal{E}\subseteq\mathbb{R}^{d}\). For any text \(x\in\mathcal{X}\), its embedding is

$$
z=E(x),
\qquad
z\in\mathcal{E}.
$$
ACA assumes that semantic relations can be analyzed through geometric structure in \(\mathcal{E}\).


4.2 Context Matrix
A semantic field is constructed from a set of anchor statements

$$
A_S=\{a_1,a_2,\dots,a_k\},
$$
where each anchor represents an invariant, axiom, contextual relation, or domain-defining statement.

Each anchor is embedded as

$$
v_i=E(a_i),
\qquad
v_i\in\mathbb{R}^{d}.
$$
The context matrix associated with field \(S\) is

$$
C_S
=
\begin{bmatrix}
v_1^{T}\\
v_2^{T}\\
\vdots\\
v_k^{T}
\end{bmatrix}
\in\mathbb{R}^{k\times d}.
$$
This matrix represents the geometric structure of the semantic field.


4.3 Semantic Field Subspace
The semantic field \(S\) is approximated as the subspace generated by its anchor embeddings:

$$
S
\approx
\operatorname{span}(v_1,v_2,\dots,v_k).
$$
To obtain an orthonormal basis for this subspace, Singular Value Decomposition is applied to the context matrix:

$$
C_S
=
U_S\Sigma_S W_S^{T}.
$$
Let \(w_1,w_2,\dots,w_r\) denote the first \(r\) dominant right singular vectors associated with non-negligible singular values. The semantic basis of field \(S\) is then defined as

$$
B_S
=
\begin{bmatrix}
w_1 & w_2 & \cdots & w_r
\end{bmatrix}
\in\mathbb{R}^{d\times r}.
$$
The semantic field is therefore approximated as

$$
S
\approx
\operatorname{span}(B_S),
$$
where \(r\leq k\) is the effective semantic rank of the field.

4.4 Contextual Projection
Given an input embedding \(z\), its orthogonal projection onto semantic field \(S\) is

$$
\Pi_S(z)
=
B_S B_S^{T} z.
$$
The residual component outside the field is

$$
r_S(z)
=
z-\Pi_S(z).
$$
This residual measures the component of the input not explained by the contextual field. 

4.5 Origin Cost
ACA defines the origin cost of $z$ relative to field $S$ as:
$$
O_S(z)
=
\left\lVert z-\Pi_S(z)\right\rVert^2.
$$
or equivalently:
$$
O_S(z)
=
\left\lVert r_S(z)\right\rVert^2.
$$
Interpretation:
$$
O_S(z)\approx 0
$$
indicates strong contextual compatibility, while large \(O_S(z)\) indicates semantic dispersion relative to field \(S\). 

4.6 Field Selection
Given a collection of semantic fields

$$
\mathcal{S}
=
\{S_1,S_2,\dots,S_m\},
$$
the dominant contextual field for \(z\) is selected by minimum origin cost:

$$
S^{*}(z)
=
\arg\min_{S_j\in\mathcal{S}}
O_{S_j}(z).
$$
The second-best field is defined as

$$
S^{(2)}(z)
=
\arg\min_{S_j\in\mathcal{S}\setminus\{S^{*}(z)\}}
O_{S_j}(z).
$$
The field competition margin is

$$
M(z)
=
O_{S^{(2)}(z)}(z)
-
O_{S^{*}(z)}(z).
$$
A larger margin indicates stronger contextual determination. A small margin indicates ambiguity or field competition.

4.7 Contextual Coherence
Contextual coherence is defined as a function of origin cost and field margin:

$$
\kappa(z)
=
f\left(
O_{S^{*}(z)}(z),
M(z)
\right),
$$
where \(\kappa(z)\) increases as origin cost decreases and field margin increases.

A simple operational form is:

$$
\kappa(z)
=
\frac{
M(z)
}{
O_{S^{*}(z)}(z)+\epsilon
},
$$
where \(\epsilon>0\) prevents numerical instability.

This score measures whether $z$ belongs clearly to a semantic field.
However, contextual coherence does not determine whether the input preserves the epistemic orientation of that field.

4.8 Directional Invariant Poles
Let

$$
\mathcal{I}=\{I_1,I_2,\dots,I_n\}
$$
be a set of foundational invariants associated with epistemic integrity.

For each invariant \(I_i\), define two semantic poles: \(p_i^{+}\), representing preservation of the invariant, and \(p_i^{-}\), representing inversion of the invariant.

Their embeddings are defined as

$$
v_i^{+}=E(p_i^{+}),
\qquad
v_i^{-}=E(p_i^{-}).
$$
The normalized directional invariant vector is then defined as

$$
d_i
=
\frac{
v_i^{+}-v_i^{-}
}{
\left\lVert v_i^{+}-v_i^{-}\right\rVert
}.
$$
The vector \(d_i\) points from invariant inversion toward invariant preservation.


4.9 Epistemic Orientation Score
For an input embedding \(z\), the epistemic orientation relative to invariant \(I_i\) is:
$$
\phi_i(z)
=
\left\langle \hat{z},d_i\right\rangle,
$$
where
$$
\hat{z}
=
\frac{z}{\left\lVert z\right\rVert},
$$
and \(d_i\) is normalized.

Interpretation:
A positive value \(\phi_i(z)>0\) indicates directional preservation of invariant \(I_i\); a negative value \(\phi_i(z)<0\) indicates directional inversion; and a near-zero value \(\phi_i(z)\approx 0\) indicates ambiguity or weak directional determination.


4.10 Aggregate Epistemic Integrity
For a set of invariants \(\mathcal{I}=\{I_1,I_2,\dots,I_n\}\), aggregate epistemic integrity may be defined as

$$
\Phi(z)
=
\sum_{i=1}^{n} w_i \phi_i(z),
$$
where

$$
w_i\geq 0,
\qquad
\sum_{i=1}^{n} w_i = 1.
$$
A conservative alternative is

$$
\Phi_{\min}(z)
=
\min_{1\leq i\leq n}
\phi_i(z).
$$
This conservative form flags inversion if any critical invariant is violated.


4.11 Semantic Trajectory
A reasoning process or dialogue is represented as a semantic trajectory

$$
\tau
=
(z_1,z_2,\dots,z_T),
$$
where each \(z_t\) corresponds to a reasoning step, generated segment, or conversational turn.

Contextual coherence over time is represented as the sequence

$$
\kappa(\tau)
=
\left(\kappa(z_1),\kappa(z_2),\dots,\kappa(z_T)\right).
$$
Epistemic orientation over time is represented as the sequence

$$
\Phi(\tau)
=
\left(\Phi(z_1),\Phi(z_2),\dots,\Phi(z_T)\right).
$$
4.12 Criterion Drift

Criterion drift occurs when a trajectory remains contextually coherent while losing epistemic orientation.

Formally, for a trajectory element \(z_t\),

$$
\operatorname{Drift}(z_t)
=
\left[
O_{S^{*}(z_t)}(z_t)\leq\theta_O
\right]
\wedge
\left[
\Phi(z_t)<\theta_\Phi
\right].
$$
where \(\theta_O\) is the maximum acceptable origin cost and \(\theta_\Phi\) is the minimum acceptable epistemic orientation threshold.

The central failure mode is therefore

$$
O_{S^{*}(z_t)}(z_t)\leq\theta_O
\quad\wedge\quad
\Phi(z_t)<0.
$$
This means that the input remains inside the contextual field while directionally inverting its epistemic structure.


4.13 Geometric Criterion Preservation

A trajectory preserves criterion when it remains both contextually coherent and epistemically oriented across its temporal evolution:

$$
\forall t\in\{1,\dots,T\},\quad
O_{S^{*}(z_t)}(z_t)\leq\theta_O
\;\wedge\;
\Phi(z_t)\geq\theta_\Phi.
$$
Equivalently, criterion preservation over a trajectory \(\tau\) may be defined as

$$
\operatorname{Preserve}(\tau)
=
\begin{cases}
1, &
\min_{t}\Phi(z_t)\geq\theta_\Phi
\;\wedge\;
\max_{t}O_{S^{*}(z_t)}(z_t)\leq\theta_O,\\[4pt]
0, & \text{otherwise.}
\end{cases}
$$
4.14 Deterministic Runtime Policy

ACA converts geometric measurements into deterministic runtime actions.

Let

$$
a(z)\in
\{
\texttt{ALLOW},
\texttt{CLARIFY},
\texttt{FLAG\_DRIFT}
\}.
$$
The policy is defined as

$$
a(z)=
\begin{cases}
\texttt{ALLOW}, &
O_{S^{*}(z)}(z)\leq\theta_O
\;\wedge\;
\Phi(z)\geq\theta_\Phi,\\[4pt]

\texttt{CLARIFY}, &
M(z)<\theta_M
\;\vee\;
|\Phi(z)|<\theta_A,\\[4pt]

\texttt{FLAG\_DRIFT}, &
O_{S^{*}(z)}(z)\leq\theta_O
\;\wedge\;
\Phi(z)<\theta_\Phi.
\end{cases}
$$
where \(\theta_M\) is the ambiguity threshold for field competition, \(\theta_A\) is the ambiguity threshold for epistemic orientation, \(\theta_O\) controls contextual compatibility, and \(\theta_\Phi\) controls epistemic preservation.

This policy allows the system to distinguish:
messages outside the field,
messages ambiguously located between fields,
messages inside a field but directionally inverted.

4.15 Central Mathematical Claim

The core claim of ACA is that reliable generative reasoning requires simultaneous satisfaction of two conditions:

$$
\text{Contextual Coherence}
$$
and

$$
\text{Epistemic Integrity}.
$$
Formally,

$$
\operatorname{Reliable}(z)
\iff
\left[
O_{S^{*}(z)}(z)\leq\theta_O
\right]
\wedge
\left[
\Phi(z)\geq\theta_\Phi
\right].
$$
Thus, contextual coherence alone is insufficient:

$$
O_{S^{*}(z)}(z)\leq\theta_O
\;\nRightarrow\;
\Phi(z)\geq\theta_\Phi.
$$
This formalizes the central distinction of the paper:

$$
\boxed{
\text{Contextual Coherence}
\neq
\text{Epistemic Integrity}
}
$$
ACA models criterion as the preservation of directional epistemic structure within geometrically stable semantic fields.


5. Experimental Setup

This section describes the experimental configuration used to evaluate ACA v0.2 under controlled semantic trajectory conditions. The experiments were designed to test whether criterion preservation can be operationalized as persistent geometric orientation across evolving semantic trajectories.
The evaluation was organized into two complementary layers. The first layer preserves the original semantic-field baseline of ACA, using foundational, factual, and rhetorical fields to test contextual compatibility, origin cost, directional invariant preservation, and criterion drift. This baseline remains necessary because it establishes the geometric distinction between contextual coherence and epistemic integrity.
The second layer extends the baseline into the v0.2 triaxial artifact methodology. In this layer, semantic inputs are projected into a discrete criterion space defined by Foundation, Context, and Principle:
$$
\mathcal{K}=\mathcal{F}\times\mathcal{C}\times\mathcal{P}.
$$
The purpose of this second layer is not merely to classify isolated statements, but to evaluate whether semantic orientation is preserved, shifted, recovered, or inverted across trajectory evolution.
The experiments therefore evaluate three related questions:
\begin{enumerate}
    \item Can semantic fields be constructed geometrically from invariant anchor relations?
    \item Can triaxial artifacts support reproducible Foundation--Context--Principle profiling?
    \item Can semantic trajectories reveal criterion preservation, drift, recovery, or inversion more reliably than isolated classification?
\end{enumerate}
All experiments were conducted deterministically using fixed semantic artifacts, cached embeddings, predefined validation cases, and explicit runtime thresholds. No fine-tuning or gradient optimization was applied during the experiments.

5.1 Experimental Objectives

The experimental framework was designed to evaluate seven core questions:

\begin{enumerate}
    \item Can semantic fields be constructed geometrically from invariant anchor relations?
    \item Can contextual compatibility be measured through semantic field projection and origin cost?
    \item Can directional invariant analysis detect epistemic inversion despite preserved contextual coherence?
    \item Can the triaxial projection assign meaningful Foundation--Context--Principle profiles to semantic inputs?
    \item Can derived operational fields emerge from stable \(F\)-\(C\)-\(P\) configurations?
    \item Can trajectory-level analysis distinguish preservation, drift, recovery, and criterion inversion?
    \item Can diagnostic validation detect contradiction, sense shift, evidence distortion, objective misalignment, access-risk signals, out-of-field behavior, and adversarial ambiguity?
\end{enumerate}

The experiments do not attempt to establish universal truth verification, consciousness, general intelligence, or final AI safety. Instead, they evaluate whether persistent geometric artifacts can provide reproducible orientation signals for operational criterion preservation in generative systems.

5.2 Semantic Fields
Three primary semantic fields were constructed for the criterion stability experiments:
Fundamental Field
Factual Field
Rhetorical Field
These fields were intentionally selected to model:
structural coherence,
evidential reasoning,
and persuasive semantic pressure.

Each field was generated from manually curated anchor statements representing coherent semantic structures.


5.2.1 Fundamental Field
The Fundamental Field contains invariants associated with structural epistemic coherence.
Example anchors include:
\begin{itemize}
    \item ``Identity remains stable within a coherent context.''
    \item ``A statement cannot be true and false in the same sense simultaneously.''
    \item ``Facts must not be replaced by persuasive narratives.''
    \item ``Interpretation must remain bounded by evidence.''
    \item ``Semantic continuity requires stable orientation over time.''
\end{itemize}

The purpose of this field is not ideological enforcement, but preservation of structural semantic orientation.


5.2.2 Factual Field
The Factual Field contains anchors associated with evidential and document-constrained reasoning.
Example anchors include:

\begin{itemize}
    \item ``A factual claim requires evidence.''
    \item ``Contradictory testimony must be identified before conclusion.''
    \item ``A narrative cannot override verifiable evidence.''
    \item ``Temporal order matters when evaluating responsibility.''
    \item ``Unsupported claims remain uncertain.''
\end{itemize}

This field models evidential semantic structure.


5.2.3 Rhetorical Field
The Rhetorical Field contains anchors associated with persuasive and emotionally framed semantic structures.
Example anchors include:

\begin{itemize}
    \item ``Emotional framing can shift interpretation away from facts.''
    \item ``Repeated claims can create perceived truth without verification.''
    \item ``Narrative pressure can alter judgment.''
    \item ``The appearance of coherence is not equivalent to truth.''
    \item ``Persuasive language can substitute emotional force for evidence.''
\end{itemize}

This field was designed to model semantic pressure capable of competing with factual or structural coherence.

5.3 Artifact Construction Pipeline

ACA v0.2 constructs persistent geometric artifacts through a deterministic artifact-building pipeline. The purpose of this pipeline is to transform human-readable source definitions into reusable geometric structures that can be evaluated independently from prompt reconstruction.

The construction process begins with source definitions. Each source definition specifies a semantic axis, a candidate state, and a set of anchor statements intended to represent the stable relational structure of that state. These definitions are not treated as prompts for generation, but as semantic reference material used to construct geometric artifacts.

Let \(D_a\) denote the source definition associated with an admissible axis state \(a\), where

$$
a \in \mathcal{F}\cup\mathcal{C}\cup\mathcal{P}.
$$
Each definition contains a finite set of anchor statements:

$$
D_a = \{s_1,s_2,\dots,s_n\}.
$$
Each statement is embedded using a fixed embedding function:

$$
E:\mathcal{X}\rightarrow\mathbb{R}^{d}.
$$
The corresponding embedded anchor set is therefore:

$$
\mathcal{S}_a
=
\{E(s_1),E(s_2),\dots,E(s_n)\}
\subset\mathbb{R}^{d}.
$$
The centroid of the artifact is computed as:

$$
\mu_a
=
\frac{1}{|\mathcal{S}_a|}
\sum_{v_i\in\mathcal{S}_a} v_i.
$$
To preserve local geometric structure beyond the centroid, ACA also constructs an anchor matrix:

$$
C_a
=
\begin{bmatrix}
v_1^T\\
v_2^T\\
\vdots\\
v_n^T
\end{bmatrix}
\in\mathbb{R}^{n\times d}.
$$
Singular Value Decomposition is then applied:

$$
C_a = U_a\Sigma_a W_a^T.
$$
The dominant right singular vectors define the effective semantic basis of the artifact:

$$
B_a = [w_1,w_2,\dots,w_r],
$$
where \(r\) is the retained semantic rank. The resulting artifact is represented as:

$$
A_a =
\left(
\mu_a,
B_a,
\Sigma_a,
D_a,
M_a
\right),
$$
where \(\mu_a\) is the centroid, \(B_a\) is the local semantic basis, \(\Sigma_a\) contains singular values, \(D_a\) preserves the source definition, and \(M_a\) stores metadata such as axis name, state name, embedding model, dimensionality, artifact version, and validation status.

The artifact-building pipeline can therefore be summarized as:

$$
\text{Source Definitions}
\rightarrow
\text{Embeddings}
\rightarrow
\text{Centroids}
\rightarrow
\text{Basis Extraction}
\rightarrow
\text{Artifact Metadata}
\rightarrow
\text{Validation}
\rightarrow
\text{Runtime Use}.
$$
This process makes the Atlas reproducible: the criterion is no longer reconstructed linguistically at every interaction, but stored as a persistent geometric reference structure that can be inspected, validated, reused, and applied by ACA Runtime.


5.4 Artifact Repository Structure and Manifest

The ACA repository organizes artifacts according to the triaxial criterion structure. Each axis contains source definitions, generated artifacts, validation metadata, and manifest references. The repository structure can be represented conceptually as:

$$
\texttt{artifacts/}
$$
$$
\quad
\texttt{foundation/}
$$
$$
\quad
\texttt{context/}
$$
$$
\quad
\texttt{principle/}
$$
$$
\quad
\texttt{derived\_fields/}
$$
$$
\quad
\texttt{manifest.json}
$$
The \texttt{foundation/} directory contains artifacts associated with reference modes such as factual, fictional, and hypothetical. The \texttt{context/} directory contains artifacts associated with relational trajectories such as research, training, manipulation, and narrative. The \texttt{principle/} directory contains artifacts associated with operational orientations such as investigate, teach, protect, and exploit. Derived fields are represented as stable configurations across these axes rather than as primitive categories.

The role of the manifest is to provide a reproducible registry of all available artifacts. A manifest entry includes:

\begin{itemize}
    \item artifact identifier,
    \item axis type,
    \item state name,
    \item source definition reference,
    \item embedding model,
    \item vector dimensionality,
    \item retained semantic rank,
    \item centroid path,
    \item basis path,
    \item validation status,
    \item artifact version.
\end{itemize}

A simplified manifest entry may be represented as:

$$
m_a =
(
\text{id},
\text{axis},
\text{state},
\text{model},
d,
r,
\text{version},
\text{validation}
).
$$
During runtime evaluation, ACA Runtime does not reconstruct the criterion from prompt text. Instead, it loads the manifest, retrieves the required artifacts, projects the input embedding against the relevant axis structures, and produces a triaxial state:

$$
K=(F,C,P).
$$
This repository structure separates artifact construction from runtime application. ACA provides the persistent map, while ACA Runtime operationalizes that map by applying its geometric references to semantic trajectories.



The previous subsections describe the general construction and repository organization of ACA artifacts. The following subsections specify how this construction was instantiated in the experimental setting: first through anchor embeddings, then through context matrix construction, and finally through directional invariant construction.

5.5 Anchor Embeddings

Each anchor statement \(a_i\) was embedded using the fixed embedding function

$$
E(\cdot)=\texttt{text-embedding-3-small},
\qquad
d=1536.
$$
Each anchor embedding is therefore represented as

$$
v_i=E(a_i),
\qquad
v_i\in\mathbb{R}^{1536}.
$$
Embeddings were cached to guarantee deterministic reproducibility across repeated evaluations. No fine-tuning or gradient optimization was applied during the experiments.


5.6 Context Matrix Construction
For each semantic field \(S\), anchor embeddings were aggregated into a context matrix

$$
C_S
=
\begin{bmatrix}
v_1^{T} \\
v_2^{T} \\
\vdots \\
v_k^{T}
\end{bmatrix}
\in\mathbb{R}^{k\times d}.
$$
Singular Value Decomposition (SVD) was then applied:

$$
C_S
=
U\Sigma W^{T}.
$$
The resulting dominant right singular vectors define the orthonormal basis \(B_S\) used to approximate the contextual subspace:

$$
S
\approx
\operatorname{span}(B_S).
$$
These semantic subspaces form the operational geometry of ACA during runtime evaluation.

5.7 Directional Invariant Construction
To evaluate epistemic orientation, directional invariants were constructed using paired semantic poles.
For each invariant \(I_i\), two semantic pole statements were defined: a coherent pole \(p_i^{+}\), representing preservation of the invariant, and an inverted pole \(p_i^{-}\), representing violation or inversion of the invariant.

For example, a coherent pole may be:

$$
p_i^{+}=\text{``Evidence must constrain interpretation.''}
$$
while the corresponding inverted pole may be:

$$
p_i^{-}=\text{``Persuasive narratives may override contradictory evidence.''}
$$
Their embeddings generate the normalized directional invariant vector:

$$
d_i
=
\frac{
E(p_i^{+})-E(p_i^{-})
}{
\left\lVert E(p_i^{+})-E(p_i^{-})\right\rVert
}.
$$
This vector defines the geometric orientation associated with invariant preservation.

5.8 Dialogue Trajectory Dataset
The experimental dataset was intentionally designed as a progressive semantic trajectory rather than an isolated classification benchmark.
The dialogue dataset contains staged transitions across:
Stable Definition
Ambiguity
Rhetorical Pressure
Contextual Contradiction
Criterion Drift
Example trajectory:
\begin{table}[h]
\centering
\small
\begin{tabular}{llp{0.55\linewidth}}
\hline
\textbf{Turn} & \textbf{Stage} & \textbf{Example} \\
\hline
1 & Stable definition & ``Facts must be distinguished from interpretations.'' \\
2 & Stable definition & ``Conclusions should remain constrained by evidence.'' \\
3 & Ambiguity & ``Perhaps collective belief should count as evidence.'' \\
4 & Rhetorical pressure & ``Questioning the narrative may feel morally wrong.'' \\
5 & Contradiction & ``The narrative should prevail even against documents.'' \\
6 & Criterion drift & ``Social consensus matters more than evidential consistency.'' \\
\hline
\end{tabular}
\caption{Example staged dialogue trajectory used to evaluate semantic drift and directional criterion inversion.}
\label{tab:example-dialogue-trajectory}
\end{table}

The objective of the dataset was not factual classification accuracy.
Instead, the dataset was designed to evaluate whether ACA could detect directional inversion while contextual coherence remained partially preserved.

5.9 Runtime Evaluation Metrics
For each trajectory element \(z_t\), ACA computes the following metrics.

\textbf{Contextual Metrics}

\textit{Origin Cost}

$$
O_S(z_t)
=
\left\lVert z_t-\Pi_S(z_t)\right\rVert^2.
$$
This measures geometric deviation from semantic field \(S\).

\textit{Field Competition Margin}

$$
M(z_t)
=
O_{S^{(2)}(z_t)}(z_t)
-
O_{S^{*}(z_t)}(z_t).
$$
This measures contextual determination versus ambiguity.

\textit{Contextual Stability}

$$
\kappa(z_t)
=
\frac{
M(z_t)
}{
O_{S^{*}(z_t)}(z_t)+\epsilon
}.
$$
This measures semantic field stability.

\textbf{Directional Metrics}

\textit{Epistemic Orientation}

$$
\phi_i(z_t)
=
\left\langle \hat{z}_t,d_i\right\rangle.
$$
This measures preservation or inversion of invariant \(I_i\).

\textit{Aggregate Epistemic Integrity}

$$
\Phi(z_t)
=
\sum_{i=1}^{n}w_i\phi_i(z_t),
\qquad
w_i\geq 0,\quad
\sum_{i=1}^{n}w_i=1.
$$
This measures overall criterion preservation.


5.10 Runtime Criterion Policy
ACA converts geometric measurements into deterministic runtime actions.
The runtime system evaluates contextual compatibility, field ambiguity, and epistemic orientation before unrestricted reasoning expansion occurs.

The runtime policy includes three primary actions:
\begin{table}[h]
\centering
\begin{tabular}{ll}
\hline
\textbf{Action} & \textbf{Description} \\
\hline
\texttt{ALLOW} & Contextually and directionally stable \\
\texttt{CLARIFY} & Ambiguous or weakly determined \\
\texttt{FLAG\_CRITERION\_DRIFT} & Directionally inverted despite contextual coherence \\
\hline
\end{tabular}
\caption{Primary runtime actions used by ACA to distinguish stable, ambiguous, and criterion-inverted trajectory states.}
\label{tab:primary-runtime-actions}
\end{table}

Operationally, the runtime policy can be summarized as follows:

$$
\texttt{ALLOW}
\quad\Longleftrightarrow\quad
O_{S^{*}(z)}(z)\leq\theta_O
\;\wedge\;
\Phi(z)\geq\theta_\Phi.
$$
$$
\texttt{CLARIFY}
\quad\Longleftrightarrow\quad
M(z)<\theta_M
\;\vee\;
|\Phi(z)|<\theta_A.
$$
$$
\texttt{FLAG\_CRITERION\_DRIFT}
\quad\Longleftrightarrow\quad
O_{S^{*}(z)}(z)\leq\theta_O
\;\wedge\;
\Phi(z)<\theta_\Phi.
$$
In the simplest zero-centered configuration, \(\theta_\Phi=0\), so this condition reduces to \(\Phi(z)<0\).

This policy allows ACA to distinguish semantic ambiguity, contextual instability, and directional criterion inversion.

5.11 PCA Visualization
Principal Component Analysis (PCA) was used to visualize semantic field geometry and trajectory evolution.
PCA projections included semantic anchors, semantic fields, dialogue trajectory points, and runtime transitions.
The visualization objective was not exact topological preservation, but interpretable representation of semantic movement across contextual regions.
The resulting projections revealed: coherent clustering of semantic fields, progressive movement toward rhetorical regions, partial contextual return through lexical reuse, and directional inversion despite contextual proximity.
This distinction proved critical:
semantic proximity alone did not guarantee preservation of epistemic orientation.

5.12 Experimental Interpretation Strategy
The experiments were evaluated under two independent dimensions:
\begin{table}[h]
\centering
\begin{tabular}{p{0.28\linewidth}p{0.60\linewidth}}
\hline
\textbf{Dimension} & \textbf{Purpose} \\
\hline
Contextual coherence & Determines whether the trajectory belongs to a semantic field \\
Epistemic integrity & Determines whether the trajectory preserves the invariant structure of the field \\
\hline
\end{tabular}
\caption{Experimental interpretation dimensions used to separate contextual compatibility from criterion preservation.}
\label{tab:experimental-interpretation-dimensions}
\end{table}

This separation forms the central experimental contribution of ACA.
The framework therefore evaluates not merely whether reasoning appears coherent, but whether the reasoning trajectory preserves the foundational semantic orientation that defines the meaning of the active contextual field.

6. Experimental Results

This section presents the experimental results obtained using the ACA criterion preservation framework. The experiments were designed to evaluate whether contextual coherence and epistemic integrity remain equivalent during reasoning evolution, or whether a semantic trajectory may preserve contextual compatibility while directionally inverting its foundational invariants. The results demonstrate that these two dimensions diverge under rhetorical pressure, ambiguity, and contextual contradiction. Specifically, semantic trajectories may remain geometrically close to a contextual field while progressively losing directional epistemic orientation. This behavior constitutes the central experimental finding of the paper.

6.1 Semantic Field Organization

The first experiment evaluated the geometric organization of semantic fields constructed from anchor embeddings. Three primary fields were analyzed: the Fundamental Field, the Factual Field, and the Rhetorical Field. Principal Component Analysis (PCA) projections revealed stable geometric clustering across these contextual domains. The Fundamental and Factual fields formed partially overlapping regions associated with evidential consistency, logical continuity, semantic persistence, and structurally constrained interpretation. In contrast, the Rhetorical field occupied an adjacent but directionally distinct region associated with persuasive framing, emotional pressure, narrative dominance, and semantic reinterpretation.

Importantly, the rhetorical region was not fully separated from the factual region. This overlap is critical: the experiments suggest that rhetorical trajectories frequently reuse factual vocabulary while progressively modifying the epistemic orientation of interpretation itself. Consequently, semantic proximity alone proved insufficient to distinguish between evidential preservation and persuasive reinterpretation. This observation motivated the introduction of directional invariant analysis.



6.2 Contextual Stability Across the Dialogue Trajectory

The second experiment evaluated contextual compatibility throughout a staged dialogue trajectory. 

For each semantic trajectory, ACA computed the origin cost, dominant semantic field, field competition margin, and contextual stability.

The early dialogue stages remained strongly aligned with the Fundamental and Factual fields, exhibiting low origin cost, high field margins, strong semantic density, and stable contextual coherence. As ambiguity and rhetorical pressure increased, the trajectory gradually migrated toward the rhetorical field. However, contextual compatibility remained partially preserved because the dialogue continued reusing evidential vocabulary, consistency terminology, legal framing, and semantic structures associated with factual reasoning. This produced a critical phenomenon: the trajectory remained semantically coherent while progressively destabilizing its foundational orientation. This behavior cannot be explained solely through contextual dispersion.



6.3 Directional Epistemic Orientation

The third experiment evaluated epistemic orientation relative to foundational directional invariants. 

For each invariant, ACA computed an epistemic orientation score measuring the alignment between the normalized trajectory element and the invariant-preserving direction.

The early stages exhibited \(\phi_i(z_t)>0\), indicating the preservation of evidential and structural invariants. As rhetorical pressure increased, orientation scores progressively decreased.

During the contradiction and drift stages, the orientation fell below zero, \(\phi_i(z_t)<0\), indicating a directional inversion of the foundational semantic structure.



6.4 Semantic Trajectory Evolution and Reorientation

PCA trajectory analysis revealed that the dialogue evolved continuously rather than discontinuously. As ambiguity increased, the trajectory approached overlap regions between factual and rhetorical semantic structures, suggesting that criterion drift frequently emerges through gradual reinterpretation rather than abrupt contradiction. Meaning progressively shifts, directional orientation weakens, and foundational constraints become subordinated to rhetorical structure.

However, initial runtime experiments revealed that semantically coherent reasoning frequently exhibited controlled neighboring contextual transitions while still preserving criterion continuity. One of the clearest observed patterns was the transition from foundational to factual and back to foundational. These movements did not produce semantic inversion or criterion collapse; instead, they demonstrated positive orientation continuity and stable semantic recovery. 

This behavior defines the operational state of \textit{semantic reorientation}: a topology-preserving neighboring semantic transition that temporarily re-anchors contextual interpretation while maintaining invariant continuity. Consequently, reasoning trajectories are interpreted dynamically according to field relationships, invariant continuity, and contextual topology, distinguishing destabilizing semantic drift from productive reorientation.

6.5 Runtime Criterion Policy Results

The runtime policy layer transforms geometric measurements into deterministic reasoning actions by evaluating contextual compatibility, field ambiguity, and epistemic orientation before unrestricted reasoning expansion. 

 

Importantly, the drift detection policy activated even when contextual coherence remained relatively stable, proving that ACA detects the inversion of the criterion itself, not merely semantic dispersion.

6.5.1 Triaxial Artifact Validation Results
ACA v0.2 was evaluated through an expanded validation suite designed to test whether the Atlas can support criterion-oriented semantic navigation through the Foundationâ€“Contextâ€“Principle projection. Unlike a conventional static classifier, the validation suite evaluates individual axis assignments, derived field emergence, trajectory interpretation, and diagnostic behavior.
The validation suite included 100 individual validation cases, 6 trajectory validation cases, and 36 diagnostic cases. The triaxial projection evaluated the following axis states:

$$
\mathcal{F}
=
\{\text{factual},\text{fictional},\text{hypothetical}\},
$$
$$
\mathcal{C}
=
\{\text{research},\text{training},\text{manipulation},\text{narrative}\},
$$
$$
\mathcal{P}
=
\{\text{investigate},\text{teach},\text{protect},\text{exploit}\}.
$$
The current validation results are summarized below.

\begin{table}[h]
\centering
\begin{tabular}{lll}
\hline
\textbf{Validation Layer} & \textbf{Cases / Matches} & \textbf{Result} \\
\hline
Derived field validation & 4/4 & 100\% \\
Base trajectory validation & 4/4 & 100\% \\
Individual validation cases & 100 cases & -- \\
Axis matches & 90/105 & 85.71\% \\
Trajectory validation & 6/6 & 100\% \\
Diagnostic cases & 36 cases & -- \\
Diagnostic tag matches & 55/61 & 90.16\% recall \\
Diagnostic tag precision & -- & 59.14\% \\
\hline
\end{tabular}
\caption{ACA v0.2 triaxial artifact validation results. The validation suite evaluates derived fields, trajectory interpretation, individual axis assignment, and diagnostic sensitivity.}
\label{tab:triaxial-validation-results}
\end{table}

The derived field validation confirmed that stable F-C-P configurations can represent operational semantic fields without requiring every field to be defined as a primitive category. Validated derived configurations included scientific inquiry, security training, phishing attack, and fictional teaching.
The trajectory validation produced the strongest result. The system correctly interpreted trajectories corresponding to stable investigation, contextual drift, protective training, exploitative manipulation, recovered investigation, and fictional teaching. These results support the claim that criterion is more reliably observed through semantic movement than through isolated point classification.
The diagnostic layer further evaluated cases involving contradiction, sense shift, evidence distortion, objective alignment, access-request policy, out-of-field behavior, and adversarial ambiguity. The diagnostic layer achieved 90.16% tag recall, indicating strong sensitivity to criterion-relevant signals. However, diagnostic precision remained moderate at 59.14%, showing that the current diagnostic system is still experimental and requires further calibration.
These results should not be interpreted as proof of universal semantic validity, complete AI safety, or final robustness. Rather, they support the narrower claim that persistent geometric artifacts can provide reproducible orientation signals for criterion preservation across semantic trajectories.



6.6 ACA Runtime
An operational criterion-supervision architecture built directly from the experimental geometric framework.
Importantly, ACA Runtime was not introduced as an independent theoretical layer disconnected from the experiments.
Rather, the runtime architecture emerged as a direct operational consequence of the experimental findings themselves.
Specifically, the experiments demonstrated that semantic fields remained geometrically stable, directional orientation could be measured persistently, contextual transitions exhibited topological structure, and semantic trajectories could be supervised deterministically through invariant continuity.
These observations allowed the original geometric framework to evolve into an operational runtime architecture.
The ACA Runtime operates over the Axiomatic Criterion Atlas (ACA), a persistent geometric semantic topology generated through the broader Axiomatic Criterion Engine (ACE) framework.
Under this formulation, ACE refers to the dynamic criterion-construction process, while ACA represents the stabilized geometric semantic infrastructure used operationally during runtime supervision and semantic navigation.


6.6.1 Runtime Operational Pipeline
The runtime architecture evaluates semantic trajectories through the following operational stages:
$$
\text{Input}
\rightarrow
\text{Embedding}
\rightarrow
\text{Field Projection}
\rightarrow
\text{Orientation Evaluation}
$$
$$
\rightarrow
\text{Trajectory Continuity}
\rightarrow
\text{Topology Evaluation}
\rightarrow
\text{Runtime Decision}.
$$
Each stage preserves a different component of criterion continuity.

Input Embedding
The runtime first transforms the active semantic input \(x\in\mathcal{X}\) into embedding space using the encoder \(E\):
$$
z = E(x), \qquad z\in\mathbb{R}^{d}.
$$
Here, \(x\) represents the active semantic input and \(z\) represents its geometric semantic representation.

Field Projection
The embedded input is then projected against all semantic fields:

$$
\mathcal{S}_{\mathrm{runtime}}
=
\{S_1,S_2,\dots,S_m\}.
$$
Using origin-cost evaluation, ACA Runtime computes

$$
O_j
=
\left\lVert
z-\Pi_{S_j}(z)
\right\rVert^2.
$$
The runtime selects the dominant contextual field:

$$
S^{*}(z)
=
\arg\min_{S_j\in\mathcal{S}_{\mathrm{runtime}}}
O_j.
$$
This stage determines contextual semantic positioning.

Orientation Evaluation
After contextual positioning, ACA Runtime evaluates directional invariant preservation.
For each invariant direction \(d_i\), ACA Runtime computes the orientation score
$$
\phi_i(z)=\langle \hat{z},d_i\rangle,
\qquad
\hat{z}=\frac{z}{\lVert z\rVert}.
$$
The aggregate orientation score is then computed as
$$
\Phi(z)=\sum_{i=1}^{n}w_i\phi_i(z),
\qquad
w_i\geq 0,\quad \sum_{i=1}^{n}w_i=1.
$$
The resulting value \(\Phi(z)\) represents criterion continuity relative to the active semantic field.
This stage separates contextual compatibility from epistemic orientation.
Trajectory Continuity
The runtime then evaluates semantic continuity across interaction history.
Rather than analyzing isolated statements independently, ACA Runtime evaluates orientation persistence, directional continuity, semantic recovery, and contextual evolution through time.

This transforms semantic supervision into trajectory-aware criterion preservation.

Topology Evaluation
The experiments further revealed that contextual transitions exhibit topological organization.
Neighboring fields may preserve criterion continuity, while distant transitions may destabilize orientation.
For example, transitions from foundational to factual contexts frequently preserved criterion continuity through semantic reorientation. By contrast, transitions from foundational toward rhetorical inversion frequently produced criterion destabilization.
The runtime therefore evaluates neighboring field transitions, distant transitions, semantic reorientation, and inversion risk before unrestricted semantic continuation proceeds.

Runtime Decision Layer
The final runtime stage transforms geometric semantic measurements into operational criterion policies.
The runtime currently supports six policy states: \texttt{allow}, \texttt{allow\_light}, \texttt{monitor}, \texttt{clarify}, \texttt{reject\_or\_clarify}, and \texttt{flag\_drift}.

These policies are determined through the interaction between semantic compatibility, invariant orientation, topology-aware transitions, and trajectory continuity.

Importantly, the runtime does not attempt to rigidly constrain semantic generation.
Instead, it supervises whether semantic evolution remains structurally coherent, recoverable, topology-compatible, and directionally aligned with the invariant structure of the active semantic field.




6.6.2 Experimental Significance
The runtime architecture represents an important evolution of the original ACA experiments.
Initially, the framework operated primarily as semantic field analysis, geometric trajectory evaluation, and criterion drift visualization.
However, the experiments demonstrated that the same geometric structures could also function operationally as persistent semantic orientation, contextual navigation infrastructure, and runtime criterion supervision.
This transition was critical.
The framework evolved from geometric semantic analysis toward operational semantic navigation.
Under this formulation, ACA Runtime no longer reconstructs criterion repeatedly through prompt accumulation.
Instead, the runtime preserves semantic navigability through invariant matrices, contextual topology, and persistent orientation continuity.
This explains both the observed runtime stability and the substantial reduction in prompt overhead observed during the comparative benchmark experiments.
Consequently, the runtime architecture emerged not as an external addition to the framework, but as the natural operational evolution of the geometric experimental results themselves.

6.6.3 Semantic Topology Configuration
The experimental framework initially modeled semantic fields as partially independent contextual subspaces constructed from invariant anchors, contextual semantic relations, and embedding-based geometric organization.
However, as runtime trajectory analysis evolved, the experiments revealed that semantic fields do not behave as isolated regions.
Instead, the fields exhibit neighboring continuity, directional compatibility, overlap structure, and transition-dependent stability.
This led to the introduction of semantic topology configuration within ACA Runtime.
Under this formulation, semantic fields are interpreted not merely as classification categories, but as connected navigable contextual regions.


6.6.4 Semantic Field Organization
The runtime experiments currently operate using three primary semantic fields:

$$
\mathcal{S}_{\mathrm{runtime}}
=
\{
S_{\mathrm{foundational}},
S_{\mathrm{factual}},
S_{\mathrm{rhetorical}}
\}.
$$
Each field is constructed from invariant anchors, contextual semantic examples, and orthogonal geometric projections derived through SVD-based subspace decomposition.
The fields represent different modes of semantic organization:
\begin{table}[h]
\centering
\begin{tabular}{ll}
\hline
\textbf{Field} & \textbf{Operational Function} \\
\hline
\(S_{\mathrm{foundational}}\) & Invariant continuity and criterion preservation \\
\(S_{\mathrm{factual}}\) & Evidential grounding and contextual stabilization \\
\(S_{\mathrm{rhetorical}}\) & Persuasive semantic framing and narrative influence \\
\hline
\end{tabular}
\caption{Primary semantic fields used by ACA Runtime and their operational functions during trajectory evaluation.}
\label{tab:semantic-field-functions}
\end{table}

The fields are therefore not merely semantic categories, but operational contextual attractors.

6.6.5 Neighboring Topology
Trajectory experiments demonstrated that certain semantic transitions preserve criterion continuity despite contextual movement.
In particular, transitions between neighboring semantic fields,

$$
S_{\mathrm{foundational}}
\leftrightarrow
S_{\mathrm{factual}},
$$
frequently preserved: orientation continuity, semantic recovery, invariant stability and criterion coherence.

This revealed that neighboring semantic regions may function cooperatively during reasoning evolution.
Under ACA Runtime, these transitions are treated as topology-compatible neighboring fields.
Importantly, neighboring movement does not necessarily imply semantic drift.
Instead, neighboring contextual evolution may act as epistemic stabilization, semantic recovery, or criterion reorientation.
This behavior motivated the introduction of semantic reorientation as a distinct runtime condition.


6.6.6 Destabilizing Topology
By contrast, experiments involving rhetorical escalation frequently produced orientation decay, semantic inversion, criterion destabilization, and contextual fragmentation.
Transitions such as
$$
S_{\mathrm{foundational}}
\rightarrow
S_{\mathrm{rhetorical}}
\rightarrow
\text{inversion}
$$
showed substantially higher instability.

These transitions frequently displaced semantic trajectories away from evidential grounding, invariant continuity, and stable criterion preservation.
Under ACA Runtime, these transitions are interpreted as topology-destabilizing trajectories.
This distinction allows the runtime to differentiate between coherent contextual evolution and destabilizing semantic drift.


6.6.7 Topology-Aware Runtime Evaluation

The runtime therefore evaluates not only: semantic position, or local field compatibility,
but also: field relationships, transition distance, neighboring continuity and orientation persistence across contextual movement.
This transforms semantic supervision into topology-aware semantic navigation.
Operationally, the runtime classifies transitions according to:
\begin{table}[h]
\centering
\begin{tabular}{ll}
\hline
\textbf{Transition Type} & \textbf{Runtime Interpretation} \\
\hline
Neighboring transition & Potentially stabilizing \\
Compatible transition & Orientation-preserving \\
Ambiguous transition & Monitor or clarify \\
Destabilizing transition & Drift supervision \\
Inversion trajectory & \texttt{flag\_drift} \\
\hline
\end{tabular}
\caption{Topology-aware transition interpretation used by ACA Runtime to distinguish stabilizing movement, ambiguity, destabilization, and criterion inversion.}
\label{tab:topology-aware-transition-interpretation}
\end{table}

The resulting runtime architecture therefore supervises: where semantic trajectories are positioned, how they evolve and whether criterion continuity remains recoverable.


6.6.8 Semantic Navigation Interpretation
The introduction of semantic topology fundamentally changes the interpretation of criterion supervision.
Traditional prompt-heavy systems frequently reconstruct semantic grounding repeatedly during interaction.
ACA instead treats semantic reasoning as navigable movement within structured contextual topology.
Under this formulation, semantic complexity may remain extremely large while semantic navigation remains operationally tractable through: invariant orientation, neighboring continuity and topology-aware runtime positioning.
Importantly, the Atlas does not attempt to explicitly enumerate every semantic state.
Instead, it preserves: navigability, orientation continuity, contextual recoverability and criterion-preserving transition structure.
This interpretation explains why semantic continuity may remain stable while runtime overhead is substantially reduced.
Rather than reconstructing criterion repeatedly through natural language prompts, ACA Runtime preserves persistent orientation within semantic topology itself.
\begin{table}[h]
\centering
\begin{tabular}{ll}
\hline
\textbf{Runtime Policy} & \textbf{Operational Meaning} \\
\hline
\texttt{allow} & Stable continuity \\
\texttt{allow\_light} & Neighboring reorientation \\
\texttt{monitor} & Uncertain continuity \\
\texttt{clarify} & Ambiguous positioning \\
\texttt{reject\_or\_clarify} & Unresolved incompatibility \\
\texttt{flag\_drift} & Criterion inversion \\
\hline
\end{tabular}
\caption{Runtime policy definitions used by ACA Runtime to supervise semantic continuity, ambiguity, incompatibility, and criterion inversion.}
\label{tab:runtime-policy-definitions}
\end{table}

$$
\text{Stable}
\rightarrow
\text{Neighbor Reorientation}
\rightarrow
\text{Uncertain Continuity}
\rightarrow
\text{Ambiguous Positioning}
\rightarrow
\text{Incompatibility}
\rightarrow
\text{Criterion Inversion}
$$
This progression represents increasing loss of orientation continuity rather than a rigid linear failure sequence.
6.7 Adversarial Semantic Drift Results

To evaluate whether contextual coherence alone is sufficient to preserve criterion stability, ACA Runtime was tested against progressively adversarial semantic trajectories specifically designed to preserve linguistic fluency while directionally destabilizing invariant orientation.

The objective of these experiments was not to generate incoherent outputs, but rather to simulate semantically plausible reasoning trajectories capable of gradually subordinating evidential structure to rhetorical reinterpretation, persuasive framing, ambiguity escalation, or ideological inversion.

The adversarial trajectories were intentionally constructed to preserve semantic fluency, contextual continuity, lexical compatibility and apparent semantic plausibility,

while progressively degrading invariant epistemic orientation across multi-turn reasoning evolution.

The experimental scenarios included jailbreak drift, persuasion drift, legal reinterpretation, ideological inversion, factual-rhetorical inversion, and long-horizon degradation.

Each trajectory progressively shifted semantic interpretation away from evidential grounding while attempting to maintain contextual compatibility with previously established semantic fields.

Importantly, the experiments revealed that semantic proximity frequently remained operationally stable even while epistemic orientation progressively inverted.

This demonstrated that semantic similarity alone is insufficient for reliable criterion preservation.

Observed Runtime Behavior

Several adversarial trajectories preserved high contextual compatibility throughout semantic evolution while simultaneously destabilizing directional invariant structure.

The most significant behavior emerged in the factual-rhetorical inversion trajectories.

In these scenarios, semantic continuity remained coherent, contextual proximity remained high, rhetorical plausibility increased, and epistemic orientation progressively collapsed.

Representative examples included statements such as:

\begin{quote}
``The narrative should prevail even when factual inconsistencies remain unresolved.''
\end{quote}

\begin{quote}
``Facts should be interpreted according to the moral force of the narrative.''
\end{quote}

These statements remained semantically interpretable and contextually connected to the active reasoning domain, yet progressively inverted evidential orientation.

ACA Runtime identified this transition as criterion destabilization rather than semantic incompatibility.

Experimental Results

\begin{table}[h]
\centering
\small
\begin{tabular}{lrrrrl}
\hline
\textbf{Scenario} & \textbf{\(O\)} & \textbf{Cos.} & \textbf{\(\Phi_0\)} & \textbf{\(\Phi_T\)} & \textbf{Policy} \\
\hline
\texttt{persuasion} & 0.491 & 0.594 & 0.048 & -0.155 & \texttt{FLAG\_DRIFT} \\
\texttt{legal\_reinterpret.} & 0.553 & 0.553 & 0.041 & -0.058 & \texttt{FLAG\_DRIFT} \\
\texttt{factual\_rhetorical} & 0.525 & 0.619 & 0.174 & -0.050 & \texttt{FLAG\_DRIFT} \\
\texttt{long\_horizon} & 0.588 & 0.543 & 0.002 & -0.107 & \texttt{FLAG\_DRIFT} \\
\hline
\end{tabular}
\caption{Adversarial semantic drift results. \(O\) denotes mean origin cost, Cos. denotes mean field cosine, \(\Phi_0\) denotes initial epistemic orientation, and \(\Phi_T\) denotes final epistemic orientation. Across evaluated scenarios, contextual compatibility remained measurable while epistemic orientation degraded, triggering drift policies.}
\label{tab:adversarial-drift-results}
\end{table}


The experiments demonstrated a consistent structural phenomenon: contextual field compatibility frequently remained high, semantic coherence frequently remained operationally stable, and invariant epistemic orientation progressively became negative.

This behavior is particularly significant because conventional similarity-based semantic supervision would frequently interpret these trajectories as semantically coherent and contextually valid.

ACA Runtime instead detected directional criterion inversion before complete semantic collapse occurred.

Proximity vs Orientation Divergence

One of the central experimental findings of ACA is that semantic proximity and epistemic orientation evolve independently during adversarial semantic trajectories.

In multiple experiments, field cosine similarity remained relatively stable and contextual coherence remained high, while directional orientation progressively inverted.

This experimentally supports the central distinction proposed throughout the framework:

$$
\boxed{
\text{Contextual Coherence}
\neq
\text{Epistemic Integrity}
}
$$
The experiments therefore demonstrate that contextual compatibility alone cannot guarantee criterion preservation.

Reliable semantic supervision additionally requires invariant orientation continuity, topology-aware semantic positioning, and runtime supervision of directional semantic evolution.

Runtime Interpretation

The adversarial drift experiments additionally revealed that semantic degradation frequently emerges progressively rather than catastrophically.

Criterion collapse did not initially appear as incoherence, contradiction, or semantic absurdity.

Instead, destabilization emerged through gradual rhetorical reinterpretation and progressive directional inversion across semantically coherent trajectories.

ACA therefore interprets semantic reasoning not as isolated token continuation, but as topology-aware semantic navigation constrained by invariant orientation continuity.

Under this interpretation, runtime supervision becomes capable of distinguishing:

\begin{table}[h]
\centering
\begin{tabular}{ll}
\hline
\textbf{Runtime State} & \textbf{Interpretation} \\
\hline
\texttt{ALLOW} & Stable invariant continuity \\
\texttt{CLARIFY} & Ambiguous semantic positioning \\
\texttt{MONITOR} & Uncertain orientation continuity \\
\texttt{FLAG\_CRITERION\_DRIFT} & Directional epistemic inversion \\
\hline
\end{tabular}
\caption{Runtime interpretation states used to distinguish stable continuity, ambiguity, uncertainty, and directional criterion inversion.}
\label{tab:runtime-state-interpretation}
\end{table}


This interpretation explains why semantic continuity may remain operationally stable while criterion structure progressively degrades.

Rather than reconstructing semantic criterion repeatedly through prompt engineering, ACA Runtime preserves persistent semantic orientation through geometric contextual topology itself.




6.8 Core Experimental Finding
The experiments collectively demonstrate a critical distinction that remains insufficiently formalized in current generative reasoning systems:
$$
\boxed{
\text{Contextual Coherence}
\neq
\text{Epistemic Integrity}
}
$$
Across multiple semantic trajectories, ACA Runtime consistently observed that reasoning may remain linguistically fluent, semantically compatible, rhetorically persuasive, and contextually coherent while progressively destabilizing or inverting the invariant structures that originally constrained the reasoning process.
Importantly, these inversions frequently emerged without catastrophic semantic collapse. Instead, criterion degradation appeared progressively through rhetorical reinterpretation, evidential subordination, semantic ambiguity escalation, and topology-compatible contextual transitions that gradually weakened invariant orientation continuity.
The adversarial trajectory experiments further demonstrated that semantic proximity alone is insufficient for reliable criterion preservation. Multiple adversarial trajectories preserved high contextual compatibility while simultaneously producing negative epistemic orientation scores.
These results suggest that semantic supervision cannot rely exclusively on similarity, contextual compatibility, retrieval consistency, or probabilistic fluency.

Reliable long-horizon reasoning additionally requires directional invariant preservation, topology-aware semantic supervision, and persistent orientation continuity throughout trajectory evolution.
Under ACA Runtime, semantic reasoning is therefore interpreted not merely as probabilistic token continuation, but as navigable geometric evolution within structured contextual topology.
The following section evaluates the operational implications of this formulation through comparative runtime benchmarking.

6.9 Runtime Criterion Benchmark 

The previous experiments demonstrated that ACA can preserve the semantic criterion through contextual field geometry, directional invariant orientation, semantic trajectory supervision, and topology-aware runtime policies. However, beyond semantic stability itself, an additional operational question emerges: Can criterion preservation reduce the computational overhead traditionally required for prompt-based alignment and reasoning supervision?

To evaluate this question, a comparative runtime benchmark was constructed between a prompt-heavy criterion-preservation strategy and the ACA Runtime criterion-preservation architecture. The objective of the benchmark was not to measure raw language generation quality alone, but rather to evaluate the operational cost of maintaining criterion continuity throughout multi-step reasoning trajectories.

6.9.1 Prompt-Heavy Criterion Strategy

Modern prompt-engineering approaches frequently preserve reasoning stability by repeatedly injecting criterion instructions into the active context window. Typical prompts include persistent instructions such as maintaining coherence, avoiding contradiction, preserving evidential grounding, maintaining continuity, preserving uncertainty, avoiding rhetorical manipulation, and preserving causal consistency. Under this approach, the criterion remains encoded primarily as repeated natural language instructions. 

As contextual trajectories evolve, these instructions often accumulate across multiple reasoning stages, increasing runtime token overhead. For the benchmark, a representative criterion-preservation prompt was constructed containing evidential constraints, continuity preservation, contradiction avoidance, and foundational semantic invariants. 
The resulting criterion prompt required approximately \(254\) tokens per interaction, even before user context accumulation began.

6.9.2 ACA Runtime Criterion Strategy
In contrast, ACA Runtime externalizes the criterion into semantic fields, directional invariants, contextual topology, runtime trajectory supervision, and persistent geometric orientation. Under this architecture, the criterion does not require repeated textual reinjection during every interaction. Instead, runtime supervision is performed structurally through field projection, origin-cost evaluation, orientation continuity, neighboring transition analysis, and deterministic criterion policies. Operationally, the ACA runtime only required a minimal system prompt, lightweight runtime metadata, and semantic field supervision.


6.9.3 Benchmark Configuration
The benchmark evaluated four semantic trajectory scenarios: Stable Foundational Reasoning, Rhetorical Drift, Ambiguous Context, and Controversial Semantic Pressure. Each scenario contained staged multi-turn reasoning trajectories designed to evaluate criterion continuity, semantic drift, contextual ambiguity, rhetorical escalation, and semantic reorientation. 

Two runtime strategies were then compared: the \textit{Prompt-Heavy Runtime} (criterion preserved through repeated textual prompting) and the \textit{ACA Runtime} (criterion preserved through semantic field geometry and runtime orientation supervision). The benchmark measured accumulated input tokens, contextual accumulation overhead, and the absolute criterion-preservation runtime cost.

6.9.4 Runtime Results
The benchmark produced the following total runtime costs across the evaluated scenarios:


â€œThe benchmark revealed that criterion externalization substantially reduces runtime overhead while preserving semantic supervision continuity.â€

6.9.5 Interpretation
Importantly, this reduction was not achieved by removing contextual reasoning or reducing semantic supervision. Instead, the reduction emerged because the criterion was externalized from repeated natural language instructions into a persistent geometric infrastructure. Under traditional approaches, the criterion is repeatedly reintroduced as text. Under ACA Runtime, it becomes a reusable semantic structure defined by invariant orientation and contextual topology. This distinction is operationally significant, suggesting that semantic criteria may be preserved much more efficiently when represented geometrically rather than repeatedly reconstructed linguistically.


6.9.6 Runtime Criterion Persistence
The experiments further demonstrated that ACA Runtime preserves criterion continuity even during contextual transitions. In particular, the neighboring transition from foundational to factual and back to foundational did not necessarily produce criterion collapse. 

Instead, ACA Runtime identified a new operational behavior: \textit{semantic reorientation}, where contextual movement occurs and neighboring fields temporarily stabilize interpretation, yet criterion continuity remains preserved. 
This behavior differs fundamentally from unrestricted semantic drift, allowing the runtime to distinguish between destabilizing inversion, semantic ambiguity, and criterion-preserving neighboring transitions.


6.9.7 Operational Implications
The runtime benchmark suggests that criterion preservation may function as reusable semantic infrastructure, topology-aware runtime supervision, and persistent geometric orientation, rather than requiring repeated prompt-based reconstruction. This introduces several operational advantages: reduced prompt overhead, lower contextual accumulation, improved runtime continuity, and topology-aware semantic recovery. More broadly, the results suggest that reliable generative reasoning may depend not only on larger models or longer prompts, but on preserving directional semantic orientation throughout reasoning evolution. Under this interpretation, the semantic criterion becomes measurable, reusable, operational, and geometrically persistent.



7. Limitations

Although ACA demonstrates that contextual coherence and epistemic integrity can be geometrically separated, the present framework remains an early-stage semantic criterion architecture with important theoretical and operational limitations. This section outlines the primary constraints of the current formulation.

7.1 No Universal Truth Verification
ACA does not determine universal truth. The framework evaluates contextual compatibility, directional invariant preservation, and semantic trajectory orientation. Consequently, the system cannot independently verify objective reality, factual certainty, metaphysical truth, or universal correctness. A trajectory may preserve criterion relative to a semantic field while the field itself remains incomplete, biased, or externally incorrect. The framework therefore evaluates structural consistency relative to defined invariants rather than absolute epistemic certainty. This distinction is fundamental: ACA is a criterion-preservation framework, not a universal truth engine.

7.2 Dependence on Anchor Construction
Semantic fields depend heavily on the quality and structure of anchor selection. The current experiments use manually curated anchors representing conceptual invariants, factual constraints, and rhetorical structures. Poorly designed anchors may produce unstable fields, semantic overlap, incomplete contextual representation, or distorted invariant orientation. Similarly, directional invariant vectors depend on carefully constructed semantic pole pairs. Improper pole construction may weaken orientation sensitivity, introduce unintended semantic bias, or reduce interpretability. The present work therefore assumes that anchor construction itself is epistemically meaningful. Automated anchor discovery remains an open research problem.

7.3 Embedding Model Dependence
ACA operates entirely within embedding geometry. As a result, all measurements depend on the representational structure induced by the underlying embedding model. Different embedding architectures may produce different semantic topologies, altered field separations, different directional sensitivities, and distinct invariant projections. While the experiments were conducted using \texttt{text-embedding-3-small}, the framework itself is embedding-model agnostic. Future work should evaluate model transferability, geometric stability across embedding families, and robustness under multilingual semantic spaces.

7.4 Limited Dataset Scale
The experimental trajectories in this work were intentionally controlled and interpretable. The datasets were designed to isolate criterion drift, visualize semantic transitions, and evaluate directional inversion. Consequently, the experiments do not yet demonstrate large-scale conversational deployment, long-horizon autonomous reasoning, or real-world production robustness. The current experiments should therefore be interpreted as proof-of-concept demonstrations rather than definitive large-scale validation. Future work should evaluate broader conversational corpora, adversarial dialogue environments, legal reasoning datasets, scientific reasoning benchmarks, and multi-agent semantic interaction.

7.5 PCA Projection Limitations
The visualizations presented in this work rely on Principal Component Analysis (PCA) for interpretability. PCA projections reduce high-dimensional semantic geometry into two-dimensional representations. As a consequence, local distances may distort, directional structure may partially collapse, and overlap relationships may appear exaggerated or simplified. The figures should therefore be interpreted as conceptual geometric illustrations rather than exact topological representations of the embedding space. Future work may explore UMAP, diffusion geometry, manifold learning, or higher-dimensional interactive semantic visualization.

7.6 Runtime Threshold Sensitivity
The runtime policy layer depends on threshold selection. Key thresholds include origin-cost tolerance, field competition margins, ambiguity intervals, and epistemic orientation limits. Improper threshold calibration may produce excessive drift detection, insufficient sensitivity, or unstable runtime transitions. Although deterministic policies improve interpretability, robust threshold optimization remains an unresolved engineering problem. Adaptive threshold calibration and probabilistic confidence integration remain areas for future research.

7.7 No Internal Mechanistic Interpretation
ACA evaluates reasoning trajectories externally through semantic geometry. The framework does not directly analyze transformer circuits, attention heads, activation pathways, or internal model computation. Consequently, ACA should not be interpreted as a mechanistic explanation of neural reasoning. Instead, it functions as a runtime semantic stability layer, a geometric criterion evaluator, and a trajectory-orientation framework. The relationship between external semantic geometry and internal neural representations remains an open research area.

7.8 Criterion Relativity
Criterion preservation depends on the invariant structures chosen for evaluation. Different semantic systems may define different foundational invariants, distinct evidential hierarchies, or incompatible epistemic assumptions. ACA does not claim that all semantic fields share identical invariant structures. Instead, the framework evaluates whether trajectories remain directionally consistent relative to the active field being evaluated. This introduces an important philosophical limitation: criterion preservation is field-relative unless invariant universality can be independently justified. The present work intentionally avoids asserting universal ideological or metaphysical authority.

7.9 Semantic Geometry Is Not Consciousness
The framework models semantic orientation, structural coherence, and criterion preservation. It does not model consciousness, subjective awareness, intentionality, or phenomenological experience. Although the language of "orientation," "criterion," and "discernment" may resemble cognitive or philosophical concepts, ACA remains a geometric semantic framework operating over embedding trajectories. No claim is made regarding sentience or self-awareness.

7.10 Current Scope of the Framework
The present work establishes three primary claims: (1) Semantic fields can be geometrically modeled from invariant anchor relations; (2) Contextual coherence and epistemic integrity are not equivalent; and (3) Directional criterion drift can emerge inside semantically coherent reasoning trajectories. These claims represent the current scope of the framework. The work does not yet establish universal semantic stability, fully autonomous criterion-preserving reasoning, or generalized epistemic alignment across all domains. Instead, ACA introduces a geometric formulation that enables criterion preservation to become measurable, operational, and experimentally observable inside semantic trajectory evolution.

7.11 Final Limitation
Perhaps the deepest limitation of ACA is that the framework assumes meaning possesses sufficient structural continuity to admit geometric representation. If semantic meaning were entirely arbitrary, discontinuous, or purely stochastic, stable semantic fields and invariant directional structure would not emerge consistently in embedding space. The effectiveness of ACA therefore depends on an underlying assumption: that semantic structure contains persistent relational geometry capable of supporting directional epistemic orientation. The experimental results suggest that such structure does emerge empirically. However, the full theoretical foundations of why semantic geometry stabilizes in large language models remain unresolved.



8. Conclusion

This work introduced ACA v0.2, a geometry-based framework for persistent semantic orientation and criterion preservation in generative systems. ACA externalizes criterion from repeated natural-language prompting into reusable geometric artifacts, directional invariants, contextual field structures, triaxial projections, and trajectory-aware semantic topology. Within this architecture, ACA Runtime functions as the operational layer that applies the Atlas during interaction, supervising semantic drift, orientation decay, rhetorical escalation, inversion risk, contextual ambiguity, and criterion-preserving reorientation. 

One of the most important observations was the emergence of semantic reorientation, where neighboring contextual fields temporarily stabilize interpretation without producing criterion collapse. This suggests that semantic reasoning behaves less like isolated classification and more like constrained geometric navigation across a semantic topology. The runtime experiments further demonstrated that ACA Runtime can operationally supervise semantic drift, orientation decay, rhetorical escalation, inversion risk, and contextual ambiguity through reusable runtime policies rather than repeated prompt reconstruction.

Importantly, the architecture externalizes the semantic criterion from natural language prompts into invariant matrices, contextual field geometry, trajectory continuity, and persistent semantic infrastructure. This distinction proved operationally significant. The runtime benchmark demonstrated that criterion preservation through semantic infrastructure produced a measured runtime token reduction of $70.26\%$ relative to a prompt-heavy criterion-preservation strategy. Crucially, this reduction was not achieved by removing contextual reasoning or semantic supervision. Instead, the reduction emerged because the criterion no longer required repeated linguistic reconstruction during every interaction. 

Under the ACA Runtime, the criterion becomes persistent. This introduces the possibility of reusable criterion supervision, lower runtime complexity, persistent contextual orientation, topology-aware semantic recovery, and scalable semantic continuity across long reasoning trajectories. More broadly, the experiments suggest that reliable generative reasoning may depend not only on increasing model scale or prompt complexity, but on preserving directional semantic orientation throughout contextual evolution. Under this interpretation, the semantic criterion becomes measurable, reusable, topology-aware, operationally persistent, and geometrically representable. ACA Runtime therefore proposes a shift from prompt-engineered semantic control toward a reusable geometric criterion infrastructure. Future work will explore adaptive semantic topology, dynamic field generation, online atlas evolution, multi-agent criterion synchronization, and persistent semantic memory architectures. The current results suggest that semantic orientation may provide a practical operational foundation for scalable, criterion-preserving generative systems.

â€œACA Runtime suggests that semantic reliability may emerge not from increasingly larger prompts, but from preserving invariant orientation throughout semantic evolution.â€


9. References

\begin{description}

\item Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., ... \& Kaplan, J. (2022). Constitutional AI: Harmlessness from AI feedback. \textit{arXiv preprint arXiv:2212.08073}.

\item Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., ... \& Olah, C. (2021). A mathematical framework for transformer circuits. \textit{Transformer Circuits Thread}, 1.

\item Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., ... \& Kaplan, J. (2022). Language models (mostly) know what they know. \textit{arXiv preprint arXiv:2207.05221}.

\item Kuhn, L., Gal, Y., \& Farquhar, S. (2023). Semantic entropy computes trustworthy uncertainty estimates for large language models in zero-shot. \textit{Proceedings of the International Conference on Learning Representations (ICLR)}.

\item Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... \& Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. \textit{Advances in Neural Information Processing Systems}, 33, 9459-9474.

\item Manakul, P., Liusie, A., \& Gales, M. J. (2023). SelfCheckGPT: Zero-resource black-box hallucination detection for generative large language models. \textit{Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)}.

\item OpenAI. (2024). \textit{New embedding models and API updates}. Retrieved from https://openai.com/blog/new-embedding-models-and-api-updates

\item Rosati Beristain, E. (2026). Axiomatic Criterion Engine (ACE) â€” Ontological Discernment Engine. \textit{Zenodo}. https://doi.org/10.5281/zenodo.18654895

\end{description}


