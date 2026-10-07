# AI Learning Roadmap 🤖

My path from Python beginner → building AI that solves real problems.
Learned the same way as Python: **concept + exercise + review**, hands-on, not passive videos.

> **The goal:** understand *how AI works* AND *how to build AI to solve any problem.*
> Python was the means to this end.

---

## Two skills, both worth having

- **AI Engineering** — building *applications* with AI models that already exist (e.g. the Claude API). Achievable early, motivating, very employable.
- **Machine Learning** — understanding *how AI works under the hood* and *training your own models*. Deeper and longer, but it's the real "how does it work."

The plan interleaves them: build deep understanding, with quick app-building wins sprinkled in to stay motivated.

---

## The Phases

| Phase | What I learn | Why it matters | Tools |
|-------|-------------|----------------|-------|
| **0. Python** *(in progress)* | Finish core + toolkit + **classes/OOP** | Every AI library is Python; ML code is class-heavy | — |
| **1. Data Python** | NumPy, pandas, matplotlib | AI = math on arrays of data; the daily toolkit | NumPy, pandas |
| **2. Just-enough math** | Vectors, matrices, dot products; derivatives & gradients; mean/variance/probability | This *is* how models compute and learn — intuition, not proofs | NumPy |
| **3. Classical ML** | Train/test split, features/labels, regression, classification, overfitting, evaluation | Foundation of all ML; train real models on real data | scikit-learn |
| **4. Deep Learning** | Neurons, forward pass, loss, gradient descent, backprop | Build a tiny net **from scratch**, then scale up | NumPy → PyTorch |
| **5. Modern AI / LLMs** | Tokens, embeddings, attention/transformers; RAG, agents, prompting | How ChatGPT/Claude work; build AI apps with real APIs | PyTorch, Claude API |

### How the two goals interleave
```
Python (now) ─► Data Python ─► Math ─► Classical ML ─► Deep Learning ─► LLMs
                    │                                                     │
                    └──────────── quick "AI app" wins with APIs ──────────┘
```

### What this means for Python right now
1. **Classes/OOP is important, not optional** — ML frameworks are built around classes. (Bonus: also unlocks linked-list LeetCode problems.)
2. **Examples bias toward data** — numbers, records, datasets — so I'm already thinking in AI's shapes.

---

## What I'll be able to BUILD (motivation fuel 🚀)

### Early wins — AI apps with existing models (Phase 1 + APIs)
- Smart chatbot for a specific job (study buddy, coding helper, language tutor)
- Document Q&A tool — ask questions about a PDF (this is **RAG**)
- Email/message summarizer
- Sentiment dashboard — % positive/negative from reviews or tweets
- An AI **agent** that uses tools (weather, math, search) and decides when

### Classical ML — train my own models (Phase 3)
- House price predictor
- Spam / not-spam classifier
- Movie recommender
- Customer churn predictor
- Handwritten digit recognizer (MNIST)

### Deep Learning — neural networks (Phase 4)
- Image classifier ("cat or dog?", "normal X-ray?") with CNNs
- **A neural net from scratch in NumPy** — the moment AI stops being magic
- Handwriting/style generator
- A game-playing AI (reinforcement learning)

### Modern AI / LLMs — generative (Phase 5)
- My own mini language model (trained on text I choose)
- Semantic search engine (search by *meaning*, not keywords)
- Voice assistant (speech → AI → response)
- An AI coding agent (a small version of Claude)
- A multi-step research agent (searches, reads, writes a cited report)

### "Wow" capstones — solve a real problem end-to-end
- Predict something from my own life/work data
- Automate an annoying task at my job with AI
- Full pipeline: **frame → gather data → train/use model → evaluate → ship**

---

## Honest expectations
- A **multi-month journey**, not weeks — but a *staircase*; each step is doable.
- **No math degree needed** — practical, intuition-first math taught as required.
- **Build at every phase** — don't wait until "ready" to make things.

---

*Progress: Phase 0 (Python) in progress — on Lesson 9 (slicing & string methods), doing LeetCode Easy alongside. See `README.md` for Python notes.*
